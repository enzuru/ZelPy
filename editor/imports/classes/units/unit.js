import '/imports/classes/factories/create_unit_sprite';

Unit = class Unit {
  constructor (client, player, x, y) {
    this.id = autoincrement();
    this.moveLimit = 1;

    this.x = x;
    this.y = y;
    this.client = client;
    this.player = player;
    this.highlights = [];
    this.status = 'available';
  }

  move(x, y) {
    this.x = x;
    this.y = y;
    this.sprite.x = pixels(x);
    this.sprite.y = pixels(y);
  }

  update(x, y) {
    this.previousX = this.x;
    this.previousY = this.y;
    this.move(x, y);
  }

  moveBack() {
    console.log(this.previousX);
    this.move(this.previousX, this.previousY);
  }
}
