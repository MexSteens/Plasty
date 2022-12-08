<template>
  <div class="row">
    <div class="form-group col-lg-12 mb-3">
      <label :for="name" class="form-label ">{{ label }}</label>
      <input
        :type="type"
        :name="name"
        class="form-control"
        id="exampleFormControlInput1"
        :placeholder="placeholder"
        :value="value"
        :disabled="disabled"
        @input="inputEvent"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "FormGroup",
  props: ["label", "name", "type", "placeholder", "value", "disabled"],
  methods: {
    inputEvent(e) {
      this.$emit("input", e.target.value);
    }
  }
};
</script>

<style scoped>
input {
  background: #fcfcfc;
  border: 1px solid #ebebeb;
  border-radius: 10px;
  height: 60px;
  width: 100%;
  line-height: 60px;
  text-indent: 14px;
}

label {
  color: #000;
  float: left;
}
</style>
