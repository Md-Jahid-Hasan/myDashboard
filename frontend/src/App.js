import React, { useContext } from 'react'
import GlobalProvider from './context/Provider'
import { GlobalContext } from './context/Provider'

function App() {
    const {authState} = useContext(GlobalContext)
    return (
        <GlobalProvider>
            {authState.user}
        </GlobalProvider>
    )
}

export default App
