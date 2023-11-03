const slides = document.querySelectorAll(".slide");
let counter = 0;

slides.forEach((slide, index) => {
    slide.style.left = `${index * 100}%`;
});

const slideImage = () => {
    slides.forEach((slide) => {
        slide.style.transform = `translateX(-${counter * 100}%)`; // Fix the typo here and add the "-" sign
    });
};

const goNext = () => {
    counter++;
    if (counter >= slides.length) {
        counter = 0; // Reset the counter to the first slide if it exceeds the number of slides
    }
    slideImage();
};

const goPrev = () => {
    counter--;
    if (counter < 0) {
        counter = slides.length - 1; // Set the counter to the last slide if it goes below 0
    }
    slideImage();
};

// Add event listeners to your buttons
document.querySelector(".nav button:nth-child(1)").addEventListener("click", goNext);
document.querySelector(".nav button:nth-child(2)").addEventListener("click", goPrev);
