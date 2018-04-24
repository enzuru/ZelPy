sendUnitBack = (input) => {
  input.unit.sprite.input.disableDrag();
  unit.moveBack();
  input.unit.sprite.input.enableDrag();
  return new Right(input);
}
