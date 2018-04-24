Rain = class Rain {
  constructor(client) {
    const canvas = client.canvas;
    const emitter = canvas.add.emitter(canvas.world.centerX, 0, 400);

    emitter.width = canvas.world.width;
    emitter.makeParticles('rain');
    emitter.minParticleScale = 0.1;
    emitter.maxParticleScale = 0.5;
    emitter.setYSpeed(300, 500);
    emitter.setXSpeed(-5, 5);
    emitter.minRotation = 0;
    emitter.maxRotation = 0;
    emitter.start(false, 1600, 5, 0);
  }
}
