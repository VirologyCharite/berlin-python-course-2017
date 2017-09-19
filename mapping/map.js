var mapboxToken = 'pk.eyJ1IjoidGVycnljb2pvbmVzIiwiYSI6ImNpcjl4ZnllZzAwNGNpZmx3YmY3dXVxNGIifQ.4ybBGHp3Zoqs-5I-tqXxJw';

var map = new ol.Map({
    target: 'map',
    layers: [

        new ol.layer.Tile({
            /* 
               Open Street Map
               source: new ol.source.OSM()
            */
            
            /*
            source: new ol.source.TileJSON({
                url: 'http://api.tiles.mapbox.com/v3/mapbox.geography-class.json',
                crossOrigin: ''
            })
            */

            // Hello this is a comment.

            source: new ol.source.XYZ({
                tileSize: [512, 512],
                url: ('https://api.mapbox.com/styles/v1/mapbox/streets-v9/tiles/{z}/{x}/{y}?access_token=' +
                      mapboxToken)
            })
        })
    ],
    view: new ol.View({
        center: ol.proj.fromLonLat([13.404954, 52.5200066]),
        zoom: 14
    })
});
