import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    loadChildren: () => import('./auth/auth.routes').then((m) => m.AUTH_ROUTES),
  },
  {
    path: 'admin',
    loadChildren: () =>
      import('./admin/admin.routes').then((m) => m.ADMIN_ROUTES),
  },
  {
    path: 'cards',
    loadChildren: () =>
      import('./cards/cards.routes').then((m) => m.CARDS_ROUTES),
  },
  {
    path: 'search',
    loadChildren: () =>
      import('./search/search.routes').then((m) => m.SEARCH_ROUTES),
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
