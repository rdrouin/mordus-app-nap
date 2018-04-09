import React, { Component } from 'react'
import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'
import Pokemon from '../components/Pokemon'
import Search from '../components/Search'

import ReactTable from 'react-table'
import * as pageActions from '../actions/PageActions'

class Page extends Component {
  componentDidMount() {
    this.props.pageActions.fetchPokemons()
  }

  handleSearch(e) {
    this.props.pageActions.filterPokemons(e.target.value)
  }

  render() {

    // TODO take data from server
    const data = [{
    hour: '5:30',
    flight: 'DC1564',
    destination: 'YPS'
  },
  {
  hour: '5:35',
  flight: 'AA9944',
  destination: 'GBD'
  }]

  const columns = [{
    Header: 'Hour',
    accessor: 'hour' // String-based value accessors!
  }, {
    Header: 'Flight number',
    accessor: 'flight',
    Cell: props => <span className='number'>{props.value}</span> // Custom cell components!
  }, {
    Header: 'Destination',
    accessor: 'destination'
  }]

  return(<ReactTable
    data={data}
    columns={columns}
  />)
  }
}

function mapStateToProps(state) {
  return {
    page: state.page
  }
}

function mapDispatchToProps(dispatch) {
  return {
    pageActions: bindActionCreators(pageActions, dispatch)
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Page)
