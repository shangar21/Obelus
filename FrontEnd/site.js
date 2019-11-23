function sayHello()
{
	alert("hello");
}

function setup() 
{
  mic = new p5.AudioIn();
  mic.start();
  createCanvas(400, 400);
}

function draw() 
{
  background(220);
  var vol = mic.getLevel();
  ellipse(200, 400, 4000*vol, 4000*vol);
  console.log(vol);
}

