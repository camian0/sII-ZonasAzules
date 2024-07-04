import { Component, OnInit } from '@angular/core';
import { MatTableModule } from '@angular/material/table';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatDialog, MatDialogModule, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { FormsModule } from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { Inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { ZonesService } from 'src/app/services/zones.service';
import { Zone } from 'src/app/models/zone';
import Swal from 'sweetalert2'

@Component({
  selector: 'app-zones',
  standalone: true,
  imports: [
    CommonModule,
    HttpClientModule,  // Importa el módulo HttpClientModule aquí
    MatButtonModule,
    MatInputModule,
    MatSelectModule,
    MatTableModule,
    MatIconModule,
    MatFormFieldModule,
    FormsModule,
    MatDialogModule
  ],
  templateUrl: './zones.component.html',
  styleUrls: ['./zones.component.css']
})
export class ZonesComponent implements OnInit {
  displayedColumns: string[] = ['name', 'address', 'latitude','longitude', 'total_car_places', 'total_moto_places', 'price_car', 
    'price_moto','observation', 'ubication', 'edit', 'delete'];

  public zones: Array<any> = [];
  
  constructor(
    public dialog: MatDialog,
    public zonesSrv: ZonesService
  ) {}

  ngOnInit(): void {
    this.getZonesBlue();
    Swal.fire({
      title: 'Error!',
      text: 'Do you want to continue',
      icon: 'error',
      confirmButtonText: 'Cool'
    })
  }

  getZonesBlue(){
    this.zonesSrv.get().subscribe((resp: any) => {
      if (resp.status === 200) {
        console.log(resp.data);
        this.zones = resp.data;
      } else {
        // Handle error here
      }
    });
  }

  openDialog(zona: Zone): void {
    const dialogRef = this.dialog.open(EditarZonaDialog, {
      width: '500px',
      data: { ...zona }
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      if (result) {
        this.getZonesBlue(); // Refrescar la tabla después de la actualización
      }
    });
  }

  buscarUbicacion() {
    console.log("puedo buscar la ubicación");
  }
}

@Component({
  selector: 'editar-zona-dialog',
  standalone: true,
  imports: [
    CommonModule,
    MatButtonModule,
    MatFormFieldModule,
    MatInputModule,
    FormsModule,
    MatDialogModule,
    HttpClientModule
  ],
  templateUrl: './modal.html'
})
export class EditarZonaDialog {
  constructor(
    public dialogRef: MatDialogRef<EditarZonaDialog>,
    @Inject(MAT_DIALOG_DATA) public data: Zone,
    private zonesSrv: ZonesService
  ) {}

  onCancel(): void {
    this.dialogRef.close();
  }

  onSave(): void {
    console.log("Prueba put");
    console.log(this.data);
    this.zonesSrv.put(this.data).subscribe(response => {
      if (response.status === 200) {
        this.dialogRef.close(this.data);
      } else {
        // Handle error here
        console.error('Error updating zone:', response.errors);
      }
    });
  }
}
