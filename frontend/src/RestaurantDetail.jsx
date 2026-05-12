export default function RestaurantDetail({ restaurant, onBack }) {
  const hours = restaurant.currentOpeningHours?.weekdayDescriptions

  return (
    <div>
      <button onClick={onBack}>← Back to Map</button>
      <h1>{restaurant.displayName.text}</h1>
      <p>{restaurant.formattedAddress}</p>
      <p>Price: ${restaurant.priceRange?.startPrice.units} - ${restaurant.priceRange?.endPrice.units}</p>
      <p>{restaurant.currentOpeningHours?.openNow ? "Open Now" : "Closed"}</p>

      <h3>Hours</h3>
      {hours ? (
        <ul>
          {hours.map((day, i) => <li key={i}>{day}</li>)}
        </ul>
      ) : <p>Hours not available</p>}
    </div>
  )
}