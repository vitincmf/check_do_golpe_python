const CACHE_NAME = "check-do-golpe-v2";

const urlsToCache = [
    "/",
    "/static/css/style.css",
    "/static/js/app.js",
    "/static/js/install.js",
    "/static/manifest.json"
];

self.addEventListener("install", event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => cache.addAll(urlsToCache))
    );
});

self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});
