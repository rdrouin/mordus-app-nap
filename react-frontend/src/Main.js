import React, { Component } from "react";
import {
  Route,
  NavLink,
  HashRouter
} from "react-router-dom";
import Home from "./Home";
import Assign from "./Assign";
import Contact from "./Contact";
import Register from "./Register";
import Login from "./Login";
import Logout from "./Logout";
import Fetcher from './Fetcher'

class Main extends Component {
  static myInstance = null;

  /**
   * @returns {Main}
   */
  static getInstance() {
      if (this.myInstance == null) {
          this.myInstance = new Main();
      }

      return this.myInstance;
  }

  fetcher = null;
  constructor(props) {
      super(props);
      this.myInstance = this;
      this.state = {isLogged: true};
      //this.updateState();
    }

  updateState(){
    var fetcher = Fetcher.getInstance();
    var state = this.state;
    console.log('here');
    console.log(fetcher.isLogged());
    state['isLogged'] = fetcher.isLogged();
    state['isAdmin'] = fetcher.isAdmin();

    this.setState(state);
    
  }

  handler(e) {
    e.preventDefault();
    this.updateState();
  }

  render() {
    return (
      <HashRouter>
        <div>
          <h1>Simple SPA</h1>
          <ul className="header">
          <li><NavLink exact to="/"><a aria-current="true" href="#/" class="active" hidden="true">Home</a></NavLink></li>
          <li><NavLink to="/assign"><a aria-current="true" href="#/assign" class="active">Assign</a></NavLink></li>
          <li><NavLink to="/contact"><a aria-current="true" href="#/contact" class="active">Contact</a></NavLink></li>
          {this.state.isAdmin ? <li><NavLink to="/register"><a aria-current="true" href="#/register" class="active">Register</a></NavLink></li> : null}
          {!this.state.isLogged ?
            <li><NavLink to="/login"><a aria-current="true" href="#/login" class="active">Login</a></NavLink></li>:
            <li><NavLink to="/logout"><a aria-current="true" href="#/logout" class="active">Logout</a></NavLink></li>}
          </ul>
          <div className="content">
            <Route exact path="/" component={Home}/>
            <Route path="/assign" component={Assign}/>
            <Route path="/contact" component={Contact}/>
            {this.state.isAdmin ? <Route path="/register" component={Register}/> : null}
            {!this.state.isLogged ? <Route path="/login" render={(props) => (
              <Login {...props} view={this.updateState.bind(this)} />)}/> :
            <Route path="/logout" render={(props) => (
              <Logout {...props} view={this.updateState.bind(this)} />)}/>}
          </div>
        </div>
        </HashRouter>
    );
  }
}

export default Main;
