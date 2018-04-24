flipUnitDirection = (input) => {
  const unit = input.unit;
  const sprite = unit.sprite;

  if ((sprite.dragX > pixels(unit.previousX)) && sprite.left) {
    sprite.left = false;
    sprite.scale.x *= -1;
  }

  if ((sprite.dragX < pixels(sprite.previousX)) && !sprite.left) {
    sprite.left = true;
    sprite.scale.x *= -1;
  }

  return new Right(input);
}
