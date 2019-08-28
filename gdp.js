var svgWidth = 1000; //960
var svgHeight = 650; // 620

var margin = {
    top: 20,
    right: 40,
    bottom: 100,
    left: 100
};

//Chart height and width
var width = svgWidth - margin.right - margin.left;
var height = svgHeight - margin.top - margin.bottom;

//Append div classed chart to the scatter element
var chart = d3.select("#scatter").append("div").classed("chart", true);

//Append SVG element to the chart for width and height
var svg = chart.append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

//Append SVG group
var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

    //Reference data to pull values to complete chart//
function BuildBar(state,state2){
    d3.json(`/barchart/${state}/${state2}`) .then((data)=>{
        // build bar chart here//
    })
}
