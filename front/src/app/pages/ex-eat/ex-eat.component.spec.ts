import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExEatComponent } from './ex-eat.component';

describe('ExEatComponent', () => {
  let component: ExEatComponent;
  let fixture: ComponentFixture<ExEatComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ExEatComponent]
    });
    fixture = TestBed.createComponent(ExEatComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
