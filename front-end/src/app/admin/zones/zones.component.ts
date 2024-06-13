import { Component } from '@angular/core';

interface Zona {
  sector: string;
  direccion: string;
  tarifa: string;
  plazasTotales: number;
  plazasDisponibles: number;
}

@Component({
  selector: 'app-zones',
  templateUrl: './zones.component.html',
  styleUrls: ['./zones.component.css']
})
export class ZonesComponent {
  idZona!: string;
  estado!: string;
  estado2!: string;
  zonas: Zona[] = [
    { sector: 'ESTADIO', direccion: 'CAR 32 A 25', tarifa: '$ 2.000', plazasTotales: 10, plazasDisponibles: 10 },
    { sector: 'ESTADIO', direccion: 'CAR 32 A 25', tarifa: '$ 2.000', plazasTotales: 10, plazasDisponibles: 2 },
    { sector: 'ESTADIO', direccion: 'CAR 32 A 25', tarifa: '$ 2.000', plazasTotales: 10, plazasDisponibles: 3 },
    { sector: 'ESTADIO', direccion: 'CAR 32 A 25', tarifa: '$ 2.000', plazasTotales: 15, plazasDisponibles: 6 }
  ];
  displayedColumns: string[] = ['sector', 'direccion', 'tarifa', 'plazasTotales', 'plazasDisponibles', 'ubicacion', 'editar'];

  buscar() {
    // Implement search functionality here
  }

  editar(zona: Zona) {
    // Implement edit functionality here
  }
}