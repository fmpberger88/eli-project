document.addEventListener("DOMContentLoaded", function () {
    const cookieBanner = document.getElementById("cookie-banner");
    const cookieAcceptButton = document.getElementById("cookie-accept");

    // Überprüfe, ob der User das Banner bereits geschlossen hat
    if(!localStorage.getItem("cookeAccepted")) {
        cookieBanner.style.display = "block";
    }

    // Wenn der User auf "Cookie akzeptieren" klickt
    cookieAcceptButton.addEventListener('click', function () {
        localStorage.setItem("cookieAccepted", "true");
        cookieBanner.style.display = "none";
    })
});