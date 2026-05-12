import {APIProvider, Map, AdvancedMarker} from '@vis.gl/react-google-maps';

export default function MyMap(){
  return (
  <APIProvider apiKey={import.meta.env.VITE_GOOGLE_MAPS_API_KEY} onLoad={() => console.log('Maps API has loaded.')}>
    <div style={{height: '100vh', width: '100%'}}>
        <Map
            defaultZoom={15}
            defaultCenter={ { lat: 36.0189, lng: -78.9206 } }
            mapId = {'a3703dc5223b10a9666982fe'}
            disableDefaultUI
            >
            
            <AdvancedMarker position={{lat: 36.0189, lng: -78.9206}} />
        </Map>
    </div>
  </APIProvider>
  )
}
