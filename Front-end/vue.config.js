const path = require("path");
const ServiceWorkerWebpackPlugin = require("serviceworker-webpack-plugin");

module.exports = {
  configureWebpack: {
    plugins: [
      new ServiceWorkerWebpackPlugin({
        entry: path.join(__dirname, "./src/service_worker.js")
      })
    ]
  },
  pwa: {
    manifestOptions: {
      name: "Plasty",
      short_name: "Plasty",
      start_url: "./",
      id: "./",
      display: "standalone",
      theme_color: "#d5e046",
      icons: [
        {
          src: "/img/logo/icon2x512.png",
          sizes: "512x512",
          type: "image/png"
        },
        {
          src: "/img/logo/icon2x192.png",
          sizes: "192x192",
          type: "image/png"
        },
        {
          src: "/img/logo/maskable_icon_x512.png",
          sizes: "512x512",
          type: "image/png",
          purpose: "maskable"
        },
        {
          src: "/img/logo/maskable_icon_x192.png",
          sizes: "192x192",
          type: "image/png",
          purpose: "maskable"
        }
      ],
    },
    iconPaths: {
    msTitleImage: "./img/icons/mstile-150x150.png"
    }
  }
};




// module.exports = {
//     pwa: {
//         name: "Plasty",
//         short_name: "Plasty",
//         start_url: "./",
//         id: "./",
//         display: "standalone",
//         theme_color: "#d5e046",
//         icons: [
//           {
//             src: "/img/logo/icon2x512.png",
//             sizes: "512x512",
//             type: "image/png"
//           },
//           {
//             src: "/img/logo/icon2x192.png",
//             sizes: "192x192",
//             type: "image/png"
//           },
//           {
//             src: "/img/logo/maskable_icon_x512.png",
//             sizes: "512x512",
//             type: "image/png",
//             purpose: "maskable"
//           },
//           {
//             src: "/img/logo/maskable_icon_x192.png",
//             sizes: "192x192",
//             type: "image/png",
//             purpose: "maskable"
//           }
//         ],
//         iconPaths: {
//         msTitleImage: "./img/icons/mstile-150x150.png"
//         },
//         workboxPluginMode: "InjectManifest",
//         workboxOptions: {
//         swSrc: "src/service_worker.js"
//       }
//     }
// };