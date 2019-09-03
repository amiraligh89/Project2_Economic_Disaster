var margin = { top: 20, right: 30, bottom: 40, left: 30 },
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x = d3.scale.linear()
    .range([0, width]);

var y = d3.scale.ordinal()
    .rangeRoundBands([0, height], 0.1);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");
// .text("% GDP Change");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .tickSize(0)
    .tickPadding(6);

var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.csv("../assets/data/final_gdpdata_v1.csv").then(function (data) {
    console.log(data)

    x.domain(d3.extent(data, function (d) { return d.GDP_Change; })).nice();
    y.domain(data.map(function (d) { return d.Quarter; }));

    svg.selectAll(".bar")
        .data(data)
        .enter().append("rect")
        .attr("class", function (d) { return "bar bar--" + (d.GDP_Change < 0 ? "negative" : "positive"); })
        .attr("x", function (d) { return x(Math.min(0, d.GDP_Change)); })
        .attr("y", function (d) { return y(d.Quarter); })
        .attr("width", function (d) { return Math.abs(x(d.GDP_Change) - x(0)); })
        .attr("height", y.rangeBand());

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .text("% GDP Change")
        .call(xAxis);

    svg.append("g")
        .attr("class", "y axis")
        .attr("transform", "translate(" + x(0) + ",0)")
        .call(yAxis);



    /********************** NEED TO UPDATE ****************************************************/
    // Handler for dropdown value change
    var dropdownChange = function () {
        var newState = d3.select(this).property('value'),
            newData = data[newState];
        updateBars(newData);
        console.log(newData);
    };

    // Get names of states, for dropdown
    var states = Object.keys(data).sort();

    var dropdown = d3.select("#vis-container")
        .insert("select", "svg")
        .on("change", dropdownChange);

    dropdown.selectAll("option")
        .data(states)
        .enter().append("option")
        .attr("value", function (d) { return d; });

    var initialData = data[states[0]];
    updateBars(initialData);
    console.log(initialData);
    /**************************************************************************/
});

function type(d) {
    d.GDP_Change = +d.GDP_Change;
    return d;
}

