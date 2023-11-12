import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { VideoComponent } from './components/video/video.component';
import { StatsComponent } from './components/stats/stats.component';
import { ExSquatComponent } from "./pages/ex-squat/ex-squat.component";
import {HomeComponent} from "./pages/home/home.component";
import { TutorialComponent } from './pages/tutorial/tutorial.component';
import { ProfilComponent } from './pages/profil/profil.component';
import {TuGestureComponent} from "./components/tu-gesture/tu-gesture.component";
const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path: 'ex/squat', component: ExSquatComponent},
  { path: 'profil', component: ProfilComponent},
  { path: 'tutorial/gesture', component: TuGestureComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
