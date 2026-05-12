import { useState } from 'react'
import Login from './Login'
import {APIProvider} from '@vis.gl/react-google-maps';
import MyMap from './MyMap'
import RestaurantDetail from './RestaurantDetail'

function App() {
  const [user, setUser] = useState(() => {
    const token = localStorage.getItem("token")
    return token ? { token } : null
  })
  const logout = () => {
    localStorage.removeItem("token")
    setUser(null)
  }
  const [selected, setSelected] = useState(null)

  if (!user) return <Login onLogin={setUser} />
  if (selected) return <RestaurantDetail restaurant={selected} onBack={() => setSelected(null)} />
  return <MyMap onSelect={setSelected} onLogout={logout}/> 

  // return <MyMap />
}

export default App
