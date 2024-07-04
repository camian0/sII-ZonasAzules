import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/evironment';

const BASE_URL: String = environment.url;

@Injectable({
  providedIn: 'root',
})
export class ZonesService {
  constructor(private http: HttpClient) {}

  get(): Observable<any> {
    return this.http.get(`${BASE_URL}blue-zone/`);
  }
  getByArea(id: any): Observable<any> {
    return this.http.get(`${BASE_URL}blue-zone/byArea/?id=${id}`);
  }
  getSectors(): Observable<any> {
    return this.http.get(`${BASE_URL}areas/`);
  }

  getById(id: any): Observable<any> {
    return this.http.get(`${BASE_URL}/-zoneById?id=${id}`);
  }

  post(json: any): Observable<any> {
    return this.http.post(`${BASE_URL}blue-zone/`, json);
  }

  postFilter(json: any): Observable<any> {
    return this.http.post(`${BASE_URL}filter`, json);
  }

  put(json: any): Observable<any> {
    return this.http.put(`${BASE_URL}blue-zone/`, json);
  }

  delete(id: any): Observable<any> {
    return this.http.delete(`${BASE_URL}blue-zone/?idNumber=${id}`);
  }
}
