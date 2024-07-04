import { Component, OnInit, Inject } from '@angular/core';
import { MatTableModule } from '@angular/material/table';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import {
  MatDialog,
  MatDialogModule,
  MatDialogRef,
  MAT_DIALOG_DATA,
} from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { FormsModule } from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { ZonesService } from 'src/app/services/zones.service';
import { Zone } from 'src/app/models/zone';
import Swal from 'sweetalert2';
import { ZoneCreate } from 'src/app/models/request/zoneCreateModel';

@Component({
  selector: 'app-zones',
  standalone: true,
  imports: [
    CommonModule,
    HttpClientModule,
    MatButtonModule,
    MatInputModule,
    MatSelectModule,
    MatTableModule,
    MatIconModule,
    MatFormFieldModule,
    FormsModule,
    MatDialogModule,
  ],
  templateUrl: './zones.component.html',
  styleUrls: ['./zones.component.css'],
})
export class ZonesComponent implements OnInit {
  displayedColumns: string[] = [
    'name',
    'address',
    'latitude',
    'longitude',
    'total_car_places',
    'total_moto_places',
    'price_car',
    'price_moto',
    'observation',
    'ubication',
    'edit',
    'delete',
  ];

  public zones: Array<any> = [];
  public sectors: Array<any> = [];
  public selectedSector: number = 0;

  constructor(public dialog: MatDialog, public zonesSrv: ZonesService) {}

  ngOnInit(): void {
    this.getZonesBlue();
    this.getSectors();
    Swal.fire({
      title: 'Error!',
      text: 'Do you want to continue',
      icon: 'error',
      confirmButtonText: 'Cool',
    });
  }

  getZonesBlue() {
    this.zonesSrv.get().subscribe((resp: any) => {
      if (resp.status === 200) {
        console.log(resp.data);
        this.zones = resp.data;
      } else {
        // Handle error here
      }
    });
  }

  getZonesBlueByArea() {
    this.zonesSrv.getByArea(this.selectedSector).subscribe((resp: any) => {
      switch (resp.status) {
        case 200:
          console.log(resp.data);
          this.zones = resp.data;
          if (this.zones.length > 0) {
            Swal.fire({
              title: 'Cargue Exitoso',
              text: resp.message,
              icon: 'success',
              confirmButtonText: 'Aceptar',
            });
          } else {
            Swal.fire({
              title: 'No se encontraron registros.',
              text: resp.message,
              icon: 'warning',
              confirmButtonText: 'Aceptar',
            });
          }
          break;
        default:
          Swal.fire({
            title: 'Oh Oh!',
            text: resp.message,
            icon: 'error',
            confirmButtonText: 'Cool',
          });
          break;
      }
    });
  }

  deleteZone(zona: Zone) {
    Swal.fire({
      title: '¿Está seguro?',
      text: 'No podrá revertir esta acción.',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Sí, eliminar',
      cancelButtonText: 'Cancelar',
    }).then((result) => {
      if (result.isConfirmed) {
        this.zonesSrv.delete(zona.id).subscribe((resp: any) => {
          switch (resp.status) {
            case 200:
              Swal.fire({
                title: 'Zona eliminada',
                text: resp.message,
                icon: 'success',
                confirmButtonText: 'Aceptar',
              });
              // Remove the deleted zone from the zones array
              const index = this.zones.findIndex((z: Zone) => z.id === zona.id);
              if (index !== -1) {
                this.zones.splice(index, 1);
              }
              this.getZonesBlue();
              break;
            case 400:
              Swal.fire({
                title: 'Error en la solicitud',
                text: resp.message,
                icon: 'warning',
                confirmButtonText: 'Aceptar',
              });
              break;
            case 500:
              Swal.fire({
                title: 'Oh Oh!',
                text: resp.message,
                icon: 'error',
                confirmButtonText: 'Cool',
              });
              break;
          }
        });
      }
    });
  }

