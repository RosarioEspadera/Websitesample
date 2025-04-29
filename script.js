// Greet visitors based on the current time
document.addEventListener("DOMContentLoaded", () => {
    const hours = new Date().getHours();
    const greeting = hours < 12 ? "Good morning!" : hours < 18 ? "Good afternoon!" : "Good evening!";
    alert(`Welcome to Crypto Insights! ${greeting}`);
});