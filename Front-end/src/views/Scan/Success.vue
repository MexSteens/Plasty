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
        <div class="row">
          <i class="fas fa-check-circle fa-4x plasty-green my-4"></i>
        </div>
        <h4>Product gescand</h4>
        <p>Uw product is succesvol gescand, hieronder ziet u informatie over het product.</p>
        <div class="row">
          <p>
            <b>Barcode:</b> <br>
            {{ product.data.barcode }}
          </p>
          <p>
            <b>Product:</b> <br>
            {{ product.data.name }}
          </p>
          <p>
            <b>Totaal aantal klachten</b> <br>
            {{ product.data.total_complaints }}
          </p>
          <hr>
        </div>
        <Footer />
      </div>
    </div>
    <Footer activepage="scanner"/>
  </div>
</template>


<script>
import axios from "axios";
import router from "../../router";

export default {
  name: "Success",
  data() {
    return {
      res: [],
      product: []
    };
  },
  // props: ['res'],
  created() {
    this.res = this.$route.params.res;

    axios.get('https://api.plasty.nl/api/product/' + this.res.data.product_id)
    .then((product) => {
      this.product = product;
    })
    .catch(() => {
      router.push({
        name: "Error",
        params: {
          barcode: this.res.data.barcode
        }
      });
    });
  },
}
</script>

<style scoped>

</style>