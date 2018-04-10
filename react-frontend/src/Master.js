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

      this.handleFindelaContingence = this.handleFindelaContingence.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {
      var fetcher = Fetcher.getInstance();
      fetcher.postfetch('horloge')
      .then(results => {
        return results.json();
      }).then(data => {
            console.log(data);
            this.returnHome();
      })

      event.preventDefault();
    }

    handleFindelaContingence(event) {
      var fetcher = Fetcher.getInstance();
      fetcher.postfetch('horloge2')
      .then(results => {
        return results.json();

      }).then(data => {
          this.returnHome();
            console.log(data);
      })

      event.preventDefault();
    }

    returnHome(){
      this.props.history.push("/");
    }

    render() {
      // TODO create a drop list for available carriers
      if (!this.state.isLogged){
        return (
        <div>
          <h2>Maître du temps</h2>
          <button onClick={this.handleSubmit}>Fin de la ronde préliminaire</button>
          <button onClick={this.handleFindelaContingence}>Fin de la deuxième ronde</button>
          <button>Retour à l'état normal</button>
        </div>
      );
    }else {
        return <Redirect to='/' />
      }
    }
}

export default withRouter(Master);
