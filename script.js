const canvas = document.getElementById('gameCanvas');
const context = canvas.getContext('2d');

const ballRadius = 20;
const ballSpeed = 5;
let ballPosX = canvas.width / 2;
let ballPosY = canvas.height / 2;

document.addEventListener('keydown', moveBall);

function moveBall(event) {
    switch (event.key) {
        case 'ArrowLeft':
            ballPosX -= ballSpeed;
            break;
        case 'ArrowRight':
            ballPosX += ballSpeed;
            break;
        case 'ArrowUp':
            ballPosY -= ballSpeed;
            break;
        case 'ArrowDown':
            ballPosY += ballSpeed;
            break;
    }
}

function drawBall() {
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.beginPath();
    context.arc(ballPosX, ballPosY, ballRadius, 0, Math.PI * 2, false);
    context.fillStyle = 'red';
    context.fill();
    context.closePath();
}

function gameLoop() {
    drawBall();
    requestAnimationFrame(gameLoop);
}

gameLoop();
