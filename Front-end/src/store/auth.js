import Vue from "vue";
import axios from "axios";

//const resourceURL = "auth";

const state = {
  auth: {
    user: null,
    access_token: localStorage.getItem('access_token'),
    refresh_token: localStorage.getItem('refresh_token'),
  },
};

const getters = {
  loggedIn: (state) => {
    return !!state.auth.access_token;
  },
  user: (state) => {
    return state.auth.user;
  },
  access_token: (state) => {
    return state.auth.access_token;
  },
  refresh_token: (state) => {
    return state.auth.refresh_token;
  },
};

const mutations = {
  login(state, data) {
    state.auth.loggedIn = true;
    Vue.set(state.auth, "user", data);
  },
  setAccessToken(state, token) {
    axios.defaults.headers.common["Authorization"] = "Bearer " + token;
    state.auth.access_token = token;
    localStorage.setItem('access_token', token);
  },
  setRefreshToken(state, token) {
    state.auth.refresh_token = token;
    localStorage.setItem('refresh_token', token);
  },
  logout(state) {
    state.auth.loggedIn = false;
    Vue.set(state.auth, "user", null);
    state.auth.access_token = null;
    localStorage.clear('access_token');
    state.auth.refresh_token = null;
    localStorage.clear('refresh_token');
  },
};

const actions = {
  checkLogin({ commit, state }) {
    if (state.auth.access_token) {
      commit("setAccessToken", state.auth.access_token);

      axios.get("auth").then((responseInfo) => {
          commit("login", responseInfo.data);
        }).catch(error => {
          console.error(error);
          commit("logout");
        });
    }
  },
  async login({ commit }, { email, password }) {
    return new Promise((resolve, reject) => {
      axios
        .post("auth", {
          email: email,
          password: password,
        })
        .then((response) => {
          console.log(response);
          commit("setAccessToken", response.data.access_token);
          commit("setRefreshToken", response.data.refresh_token);

          axios.get("auth").then((responseInfo) => {
              commit("login", responseInfo.data);
              resolve(responseInfo.data);
            }).catch(error => {
              console.error(error);
              commit("logout");
              reject(error);
            });
        })
        .catch((error) => {
          console.error(error);
          reject(error);
        });
    });
  },
};

export default {
  state,
  actions,
  mutations,
  getters,
};
