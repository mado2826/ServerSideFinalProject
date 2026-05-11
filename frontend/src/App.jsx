import { useState } from 'react'
import Login from './Login'
import {APIProvider} from '@vis.gl/react-google-maps';
import MyMap from './MyMap'

console.log(import.meta.env.VITE_GOOGLE_CLIENT_ID)

function App() {
  const [user, setUser] = useState(0)

  if (!user) return <Login onLogin={setUser} />

  return <MyMap />
}

export default App
