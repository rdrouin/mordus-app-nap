import React, { Component } from "react";
import Fetcher from './Fetcher'

class Register extends Component {
  constructor(props) {
      super(props);
      this.state = { username: "", password: "", transporter: "" };

      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
      this.fetchAssignation();
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
      fetcher.postfetch('register', formdata)
      .then(results => {
        return results.json();
      }).then(data => {
        console.log(data);
      })

      event.preventDefault();
    }

    render() {
      // TODO create a drop list for available carriers
      return (
        <div>
          <h2>Register a new user</h2>
          <form onSubmit={this.handleSubmit}>
                         <label>Username: </label><input type="text" value={this.state.username} id="username" onChange={this.handleChange}/><br/>
                         <label>Password: </label><input type="password" value={this.state.password} id="password" onChange={this.handleChange}/><br/>
                         <label>Carrier: </label><input type="text" value={this.state.transporter} id="transporter" onChange={this.handleChange}/><br/>
                     <input type="submit" value="Submit" />
                 </form>
        </div>
      );
    }

    fetchAssignation(){
      var fetcher = Fetcher.getInstance();
      //fetcher.fetch('flights')
      console.log('Fetching1')
      fetcher.fetch('assign')
      .then(results => {
        return results.json();
      }).then(data => {
        this.setState({ inputs: Array(data.flightCount).join(".").split(".")});
      })
    }

    appendInput() {
          var newInput = `input-${this.state.inputs.length}`;
          this.setState({ inputs: this.state.inputs.concat([newInput]) });
      }
}

export default Register;
