let a:number = 10;
let b:number = 20;

let button = document.querySelector("#count") as HTMLButtonElement | null

increase()

if(button) {
    button.addEventListener("click", increase);
}

function increase() {
    a += 1;
    const title = document.querySelector("#title")
    if(title) {
        title.innerHTML = `${a + b}`;
    }
}