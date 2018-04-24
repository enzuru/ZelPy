createPopupOptionsSprite = (popup) => {
  const unit = popup.unit;
  const canvas = unit.client.canvas;
  const width = 150;
  const height = 100;
  const bmd = canvas.add.bitmapData(width, height);

  bmd.ctx.beginPath();
  bmd.ctx.rect(unit.sprite.x, unit.sprite.y, width, height);
  bmd.ctx.fillStyle = '#ffffff';
  bmd.ctx.fill();

  var sprite = canvas.add.sprite(
    unit.sprite.x + unit.sprite.width,
    unit.sprite.y + unit.sprite.height,
    bmd,
  );
  sprite = sprite.anchor.setTo(0.5, 0.5);
  sprite.unit = unit;

  return sprite;
}
