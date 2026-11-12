document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".commentBtn").forEach((Btn) => {
            Btn.addEventListener("click", () => {
                Btn.nextElementSibling.classList.toggle("open");
        });
    });
});