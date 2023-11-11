import {Component, Input} from '@angular/core';

@Component({
  selector: 'app-shape',
  templateUrl: './shape.component.html',
  styleUrls: ['./shape.component.scss']
})

export class ShapeComponent {
  @Input() shape: string = "assets/squat_up";
}
