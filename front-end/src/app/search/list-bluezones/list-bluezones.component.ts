import { Component } from '@angular/core';
import { getData, postData } from '../../../request/request';
import { MatSnackBar } from '@angular/material/snack-bar';
import { NotificationService } from '../../shared/services/notifications.service';
import { MatTableModule } from '@angular/material/table';
import { CommonModule } from '@angular/common';
import { MatIconModule } from '@angular/material/icon';
import { MatSelectModule } from '@angular/material/select';
import { MatFormFieldModule } from '@angular/material/form-field';
import { Area } from 'src/app/models/response/area';
import { ResposeDto } from 'src/app/models/response/response-dto';
import Swal from 'sweetalert2';
import { PlaceType } from 'src/app/models/response/place-types';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatInputModule } from '@angular/material/input';
import { MatNativeDateModule } from '@angular/material/core';
import { NgxMatDatetimePickerModule, NgxMatTimepickerModule, NgxMatNativeDateModule } from '@angular-material-components/datetime-picker';
import { AbstractControl, FormBuilder, FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';


interface Food {
  value: string;
  viewValue: string;
}
@Component({
  selector: 'app-list-bluezones',
  standalone: true,
  templateUrl: './list-bluezones.component.html',
  styleUrls: ['./list-bluezones.component.css'],
  imports: [MatTableModule, CommonModule,
    MatIconModule, MatSelectModule, MatFormFieldModule,
    MatDatepickerModule, MatInputModule, MatNativeDateModule,
    NgxMatDatetimePickerModule, NgxMatTimepickerModule,
    FormsModule, ReactiveFormsModule, NgxMatNativeDateModule],
})
export class ListBluezonesComponent {
  blueZones = [];
  displayedColumns: string[] = ['id', 'name', 'address', 'total_places_free', 'ubications'];
  dataSource = this.blueZones;
  areas: Area[] = [];
  placeTypes: PlaceType[] = [];
  // initialDateControl = new FormControl();
  // finalDateControl = new FormControl();
  showSpinners = true;
  showSeconds = true;
  stepHour = 1;
  stepMinute = 1;
  stepSecond = 1;
  touchUi = true;
  color = 'primary';
  enableMeridian = false;
  disableMinute = false;
  hideTime = false;
  // minDate: Date; // Define minDate como tipo Date
  // maxDate: Date; // Define maxDate como tipo Date
  myFormGroup: FormGroup = new FormGroup({});




  constructor(
    private notificationService: NotificationService,
    private formBuilder: FormBuilder
  ) {
  }

  ngOnInit() {
    this.myFormGroup = this.formBuilder.group({
      initialDateControl: new FormControl('', [Validators.required]),
      finalDateControl: new FormControl('', [Validators.required]),
      sectorControl: new FormControl('', [Validators.required]),
      placeTypeControl: new FormControl('', [Validators.required]),
    });
    this.getAreas(1);
    this.getPlaceTypes();
  }
  get getinitialDate(): AbstractControl | null { return this.myFormGroup.get('initialDateControl'); }
  get getfinalDate(): AbstractControl | null { return this.myFormGroup.get('finalDateControl'); }
  get getSector(): AbstractControl | null { return this.myFormGroup.get('sectorControl'); }
  get getPlaceType(): AbstractControl | null { return this.myFormGroup.get('placeTypeControl'); }

  onSubmit() {
    const startDate = this.getinitialDate?.value;
    const endDate = this.getfinalDate?.value;

    if (new Date(startDate) >= new Date(endDate)) {
      Swal.fire({
        title: "warning",
        text: "La fecha de inicio debe ser menor a la fecha de finalización",
        icon: "warning"
      });
      return;
    }

    this.getBlueZones();
  }


  async getBlueZones(): Promise<void> {
    const start_date = new Date(new Date(this.getinitialDate?.value).getTime() - 5 * 60 * 60 * 1000).toISOString();
    const finish_date = new Date(new Date(this.getfinalDate?.value).getTime() - 5 * 60 * 60 * 1000).toISOString();
    const res: ResposeDto = await postData('blue-zone/filter', {
      "areaId": this.getSector?.value,
      "placeTypeId": this.getPlaceType?.value,
      "start_date": start_date,
      "finish_date": finish_date
    }, true);

    if (res.status == 400) {
      Swal.fire({
        title: "Intentelo nuevamente",
        text: res.message,
        icon: "warning"
      })
      return;
    }

    if (res.status === 200) {
      this.notificationService.success('Zona azules obtenidas con exito');
      this.blueZones = res.data;
      return;
    }

  }

  async getAreas(page: number): Promise<void> {
    const res: ResposeDto = await getData('areas', { page, sizePage: 10 });

    if (res.status === 200) {
      this.areas = res.data;
      return;
    }

  }

  async getPlaceTypes(): Promise<void> {
    const res: ResposeDto = await getData('place-types', {});

    if (res.status === 200) {
      this.placeTypes = res.data;
      return;
    }

  }

  ubication(element: any) {
  }

  next(){
  }
  
  prev(){
  }
}
