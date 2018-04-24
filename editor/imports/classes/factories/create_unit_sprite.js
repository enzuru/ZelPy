import '/imports/classes/units/events/on_drag_start';
import '/imports/classes/units/events/on_drag_update';
import '/imports/classes/units/events/on_drag_stop';

createUnitSprite = (unit, spriteName) => {
  const sprite = unit.client.canvas.add.sprite(
    pixels(unit.x),
    pixels(unit.x),
    spriteName
  );
  const scale = Display.unitScale;

  //sprite.animations.play('walk', 5, false);
  //sprite.scale.x *= 5;
  //sprite.scale.y *= 5;

  sprite.inputEnabled  = true;
  sprite.input.enableDrag();
  sprite.animations.add('walk');
  sprite.input.enableSnap(scale, scale, false, true);
  sprite.left = true;
  sprite.boundsPadding = 0;
  sprite.events.onDragStart.add(onDragStart, this);
  sprite.events.onDragUpdate.add(onDragUpdate, this);
  sprite.events.onDragStop.add(onDragStop, this);
  sprite.unit = unit;

  return sprite;
}
