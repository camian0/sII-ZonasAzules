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
  titular_name: '',
  number: '',
  cvc: '',
  user_id: 2,
  expiry_date: ''  
  };

  saveCard = false;

  privacyAccepted = false;
  selectedCardBrand: string | null = null;

  public totalRes: number = 0;
  

  constructor(private http: HttpClient, public totalRsv: creditcardService, public newCard: creditcardService) { }

  ngOnInit(): void {
    this.getTotal();
  }



  getTotal() {
    this.totalRsv.getReservUserById(2).subscribe((resp: any) => {
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
      if(!this.saveCard){this.newCard.postCard(this.card).subscribe((resp: any) => {
        if (resp.status === 200) {
          console.log(resp.data)
          this.newCard = resp.data;
        }
      })}
      
    }
  
   

    // Este método se llamará cuando se haga clic en una marca de tarjeta
  selectCardBrand(brand: string) {
    this.selectedCardBrand = brand;
    console.log(`Selected card brand: ${brand}`);
  }
      
    
}

