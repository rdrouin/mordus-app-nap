export default class Fetcher {

    static myInstance = null;

    _userID = "";


    /**
     * @returns {CommonDataManager}
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

    fetch(url, method='get'){
      return fetch('http://localhost:8932/' + url, {
        method: method,
        headers: {
          Accept: 'application/json',
          "api_username": 1,
          "api_access_token" : "123",
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