  getSectors() {
    this.zonesSrv.getSectors().subscribe((resp: any) => {
      if (resp.status === 200) {
        console.log(resp.data);
        this.sectors = resp.data;
      } else {
        // Handle error here
      }
    });
  }

  openDialog(zona: Zone): void {
    const dialogRef = this.dialog.open(EditZoneDialog, {
      width: '500px',
      data: { ...zona, sectors: this.sectors },
    });

    dialogRef.afterClosed().subscribe((result) => {
      console.log('The dialog was closed');
      if (result) {
        this.getZonesBlue(); // Refrescar la tabla después de la actualización
      }
    });
  }

  buscarUbicacion() {
    console.log('puedo buscar la ubicación');
  }

  eliminarZona(zone: Zone) {
    console.log('Eliminar zona', zone);
    this.deleteZone(zone);
  }

  buscar() {
    this.getZonesBlueByArea();
  }

  create() {
    const dialogRef = this.dialog.open(CreateZoneDialog, {
      width: '500px',
      data: { sectors: this.sectors },
    });

    dialogRef.afterClosed().subscribe((result) => {
      console.log('The dialog was closed');
      if (result) {
        this.getZonesBlue(); // Refrescar la tabla después de la creación
      }
    });
  }
}

@Component({
  selector: 'editar-zona-dialog',
  templateUrl: './modal.html',
  standalone: true,
  imports: [
    CommonModule,
    MatButtonModule,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    FormsModule,
    MatDialogModule,
    HttpClientModule,
  ],
})
export class EditZoneDialog {
  public sectors: Array<any> = [];

  constructor(
    public dialogRef: MatDialogRef<EditZoneDialog>,
    @Inject(MAT_DIALOG_DATA) public data: Zone,
    private zonesSrv: ZonesService
  ) {}

  onCancel(): void {
    this.dialogRef.close();
  }

  onSave(): void {
    this.zonesSrv.put(this.data).subscribe((response) => {
      switch (response.status) {
        case 200:
          Swal.fire({
            title: 'Zona actualizada',
            text: response.message,
            icon: 'success',
            confirmButtonText: 'Aceptar',
          });
          this.dialogRef.close(this.data);
          break;
        case 400:
          Swal.fire({
            title: 'Error en la solicitud',
            text: response.message,
            icon: 'warning',
            confirmButtonText: 'Aceptar',
          });
          this.dialogRef.close(this.data);
          break;
        default:
          Swal.fire({
            title: 'Oh Oh!',
            text: response.message,
            icon: 'error',
            confirmButtonText: 'Cool',
          });
          console.error('Error updating zone:', response.errors);
          break;
      }
    });
  }
}

@Component({
  selector: 'crear-zona-dialog',
  templateUrl: './createZone.html',
  standalone: true,
  imports: [
    CommonModule,
    MatButtonModule,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    FormsModule,
    MatDialogModule,
    HttpClientModule,
  ],
})
export class CreateZoneDialog {
  public data: ZoneCreate = {
    name: '',
    address: '',
    observation: '',
    latitude: 0,
    longitude: 0,
    total_car_places: 0,
    total_moto_places: 0,
    price_car: 0,
    price_moto: 0,
    area_id: 0,
  };
  public sectors: Array<any> = [];

  constructor(
    public dialogRef: MatDialogRef<CreateZoneDialog>,
    @Inject(MAT_DIALOG_DATA) public dialogData: any,
    private zonesSrv: ZonesService
  ) {
    this.sectors = dialogData.sectors;
  }

  onCancel(): void {
    this.dialogRef.close();
  }

  onSave(): void {
    console.log(this.data);
    this.zonesSrv.post(this.data).subscribe((response) => {
      if (response.status === 200) {
        Swal.fire({
          title: 'Zona creada',
          text: response.message,
          icon: 'success',
          confirmButtonText: 'Aceptar',
        });
        this.dialogRef.close(this.data);
      } else {
        Swal.fire({
          title: 'Error en la solicitud',
          text: response.message,
          icon: 'warning',
          confirmButtonText: 'Aceptar',
        });
        this.dialogRef.close();
      }
    });
  }
}
