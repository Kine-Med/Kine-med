import {Component, Input} from '@angular/core';

@Component({
  selector: 'app-shape',
  templateUrl: './shape.component.html',
  styleUrls: ['./shape.component.scss']
})

export class ShapeComponent {
  @Input() shape: string = "assets/squat_down.png";

  constructor() {
    setInterval(() => this.squatYourBootieBootie(), 1300);
  }

  squatYourBootieBootie() {
    console.log(this.shape)
    if (this.shape.includes("up"))
      this.shape = "assets/squat_down.png"
    else
      this.shape = "assets/squat_up.png"
  }
}
