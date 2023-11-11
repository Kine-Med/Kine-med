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
  bool: boolean = false;
  bool2: boolean = false;

  ngOnInit(): void {
    this.setupCamera();
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
      this.bool = true;
      this.bool2 = false;
    }, 4000);

  }


  async sendFrameToServer() {
    this.n = this.n + 1;
    const canvas = document.createElement('canvas');
    const videoElement: HTMLVideoElement = <HTMLVideoElement>document.getElementById("videoSource")
    canvas.width = videoElement.videoWidth;
    canvas.height = videoElement.videoHeight;
    var canvasContext = canvas.getContext("2d");
    canvasContext!.drawImage(videoElement, 0, 0);
    const imageDataURL = canvas.toDataURL('image/jpeg');
    /*fetch('http://localhost:5000/feed', {
      method: 'POST',
      body: JSON.stringify({ imageDataURL }), // You can adjust the data format as needed
      headers: {
        'Content-Type': 'application/json',
      },
    });*/
  }


  async setupCamera() {
    try {
      var constraints = {
        audio: false,
        video: {}
      };
      const stream = await navigator.mediaDevices.getUserMedia(constraints);
      const videoElement: HTMLVideoElement = <HTMLVideoElement>document.getElementById("videoSource")
      videoElement.srcObject = stream;
      setInterval(this.sendFrameToServer, 200);
    } catch (error) {
      console.error('Error accessing the webcam:', error);
    }
  }
}
