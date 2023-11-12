import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TuKneeComponent } from './tu-knee.component';

describe('TuKneeComponent', () => {
  let component: TuKneeComponent;
  let fixture: ComponentFixture<TuKneeComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TuKneeComponent]
    });
    fixture = TestBed.createComponent(TuKneeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
