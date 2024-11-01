var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/',
    '/offline/',
    '/static/css/style.css',
    '/static/js/script.js',
    '/static/images/Hopelismlogo48.png',
    '/static/images/Hopelismlogo60.png',
    '/static/images/Hopelismlogo72.png',
    '/static/images/Hopelismlogo76.png',
    '/static/images/Hopelismlogo96.png',
    '/static/images/Hopelismlogo120.png',
    '/static/images/Hopelismlogo144.png',
    '/static/images/Hopelismlogo152.png',
    '/static/images/Hopelismlogo167.png',
    '/static/images/Hopelismlogo180.png',
    '/static/images/Hopelismlogo192.png',
    '/static/images/Hopelismlogo512.png',
    '/static/images/splash-200x320.png',
    '/static/images/splash-320x480.png',
    '/static/images/splash-480x800.png',
    '/static/images/splash-720x1280.png',
    '/static/images/splash-960x1600.png',
    '/static/images/splash-1280x1920.png',
    '/static/images/splash-1440x2560.png',
    '/static/images/splash-644x1136.png',
    '/static/images/splash-750x1334.png',
    '/static/images/splash-828x1792.png',
    '/static/images/splash-1125x2436.png',
    '/static/images/splash-1242x2688.png',
    '/static/images/splash-1536x2047.png',
    '/static/images/splash-1668x2388.png',
    '/static/images/Hopsstarcampus96x96.png',
    '/static/images/Hopsstarnotes96x96.png',
    '/static/images/Hopsstarcheatsheet96x96.png',
    '/static/images/Hopsstarreasearch96x96.png',
    '/static/images/Hopsstarcareers96x96.png',
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('offline');
            })
    )
});