import React, { Component } from "react";
import Fetcher from './Fetcher'
import Main from './Main'

import {
  Route,
  Redirect,
  withRouter,
} from "react-router-dom";

class Login extends Component {
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
      //alert('The following flights are ' + this.state.inputs);
      var fetcher = Fetcher.getInstance();
      //fetcher.fetch('flights')
      console.log('Sending results');
      let formdata = new FormData();
      formdata.append('username', this.state.username)
      formdata.append('password', this.state.password)
      formdata.append('transporter', this.state.transporter)
      fetcher.postfetch('login', formdata)
      .then(results => {
        return results.json();
      }).then(data => {
        if ('auth' in data) {
          if (data['auth'] == 'ok'){
            console.log(data)
            var fetcher = Fetcher.getInstance();
            fetcher.setUserID(data['username']);
            fetcher.setUserToken(data['token']);
            this.props.view();
          }
        }
        this.props.history.push("/");
      })

      event.preventDefault();
    }

    render() {
      // TODO create a drop list for available carriers
      if (!this.state.isLogged){
        return (
        <div>
          <h2>Login</h2>
          <form onSubmit={this.handleSubmit}>
                         <label>Username: </label><input type="text" value={this.state.username} id="username" onChange={this.handleChange}/><br/>
                         <label>Password: </label><input type="password" value={this.state.password} id="password" onChange={this.handleChange}/><br/>
                     <input type="submit" value="Submit" />
                 </form>
        </div>
      );
    }else {
        return <Redirect to='/' />
      }
    }
}

export default withRouter(Login);
