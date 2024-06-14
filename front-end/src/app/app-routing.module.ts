import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { authGuard } from './guards/auth-guard.guard';

const routes: Routes = [
  {
    path: '',
    loadChildren: () => import('./auth/auth.routes').then((m) => m.AUTH_ROUTES),
  },
  {
    path: 'admin',
    loadChildren: () =>
      import('./admin/admin.routes').then((m) => m.ADMIN_ROUTES),
    canActivate: [authGuard],
  },
  {
    path: 'cards',
    loadChildren: () =>
      import('./cards/cards.routes').then((m) => m.CARDS_ROUTES),
    canActivate: [authGuard],
  },
  {
    path: 'search',
    loadChildren: () =>
      import('./search/search.routes').then((m) => m.SEARCH_ROUTES),
    canActivate: [authGuard],
  },
  {
    path: 'welcome',
    loadChildren: () =>
      import('./welcome/welcome.routes').then((m) => m.COME_ROUTES),
    canActivate: [authGuard],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
