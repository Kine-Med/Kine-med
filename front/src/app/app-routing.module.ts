import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ExSquatComponent } from "./pages/ex-squat/ex-squat.component";
import {HomeComponent} from "./pages/home/home.component";
import { ProfilComponent } from './pages/profil/profil.component';
import {TuGestureComponent} from "./pages/tu-gesture/tu-gesture.component";
import { ExKneeComponent } from './pages/ex-knee/ex-knee.component';
import {TuKneeComponent} from "./pages/tu-knee/tu-knee.component";
import {TuFruitComponent} from "./pages/tu-fruit/tu-fruit.component";
import { ExEatComponent } from './pages/ex-eat/ex-eat.component';

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path: 'ex/squat', component: ExSquatComponent},
  { path: 'profil', component: ProfilComponent},
  { path: 'tutorial/gesture', component: TuGestureComponent},
  { path: 'tutorial/knee', component: TuKneeComponent},
  { path: 'ex/knee', component: ExKneeComponent},
  { path: 'ex/eat', component: ExEatComponent},
  { path: 'tutorial/fruit', component: TuFruitComponent},
  { path: 'ex/knee', component: ExKneeComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
