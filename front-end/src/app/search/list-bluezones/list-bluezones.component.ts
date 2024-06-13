import { Component } from '@angular/core';
import { getData } from '../../../request/request';
import { MatSnackBar } from '@angular/material/snack-bar';
import { NotificationService } from '../../shared/services/notifications.service';
import { MatTableModule } from '@angular/material/table';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-list-bluezones',
  standalone: true,
  templateUrl: './list-bluezones.component.html',
  styleUrls: ['./list-bluezones.component.css'],
  imports: [MatTableModule, CommonModule],
})
export class ListBluezonesComponent {
  token: string =
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InVzZXJAZXhhbXBsZS5jb20iLCJyb2xlX2lkIjoyfQ.D8IqHKmqU1Sx3KgtPKvhhG-Tr9YsPnh8_KYPyCk7lC0';
  model: object;
  blueZones = [];
  displayedColumns: string[] = ['id', 'name', 'address', 'observation'];
  dataSource = this.blueZones;
  constructor(public notificationService: NotificationService) {
    this.model = {
      id: 0,
      name: '',
      address: '',
      observation: '',
    };
  }
  ngOnInit() {
    this.getBlueZones();
  }

  async getBlueZones(): Promise<void> {
    localStorage.setItem('token', this.token);
    await getData('blue-zone', {})
      .then((res) => {
        if (res.status === 200) {
          this.notificationService.success('Zona azules obtenidas con exito');
          this.blueZones = res.data;
          console.log('blue', this.blueZones);
          return;
        }
        console.log('error', res.message);
      })
      .catch(() => {
        console.log('alguna cosa');
      });
  }
}
