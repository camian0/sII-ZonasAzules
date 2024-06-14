import { Routes } from '@angular/router';
import { ListBluezonesComponent } from './list-bluezones/list-bluezones.component';
import { MapComponent } from './map/map.component';

export const SEARCH_ROUTES: Routes = [
  { path: 'list', component: ListBluezonesComponent },
  { path: 'map', component: MapComponent },
];
