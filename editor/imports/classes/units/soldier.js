import '/imports/classes/units/unit';

Soldier = class Soldier extends Unit {
  constructor (client, player, x, y) {
    super(client, player, x, y);

    this.moveLimit = 1;
    this.sprite = createUnitSprite(this, 'soldier');
  }
}
