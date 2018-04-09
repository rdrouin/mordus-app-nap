import React, { Component } from 'react'
import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'
import Pokemon from '../components/Pokemon'
import Search from '../components/Search'

import ReactTable from 'react-table'
import * as headerActions from '../actions/HeaderActions'

class Page extends Component {
  componentDidMount() {
    this.props.headerActions.fetchHeader()
  }

  handleSearch(e) {
    this.props.headerActions.filterHeader(e.target.value)
  }

  render() {

    // TODO take data from server
    const data = "User jean-guy"

  return(<ul id="menu">
          <li><button type="button" onClick={homeClick}>Homepage</button></li>
          <li><button type="button" onClick={assignationClick}>Assignation</button></li>
          <li>{data}</li>
          <li><button type="button" onClick={signoutClick}>Sign out</button></li>
        </ul>)
  }
}

function signoutClick(e) {
  e.preventDefault();
  console.log('Signout clicked');
}

function homeClick(e) {
  e.preventDefault();
  console.log('Homepage clicked');
}

function assignationClick(e) {
  e.preventDefault();
  console.log('Assignation clicked');
}

function mapStateToProps(state) {
  return {
    page: state.page
  }
}

function mapDispatchToProps(dispatch) {
  return {
    headerActions: bindActionCreators(headerActions, dispatch)
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Page)
