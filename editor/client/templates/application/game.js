import '/imports/classes/base/client';
import '/imports/classes/base/rain';
import '/imports/classes/units/soldier';

var player = location.search.split('player=')[1]
if (!player) player = '1';

var width = window.innerWidth;
var height = window.innerHeight;

var client = new Client(Display.maxWidth, Display.maxHeight, player, init, preload, create, render);
var canvas = client.canvas;

var firstRunPortrait;

function handleIncorrect() {
  if (!canvas.device.desktop) {
    document.getElementById("turn").style.display = "block";
  }
}

function handleCorrect() {
  if (!canvas.device.desktop) {
    if (firstRunPortrait) {
	  canvas.width = width;
	  canvas.height = height + 10;
	  canvas.renderer.resize(canvas.width, canvas.height);
	  canvas.state.start("Play");		
	}
	document.getElementById("turn").style.display = "none";
  }

  window.addEventListener("load",function() {
	// Set a timeout...
	setTimeout(function(){
	  // Hide the address bar!
	  window.scrollTo(0, 1);
	}, 0);
  });
}

var result = 'Drag a sprite';

function init() {
  canvas.scale.scaleMode = Phaser.ScaleManager.SHOW_ALL;
  canvas.scale.setMinMax(
    Display.minWidth,
    Display.minHeight,
    Display.maxWidth,
    Display.maxHeight,
  );
}

function preload() {
  firstRunPortrait = canvas.scale.isGamePortrait;
  canvas.load.spritesheet('ms', 'images/wars.png', 67, 66);
  canvas.load.spritesheet('rain', 'images/rain.png', 17, 17);
  canvas.load.image('grid', 'images/background2.png');
  canvas.load.image('soldier', 'images/soldier2.png');

  canvas.scale.forceOrientation(true, false);
  canvas.scale.enterIncorrectOrientation.add(handleIncorrect);
  canvas.scale.leaveIncorrectOrientation.add(handleCorrect);
}

function create() {
  //const rain = new Rain(client);
  canvas.add.sprite(0, 0, 'grid');

  const soldier1 = new Soldier(client, 1, 0, 0);
  client.add(soldier1);
  
  const soldier2 = new Soldier(client, 2, 2, 2);
  client.add(soldier2);
}

function update() {
  //
}

function render() {
  canvas.debug.text(result, 10, 20);
  var posts = Posts.find({executed: false, player: {$ne: player}}, {sort: {submitted: 1}});
  posts.forEach(function(lastPost) {
    client.objects[lastPost.id].update(lastPost.x, lastPost.y);
    Posts.update(lastPost._id, { $set: {executed: true}});
  });
}

const setBoard = () => {
  var posts = Posts.find({}, {sort: {submitted: -1}});
  console.log("loading...");
  console.log(posts.count());
  posts.forEach(function(lastPost) {
    if (lastPost.x) {
      console.log('fuck yeah');
      client.objects[lastPost.id].update(lastPost.x, lastPost.y);
    }
  });
}

setTimeout(setBoard, 1000);
