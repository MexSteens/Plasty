<template>
  <div class="begin">
    <div class="container p-4">
      <div class="installationpopup">
      </div>
      <div>
        <!-- Modal -->
        <div class="modal fade" ref="exampleModal" tabindex="-1" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Install the Plasty app</h5>
                <button type="button" class="btn-close" @click="modal.hide()" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <p>With this app you can help our planet by scanning products with excess plastic</p>
                <p>If you are not on IOS, just press the install button to download our app &#128512;</p>
                <p>If you are using IOS, tap<a title="Alexander Madyankin, Roman Shamin, MIT &lt;http://opensource.org/licenses/mit-license.php&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Ei-share-apple.svg"><img width="30" alt="Ei-share-apple" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Ei-share-apple.svg/512px-Ei-share-apple.svg.png"></a>then <b>add to home screen</b></p>
                <div class="col-12 text-center"><button type="button" class="btn btn-primary" @click="installer()">Install</button></div>
              </div>
            </div>
          </div>
        </div>
      </div>
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
            <h4>Login or register</h4>
            <p>
              Welcome to Plasty! To continue on your journey, please login or register.
            </p>

            <!-- STEPS -->
            <div class="all-steps" id="all-steps">
              <a href="/">
                <span class="step active"></span>
              </a>
              <a href="/register">
                <span class="step"></span>
              </a>
              <a href="/login">
                <span class="step"></span>
              </a>
            </div>
            <!-- END STEPS -->
          </div>
          <a href="/login" class="text-decoration">
            <div class="card begin-card">
              <div class="container">
                <div class="row" style="">
                  <div class="col-lg-4 col-4">
                    <i class="fas fa-check-circle fa-3x plasty-green"></i>
                  </div>
                  <div class="col-lg-6 col-8">
                    <h5>I already have an account</h5>
                  </div>
                </div>
              </div>
            </div>
          </a>

          <a href="/register" class="text-decoration">
            <div class="card begin-card">
              <div class="container">
                <div class="row" style="">
                  <div class="col-lg-4 col-4">
                    <i class="fas fa-times-circle fa-3x plasty-red"></i>
                  </div>
                  <div class="col-sm-6 col-md-8 col-lg-8 col-8">
                    <h5>I don't have an account</h5>
                  </div>
                </div>
              </div>
            </div>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Modal } from 'bootstrap'

export default {
  name: "begin",
  data: () => ({
    modal: null,
    installer: undefined
  }),
  created() {
    let installPrompt;

    window.addEventListener("beforeinstallprompt", e => {
      e.preventDefault();
      // Stash the event so it can be triggered later.
      installPrompt = e;
    });
    
    this.installer = () => {
      installPrompt.prompt();
      installPrompt.userChoice.then(result => {
        if (result.outcome === "accepted") {
          console.log("User accepted");
        } else {
          console.log("Used denied");
        }
        installPrompt = null;
      });
    };
  },
  mounted() {
    this.modal = new Modal(this.$refs.exampleModal)
    this.modal.show()
  },
};
</script>

<style scoped>
.begin-card {
  background: #fcfcfc;
  border: 1px solid #ebebeb;
  border-radius: 10px;
  padding: 40px;
  text-align: left;
  margin-top: 20px;
}

.installerbutton, .installerbutton:active, .installerbutton:visited {
  background-color: #d5e046!important;
  border-color: #d5e046!important;
}

</style>
