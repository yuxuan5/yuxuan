/**
 * Created by storm on 2017/5/18.
 */
let gradient = {
    .05: '#FFFFCC',
    .5: '#FED976',
    .7: '#FD8D3C',
    .85: '#E31A1C',
    1: '#800050'
};

let canvas = document.createElement("canvas");
let ctx = canvas.getContext("2d");
let gradc = ctx.createLinearGradient(0, 0, 0, 256);
canvas.width=1;
canvas.height=256;

for (let key in gradient) {
    gradc.addColorStop(key, gradient[key]);
}

ctx.fillStyle = gradc;
ctx.fillRect(0, 0, 1, 256);

let color = ctx.getImageData(0, 0, 1, 256).data;

export { gradient, color };
