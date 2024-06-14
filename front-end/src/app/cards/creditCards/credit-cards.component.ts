import { Card } from './../../models/card';
import { Component, Inject, OnInit } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { creditcardService } from 'src/app/services/credit-card.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatDialog, MatDialogModule, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatTableModule } from '@angular/material/table';
import { MatIconModule } from '@angular/material/icon';


@Component({
  selector: 'app-credit-cards',
  templateUrl: './credit-cards.component.html',
  styleUrls: ['./credit-cards.component.css'],
  standalone: true,

  imports: [
    CommonModule,
    FormsModule,
    MatDialogModule,
    MatButtonModule,
    MatInputModule,
    MatSelectModule,
    MatTableModule,
    MatIconModule,
    MatFormFieldModule
  ]
})
export class CreditCardsComponent implements OnInit {
  card = {
    titular_name: '',
    number: '',
    cvc: '',
    user_id: 2,
    expiry_date: ''
  };

  saveCard = false;

  privacyAccepted = false;
  selectedCardBrand: string | null = null;

  public listaTarjetas: Array<Card> = [];

 

  public totalRes: number = 0;


  constructor(private http: HttpClient, public totalRsv: creditcardService, public newCard: creditcardService,
    public dialog: MatDialog, public misTarjetas: creditcardService
  ) { }

  ngOnInit(): void {
    this.getTotal();
    this.getTarjetas();
  }



  getTotal() {
    this.totalRsv.getReservUserById(2).subscribe((resp: any) => {
      if (resp.status === 200) {
        console.log(resp.data)
        this.totalRes = resp.data[0].total_price;
      }
    })
  }

  getTarjetas() {
    this.misTarjetas.getCardUserById(2).subscribe((resp: any) => {
      if (resp.status === 200) {
        console.log(resp.data)
        this.listaTarjetas= resp.data;
      } else {
        console.error('Error al obtener tarjetas', resp);
      }
    });
  }


  onSubmit() {
    if (!this.privacyAccepted) {
      alert("Debe aceptar la política de privacidad.");
      return;
    }
    if (!this.saveCard) {
      this.newCard.postCard(this.card).subscribe((resp: any) => {
        if (resp.status === 200) {
          console.log(resp.data)
          this.newCard = resp.data;
        }
      })
    }

  }



  // Este método se llamará cuando se haga clic en una marca de tarjeta
  selectCardBrand(brand: string) {
    this.selectedCardBrand = brand;
    console.log(`Selected card brand: ${brand}`);
  }


  openDialog(): void {
    const dialogRef = this.dialog.open(MostrarTarjetasDialog, {
      width: '500px',
      data: { tarjetas: this.listaTarjetas }
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      if (result) {
        this.getTarjetas(); // Refrescar la tabla después de la actualización
      }
    });
  }


}

@Component({
  selector: 'mostrar-tarjetas-dialog',
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
export class MostrarTarjetasDialog {

  


  constructor(
    public dialogRef: MatDialogRef<MostrarTarjetasDialog>,
    @Inject(MAT_DIALOG_DATA) public data: { tarjetas: Card[] },
    private cardsSrv: creditcardService, 
  ) { }

  onCancel(): void {
    this.dialogRef.close();
  }

  onSave(): void {
    /* console.log("Prueba put");
     console.log(this.data);
     this.cardsSrv.put(this.data).subscribe(response => {
       if (response.status === 200) {
         this.dialogRef.close(this.data);
       } else {
         // Handle error here
         console.error('Error updating zone:', response.errors);
       }
     });
   }*/
  }

  eliminarTarjeta(index: number): void {
    const tarjeta = this.data.tarjetas[index];
    const numeroLimpio = tarjeta.number.replace(/\s+/g, '');

    this.cardsSrv.delete(numeroLimpio).subscribe(()=>{
      this.data.tarjetas.splice(index,1);
    },
  error => {
    console.error('Error al eliminar la tarjeta', error);
  });
  }
}
