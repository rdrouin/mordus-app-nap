import React, { Component } from "react";

class Assign extends Component {
  constructor(props) {
      super(props);
      this.state = { inputs: ["text"] };

      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }

  handleChange(event) {
    var index = event.target.id;
    index = index.replace("input", "");
    var state = this.state;
    state['inputs'][index] = event.target.value;
    this.setState(state);
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.inputs);
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
               <button onClick={ () => this.appendInput() }>
                   CLICK ME TO ADD AN INPUT
               </button>
      </div>
    );
  }

  appendInput() {
        var newInput = `input-${this.state.inputs.length}`;
        this.setState({ inputs: this.state.inputs.concat([newInput]) });
    }


}

export default Assign;
