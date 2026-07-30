"use strict";
let a = 10;
let b = 20;
let button = document.querySelector("#count");
increase();
if (button) {
    button.addEventListener("click", increase);
}
function increase() {
    a += 1;
    const title = document.querySelector("#title");
    if (title) {
        title.innerHTML = `${a + b}`;
    }
}
