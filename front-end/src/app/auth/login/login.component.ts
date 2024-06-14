import { Component, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { postData, getData } from 'src/request/request';
import { AbstractControl, FormBuilder, FormControl, FormGroup, FormsModule, NgForm, ReactiveFormsModule, Validators } from "@angular/forms";
import { CommonModule } from '@angular/common';
import { AuthModelRequest } from 'src/app/models/request/authModel';
import { ResposeDto } from 'src/app/models/response/response-dto';
import Swal from 'sweetalert2';
@Component({
  selector: 'app-login',
  standalone: true,
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    FormsModule
  ]
})
export class LoginComponent {

  myFormGroup: FormGroup = new FormGroup({});
  authModelRequest: AuthModelRequest = new AuthModelRequest();
  menus: any[] = new Array();

  constructor(
    private formBuilder: FormBuilder,
    private router: Router
  ) { }


  ngOnInit() {
    this.myFormGroup = this.formBuilder.group({
      username: new FormControl('', [Validators.required]),
      password: new FormControl('', [Validators.required])
    });
  }

  get getUsername(): AbstractControl | null { return this.myFormGroup.get('username'); }
  get getPassword(): AbstractControl | null { return this.myFormGroup.get('password'); }

  async onSubmit() {
    await this.login();

  }


  async login() {
    const path: string = "auth";
    this.authModelRequest.email = this.getUsername?.value;
    this.authModelRequest.password = this.getPassword?.value;

    const res: ResposeDto = await postData(path, this.authModelRequest, false);
    if (res.status == 400) {
      Swal.fire({
        title: "Intentelo nuevamente",
        text: res.message,
        icon: "warning"
      })
      return;
    }

    if (res.status == 200) {
      window.localStorage.setItem("token", res.data);
      await this.getMenus();
      this.router.navigate(['/welcome']);
    }
  }

  async getMenus() {
    const path: string = `auth/menu`;

    const res: ResposeDto = await getData(path, { email: this.getUsername?.value });
    console.log(res)

    if (res.status == 200) {
      this.menus = res.data;
      window.localStorage.setItem("menus", JSON.stringify(this.menus));
    }
  }
}
