<template>
    <div id="leaflet-map" style="width: 100%; height: 100%">
    </div>
</template>

<script>
    import L from 'leaflet'
    import _ from 'underscore'
    import customIcon from '../../node_modules/leaflet/dist/images/marker-icon.png'
    import customIconShadow from '../../node_modules/leaflet/dist/images/marker-shadow.png'
    import '../lib/Leaflet.ChineseTmsProviders/src/leaflet.ChineseTmsProviders'
    import '../lib/Leaflet.heat/dist/leaflet-heat'
    import '../lib/Leaflet.draw/dist/leaflet.draw-src'
    import { mapState, mapActions } from 'vuex'
    import { getTgWithinCircle, getTgWithinBox, getUserInCircle, getUserInBox } from '../api/api'
    import { gradient, color } from '../config/mapconfig'

    let drawnItems = L.featureGroup();

    export default {
        name: 'leaflet-map',
        data() {
            return {
                _map: undefined,            // 地图容器
                _tileLayer: undefined,
                _wmaLayer: undefined,       // 底图
                _heatLayer: undefined,      // 热力层
                _layerGroup: undefined,     //
                _customIcon: undefined,     // 自定义图标

                _controlLayer: undefined,   // 绘图控制层

                heatOption: {
                    minOpacity: 0.1,
                    maxZoom: 16,
                    max: 70000,
                    radius: 12,
                    blur: 10,
                    gradient: gradient
                }
            };
        },
        computed: {
            ...mapState([
                'searchLine',
                'searchLineResult',
                'searchTg',
                'searchTgResult',
                'userType',
                'searchUser',
                'searchUserResult',
                'algorithmType',
                'analyzeMethod'
            ])
        },
        watch: {
            searchLine: function () {
                let data = this.searchLineResult.heat_data;
                this.drawHeatMap(data, this._heatLayer);
            },
            searchTg: function () {
                let result = this.searchTgResult;
                console.log(result);
                if (result.status === 200) {
                    let data = {
                        tg_point: result.tg_info,
                        user_point: result.heat_data
                    };
                    // this._layerGroup.clearLayers();
                    this.drawHeatPoint(data, this._layerGroup, this._map);
                } else {
                    alert(result.message);
                }
            },
            searchUser: function () {
                let result = this.searchUserResult;
                // console.log(result);
                if (result.status === 200) {
                    let data = {
                        tg_point: result.tg_info,
                        user_point: result.heat_data
                    };
                    // this._layerGroup.clearLayers();
                    this.drawHeatPoint(data, this._layerGroup, this._map);
                } else {
                    alert(result.message);
                }
            },
            analyzeMethod: function (val) {
                console.log(val);
                if (val === 'cluster') {
                    this._layerGroup.clearLayers();
                }
            }
        },
        methods: {
            ...mapActions([
                'searchUserInShapeAction'
            ]),
            init() {
                this._map = new L.Map('leaflet-map', {
                    center: new L.LatLng(31.1, 121.63),
                    zoom: 10,
                    attributionControl: false
                });
                this._wmsLayer = L.tileLayer.wms('http://tseg4:8080/geowebcache/service/wms', {
                    layers: 'Shanghai',
                    format: 'image/png'
                });
                this._tileLayer = L.tileLayer.chinaProvider('GaoDe.Normal.Map', {
                    // maxZoom: 16,
                    minZoom: 10
                });
                this._customIcon = L.icon({
                    iconUrl: customIcon,
                    shadowUrl: customIconShadow
                });
                drawnItems.addTo(this._map);
                this._controlLayer = L.control.layers({
                    'gaode': this._tileLayer.addTo(this._map)  // this._wmsLayer.addTo(this._map)
                }, {
                    'drawlayer': drawnItems
                }, {
                    'position': 'topleft',
                    collapsed: true
                }).addTo(this._map);

                this._heatLayer = L.heatLayer([], this.heatOption).addTo(this._map);
                this._layerGroup = L.layerGroup();

                this._map.addControl(new L.Control.Draw({
                    edit: {
                        featureGroup: drawnItems,
                        poly: {
                            allowIntersection: false
                        }
                    },
                    draw: {
                        polyline: false,
                        polygon: {
                            allowIntersection: false,
                            showArea: true
                        }
                    }
                }));
                this._map.on(L.Draw.Event.CREATED, this.drawAction);
            },
            drawAction(event) {
                let layer = event.layer;
                let params;
                if (event.layerType === 'circle') {
                    let radius = layer.getRadius();
                    let latlng = layer._latlng;
                    params = {
                        shape: 'circle',
                        queryParams: {
                            userType: this.userType,
                            coord: latlng,
                            maxDistance: radius
                        }
                    };
                } else if (event.layerType === 'rectangle') {
                    let bounds = layer.getBounds();
                    params = {
                        shape: 'rectangle',
                        queryParams: {
                            userType: this.userType,
                            bounds: bounds
                        }
                    };
                }
                this.searchUserInShapeAction(params);
                drawnItems.addLayer(layer);
            },
            drawHeatPoint(data, layerGroup, map) {
                // layerGroup.clearLayers();
                this._heatLayer.setLatLngs([]);
                let icon = this._customIcon;
                if (data['tg_point']) {
                    this._map.panTo(data['tg_point'][0].coordinates);
                    data['tg_point'].forEach(function (d) {
                        L.marker(d.coordinates, {
                            icon: icon
                        }).addTo(layerGroup);
                    });
                }
                if (data['user_point']) {
                    data['user_point'].forEach(function (d) {
                        L.circleMarker(d.coordinates, {
                            color: d.color,
                            fillColor: d.color,
                            radius: 3
                        }).addTo(layerGroup);
                    });
                }
                layerGroup.addTo(map);
            },
            drawHeatMap(points, layer) {
                this._layerGroup.clearLayers();
                let center = [points[0][0], points[0][1]];
                this._map.panTo(center);
                console.log(points);
                layer.setLatLngs(points);
            }
        },
        mounted: function () {
            this.init();
        }
    }
</script>

<style scoped lang="scss">
    @import "../../node_modules/leaflet/dist/leaflet.css";
    @import "../lib/Leaflet.draw/dist/leaflet.draw.css";
    .xixi {
        color: rgba(130, 1, 80, 1);
    }
</style>