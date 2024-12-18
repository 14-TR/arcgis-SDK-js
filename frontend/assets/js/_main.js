require([
    "esri/Map",
    "esri/views/SceneView",
    "esri/layers/GeoJSONLayer"
], function(Map, SceneView, GeoJSONLayer) {
    
    // 1. Create the globe map
    const map = new Map({
        // Dark gray canvas basemap
        basemap: "dark-gray-vector",
    });

    // 2. SceneView (3D)
    const view = new SceneView({
        container: "viewDiv",
        map: map,
        camera: {
            position: [0, 0, 20000000], // Start high up
            tilt: 0
        }
    });

    // 3. GeoJSONLayer for Environmental Change Peaks
    let geojsonLayer;

    // Function to load GeoJSON dynamically based on year
    function loadGeoJSON(year) {
        const geojsonPath = `http://localhost:8000/geojson/temperature_anomalies_${year}.geojson`; // Replace with your backend server URL
        
        if (geojsonLayer) {
            map.remove(geojsonLayer);
        }

        geojsonLayer = new GeoJSONLayer({
            url: geojsonPath,
            renderer: {
                type: "simple",
                symbol: {
                    type: "point-3d", // 3D symbol
                    symbolLayers: [{
                        type: "object", // Object for peaks
                        resource: { primitive: "cylinder" }, // 3D cylinder shape
                        material: { color: "blue" }, // Change peak color
                    }]
                },
                visualVariables: [{
                    type: "size", // Adjust size dynamically based on anomaly
                    field: "Anomaly",
                    minDataValue: -5,
                    maxDataValue: 5,
                    minSize: 500000, // Minimum peak height
                    maxSize: 3000000 // Maximum peak height
                }, {
                    type: "color", // Adjust color based on anomaly
                    field: "Anomaly",
                    stops: [
                        { value: -5, color: "#0000FF" }, // Cold anomalies (blue)
                        { value: 0, color: "#FFFFFF" },  // Neutral (white)
                        { value: 5, color: "#FF0000" }   // Warm anomalies (red)
                    ]
                }]
            },
            popupTemplate: {
                title: "Temperature Anomaly",
                content: `
                    Latitude: {Latitude}<br>
                    Longitude: {Longitude}<br>
                    Anomaly: {Anomaly} °C
                `
            }
        });

        map.add(geojsonLayer);
    }

    // Load initial year
    loadGeoJSON(2020);

    // Add event listener for year selection
    document.getElementById("yearSelector").addEventListener("change", function(event) {
        const selectedYear = event.target.value;
        loadGeoJSON(selectedYear);
    });
});
