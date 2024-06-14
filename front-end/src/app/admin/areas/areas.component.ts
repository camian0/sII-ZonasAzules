import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { Component, Inject, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MAT_DIALOG_DATA, MatDialog, MatDialogModule, MatDialogRef } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatTableModule } from '@angular/material/table';
import { Area } from 'src/app/models/areaModel';
import { AreasService } from 'src/app/services/areas.services';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-areas', 
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
    MatDialogModule
  ],
  templateUrl: './areas.component.html',
  styleUrls: ['./areas.component.css']
})
export class AreasComponent implements OnInit  {
  displayedColumns: string[] = ['name', 'edit', 'delete'];
  public areas: Array<any> = [];

  constructor(
    public dialog: MatDialog,
    public areasSrv: AreasService
  ) {}

  ngOnInit(): void {
    this.getAreas();
  }

  getAreas() {
    this.areasSrv.get().subscribe((resp: any) => {
      if (resp.status === 200) {
        console.log(resp.data);
        this.areas = resp.data;
      } else {
        // Handle error here
      }
    });
  }

  editArea(area: Area): void {
    const dialogRef = this.dialog.open(EditAreaDialog, {
      width: '500px',
      data: { ...area, sectors: this.areas }
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      if (result) {
        this.getAreas(); // Refrescar la tabla después de la actualización
      }
    });
  }

  deleteZone(area: Area) {
    Swal.fire({
      title: '¿Está seguro?',
      text: 'No podrá revertir esta acción.',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Sí, eliminar',
      cancelButtonText: 'Cancelar'
    }).then((result) => {
      if (result.isConfirmed) {
        this.areasSrv.delete(area.id).subscribe((resp: any) => {
          switch (resp.status) {
            case 200:
              Swal.fire({
                title: 'Área eliminada',
                text: resp.message,
                icon: 'success',
                confirmButtonText: 'Aceptar'
              });
              // Remove the deleted area from the areas array
              const index = this.areas.findIndex((a: Area) => a.id === area.id);
              if (index !== -1) {
                this.areas.splice(index, 1);
              }
              this.getAreas();
              break;
            case 400:
              Swal.fire({
                title: 'Error en la solicitud',
                text: resp.message,
                icon: 'warning',
                confirmButtonText: 'Aceptar'
              });
              break;
            case 500:
              Swal.fire({
                title: 'Oh Oh!',
                text: resp.message,
                icon: 'error',
                confirmButtonText: 'Aceptar'
              });
              break;
          }
        });
      }
    });
  }

  openDialog(area: Area): void {
    const dialogRef = this.dialog.open(EditAreaDialog, {
      width: '500px',
      data: { ...area }
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      if (result) {
        this.getAreas(); // Refrescar la tabla después de la actualización
      }
    });
  }
}

@Component({
  selector: 'editar-zona-dialog',
  templateUrl: './editArea.html',
  standalone: true,
  imports: [
    CommonModule,
    MatButtonModule,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    FormsModule,
    MatDialogModule,
    HttpClientModule
  ]
})
export class EditAreaDialog {
  public sectors: Array<any> = [];

  constructor(
    public dialogRef: MatDialogRef<EditAreaDialog>,
    @Inject(MAT_DIALOG_DATA) public data: Area,
    private areasSrv: AreasService
  ) {
    
  }

  onCancel(): void {
    this.dialogRef.close();
  }

  onSave(): void {
    this.areasSrv.put(this.data).subscribe(response => {
      switch (response.status) {
        case 200:
          Swal.fire({
            title: 'Zona actualizada',
            text: response.message,
            icon: 'success',
            confirmButtonText: 'Aceptar'
          });
          this.dialogRef.close(this.data);
          break;
        case 400:
          Swal.fire({
            title: 'Error en la solicitud',
            text: response.message,
            icon: 'warning',
            confirmButtonText: 'Aceptar'
          });
          this.dialogRef.close(this.data);
          break;
        default:
          Swal.fire({
            title: 'Oh Oh!',
            text: response.message,
            icon: 'error',
            confirmButtonText: 'Aceptar'
          });
          console.error('Error updating zone:', response.errors);
          break;
      }
    });
  }
}
