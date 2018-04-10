import React, { Component } from "react";
import Fetcher from './Fetcher'

class Logout extends Component {
  constructor(props) {
      super(props);

      var fetcher = Fetcher.getInstance();
      fetcher.logout();
    }

    render() {
      // TODO create a drop list for available carriers
      return (
        <div>
          <h2>You have logged out</h2>
        </div>
      );
    }
}

export default Logout;
