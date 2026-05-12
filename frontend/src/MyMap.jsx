import {APIProvider, Map, AdvancedMarker} from '@vis.gl/react-google-maps';
import { useState, useEffect } from "react"

export default function MyMap({ onSelect, onLogout }){
  const [restaurants, setRestaurants] = useState([])
  const [selected, setSelected] = useState(null)
  const [hovering, setHovering] = useState(null)

  useEffect(() => {
    const fetchRestaurants = async ()=>{
    const res = await fetch("http://localhost:5000/api/restaurants?lat=36.0189&lng=-78.9206")
    const data = await res.json()
    if (res.ok) {
      setRestaurants(data.places)
      setRestaurants([...data.places, {
        id: "quickly-tea-house",
        displayName: { text: "Quickly Tea House" },
        location: { latitude: 36.010893584481494, longitude: -78.92888121318308 },
        formattedAddress: "2604A Hillsborough Rd, Durham, NC 27705"
      }])
      console.log(data)
    } else {
        alert(data.error)
    }
  }
  fetchRestaurants()
  }, [])
  // console.log(restaurants)
  // console.log(selected)

  return (
  <APIProvider apiKey={import.meta.env.VITE_GOOGLE_MAPS_API_KEY} onLoad={() => console.log('Maps API has loaded.')}>
      <button onClick={onLogout} style={{position: "absolute", top: 10, right: 10, zIndex: 999}}>
        Logout
      </button>
    <div style={{height: '100vh', width: '100%'}}>
        <Map
            defaultZoom={15}
            defaultCenter={ { lat: 36.0189, lng: -78.9206 } }
            mapId = {'a3703dc5223b10a9666982fe'}
            disableDefaultUI
            >
            
            <AdvancedMarker position={{lat: 36.0189, lng: -78.9206}}>
              NCSSM
            </AdvancedMarker>
            {(restaurants || []).map(r => (
              <AdvancedMarker key={r.id}
                position={{lat: r.location.latitude, lng: r.location.longitude}}
                clickable={true}
                onClick={() => onSelect(r)}
                onMouseEnter={() => setHovering(r)}
                onMouseLeave={() => setHovering(null)}>
                  <div style={{ background: "white", padding: "2px 6px", borderRadius: 4, fontSize: 12, fontWeight: "bold" }}>
                    {r.displayName.text}
                  </div>
                </AdvancedMarker>))}
        </Map>
    </div>
  </APIProvider>
  )
}
