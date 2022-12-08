<template>
  <div class="register">
    <div class="container p-4" style="margin-bottom: 100px">
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
            <h4>Register</h4>
            <p>
              Register your account here. If you already have an account, please login by clicking <a class="link" href="./login">here</a>
            </p>

            <!-- STEPS -->
            <div class="all-steps" id="all-steps">
              <a href="/">
                <span class="step"></span>
              </a>
              <a href="/register">
                <span class="step active"></span>
              </a>
              <a href="/login">
                <span class="step"></span>
              </a>
            </div>
            <!-- END STEPS -->
          </div>
          <form action="/home" method="POST">
            <FormGroup
              label="Name"
              name="name"
              type="text"
              placeholder="your full name"
              v-model="name"
            />
            <FormGroup
              label="E-mailaddress"
              name="email"
              type="email"
              placeholder="your e-mailaddress"
              v-model="email"
            />
            <FormGroup
              label="Password"
              name="password"
              type="password"
              placeholder="your password"
              v-model="password"
            />
            <FormGroup
              label="Repeat password"
              name="confirm-password"
              type="password"
              placeholder="repeat your password"
              v-model="passwordConfirm"
            />
          </form>
          <Button value="Register" type="submit" @click="register()"></Button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import FormGroup from "@/components/Form/FormGroup.vue";
import Button from "@/components/Button/Button.vue";
import axios from "axios";

export default {
  name: "Register",
  components: {
    FormGroup,
    Button,
  },
  data() {
    return {
      name: '',
      email: '',
      password: '',
      passwordConfirm: ''
    };
  },
  methods: {
    register() {
      if (this.password !== this.passwordConfirm) {
        console.log("Password does not match!");
        // Hier nog een pop melding ofzo
        return;
      }

      console.log('test');

      axios.post("user", {
        name: this.name,
        email: this.email,
        password: this.password,
      }).then(() => {
        this.$store.dispatch('login', {
          email: this.email,
          password: this.password
        }).then(() => {
          // Login successful
          this.$router.push('/home');
        }).catch(error => {
          // Login failed
          // Do something with the error...
          console.error(error);
        });
      }).catch(error => {
        console.error(error)
        // Error popup
      })
    },
  },
};
</script>

<style ></style>
