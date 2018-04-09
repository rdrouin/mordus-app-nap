import {
  REQUEST_ASSIGNATION,
  RECEIVE_ASSIGNATION
} from '../constants/Assignation'

function requestHeader() {
  return {
    type: REQUEST_ASSIGNATION
  }
}

function receiveHeader(json) {
  return {
    type: RECEIVE_ASSIGNATION,
    Header: json.results
  }
}

export function fetchHeader() {

  return dispatch => {
    dispatch(requestHeader())
    /*return fetch(`https://pokeapi.co/api/v2/pokemon/?limit=784`)
      .then(response => response.json())
      .then(json => dispatch(receiveHeader(json)))*/
  }

}
