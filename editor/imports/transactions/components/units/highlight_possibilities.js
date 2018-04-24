highlightPossibilities = (input) => {
  const canvas = input.unit.client.canvas;
  const sprite = input.unit.sprite;
  [[1, 0], [-1, 0], [0, -1], [0, 1]].forEach((element) => {
    var highlight;
    var bmd = canvas.add.bitmapData(Display.unitScale, Display.unitScale);
    bmd.ctx.beginPath();
    bmd.ctx.rect(0, 0, Display.unitScale, Display.unitScale);
    bmd.ctx.fillStyle = '#000000';
    bmd.ctx.fill();
    var xDelta = element[0] * Display.unitScale;
    var yDelta = element[1] * Display.unitScale;
    highlight = canvas.add.sprite(sprite.centerX + xDelta, sprite.centerY + yDelta, bmd);
    highlight.anchor.setTo(0.5, 0.5);
    highlight.alpha = 0.2;

    input.unit.highlights = input.unit.highlights.concat(highlight);
  });
  return new Right(input);
}
