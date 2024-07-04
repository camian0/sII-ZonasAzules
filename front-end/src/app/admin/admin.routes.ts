import { Routes } from '@angular/router';
import { ZonesComponent } from './zones/zones.component';
import { AreasComponent } from './areas/areas.component';

export const ADMIN_ROUTES: Routes = [
  { path: 'AdminZone', component: ZonesComponent },
  { path: 'AdminArea', component: AreasComponent },
];
