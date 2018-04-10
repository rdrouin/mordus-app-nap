import React, { Component } from "react";
import Fetcher from './Fetcher'
import Select from 'react-select';
import 'react-select/dist/react-select.css';

class Assign extends Component {
  constructor(props) {
      super(props);
      this.state = { inputs: [] ,
                      options:['test']};
      this.options = ['test1', 'test2']

      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
      this.fetchAssignation();
    }

  handleChange(id, event) {
    console.log('hey')
    console.log(event)
    var index = id;
    var state = this.state;
    console.log(state)
    state['inputs'][index] = event.value;
    this.setState(state);
  }

  handleSubmit(event) {

    //alert('The following flights are ' + this.state.inputs);
    var fetcher = Fetcher.getInstance();
    //fetcher.fetch('flights')
    console.log('Sending results');
    let formdata = new FormData();
    formdata.append('values', JSON.stringify(this.state.inputs))
    fetcher.postfetch('assign', formdata)
    .then(results => {
      return results.json();
    }).then(data => {
      console.log(data);
    })

    event.preventDefault();
  }

  render() {
    return (
      <div>
        <h2>Assign flights</h2>
        <form onSubmit={this.handleSubmit}>
                   <div id="dynamicInput">
                       {this.state.inputs.map((input, index)=> <Select
        name="form-field-name"
        id={index}
        value={input}
        onChange={this.handleChange.bind(this, index)}
        options={this.state.options}
      />)}
                   </div>
                   <input type="submit" value="Submit" />
               </form>
      </div>
    );
  }

  _onSelect(){

  }

  fetchAssignation(){
    var fetcher = Fetcher.getInstance();
    //fetcher.fetch('flights')
    console.log('Fetching1')
    fetcher.fetch('assign')
    .then(results => {
      return results.json();
    }).then(data => {
      console.log(data)
      this.setState({ inputs: Array(data.flightCount).join(".").split("."),
                      options:data.flights});
    })
  }

}

export default Assign;
