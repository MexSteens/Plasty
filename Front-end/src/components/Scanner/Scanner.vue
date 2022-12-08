<template>
  <div class="scanner">
    <StreamBarcodeReader
        @decode="(a, b, c) => onDecode(a, b, c)"
    ></StreamBarcodeReader>
    {{ text || "Nothing" }}
  </div>
</template>

<script>
import { StreamBarcodeReader } from "vue-barcode-reader";
// import FormGroup from "../Form/FormGroup";
import axios from 'axios';
import router from "../../router";

export default {
  name: "Scanner",
  components: {
    StreamBarcodeReader,
    // FormGroup
  },
  data() {
    return {
      text: "",
      id: null
    };
  },
  props: {
    msg: String,
  },
  methods: {
    onDecode(a, b, c) {
      console.log(a, b, c);
      this.text = a;
      axios.post('https://api.plasty.nl/api/scan/' + a)
      .then((res) => {
        router.push({
          name: "Success",
          params: {
            res: res
          }
        });
      })
      .catch(() => {
        router.push({
          name: "Error",
          params: {
            error: a
          }
        });
      });
      // if (this.id) clearTimeout(this.id);
      // this.id = setTimeout(() => {
      //   if (this.text === a) {
      //     this.text = "";
      //   }
      // }, 5000);
    },
  },
};
</script>

<style scoped>
  .show {
    display: block;
  }

  .model-height {
    min-height: 80vh;
  }

  .mb-8 {
    margin-bottom: 3rem!important;
  }
  .hidden {
    display: block;
  }
</style>