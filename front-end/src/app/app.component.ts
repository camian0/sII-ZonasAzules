import { Component, inject } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'front-end-angular';
  router = inject(Router);
  token = localStorage.getItem('token');

  logOut(): void {
    localStorage.clear();
    this.router.navigateByUrl('');
    console.log('saliendo');
  }
}
