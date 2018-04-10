## Ce script vise à effectuer l'ordonnancement de la capacité des vols
# 1) Packages
library(dplyr)
library(RPostgreSQL)
library(sqldf)

drv <- dbDriver("PostgreSQL")

conn <- dbConnect(
  drv, 
  dbname = "postgres",
  host = "localhost",
  port = "5432",
  user = "postgres",
  password = "postgres"
  
)



#dbSendQuery()

#dbWriteTable()

#table <- dbGetQuery(conn,  "select * from pop_srdomi100")

#read.csv(".\\tbl_capacite.csv", stringsAsFactors = FALSE)


#2) Fetch data
capacity <- dbGetQuery(conn,"select * from cap_horaire") %>% 
  mutate(cap_timestamp =  as.POSIXct(cap_timestamp, format = "%Y-%m-%d %H:%M")) %>% 
  filter(cap_timestamp == max(cap_timestamp)) %>% 
  mutate(group_name = "total_pool")
#dbDisconnect(conn)

#read.csv(".\\tbl_algo_regles_affaire.csv", stringsAsFactors = FALSE)
rules <- dbGetQuery(conn,"select * from regle_aff")
rules$drag_capacity_from[rules$drag_capacity_from == "total_pool"] <- "main_total_pool"
rules$drag_capacity_to[rules$drag_capacity_to == "total_pool"] <- "main_total_pool"
# rules <- rules[-1,]
#dbDisconnect(conn)

#read.csv(".\\tbl_group.csv", stringsAsFactors = FALSE)
groups <- dbGetQuery(conn,"select * from priority_group") %>% 
  mutate(capacity = 0) %>% 
  rbind(capacity %>%
          mutate(id_group = 0,
                 fc_code="zz",
                 group_type = "main",
                 group_class = "none",
                 capacity = cap_value) %>% 
          select(id_group, fc_code, group_name, group_type, group_class, capacity)) %>% 
  mutate(group_name = paste0(group_type, "_", group_name))

#3) Run règles d'affaires
# A) Set up constants 
i <- 1
i_max <- nrow(rules)
# i_max <- 9

# B) Loop over each rule in rules
for (i in i:i_max) {
# CALCULATE CAPACITY TO TRANSFER
  cap_transfer <- 0
  
  ## TEST FOR CAPACITY_LESS OR CAPACITY_MORE
  condition1 <-  TRUE
  while(condition1 == TRUE){
  
    if(rules$condition_type[i] %in% c("if_capacity_more") &
       groups$capacity[groups$group_name == rules$drag_capacity_from[i]] < as.numeric(rules$condition_value[i])){
      i <- i + 1
      print("if_capacity_more is FALSE")
      condition1 <- TRUE
      
    } else if(rules$condition_type[i] %in% c("if_capacity_less") & 
       groups$capacity[groups$group_name == rules$drag_capacity_from[i]] > as.numeric(rules$condition_value[i])){
      i <- i + 1
      print("if_capacity_less is FALSE")
      condition1 <- TRUE
      
    } else {
      
      condition1 <- FALSE
    }
  } # end while
    
  ## Proceed as usual
  if(rules$drag_type[i] == "absolute"){
    
    cap_transfer <- min(rules$drag_value[i], 
                        groups$capacity[groups$group_name == rules$drag_capacity_from[i]])
    
  } else if(rules$drag_type[i] == "percent"){
    
    cap_transfer <- min(groups$capacity[groups$group_name == rules$drag_capacity_from[i]], 
                        ceiling(groups$capacity[groups$group_name == rules$drag_capacity_from[i]] * rules$drag_value[i]))
  }
  
# REMOVE FROM EXISTING CAPACITY
  groups$capacity[groups$group_name == rules$drag_capacity_from[i]] <- groups$capacity[groups$group_name == rules$drag_capacity_from[i]] - cap_transfer
  
# ADD TO
  groups$capacity[groups$group_name == rules$drag_capacity_to[i]] <- groups$capacity[groups$group_name == rules$drag_capacity_to[i]] + cap_transfer
    

# VERIFY PROPAGATION
  if(rules$propagation[i] == TRUE & cap_transfer > 0){
    
    # DO PROPAGATION FOR ALL ITEMS RELATED
    ## CALCULATE HOW MANY ITEMS TO ITERATE ONE
    items <- groups %>% 
                filter(group_class == rules$drag_capacity_to[i], group_type == "op")
    if (rules$condition_type[i] == "except") {
      
      items <- items %>% 
        filter(!(group_name %in% rules$condition_value[i]))
      
    } else if (rules$condition_type[i] == "within") {
      
      items <- items %>% 
        filter(group_name %in% rules$condition_value[1])
      
    }
    
    ## Iterate on every item in items
    items$capacity_to_add <- c(rep(1, groups$capacity[groups$group_name == rules$drag_capacity_to[i]]),
                               rep(0, nrow(items) - groups$capacity[groups$group_name == rules$drag_capacity_to[i]])
    )
    
    ## Remove capacity allocation
    groups$capacity[groups$group_name == rules$drag_capacity_to[i]] <- 0
    
    ## Add new capacity
    groups <- groups %>% 
      left_join(items %>% select(group_name, capacity_to_add),
                by = c("group_name"
                       )) %>% 
      mutate(capacity = if_else(!is.na(capacity_to_add), capacity + capacity_to_add, capacity)) %>% 
      select(-capacity_to_add)
    
    ## Clean environment
    rm(items)
    
    ## Verbose
    print(paste0("Propagation - iter ", i, " capacity total ", sum(groups$capacity)))
    
  } else {
    
    print(paste0("no propagation", " capacity total ", sum(groups$capacity)))
  
  }
  
} # end for


groups <- groups[groups$capacity>0, ]
groups$timestamp_open <- Sys.time()
groups$timestamp_close <- Sys.time()+30*60
groups$plage_horaire=1

## Send the assignation to the public server
## ÉCRIRE LE CODE

#attribution_prel
dbWriteTable(conn, "att_prel", groups ,append=TRUE)


  