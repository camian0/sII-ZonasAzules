import { Injectable } from '@angular/core';
import {
  HttpInterceptor,
  HttpRequest,
  HttpHandler,
  HttpEvent
} from '@angular/common/http';
import { Observable } from 'rxjs';
 
@Injectable()
export class TokenInterceptor implements HttpInterceptor {
  constructor() {}
 
  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<any> {
    //const token = localStorage.getItem('token');
    const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Imphcm9sMTU5MEBnbWFpbC5jb20iLCJyb2xlX2lkIjoyfQ.P1D9I9UC1nd6rmp-1Mo8j4UTFM4dq0083JrZT697-LQ";
    if (token) {
      const modifiedRequest = request.clone({
        setHeaders: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json'
        }
      });
      return next.handle(modifiedRequest);
    } else {
      return next.handle(request);
    }
  }
}