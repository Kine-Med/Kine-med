import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TuGestureComponent } from './tu-gesture.component';

describe('TuGestureComponent', () => {
  let component: TuGestureComponent;
  let fixture: ComponentFixture<TuGestureComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TuGestureComponent]
    });
    fixture = TestBed.createComponent(TuGestureComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
