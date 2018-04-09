import {
  REQUEST_ASSIGNATION,
  RECEIVE_ASSIGNATION
} from '../constants/Assignation.js'

const initialState = {
  isFetched: false,
  pokemons: [],
  displayedPokemons: []
}

export default function assignation(state = initialState, action) {

  switch (action.type) {
    case REQUEST_ASSIGNATION:
      return {
        ...state,
        isFetched: true
      }

    case RECEIVE_ASSIGNATION:
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

    default:
      return state
  }

}
