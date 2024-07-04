import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/evironment';
 
const BASE_URL: String = environment.url;
 
 
@Injectable({
  providedIn: 'root'
})
export class creditcardService {
 
  constructor(
    private http: HttpClient
  ) {
 
  }

  get(): Observable<any> {
    return this.http.get(`${BASE_URL}/?page=1&sizePage=10`);
  }

  getCardUserById(id:any): Observable<any> {
    return this.http.get(`${BASE_URL}creditcard/byUserId?user_id=${id}`);
  }

  getReservUserById(id:any): Observable<any> {
    return this.http.get(`${BASE_URL}reservations/byId?reservation_id=${id}`);
  }

  post(json:any): Observable<any> {
    return this.http.post(`${BASE_URL}`,json);
  }

  postCard(json:any): Observable<any> {
    return this.http.post(`${BASE_URL}creditcard/card`, json);
  }

  postFilter(json:any): Observable<any> {
    return this.http.post(`${BASE_URL}/filter`,json);
  }

  patch(json:any): Observable<any> {
    return this.http.patch(`${BASE_URL}`,json);
  }
 
  delete(number:any): Observable<any> {
    return this.http.delete(`${BASE_URL}creditcard/${number}`);
  }
}