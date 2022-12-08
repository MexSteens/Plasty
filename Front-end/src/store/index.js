import Vue from "vue";
import Vuex from "vuex";
import auth from "./auth";
import company from "./company.js";
import product from "./product.js";
// import complaint from "./complaint.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    company: {},
    product: {},
    // complaint: {},
    ...auth.state,
  },
  mutations: {
    ...company.mutations,
    ...product.mutations,
    // ...complaint.mutations
    ...auth.mutations,
  },
  actions: {
    ...company.actions,
    ...product.actions,
    // ...complaint.actions
    ...auth.actions,
  },
  modules: {},
  getters: {
    ...company.getters,
    ...product.getters,
    // ...complaint.getters
    ...auth.getters,
  }
});
