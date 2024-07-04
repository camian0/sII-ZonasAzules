import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreditCardsComponent } from './credit-cards.component';

describe('CreditCardsComponent', () => {
  let component: CreditCardsComponent;
  let fixture: ComponentFixture<CreditCardsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CreditCardsComponent]
    });
    fixture = TestBed.createComponent(CreditCardsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
