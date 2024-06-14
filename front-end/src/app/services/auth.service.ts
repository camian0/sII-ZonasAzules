import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/evironment';
 
const BASE_URL: String = environment.url;
 
 
@Injectable({
  providedIn: 'root'
})
export class AuthService {
 
  constructor(
    private http: HttpClient
  ) {
 
  }

  login(json:any): Observable<any> {
    return this.http.post(`${BASE_URL}/auth`,json);
  }
  
}