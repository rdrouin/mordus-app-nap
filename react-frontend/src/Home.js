import React, { Component } from "react";
import ReactTable from 'react-table'

class Home extends Component {
  render() {

    var data = this.fetchFlights();
    const columns = [{
      Header: 'Time',
      accessor: 'time' // String-based value accessors!
    }, {
      Header: 'FlightNumber',
      accessor: 'flight' // String-based value accessors!
    },
    {
      Header: 'Destination',
      accessor: 'destination' // String-based value accessors!
    }]

    return (
      <div>
        <h2>Flight schedule</h2>
        <ReactTable
          data={data}
          columns={columns}
        />

      </div>
    );
  }

  fetchFlights(){
    const data=[{'time':'5:30', 'flight':'AC143', 'destination':'YPO'},{'time':'5:35', 'flight':'GC443', 'destination':'STO'}]
    return data;

  }
}

export default Home;
