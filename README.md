var diameter = 50;
var diameter1 = 5;

var drawCave = function(x, y) {
  fill(55,44,44);
  arc(x, (y + 100), 100, 120, radians(180), radians(360));

  fill(0,0,0);
  arc(x, (y + 100), 50, 60, radians(180), radians(360));

};

var mouthOpen = 0;
var x = 0, y = 0; // declare two vars on a single line!
var a = 0, b = 0;
var direction = 1; // 1 right, -1 left
var ydirection = 0

const faceRight = 1
const faceLeft = -1; // Know whether facing right or left

var speed = 5;


function setup() {
  createCanvas(800, 600);
  frameRate(60); //Frames per second
  y = height/2;
}

function draw() {

  background(0,0,255);
  for (var i = 200; i <= 600; i = i + 400) {
    drawCave(i, 2);
}

  noStroke()
  fill(225, 225, 0);
  arc(x, y, diameter, diameter, 0, radians(360));

  fill(0, 0, 0);
  arc((x - 10), (y - 10) , diameter1, diameter1, 0, radians(360));

  fill(0, 0, 0);
  arc((x + 10), (y - 10), diameter1, diameter1, 0, radians(360));

  fill(0,0,0);
  square((x-10),(y),20,5,5,5,5);

  if ((x > width -  diameter) || (x < diameter)  || (y > height - diameter ) || ( y < diameter )) // new edge detection
  // if ((x > width + diameter) || (x < 0 - diameter) || (y > height + diameter) || ( y < 0 - diameter)) // new edge detection
  {
      direction = - direction;
      ydirection = - direction;
      x = (diameter, width - diameter); // keep on screen 
      y = (diameter, height - diameter); // keep on screen 
  }

  // Check key presses format
  if (keyIsPressed)
  {
    if (key == "a") {
      direction = faceLeft
      x += speed * direction;
      ydirection = 0
    }
    else if (key == "d") {
      direction = faceRight
      x += speed * direction;
      ydirection = 0
    } 
    else if ((key == "w")) {
      ydirection =  - 1
      y += speed * ydirection; 
      direction = 0
    }
    else if ((key == "s")) {
      ydirection = 1
      y += speed * ydirection; 
      direction = 0
    }
  }}
