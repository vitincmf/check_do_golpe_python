
const CACHE_NAME = "check-do-golpe-v1";
const URLS = ["/", "/static/style.css", "/static/app.js", "/static/manifest.json"];

self.addEventListener("install", event => {
    event.waitUntil(caches.open(CACHE_NAME).then(cache => cache.addAll(URLS)));
});

self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request).then(response => response || fetch(event.request))
    );
});
