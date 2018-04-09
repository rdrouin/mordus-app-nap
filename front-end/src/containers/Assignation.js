import React, { Component } from 'react'
import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'
import Assignation from '../components/Assignation'

import ReactTable from 'react-table'
import * as assignationActions from '../actions/AssignationActions'

class Page extends Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};
  }

  setState(state){
    this.state = state
  }

  componentDidMount() {
    this.props.assignationActions.fetchHeader()
  }

  handleSearch(e) {
    this.props.assignationActions.filterHeader(e.target.value)
  }

  onTodoChange(val) {
    this.setState({value: val});
  }

  AcceptAssignation(event) {
    console.log('A name was submitted: ' + this.state.value);
    alert('A name was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return(<form onSubmit={this.AcceptAssignation}>
            <label>
              <input type="text" value={this.state.name1} onChange={e => this.onTodoChange(e.target.value)}/>
              <input type="text" value={this.state.name2} onChange={e => this.onTodoChange(e.target.value)}/>
            </label>
            <input type="submit" value="Submit" />
          </form>
        )
  }
}


function mapStateToProps(state) {
  return {
    page: state.page
  }
}

function mapDispatchToProps(dispatch) {
  return {
    assignationActions: bindActionCreators(assignationActions, dispatch)
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Page)
