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
    const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InVzZXJAZXhhbXBsZS5jb20iLCJyb2xlX2lkIjoyfQ.Frv_u-7vKB1Zhvc8FPcL76QNp2HkvGv8fuOeBvaxeZ0";
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