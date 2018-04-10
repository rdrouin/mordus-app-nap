## Ce script va récupérer les résultats des allocations par les transporteurs pour regrouper le tout dans un data pool
# 1) Library
library(RPostgreSQL)
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
  password = "postTrans"
  
)



# 2) Fetch data
att_prel <-dbGetQuery(conn,"select * from att_prel") %>% 
  mutate(timestamp_open =  as.POSIXct(timestamp_open, format = "%Y-%m-%d %H:%M")) %>% 
  mutate(timestamp_close =  as.POSIXct(timestamp_close, format = "%Y-%m-%d %H:%M"))
dbDisconnect(conn)

att_conf <- dbGetQuery(conn,"select * from att_conf") %>% 
  mutate(timestamp =  as.POSIXct(timestamp, format = "%Y-%m-%d %H:%M"))
dbDisconnect(conn)

# 3) Calcul de la capacité non utilisée
open_capacity <- att_prel %>% 
  left_join(att_conf %>% 
              group_by(id_att_prel) %>% 
              summarise(n = n_distinct(id_att_conf)),
            by = "id_att_prel") %>% 
  mutate(capacity_available = value - n) %>% 
  filter(capacity_available > 0)

# 4) Envoie de la table à postgres
open_capacity_pool <- open_capacity %>%                       ### DANS LOBJET EN PRODUCTION, NE PAS INCLURE LE CHAMP OPEN_CAPACITY_POOL_ID
  mutate(open_capacity_pool_id = 1:nrow(open_capacity)) %>% 
  mutate(timestamp_open_capacity_pool = Sys.time()) %>% 
  select(open_capacity_pool_id, plage_horaire, capacity_available, timestamp_open_capacity_pool)
# write.csv(open_capacity_pool, file = ".\\open_capacity_pool.csv", row.names = FALSE)
