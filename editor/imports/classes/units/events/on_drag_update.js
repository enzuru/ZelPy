import '/imports/transactions/transactions/units/update_moving_unit'

onDragUpdate = (sprite, pointer, dragX, dragY) => {
  unit = sprite.unit;
  updateMovingUnit({ unit, pointer, dragX, dragY});
}
