import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { creditcardService } from 'src/app/services/credit-card.service';

@Component({
  selector: 'app-credit-cards',
  templateUrl: './credit-cards.component.html',
  styleUrls: ['./credit-cards.component.css']
})
export class CreditCardsComponent implements OnInit {
  card = {
    cardNumber: '',
    expiryDate: '',
    cvc: '',
    name: '',
    saveCard: false
  };

  privacyAccepted = false;

  public totalRes: number = 20;
  

  constructor(private http: HttpClient, public totalRsv: creditcardService) { }

  ngOnInit(): void {
    this.getTotal();
  }



  getTotal() {
    this.totalRsv.getUserById(2).subscribe((resp: any) => {
      if (resp.status === 200) {
        console.log(resp.data)
        this.totalRes = resp.data[0].total_price;
      }
    })
  }



  
    onSubmit() {
      if (!this.privacyAccepted) {
        alert("Debe aceptar la política de privacidad.");
        return;
      }
      this.totalRsv.post(this.card).subscribe((resp: any) => {
        if (resp.status === 200) {
          console.log(resp.data)
          this.totalRes = resp.data[0].total_price;
        }
      })
    }
  
    // Este método se llamará cuando se haga clic en una marca de tarjeta
    selectCardBrand(brand: string) {
      console.log(`Selected card brand: ${brand}`);
      // Aquí puedes manejar la lógica para la marca de tarjeta seleccionada
    }
      
}

