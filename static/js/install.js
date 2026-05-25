let deferredPrompt;

window.addEventListener("beforeinstallprompt", (e) => {
    e.preventDefault();
    deferredPrompt = e;

    const installButton = document.getElementById("installBtn");

    if (installButton) {
        installButton.style.display = "flex";

        installButton.addEventListener("click", async () => {
            deferredPrompt.prompt();
            await deferredPrompt.userChoice;
            deferredPrompt = null;
            installButton.style.display = "none";
        });
    }
});
