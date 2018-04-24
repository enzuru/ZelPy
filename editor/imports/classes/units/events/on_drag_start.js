import '/imports/transactions/transactions/units/start_moving_unit'

onDragStart = (sprite, pointer) => {
  unit = sprite.unit;
  startMovingUnit({ unit, pointer });
}
