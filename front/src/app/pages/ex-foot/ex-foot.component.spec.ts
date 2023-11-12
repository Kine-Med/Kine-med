import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExFootComponent } from './ex-foot.component';

describe('ExFootComponent', () => {
  let component: ExFootComponent;
  let fixture: ComponentFixture<ExFootComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ExFootComponent]
    });
    fixture = TestBed.createComponent(ExFootComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
