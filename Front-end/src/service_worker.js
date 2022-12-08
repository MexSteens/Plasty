// import { registerRoute } from 'workbox-routing';
// import { StaleWhileRevalidate } from 'workbox-strategies';
// import { Plugin } from 'workbox-expiration';
// import { precacheAndRoute } from 'workbox-precaching';

console.log("hello world from the SW!");

// precacheAndRoute(self.serviceWorkerOption.assets);

// registerRoute(
//     /\.(?:png|gif|jpg|jpeg|svg)$/,
//     new StaleWhileRevalidate({
//         cacheName: 'images',
//         plugins: [
//             new Plugin({
//                 maxEntries: 60,
//                 maxAgeSeconds: 30 * 24 * 60 * 60, // 30 Days
//             }),
//         ],
//     })
// );

// self.addEventListener("fetch", function (event) {


//     event.respondWith(
//       caches.open("dynamiccache").then(function (cache) {
//         return fetch(event.request).then(function (res) {
//           cache.put(event.request, res.clone());
//           return res;
//         })
//       })
//     )
// });

