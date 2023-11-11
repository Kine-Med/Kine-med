import { Component } from '@angular/core';

@Component({
  selector: 'app-video',
  templateUrl: './video.component.html',
  styleUrls: ['./video.component.scss']
})
export class VideoComponent {
  ngOnInit(): void {
    this.setupCamera();
  }

  async setupCamera() {
    try {
      var constraints = {
        audio: false,
        video: { width: 640, height: 500 }
      };
      const stream = await navigator.mediaDevices.getUserMedia(constraints);
      const videoElement: HTMLVideoElement = <HTMLVideoElement>document.getElementById("videoElement")
      videoElement.srcObject = stream;
    } catch (error) {
      console.error('Error accessing the webcam:', error);
    }
  }
}
