checkIfDistanceAllowed = (input) => {
  const unit = input.unit;
  const abs = Math.abs;
  const distance = abs(tiles(unit.sprite.x) - unit.previousX) +
                   abs(tiles(unit.sprite.y) - unit.previousY);

  if (distance > unit.moveLimit) {
    return new Left("Distance too far for unit");
  }

  return new Right(input);
}
