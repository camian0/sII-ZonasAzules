import { Token } from '@angular/compiler';
import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class GetTokenService {
  private token = new BehaviorSubject<string>(''); // Puedes cambiar el tipo según sea necesario
  token$ = this.token.asObservable();

  // getRokent(): string | null {
  //   let token = localStorage.getItem('token');
  //   return token;
  // }

  setVariable(newValue: string): void {
    this.token.next(newValue);
  }

  getVariable(): string {
    return this.token.getValue();
  }
}
