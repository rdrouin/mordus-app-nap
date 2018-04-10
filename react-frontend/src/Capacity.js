import React, { Component } from "react";
import Fetcher from './Fetcher'
import Main from './Main'

import {
  Route,
  Redirect,
  withRouter,
} from "react-router-dom";

class Capacity extends Component {
  constructor(props) {
      super(props);
      this.state = {'capacity' : []};

      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
      this.fetchCapacities()
    }

    handleChange(event) {
      var index = event.target.id;
      index = index.replace("input", "");
      var state = this.state;
      state['capacity'][index]['cap_value'] = event.target.value;
      this.setState(state);
    }

    fetchCapacities(){
      var fetcher = Fetcher.getInstance();
      //fetcher.fetch('flights')
      console.log('Fetching1')
      fetcher.fetch('capacity')
      .then(results => {
        return results.json();
      }).then(data => {
        console.log(data);
        this.setState(data);
      })
    }

    handleSubmit(event) {
      //alert('The following flights are ' + this.state.inputs);
      var fetcher = Fetcher.getInstance();
      //fetcher.fetch('flights')
      console.log('Sending results');
      console.log(this.state);
      let formdata = new FormData();
      formdata.append('json', JSON.stringify(this.state))
      fetcher.postfetch('capacity', formdata)
      .then(results => {
        return results.json();
      }).then(data => {
        if ('auth' in data) {
          if (data['auth'] == 'ok'){
            console.log(data)
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
          <h2>Capacité</h2>
          <form onSubmit={this.handleSubmit}>
              <div id="dynamicInput">
                  {this.state.capacity.map((input, index)=> <div><label>{input.cap_timestamp}</label> <input type="text" value={input.cap_value} id={"input" + index} onChange={this.handleChange} /> <br/> </div>)}
              </div>
                     <input type="submit" value="Entrer" />
                 </form>
        </div>
      );
    }else {
        return <Redirect to='/' />
      }
    }
}

export default withRouter(Capacity);
