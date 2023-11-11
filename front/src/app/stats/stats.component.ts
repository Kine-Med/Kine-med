import { Component } from '@angular/core';

@Component({
  selector: 'app-stats',
  templateUrl: './stats.component.html',
  styleUrls: ['./stats.component.scss']
})
export class StatsComponent {
  public progres: number = 0;
  public max: number = 30;
  ngOnInit(): void {
    this.progres = 1;
  }
}
