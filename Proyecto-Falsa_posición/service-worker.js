const CACHE_NAME = 'falsaposition-v2';
const urlsToCache = [
  'index.html',
  'juego.html',
  'manifest.json'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondInWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});