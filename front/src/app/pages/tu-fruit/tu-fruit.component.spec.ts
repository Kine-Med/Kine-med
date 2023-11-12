import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TuFruitComponent } from './tu-fruit.component';

describe('TuFruitComponent', () => {
  let component: TuFruitComponent;
  let fixture: ComponentFixture<TuFruitComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TuFruitComponent]
    });
    fixture = TestBed.createComponent(TuFruitComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
