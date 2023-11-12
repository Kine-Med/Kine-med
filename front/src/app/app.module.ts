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
import { ProfilComponent } from './pages/profil/profil.component';
import { CardComponent } from './components/card/card.component';
import { TuGestureComponent } from './pages/tu-gesture/tu-gesture.component';
import { ExKneeComponent } from './pages/ex-knee/ex-knee.component';
import { TuKneeComponent } from './pages/tu-knee/tu-knee.component';
import { TuFruitComponent } from './pages/tu-fruit/tu-fruit.component';
import { ExEatComponent } from './pages/ex-eat/ex-eat.component';


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
    ProfilComponent,
    CardComponent,
    TuGestureComponent,
    ExKneeComponent,
    TuKneeComponent,
    TuFruitComponent,
    ExEatComponent,
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
