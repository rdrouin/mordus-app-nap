import React from 'react'
import { render } from 'react-dom'
import { Provider } from 'react-redux'
import Page from './containers/Page'
import Header from './containers/Header'
import './style/main.css'
import configureStore from './store/configureStore'

const store = configureStore()

render(
  <Provider store={store}>
    <Page />
  </Provider>,
  document.getElementById('root')
)

render(
  <Provider store={store}>
    <Header />
  </Provider>,
  document.getElementById('header')
)
