import {Component, ElementRef, ViewChild} from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'KineMed';

  constructor(private router: Router) {}

  selectedButton: number = 1;

  onButtonClick(buttonNumber: number): void {
    switch (buttonNumber) {
      case 1:
        this.router.navigate(['/home']);
        break;
      case 2:
        this.router.navigate(['/search']);
        break;
      case 3:
        this.router.navigate(['/messages']);
        break;
      case 4:
        this.router.navigate(['/notifications']);
        break;
      case 5:
        this.router.navigate(['/profile']);
        break;
    }
  }
}
