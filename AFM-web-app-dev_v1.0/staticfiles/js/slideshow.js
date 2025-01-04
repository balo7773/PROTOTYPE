document.addEventListener('DOMContentLoaded', function() {
    let slideIndex = 0;
    let timeoutHandle;
    const slides = document.querySelectorAll(".slide");
    
    showSlides();
    
    function showSlides() {
        if (timeoutHandle) clearTimeout(timeoutHandle);
        slides.forEach(slide => slide.style.display = "none");
        slideIndex++;
        if (slideIndex > slides.length) slideIndex = 1;
        slides[slideIndex - 1].style.display = "block";
        timeoutHandle = setTimeout(showSlides, 3000);
    }
    
    window.changeSlide = function(n) {
        if (timeoutHandle) clearTimeout(timeoutHandle);
        slideIndex += n;
        if (slideIndex > slides.length) slideIndex = 1;
        if (slideIndex < 1) slideIndex = slides.length;
        slides.forEach(slide => slide.style.display = "none");
        slides[slideIndex - 1].style.display = "block";
        timeoutHandle = setTimeout(showSlides, 3000);
    };
});