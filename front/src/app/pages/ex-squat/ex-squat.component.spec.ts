import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExSquatComponent } from './ex-squat.component';

describe('ExSquatComponent', () => {
  let component: ExSquatComponent;
  let fixture: ComponentFixture<ExSquatComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ExSquatComponent]
    });
    fixture = TestBed.createComponent(ExSquatComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
