import React, { Component } from "react";
import Fetcher from './Fetcher'
import Main from './Main'

import {
  Redirect,
} from "react-router-dom";

class Logout extends Component {
  constructor(props) {
      super(props);

      var fetcher = Fetcher.getInstance();
      fetcher.logout();
      console.log(this.props.view);
      this.props.view();
    }

    render() {
      // TODO create a drop list for available carriers
      return <Redirect to='/' />
    }
}

export default Logout;
