import {
  REQUEST_HEADER,
  RECEIVE_HEADER,
  FILTER_HEADER
} from '../constants/Header.js'

const initialState = {
  isFetched: false,
  pokemons: [],
  displayedPokemons: []
}

export default function pokemon(state = initialState, action) {

  switch (action.type) {
    case REQUEST_HEADER:
      return {
        ...state,
        isFetched: true
      }

    case RECEIVE_HEADER:
      let pokemons = action.pokemons.map(pokemon => {
        let { url } = pokemon
        pokemon.id = url.substring(34, url.length - 1)

        return pokemon
      })

      return {
        ...state,
        pokemons,
        displayedPokemons: pokemons.slice(0, 60),
        isFetched: false
      }

    case FILTER_HEADER:
      let displayedPokemons = state.pokemons.filter(pokemon => {
        if (pokemon.name.includes(action.searchTerm.toLowerCase())) {
          return true
        }

        return false
      }).slice(0, 60)

      return {
        ...state,
        displayedPokemons
      }

    default:
      return state
  }

}
