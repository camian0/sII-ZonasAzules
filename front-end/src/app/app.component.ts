import { Component, inject } from '@angular/core';
import { Router } from '@angular/router';
import { GetTokenService } from './shared/services/get-token.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'front-end-angular';
  router = inject(Router);
  token: string = '';
  private subscription?: Subscription;

  constructor(private serviceToken: GetTokenService) {}

  ngOnInit() {
    this.subscription = this.serviceToken.token$.subscribe((value) => {
      this.token = value;
    });
  }

  logOut(): void {
    localStorage.clear();
    this.router.navigateByUrl('');
    console.log('saliendo');
  }
}
