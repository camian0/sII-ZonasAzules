import { Component, OnInit, Renderer2 } from '@angular/core';
import * as mapboxgl from 'mapbox-gl';
import { environment } from '../../../environments/evironment';
import { MatIconModule } from '@angular/material/icon';
import { getData } from '../../../request/request';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-map',
  standalone: true,
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css'],
  imports: [MatIconModule],
})
export class MapComponent implements OnInit {
  map: mapboxgl.Map | undefined;
  blueZones: Array<any> = [];
  constructor(private renderer: Renderer2) {}

  // GEOJSON = {
  //   type: 'FeatureCollection',
  //   features: [
  //     {
  //       type: 'Feature',
  //       geometry: {
  //         type: 'Point', //longitud, latitud 5.058404, -75.489142
  //         coordinates: [-75.489142, 5.058404],
  //       },
  //       properties: {
  //         title: 'Estadio',
  //         description: 'Frente calenda',
  //       },
  //     },
  //     {
  //       type: 'Feature',
  //       geometry: {
  //         type: 'Point',
  //         coordinates: [-75.490952, 5.057253],
  //       },
  //       properties: {
  //         title: 'Estadio',
  //         description: 'Frente estadio',
  //       },
  //     },
  //     {
  //       type: 'Feature',
  //       geometry: {
  //         type: 'Point',
  //         coordinates: [-75.501138, 5.062699],
  //       },
  //       properties: {
  //         title: 'Hospital',
  //         description: 'Frente hospital de caldas',
  //       },
  //     },
  //   ],
  // };

  ngOnInit(): void {
    this.getBlueZones();
    this.createMap();
  }

  createMap(): void {
    (mapboxgl as any).accessToken = environment.mapBoxToken;
    this.map = new mapboxgl.Map({
      container: 'map', // ID del elemento en el template
      style: 'mapbox://styles/mapbox/streets-v11', // Estilo del mapa
      center: [-75.4941952, 5.0561024], // Posición inicial [longitud, latitud]
      zoom: 12.9, // Nivel de zoom inicial
    });
  }

  addMarkers(map: any): void {
    for (let item of this.blueZones) {
      let newDiv = this.renderer.createElement('div');
      this.renderer.addClass(newDiv, 'marker');
      new mapboxgl.Marker(newDiv)
        .setLngLat([item.longitude, item.latitude])
        .setPopup(
          new mapboxgl.Popup() // add popups
            .setHTML(
              `
               <h2>${item.name}</h2>
               <h6>${item.address}</h6>
                  <div class="info-container">
                    <div class="info-block">
                      <div class="icon">
                        <img
                          class="icon-location"
                          src="../../../assets/icons/directions_car_24dp blue.svg"
                          alt="Car"
                        />
                      </div>
                      <div class="info">
                        <p style="color: rgb(10, 165, 10);">Disponibles: <span>${item.total_car_places}</span></p>                        
                      </div>
                    </div>
                    <div class="divider"></div>
                    <div class="info-block">
                      <div class="icon">
                        <img
                          class="icon-location"
                          src="../../../assets/icons/motorcycle_24dp_blue.svg"
                          alt="Bike"
                        />
                      </div>
                      <div class="info">
                        <p style="color: rgb(10, 165, 10);">Disponibles <span>${item.total_moto_places} </span></p>                        
                      </div>
                    </div>
                  </div>
              `
            )
        )
        .addTo(map);
    }
  }

  async getBlueZones(): Promise<any> {
    await getData('blue-zone', {})
      .then((res) => {
        if (res.status === 200) {
          Swal.fire({
            title: 'Éxito',
            text: res.message,
            icon: 'success',
            showConfirmButton: false,
            timer: 1000,
          });
          this.blueZones = res.data;
          this.addMarkers(this.map);
          return;
        }
      })
      .catch(() => {
        console.log();
      });
  }
}
