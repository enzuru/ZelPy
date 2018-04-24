Client = class Client {
  constructor(width, height, player, init, preload, create, render) {
    this.canvas = new Phaser.Game(
      width,
      height,
      Phaser.AUTO,
      'phaser-example',
      {
        init: init,
        preload: preload,
        create: create,
        render: render
      }
    );
    this.player = player;
    this.objects = {};
  }

  add(object) {
    this.objects[object.id] = object;
  }
}
