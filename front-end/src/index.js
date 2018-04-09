import React from 'react'
import { render } from 'react-dom'
import { Provider } from 'react-redux'
import Page from './containers/Page'
import Header from './containers/Header'
import Assignation from './containers/Assignation'
import './style/main.css'
import configureStore from './store/configureStore'

const store = configureStore()


render(
  <Provider store={store}>
    <Page />
  </Provider>,
  document.getElementById('root_list')
)

render(
  <Provider store={store}>
    <Header />
  </Provider>,
  document.getElementById('header')
)

render(
  <Provider store={store}>
    <Assignation />
  </Provider>,
  document.getElementById('root_assignation')
)
