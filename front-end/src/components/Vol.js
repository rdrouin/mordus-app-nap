import React from 'react'

const Vol = ({ vol }) => (
  <li className="vol_item">
    <button
      type="button"
      className="pokemons__sprite"
      style={{
        backgroundImage: `url(${`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pokemon.id}.png`})`
      }}
    />
    <p className="pokemons__name">{pokemon.name}</p>
  </li>
)

export default Pokemon
