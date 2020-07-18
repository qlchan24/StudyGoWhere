// let locationjson = Promise.resolve(
//   fetch('{% url "sgw:locationjson" %}').then((x) => x.json())
// );

// let studyspotjson = Promise.resolve(
//   fetch('{% url "sgw:studyspotjson" %}').then((x) => x.json())
// );

// console.log(locationjson);
// console.log(studyspotjson);

// locationjson.then((x) => {
//   const chosen_id = x.filter((y) => y.fields.locationName == "COM1")[0].pk;

//   console.log(chosen_id);

//   studyspotjson.then((x) => {
//     const lol = x
//       .filter((y) => y.fields.locationName == chosen_id)
//       .map((x) => x.fields.description);
//     console.log(lol);
//   });
// });

// To include the studyspots:
// method 1:
// for each study spot in list:
// get point lat and lon
// var lon = "{{ studyspot.geometry.x }}";
// var lat = "{{ studyspot.geometry.y }}";
// add marker to map (and check for color):
// for red: L.marker([lat, lon],{color: 'red',fillColor: '#f03',fillOpacity: 0.5,}).addTo(map);

// method 2:geojson
// var studyspots = [{
//     "type": "Feature",
//     "properties": { "name": "hssml","crowdedness": "2","show_on_map": true },
//     "geometry": {
//     "type": "Point",
//     "coordinates": [x1,y1]
//     }
// }, {
//     "type": "Feature",
//     "properties": { "name": "com1 annex","crowdedness": "3","show_on_map": true },
//     "geometry": {
//     "type": "Point",
//     "coordinates": [x2,y2]
//     }
// }];

// function onEachFeature(feature, layer) {
//     layer.on({
//     mouseover: highlightFeature, //to be implemented
//     mouseout: resetHighlight, //to be implemented
//     click: do_something //to be implemented
//     });
// }

// L.geoJSON(studyspots, {
//     style: function (feature) {
//     switch (feature.properties.crowdedness) {
//         case '3': return { color: "#ff0000" };
//         case '2': return { color: "#ffff00" };
//         case '1': return { color: "#00ff00" };
//     }
//     },
//     filter: function(feature, layer) {
//     return feature.properties.show_on_map;
//     },
//     onEachFeature: onEachFeature
// }).addTo(map);
