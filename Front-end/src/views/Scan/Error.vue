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
          <i class="fas fa-times-circle fa-4x plasty-red my-4"></i>
        </div>
        <h4>Product niet gevonden</h4>
        <p>Uw product is niet gevonden, hieronder kunt u de productnaam invoeren.</p>
        <div class="row">
          <p>{{ error }}</p>
        </div>
        <div class="row">
          <form>
            <FormGroup
                label="Barcode"
                name="barcode"
                type="text"
                placeholder="Barcode"
                disabled="true"
                :value="barcode"
            />

            <FormGroup
                label="Product naam"
                name="productname"
                type="text"
                placeholder="Product naam"
            />
            <Button value="Product invoeren" />
          </form>
        </div>
        <Footer />
      </div>
    </div>
    <Footer activepage="scanner"/>
  </div>
</template>


<script>
import FormGroup from "../../components/Form/FormGroup";
import Button from "../../components/Button/Button";
import axios from "axios";
import router from "../../router";

export default {
  name: "Error",
  components: {
    FormGroup,
    Button
  },
  data() {
    return {
      barcode: "",
      productname: ""
    };
  },
  created() {
    this.barcode = this.$route.params.error;
  },
  methods: {
    onSubmit() {
      axios.post("http://localhost:5000/api/product", {
        'barcode': this.barcode,
        'name': this.productname
      })
      .then((res) => {
        router.push({
          name: "Success",
          params: {
            res: res
          }
        });
      })
      .catch((error) => {
        router.push({
          name: "Error",
          params: {
            res: error
          }
        });
      });
    }
  }
}
</script>

<style scoped>

</style>