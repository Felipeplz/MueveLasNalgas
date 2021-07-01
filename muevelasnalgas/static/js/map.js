var platform = new H.service.Platform({
  'apikey': '-igx-K35_7339M64eO-YBL5SnUS5G0k1AHKKW7-Ab6E'
});

var defaultLayers = platform.createDefaultLayers();

var map = new H.Map(document.getElementById('mapContainer'),
            defaultLayers.vector.normal.map,
            {
                zoom: 12,
                center: {lat: -33.46468, lng: -70.65655},
                pixelRatio: window.devicePixelRatio || 1
            });

window.addEventListener('resize', () => map.getViewPort().resize());

var ui = H.ui.UI.createDefault(map, defaultLayers);

var mapEvents = new H.mapevents.MapEvents(map);
var behavior = new H.mapevents.Behavior(mapEvents);

// function startClustering(map, data) {
//   var dataPoints = data.map(function (item) {
//     return new H.clustering.DataPoint(item.latitude, item.longitude);
//   });

//   var clusteredDataProvider = new H.clustering.Provider(dataPoints, {
//     clusteringOptions: {
//       eps: 32,
//       minWeight: 2
//     }
//   });

//   var clusteringLayer = new H.map.layer.ObjectLayer(clusteredDataProvider);

//   map.addLayer(clusteringLayer);
// }

function addMarkerToGroup(group, coordinate, html, icon) {
  var marker = new H.map.DomMarker(coordinate, icon);
  // add custom data to the marker
  marker.setData(html);
  group.addObject(marker);
}