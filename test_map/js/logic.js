
// URL for county lines plates data
countyLink = "CountiesPlusUnemp2018.geojson";
centerLoc = [39.82, -98.58];


// Function that will determine the color of a county based on its unemployment rate
function getColor(d) {
  //console.log(d);
  return d > 10  ? '#800026' :
         d > 8   ? '#bd0026' :
         d > 6   ? '#e31a1c' :
         d > 5   ? '#fc4e2a' :
         d > 4   ? '#fd8d3c' :
         d > 3   ? '#feb24c' :
         d > 2   ? '#fed976' :
         d > 1   ? '#ffeda0' :
          '#ffffcc' 
}
function getColor2(d) {
  //console.log(d);
  return d > 10  ? '#543005' :
         d > 8   ? '#8c510a' :
         d > 8   ? '#bf812d' :
         d > 6   ? '#dfc27d' :
         d > 5   ? '#f6e8c3' :
         d > 4   ? '#c7eae5' :
         d > 3   ? '#80cdc1' :
         d > 2   ? '#35978f' :
         d > 1   ? '#01665e' :
          '#003c30' 
}

function getColor3(d) {
  //console.log(d);
  return d > 10  ? '#a50026' :
         d > 8   ? '#d73027' :
         d > 8   ? '#f46d43' :
         d > 6   ? '#fdae61' :
         d > 5   ? '#fee08b' :
         d > 4   ? '#d9ef8b' :
         d > 3   ? '#a6d96a' :
         d > 2   ? '#66bd63' :
         d > 1   ? '#1a9850' :
          '#006837' 
}

var colorScale = d3.scaleLinear()
    .domain([0, 20])
    .range(["#ffffcc", "darkred"]);


// Adding tile layer
var usmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
});

// Add a layer for the county boundaries
var countyLayer = new L.LayerGroup();

var geoJson;

// Pull in the county geojson file
d3.json(countyLink, function(countyData){

  console.log(countyData);

  feature = countyData.features;
  console.log(feature);

  // Add a layer with the county outlines.
  geoJson = L.geoJson(countyData,{
    

    // Style for each feature (in this case a neighborhood)
    style: function(feature) {
      return {
        color: "white",
        // Call the chooseColor function to decide which color to color each county (color based on unemployment rate)
        fillColor: getColor3(feature.properties.UnemploymentRate),
        fillOpacity: 0.75,
        weight: 1
        }
    },

    // Called on each feature
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
        }
      });
      // Giving each feature a pop-up with information about that specific feature
      layer.bindPopup("<h1>" + feature.properties.NAME +', ' + feature.properties.StateAbbr +
      "</h1> <br> <h2>Unemployement Rate: " + feature.properties.UnemploymentRate + "</h2>");
    
      layer.setStyle({
        fillColor: getColor3(feature.properties.UnemploymentRate)
      });

    }
  }).addTo(countyLayer);

});


// Create a baseMaps object to hold the lightmap layer
var baseMaps = {
  "US"    : usmap
};

// Create an overlayMaps object to hold the earthquakes layer
var overlayMaps = {
  "Counties": countyLayer
};


// Create the map object with options
var myMap = L.map("map", {
  center: centerLoc,
  zoom: 4,
  layers: [usmap]
});

// Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
L.control.layers(baseMaps, overlayMaps, {
  collapsed: false
}).addTo(myMap);

