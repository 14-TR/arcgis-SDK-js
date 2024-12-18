require([
    "esri/Map",
    "esri/views/SceneView",
    "esri/layers/GeoJSONLayer"
], function(Map, SceneView, GeoJSONLayer) {
    
    // 1. Create the globe map
    const map = new Map({
        basemap: "satellite"
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

    // 3. Add GeoJSONLayer
    const geojsonLayer = new GeoJSONLayer({
        url: "http://localhost:8000/geojson/temperature_anomalies_2020.geojson",
        renderer: {
            type: "simple", // Render as points
            symbol: {
                type: "simple-marker", // Basic point symbol
                color: "red",
                size: 8
            }
        },
        popupTemplate: {
            title: "{LocationName}",
            content: `
                Change Rate: <b>{ChangeRate}</b><br>
                Year: {Year}
            `
        }
    });

    map.add(geojsonLayer);
});
