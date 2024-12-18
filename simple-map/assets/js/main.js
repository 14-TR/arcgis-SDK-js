require([
    "esri/Map",
    "esri/views/MapView",
    "esri/Graphic",
    "esri/layers/GraphicsLayer"
], function(Map, MapView, Graphic, GraphicsLayer) {
    // Create a Map instance
    const map = new Map({
        basemap: "topo-vector" // Choose a basemap
    });

    // Create a MapView instance
    const view = new MapView({
        container: "viewDiv", // ID of the div where the map will be displayed
        map: map,
        center: [-100.33, 25.69], // Longitude, Latitude (default location)
        zoom: 4 // Zoom level
    });

    // Create a GraphicsLayer to hold graphics (points, lines, polygons)
    const graphicsLayer = new GraphicsLayer();
    map.add(graphicsLayer);

    // Function to add a point graphic
    function addPoint(event) {
        const point = {
            type: "point", // Geometry type
            longitude: event.mapPoint.longitude,
            latitude: event.mapPoint.latitude
        };

        const markerSymbol = {
            type: "simple-marker", 
            color: [226, 119, 40], // Orange
            outline: {
                color: [255, 255, 255], // White
                width: 2
            }
        };

        const pointGraphic = new Graphic({
            geometry: point,
            symbol: markerSymbol
        });

        graphicsLayer.add(pointGraphic);
    }

    // Listen for map clicks to add points
    view.on("click", addPoint);
});
