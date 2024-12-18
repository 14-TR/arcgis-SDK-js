const express = require("express");
const path = require("path");

const app = express();
const port = 8000;

// Serve the temperature anomalies GeoJSON directory
app.use("/geojson", express.static(path.join(__dirname, "/data/temperature_anomalies_geojson")));

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/geojson`);
});
