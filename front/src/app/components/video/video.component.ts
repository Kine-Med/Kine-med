import {Component, EventEmitter, Output} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

@Component({
  selector: 'app-video',
  templateUrl: './video.component.html',
  styleUrls: ['./video.component.scss']
})

export class VideoComponent {
  constructor(private http: HttpClient) { setTimeout(() => { this.timer()}, 200)};

  n: number = 3;
  bool2: boolean = false;

  ngOnInit(): void {
    console.log("VideoComponent");
    console.error("VideoComponent");
  }

  timer() {
    setTimeout(() => {
      this.n = 2;
    }, 1000);
    setTimeout(() => {
      this.n = 1;
    }, 2000);   setTimeout(() => {
      this.n = 0;
      this.bool2 = true;
    }, 3000);
    setTimeout(() => {
      this.bool2 = false;
    }, 4000);

  } 
}
