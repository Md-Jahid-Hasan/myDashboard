import React, {createContext, useReducer} from 'react'
import { authInititalState, taskInitialState } from './initialState'
import { auth, task } from './reducers'

export const GlobalContext = createContext({})

const GlobalProvider = ({children}) => {
    const [authState, authDispatch] = useReducer(auth, authInititalState)
    const [taskState, taskDispatch] = useReducer(task, taskInitialState)

    return (
        <GlobalContext.Provider value={{...authState, authDispatch, taskState, taskDispatch}}>
            {children}
        </GlobalContext.Provider>
    )
}

export default GlobalProvider
