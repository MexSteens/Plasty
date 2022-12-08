<template>
  <div class="login">
    <div class="container p-4">
      <div class="row justify-content-center d-flex mt-4">
        <div
          class="col-12 col-sm-12 col-md-8 col-lg-4"
          style="margin: 0 auto; display: block"
        >
          <div class="d-flex justify-content-center login-head mt-4">
            <a href="/home">
              <img
                src="/img/logo/logo.png"
                alt=""
                width="300"
                class="mt-4 mb-2"
              />
            </a>
          </div>
          <div class="text-center">
            <h4>Login</h4>
            <p>
              Login to your account here. If you don't have an account, please register by clicking <a class="link" href="./register">here</a>
            </p>

            <!-- STEPS -->
            <div class="all-steps" id="all-steps">
              <a href="/">
                <span class="step"></span>
              </a>
              <a href="/register">
                <span class="step"></span>
              </a>
              <a href="/login">
                <span class="step active"></span>
              </a>
            </div>
            <!-- END STEPS -->
          </div>
          <form>
            <FormGroup
              v-model="email"
              label="E-mailaddress"
              name="email"
              type="email"
              placeholder="your e-mailaddress"
            />
            <FormGroup
              v-model="password"
              label="Password"
              name="password"
              type="password"
              placeholder="your password"
            />
          </form>
          <Button value="Login" @click="login()" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import FormGroup from "@/components/Form/FormGroup.vue";
import Button from "@/components/Button/Button.vue";

export default {
  name: "Login",
  data () {
    return {
      email: '',
      password: ''
    }
  },
  components: {
    FormGroup,
    Button,
  },
  methods: {
    login() {
      this.$store.dispatch('login', {
        email: this.email,
        password: this.password
      }).then(() => {
        // Login successful
        this.$router.push('home');
      }).catch(error => {
        // Login failed
        // Do something with the error...
        console.error(error);
      });
    },
  },
};
</script>

<style>
.link {
  text-decoration: none;
  color: #d5e046;
}
</style>