import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { VideoComponent } from './video/video.component';
import { StatsComponent } from './stats/stats.component';
import {HttpClientModule} from "@angular/common/http";
import { RocketsComponent } from './rockets/rockets.component';

@NgModule({
  declarations: [
    AppComponent,
    VideoComponent,
    StatsComponent,
    RocketsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
