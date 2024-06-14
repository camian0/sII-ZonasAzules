import { Component } from '@angular/core';
import { GetTokenService } from 'src/app/shared/services/get-token.service';

@Component({
  selector: 'app-come',
  standalone: true,
  templateUrl: './come.component.html',
  styleUrls: ['./come.component.css'],
})
export class ComeComponent {
  token: string = '';

  constructor(private tokenService: GetTokenService) {}

  updateValue(): void {
    this.tokenService.setVariable(this.token);
  }

  ngOnInit() {
    this.token = localStorage.getItem('token')!;

    this.updateValue();
  }
}
