import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { VideoComponent } from './video/video.component';
import { StatsComponent } from './stats/stats.component';
import { ExSquatComponent } from "./ex-squat/ex-squat.component";

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: VideoComponent },
  { path: 'search', component: StatsComponent },
  { path: 'exercice/squat', component: ExSquatComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
