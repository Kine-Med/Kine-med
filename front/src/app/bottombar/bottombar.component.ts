import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-bottombar',
  templateUrl: './bottombar.component.html',
  styleUrls: ['./bottombar.component.scss']
})
export class BottombarComponent {
  @Output() buttonClick = new EventEmitter<number>();

  onButtonClick(buttonNumber: number): void {
    this.buttonClick.emit(buttonNumber);
  }

}
