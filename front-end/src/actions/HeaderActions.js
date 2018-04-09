import {
  REQUEST_HEADER,
  RECEIVE_HEADER,
  FILTER_HEADER
} from '../constants/Header'

function requestHeader() {
  return {
    type: REQUEST_HEADER
  }
}

function receiveHeader(json) {
  return {
    type: RECEIVE_HEADER,
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

export function filterHeader(searchTerm) {
  return {
    type: FILTER_HEADER,
    searchTerm
  }
}
