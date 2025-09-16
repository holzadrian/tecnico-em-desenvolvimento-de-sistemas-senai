let velocidadeX = -7;
let velocidadeY = 5;
let posicaoX = 90;
let posicaoY = 267;
let cor = [255, 190, 200];

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(cor[0], cor[1], [2]);
  
  // círculo
  fill(0, 0, 0);
  stroke(100, 100, 100);
  ellipse(posicaoX, posicaoY, 100);

  // inverter direção se bater nas bordas
  if (posicaoX >= 350 || posicaoX <= 50) {
    velocidadeX = velocidadeX * -1;
  
  }
  if (posicaoY >= 350 || posicaoY <= 50) {
    velocidadeY = velocidadeY * -1;
  }

  // mover
  posicaoX = posicaoX + velocidadeX;
  posicaoY = posicaoY + velocidadeY;
  
  rect(330, 330, 40)
}

  function mousePressed() {
    if(mouseX >- 330 && mouseX <= 370 && mouseY >= 330 && mouseY <= 370)
    cor = [255, 0, 0];
}