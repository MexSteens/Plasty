<template>
  <div class="scan">
    <div class="container p-4">
      <div class="row justify-content-center d-flex mt-4">
        <div
          class="col-12 col-sm-12 col-md-8 col-lg-4"
          style="margin: 0 auto; display: block"
        >
          <div class="d-flex justify-content-center login-head mt-4">
            <img
              src="/img/logo/logo.png"
              alt=""
              width="300"
              class="mt-4 mb-2"
            />
          </div>
        </div>
      </div>
      <div class="text-center">
        <h4>Scan uw product</h4>
        <p>Zorg ervoor dat de barcode zichtbaar is voor de scanner</p>

        <Scanner />
        <Footer />
      </div>
    </div>
    <Footer activepage="scanner"/>
  </div>
</template>

<script>
import Scanner from "../components/Scanner/Scanner";
import Footer from "../components/Layout/Footer";

export default {
  name: "Scan",
  components: {
    Scanner,
    Footer
  }
};
</script>

<style scoped></style>
