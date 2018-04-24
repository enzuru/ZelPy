saveMove = (input) => {
  const unit = input.unit;

  unit.move(tiles(unit.sprite.x), tiles(unit.sprite.y));

  Posts.insert({
    id: unit.id,
    player: unit.player,
    x: unit.x,
    y: unit.y,
    submitted: Date.now,
    executed: false
  });

  return new Right(input);
}
