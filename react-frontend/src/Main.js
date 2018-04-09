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

class Main extends Component {
  render() {
    return (
      <HashRouter>
        <div>
          <h1>Simple SPA</h1>
          <ul className="header">
          <li><NavLink exact to="/"><a aria-current="true" href="#/" class="active">Home</a></NavLink></li>
          <li><NavLink to="/assign"><a aria-current="true" href="#/assign" class="active">Assign</a></NavLink></li>
          <li><NavLink to="/contact"><a aria-current="true" href="#/contact" class="active">Contact</a></NavLink></li>
          <li><NavLink to="/register"><a aria-current="true" href="#/register" class="active">Register</a></NavLink></li>
          </ul>
          <div className="content">
            <Route exact path="/" component={Home}/>
            <Route path="/assign" component={Assign}/>
            <Route path="/contact" component={Contact}/>
            <Route path="/register" component={Register}/>
          </div>
        </div>
        </HashRouter>
    );
  }
}

export default Main;
