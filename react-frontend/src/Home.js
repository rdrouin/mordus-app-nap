import React, { Component } from "react";
import ReactTable from 'react-table'
import Websocket from 'react-websocket';
import Fetcher from './Fetcher'

class Home extends Component {
  constructor(props) {
      super(props);
      this.state = { flights: [] };
      this.fetchFlights();

      /*this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);*/
    }

    handleData(data) {
      this.setState(data);
    }

  render() {
    const columns = [{
      Header: 'Heure',
      accessor: 'time' // String-based value accessors!
    }, {
      Header: 'Numéro du vol',
      accessor: 'flightNumber' // String-based value accessors!
    },
    {
      Header: 'Destination',
      accessor: 'destination' // String-based value accessors!
    },
    {
      Header: 'Type',
      accessor: 'status' // String-based value accessors!
    }]

    return (
      <div>
        <h2>Départs</h2>
        <ReactTable
          data={this.state.flights}
          columns={columns}
        />
      </div>
    );
  }

  fetchFlights(){
    var fetcher = Fetcher.getInstance();
    //fetcher.fetch('flights')
    console.log('Fetching')
    fetcher.fetch('flights')
    .then(results => {
      return results.json();
    }).then(data => {
      this.setState(data);
    })

  }
}

export default Home;
