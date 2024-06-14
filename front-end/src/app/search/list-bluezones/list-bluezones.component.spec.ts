import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListBluezonesComponent } from './list-bluezones.component';

describe('ListBluezonesComponent', () => {
  let component: ListBluezonesComponent;
  let fixture: ComponentFixture<ListBluezonesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ListBluezonesComponent]
    });
    fixture = TestBed.createComponent(ListBluezonesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
