
require([
    "esri/Map",
    "esri/views/SceneView",
    "esri/layers/FeatureLayer",
    "esri/renderers/UniqueValueRenderer"
], function(Map, SceneView, FeatureLayer, UniqueValueRenderer) {
    
    // 1. Create the globe map
    const map = new Map({
        basemap: "satellite" // High-quality satellite imagery
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

    // 3. FeatureLayer for the Peaks (Environmental Change)
    const environmentalLayer = new FeatureLayer({
        url: "YOUR_FEATURE_LAYER_URL", // Replace with your environmental change layer
        renderer: {
            type: "simple", // Use a simple renderer for 3D "peaks"
            symbol: {
                type: "point-3d", // 3D symbol
                symbolLayers: [{
                    type: "object", // Object for peaks
                    resource: { primitive: "cylinder" }, // 3D cylinder shape
                    material: { color: "red" }, // Change peak color
                    height: "{ChangeRate} * 5000", // Height of the cylinder based on change rate
                    width: 300000 // Width of the cylinder
                }]
            },
            visualVariables: [{
                type: "size", // Make the peak size proportional to the change rate
                field: "ChangeRate",
                minDataValue: 1,
                maxDataValue: 10,
                minSize: 500000,
                maxSize: 3000000
            }]
        },
        popupTemplate: {
            title: "{LocationName}",
            content: `
                Change Rate: <b>{ChangeRate}</b><br>
                Type: {ChangeType}<br>
                Year: {Year}`
        }
    });

    map.add(environmentalLayer); // Add the layer to the map
});