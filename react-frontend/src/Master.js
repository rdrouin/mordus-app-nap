import React, { Component } from "react";
import Fetcher from './Fetcher'
import Main from './Main'

import {
  Route,
  Redirect,
  withRouter,
} from "react-router-dom";

class Master extends Component {
  constructor(props) {
      super(props);
      this.state = { username: "", password: ""};

      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
      var index = event.target.id;
      index = index.replace("input", "");
      var state = this.state;
      state[index] = event.target.value;
      this.setState(state);
    }

    handleSubmit(event) {
      var fetcher = Fetcher.getInstance();
      fetcher.postfetch('horloge')
      .then(results => {
        return results.json();
      }).then(data => {
            console.log(data)
            this.props.history.push("/");
      })

      event.preventDefault();
    }

    handleFindelaContingence(event) {
      var fetcher = Fetcher.getInstance();
      fetcher.postfetch('horloge2')
      .then(results => {
        return results.json();
      }).then(data => {
            console.log(data);
      })

      event.preventDefault();
    }

    render() {
      // TODO create a drop list for available carriers
      if (!this.state.isLogged){
        return (
        <div>
          <h2>Login</h2>
          <button onClick={this.handleSubmit}>Fin de la ronde</button>
          <button onClick={this.handleFindelaContingence}>Fin de la contingence</button>
        </div>
      );
    }else {
        return <Redirect to='/' />
      }
    }
}

export default withRouter(Master);
