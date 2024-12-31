const slider = document.getElementById("text_slider");
const textContainer = document.getElementById("text_container");

const texts = textContainer.children;

slider.addEventListener("input", (event)=>{
    Array.from(texts).map((text)=>{
        text.style.fontWeight = event.target.value * 10;
    });
})