<template>
  <button type="button" class="form-btn w-100" @click="$emit('click', value)">{{ value }}</button>
</template>

<script>
export default {
  name: "Button",
  props: ["value"],
};
</script>

<style scoped>
.form-btn {
  background: #d5e046;
  border: 1px solid #bbc441;
  border-radius: 10px;
  height: 60px;
  width: 100%;
  line-height: 45px;
  text-indent: 14px;
  letter-spacing: 10px;
  text-transform: uppercase;
  font-weight: bold;
  color: #fff;
}
</style>
