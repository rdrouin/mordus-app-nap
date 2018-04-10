import React, { Component } from "react";
import Fetcher from './Fetcher'
import Main from './Main'
import ReactTable from 'react-table'

import {
  Route,
  Redirect,
  withRouter,
} from "react-router-dom";

class Rules extends Component {
  constructor(props) {
      super(props);
      this.state = {};

      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
      this.fetchRules();
    }

    handleChange(event) {
      var state = this.state;
      var id = event.target.id.split(',')
      id[1] = id[1] - state['rules'][0]['id']
      state['rules'][id[1]][id[0]] = event.target.value;
      this.setState(state);
    }

    handleSubmit(event) {
      //alert('The following flights are ' + this.state.inputs);
      var fetcher = Fetcher.getInstance();
      //fetcher.fetch('flights')
      console.log('Sending results');
      let formdata = new FormData();
      formdata.append('rules', JSON.stringify(this.state.rules))
      fetcher.postfetch('rules', formdata)
      .then(results => {
        return results.json();
      }).then(data => {
          this.fetchRules();
      })

      event.preventDefault();
    }

    render(){
      const columns = [
        {
  header: '#',
  columns: [{
    accessor: 'id',
    render: row => {
      return <div>{row}</div>;
    },
    width: 40,
    hideFilter: false
  }]
},{
      Header: 'Capacity from',
      id: 'capacity_from',
      accessor: d => [d.drag_capacity_from, d.id], // String-based value accessors!
      Cell: ({value}) => (<input onChange={this.handleChange} id={['drag_capacity_from', value[1]]} value={value[0]}></input>)
    },
    {
      Header: 'Capacity to',
      id: 'capacity_to',
      accessor: d => [d.drag_capacity_to, d.id], // String-based value accessors!
      Cell: ({value}) => (<input onChange={this.handleChange} id={['drag_capacity_to', value[1]]} value={value[0]}></input>)
    },
    {
      Header: 'Data type',
      id: 'drag_type',
      accessor: d => [d.drag_type, d.id], // String-based value accessors!
      Cell: ({value}) => (<input onChange={this.handleChange} id={['drag_type', value[1]]} value={value[0]}></input>)
    },
    {
      Header: 'Data value',
      id: 'drag_value',
      accessor: d => [d.drag_value, d.id], // String-based value accessors!
      Cell: ({value}) => (<input onChange={this.handleChange} id={['drag_value', value[1]]} value={value[0]}></input>)
    }]

    return (
      <div>
        <h2>Flight schedule</h2>
        <button onClick={this.handleSubmit} >Commit </button>
        <ReactTable
          data={this.state.rules}
          columns={columns}
        />
      </div>
    );
  }

  fetchRules(){
    var fetcher = Fetcher.getInstance();
    //fetcher.fetch('flights')
    console.log('Fetching')
    fetcher.fetch('rules')
    .then(results => {
      console.log(results);
      return results.json();
    }).then(data => {
      this.setState(data);
      console.log(this.state)
    })
  }
}

export default withRouter(Rules);
