import React, { Component } from "react";
import Fetcher from './Fetcher'

class Assign extends Component {
  constructor(props) {
      super(props);
      this.state = { inputs: [] };

      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
      this.fetchAssignation();
    }

  handleChange(event) {
    var index = event.target.id;
    index = index.replace("input", "");
    var state = this.state;
    state['inputs'][index] = event.target.value;
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
                       {this.state.inputs.map((input, index)=> <input type="text" value={input} id={"input" + index} onChange={this.handleChange} />)}
                   </div>
                   <input type="submit" value="Submit" />
               </form>
      </div>
    );
  }

  fetchAssignation(){
    var fetcher = Fetcher.getInstance();
    //fetcher.fetch('flights')
    console.log('Fetching1')
    fetcher.fetch('assign')
    .then(results => {
      return results.json();
    }).then(data => {
      this.setState({ inputs: Array(data.flightCount).join(".").split(".")});
    })
  }

  appendInput() {
        var newInput = `input-${this.state.inputs.length}`;
        this.setState({ inputs: this.state.inputs.concat([newInput]) });
    }


}

export default Assign;
