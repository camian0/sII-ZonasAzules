import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/evironment';
 
const BASE_URL: String = environment.url;
 
 
@Injectable({
  providedIn: 'root'
})
export class AreasService {
 
  constructor(
    private http: HttpClient
  ) {
 
  }

  get(): Observable<any> {
    return this.http.get(`${BASE_URL}areas/`);
  }

  post(json:any): Observable<any> {
    return this.http.post(`${BASE_URL}areas/`,json);
  }

  put(json:any): Observable<any> {
    return this.http.put(`${BASE_URL}areas/`,json);
  }
 
  delete(id:any): Observable<any> {
    return this.http.delete(`${BASE_URL}areas?idArea=${id}`);
  }
}