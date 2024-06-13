import { Component } from '@angular/core';
import * as mapboxgl from 'mapbox-gl';
import { environment } from '../../../environments/evironment';

@Component({
  selector: 'app-map',
  standalone: true,
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css'],
})
export class MapComponent {
  map: mapboxgl.Map | undefined;
  GEOJSON = {
    type: 'FeatureCollection',
    features: [
      {
        type: 'Feature',
        geometry: {
          type: 'Point',
          coordinates: [-77.032, 38.913],
        },
        properties: {
          title: 'Mapbox',
          description: 'Washington, D.C.',
        },
      },
      {
        type: 'Feature',
        geometry: {
          type: 'Point',
          coordinates: [-122.414, 37.776],
        },
        properties: {
          title: 'Mapbox',
          description: 'San Francisco, California',
        },
      },
    ],
  };

  ngOnInit(): void {
    (mapboxgl as any).accessToken = environment.mapBoxToken;
    this.map = new mapboxgl.Map({
      container: 'map', // ID del elemento en el template
      style: 'mapbox://styles/mapbox/streets-v11', // Estilo del mapa
      center: [-75.4941952, 5.0561024], // Posición inicial [longitud, latitud]
      zoom: 12.9, // Nivel de zoom inicial
    });
    this.map.addControl(new mapboxgl.NavigationControl());
    this.map.addControl(new mapboxgl.FullscreenControl());
    this.map.addControl(
      new mapboxgl.GeolocateControl({
        positionOptions: {
          enableHighAccuracy: true,
        },
        trackUserLocation: true,
      })
    );
  }
}
