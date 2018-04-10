export default class Fetcher {

    static myInstance = null;

    _userID = "";
    _token = "";
    _admin = false;


    /**
     * @returns {Fetcher}
     */
    static getInstance() {
        if (this.myInstance == null) {
            this.myInstance = new Fetcher();
        }

        return this.myInstance;
    }

    getUserID() {
        return this._userID;
    }

    setUserID(id) {
        this._userID = id;
    }

    getUserToken() {
        return this._token;
    }

    setUserToken(token) {
        this._token = token;
    }

    isLogged(){
      return this._userID != "" && this._token != "";
    }

    setIsAdmin(isAdmin){
      this._admin = isAdmin;
    }

    isAdmin(){
      return this._admin;
    }

    logout(){
      if (this._userID != ""){
        this._userID = "";
        this._token = "";
        this._admin = false;
        return true;
      }
      else {
        return false;
      }
    }

    fetch(url, method='get'){
      return fetch('http://localhost:8932/' + url, {
        method: method,
        headers: {
          Accept: 'application/json',
          "api_username": this._userID,
          "api_access_token" : this._token,
        }
      })
    }

    postfetch(url, body=''){
      return fetch('http://localhost:8932/' + url, {
        method: 'post',
        headers: {
          Accept: 'application/json',
          "api_username": 1,
          "api_access_token" : "123",
        },
        body:body
      })
    }
}
