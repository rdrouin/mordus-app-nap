import React, { Component } from "react";
import Fetcher from './Fetcher'
import Main from './Main'
import ReactTable from 'react-table'

import {
  Route,
  Redirect,
  withRouter,
} from "react-router-dom";

class Alert extends Component {
  constructor(props) {
      super(props);
      this.state = { alert: []};

      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
      this.fetchFlights();
    }

    handleChange(event) {
      var index = event.target.id;
      index = index.replace("input", "");
      var state = this.state;
      state[index] = event.target.value;
      this.setState(state);
      this.fetchFlights();
    }

    handleSubmit(event) {
      //alert('The following flights are ' + this.state.inputs);
      var fetcher = Fetcher.getInstance();
      //fetcher.fetch('flights')
      console.log('Sending results');
      let formdata = new FormData();
      formdata.append('alert', this.state.username)
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
            fetcher.setIsAdmin(data['isAdmin']);
            fetcher.setIsNav(data['isNav']);
            this.props.view();
          }
        }
        this.props.history.push("/");
      })

      event.preventDefault();
    }

    render() {
      const columns = [{
      Header: 'Time',
      accessor: 'cap_timestamp' // String-based value accessors!
    }, {
      Header: 'Capacity',
      accessor: 'cap_value' // String-based value accessors!
    },
    {
      Header: 'Demand',
      accessor: 'demand' // String-based value accessors!
    },
    {
        id: 'button',
        accessor: 'cap_timestamp',
        Cell: ({value}) => (<button onClick={()=>{this.editRow(value)}}>ALERT</button>)
    }]

    return (
      <div>
        <h2>Flight schedule</h2>
        <ReactTable
          data={this.state.alert}
          columns={columns}
        />
      </div>
    );
    }

    editRow(id){
      var fetcher = Fetcher.getInstance();
      console.log('Fetching')
      let formdata = new FormData();
      formdata.append('alert', id)
      fetcher.postfetch('alert', formdata)
      .then(results => {
        return results.json();
      }).then(data => {
        console.log(data)
      })
    }

    fetchFlights(){
      var fetcher = Fetcher.getInstance();
      //fetcher.fetch('flights')
      console.log('Fetching')
      fetcher.fetch('alert')
      .then(results => {
        console.log(results);
        return results.json();
      }).then(data => {
        this.setState(data);
        console.log(this.state)
      })
    }
}

export default withRouter(Alert);
