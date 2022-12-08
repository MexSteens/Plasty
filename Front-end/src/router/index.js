import Vue from "vue";
import VueRouter from "vue-router";

// AUTH
import Login from "../views/Auth/Login.vue";
import Register from "../views/Auth/Register.vue";
import Begin from "../views/Auth/Home.vue";

// USER
import Home from "../views/Home";
import Scan from "../views/Scan";
import Account from "../views/Account"
import RecentlyScanned from "../views/Recently-scanned-account"
import Success from "../views/Scan/Success";
import Error from "../views/Scan/Error";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "begin",
    component: Begin,
    meta: {
      isAuthenticated: true
    }
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    meta: {
      isAuthenticated: true
    }
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
    meta: {
      isAuthenticated: true
    }
  },
  {
    path: "/home",
    name: "Home",
    component: Home,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/scan",
    name: "Scan",
    component: Scan,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/scan/succes",
    name: "Success",
    component: Success,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/scan/error",
    name: "Error",
    component: Error,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/account",
    name: "Account",
    component: Account,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/recently-scanned",
    name: "Recently-scanned",
    component: RecentlyScanned,
    meta: {
      requiresAuth: true
    }
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
