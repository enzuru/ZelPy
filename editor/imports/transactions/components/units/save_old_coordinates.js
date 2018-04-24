saveOldCoordinates = (input) => {
  const unit = input.unit;

  unit.previousX = unit.x;
  unit.previousY = unit.y;

  return new Right(input);
}
