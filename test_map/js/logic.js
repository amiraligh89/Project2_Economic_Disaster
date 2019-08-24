
// URL for county lines plates data
countyLink = "counties2018.geojson";
centerLoc = [39.82, -98.58];


// Function that will determine the color of a county based on its unemployment rate
function getColor(d) {
  return d > 13  ? '#800026' :
         d > 11  ? '#bd0026' :
         d > 9   ? '#e31a1c' :
         d > 7   ? '#fc4e2a' :
         d > 6   ? '#fd8d3c' :
         d > 5   ? '#feb24c' :
         d > 4   ? '#fed976' :
         d > 3   ? '#ffeda0' :
          '#ffffcc' 
}


// Adding tile layer
var streetmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
});
console.log("You just added a tile layer to myMap");

// Add a layer for the county boundaries
var countyLayer = new L.LayerGroup();

// Pull in the county geojson file
d3.json(countyLink, function(countyData){
  console.log(countyData);

  // Add a layer with the county outlines.
  L.geoJson(countyData,{
    color: "blue",
    weight: 2
  }).addTo(countyLayer);
/*
  onEachFeature: function(feature, layer) {
    // Setting various mouse events to change style when different events occur
    layer.on({
      // On mouse over, make the feature (neighborhood) more visible
      mouseover: function(event) {
        layer = event.target;
        layer.setStyle({
          fillOpacity: 0.9
        });
      },
      // Set the features style back to the way it was
      mouseout: function(event) {
        geoJson.resetStyle(event.target);
      },
      // When a feature (neighborhood) is clicked, fit that feature to the screen
      click: function(event) {
        map.fitBounds(event.target.getBounds());
      }
    });
    // Giving each feature a pop-up with information about that specific feature
    layer.bindPopup("<h1>" + features.properties.STATEFP + features.properties.COUNTYFP +
     "</h1> <br> <h2>" + features.properties.NAME + "</h2>");
  }
*/

});


// Create a baseMaps object to hold the lightmap layer
var baseMaps = {
  "Light"    : streetmap
};

// Create an overlayMaps object to hold the earthquakes layer
var overlayMaps = {
  "Counties": countyLayer
};


// Create the map object with options
var myMap = L.map("map", {
  center: centerLoc,
  zoom: 4,
  layers: [streetmap]
});

// Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
L.control.layers(baseMaps, overlayMaps, {
  collapsed: false
}).addTo(myMap);
