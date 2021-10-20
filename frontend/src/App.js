import React, {useContext} from 'react'
import {GlobalContext} from './context/Provider'

function App() {
    const {user} = useContext(GlobalContext)
    console.log(user)
    return (
        <>
            <div>Hello</div>
            <h1>{user}</h1>
        </>
    )
}

export default App
