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
  fetcher = null;
  constructor(props) {
      super(props);
      this.state = {isLogged: true};
      this.updateState();
    }

  updateState(){
    var fetcher = Fetcher.getInstance();
    var state = this.state;
    console.log('here');
    console.log(fetcher.isLogged());
    state['isLogged'] = fetcher.isLogged();
    this.setState(state);
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
          <li><NavLink to="/register"><a aria-current="true" href="#/register" class="active">Register</a></NavLink></li>
          {!this.state.isLogged ?
            <li><NavLink to="/login"><a aria-current="true" href="#/login" class="active">Login</a></NavLink></li>:
            <li><NavLink to="/logout"><a aria-current="true" href="#/logout" class="active">Logout</a></NavLink></li>}
          </ul>
          <div className="content">
            <Route exact path="/" component={Home}/>
            <Route path="/assign" component={Assign}/>
            <Route path="/contact" component={Contact}/>
            <Route path="/register" component={Register}/>
            <Route path="/login" component={Login}/>
            <Route path="/logout" component={Logout}/>
          </div>
        </div>
        </HashRouter>
    );
  }
}

export default Main;
