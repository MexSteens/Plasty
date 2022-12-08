import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import runtime from "serviceworker-webpack-plugin/lib/runtime";
import orderBy from 'lodash';


if ("serviceWorker" in navigator) {
  runtime.register();
}

Vue.use(orderBy)

Vue.config.productionTip = false;

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.loggedIn) {
      next({
        name: 'begin',
        params: {
          next: from.path
        }
      })
    } else {
      next()
    }
  } else {
    next()
  }

  if(to.matched.some(record => record.meta.isAuthenticated)) {
    if(store.getters.loggedIn) {
      next({
        name: 'Home',
        params: {
          next: from.path
        }
      })
    } else {
      next()
    }
  }
})

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
