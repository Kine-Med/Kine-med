import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { VideoComponent } from './components/video/video.component';
import { StatsComponent } from './components/stats/stats.component';
import { HttpClientModule } from "@angular/common/http";
import { RocketsComponent } from './components/rockets/rockets.component';
import { ShapeComponent } from './components/shape/shape.component';
import { ExSquatComponent } from './pages/ex-squat/ex-squat.component';
import { HomeComponent } from './pages/home/home.component';
import { FooterComponent } from './footer/footer.component';
import { TutorialComponent } from './pages/tutorial/tutorial.component';
import { ProfilComponent } from './pages/profil/profil.component';
import { CardComponent } from './components/card/card.component';
import { TuGestureComponent } from './components/tu-gesture/tu-gesture.component';
import { ExFootComponent } from './pages/ex-foot/ex-foot.component';


@NgModule({
  declarations: [
    AppComponent,
    VideoComponent,
    StatsComponent,
    RocketsComponent,
    ShapeComponent,
    RocketsComponent,
    ExSquatComponent,
    HomeComponent,
    FooterComponent,
    TutorialComponent,
    ProfilComponent,
    CardComponent,
    TuGestureComponent,
    ExFootComponent,
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
