import { combineReducers } from 'redux'
import page from './page'
import header from './header'
import assignation from './assignation'

export default combineReducers({
  page,
  header,
  assignation
})
