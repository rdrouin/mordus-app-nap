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
import Capacity from './Capacity'
import Alert from './Alert'
import Rules from './Rules'
import Master from './Master'
import LogoImg from './img/adm.jpg';

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
      this.updateState();
    }

  updateState(){
    var fetcher = Fetcher.getInstance();
    var state = this.state;
    console.log('here');
    console.log(fetcher.isLogged());
    state['isLogged'] = fetcher.isLogged();
    state['isAdmin'] = fetcher.isAdmin();
    state['isNav'] = fetcher.isNav();
    state['user'] = fetcher.getUserID();

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
          <img src={LogoImg} />
          <h1>Visualisateur de vols</h1>
          {this.state.isLogged ?
          <h2>Bonjour - {this.state.user}</h2>:null}
          <ul className="header">
          <li><NavLink exact to="/"><a aria-current="true" href="#/" class="active" hidden="true">Horaire</a></NavLink></li>
          {this.state.isLogged && !this.state.isAdmin && !this.state.isNav && this.state.user != 'sgat'  ? <li><NavLink to="/assign"><a aria-current="true" href="#/assign" class="active">Assignation</a></NavLink></li> : null}
          {this.state.isLogged && this.state.user == 'sgat' ? <li><NavLink to="/alert"><a aria-current="true" href="#/alert" class="active">Alerte</a></NavLink></li> : null}
          {this.state.isLogged && this.state.isAdmin? <li><NavLink to="/rules"><a aria-current="true" href="#/rules" class="active">Règles</a></NavLink></li> : null}
          {this.state.isAdmin ? <li><NavLink to="/register"><a aria-current="true" href="#/register" class="active">Nouvel usager</a></NavLink></li> : null}
            {this.state.isNav ?
              <li><NavLink to="/nav"><a aria-current="true" href="#/nav" class="active">Capacité</a></NavLink></li>: null}
          {false ? <li><NavLink to="/contact"><a aria-current="true" href="#/contact" class="active">Contact</a></NavLink></li>:null}
          <li><NavLink to="/master"><a aria-current="true" href="#/master" class="active">Temporel</a></NavLink></li>
          {!this.state.isLogged ?
            <li><NavLink to="/login"><a aria-current="true" href="#/login" class="active">Se connecter</a></NavLink></li>:
            <li><NavLink to="/logout"><a aria-current="true" href="#/logout" class="active">Se déconnecter</a></NavLink></li>}
          </ul>
          <div className="content">
            <Route exact path="/" component={Home}/>
            <Route path="/assign" component={Assign}/>
            <Route path="/contact" component={Contact}/>
            <Route path="/alert" component={Alert}/>
            <Route path="/rules" component={Rules}/>
            <Route path="/master" component={Master}/>
            {this.state.isAdmin ? <Route path="/register" component={Register}/> : null}
            {this.state.isNav ? <Route path="/nav" component={Capacity}/> : null}
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
