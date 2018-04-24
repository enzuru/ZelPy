import '/imports/transactions/transactions/units/end_moving_unit'

onDragStop = (sprite, pointer) => {
  unit = sprite.unit;
  endMovingUnit({ unit, pointer });
}
