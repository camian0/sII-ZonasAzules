import { Component } from '@angular/core';
import { getData } from '../../../request/request';

@Component({
  selector: 'app-list-bluezones',
  standalone: true,
  templateUrl: './list-bluezones.component.html',
  styleUrls: ['./list-bluezones.component.css'],
})
export class ListBluezonesComponent {
  model: object;
  constructor() {
    this.model = {
      id: 0,
      name: '',
      address: '',
      observation: '',
    };
  }

  async getBlueZones() {
    await getData('blue-zone', {})
      .then((res) => {
        console.log('otra cosa');
      })
      .catch(() => {
        console.log('alguna cosa');
      });
  }
}
