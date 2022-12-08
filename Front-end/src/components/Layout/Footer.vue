<template>
  <div class="footer">
    <div class="container">
      <div class="row">
        <div class="col-4">
          <div class="centered">
            <a href="./home" class="link-text">
              <i class="fas fa-home fa-sm" :class="{coloricon: true, active: activepage === 'home'}"></i>
            </a>
          </div>
        </div>

        <div class="col-4">
          <div class="centered">
            <a href="./scan" class="link-text">
              <i class="fas fa-plus-circle" :class="{coloricon: true, active: activepage === 'scanner'}"></i>
            </a>
          </div>
        </div>

        <div class="col-4">
          <div class="centered">
            <a href="./account" class="link-text">
              <i class="fas fa-user-circle coloricon" :class="{coloricon: true, active: activepage === 'account'}"></i>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer",
  props: {
    activepage: String
  }
}
</script>

<style scoped>
.footer {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: #ffffff;
  border-top: 1px solid #F3F3F3;
  color: #000;
  padding: 8px 0;
  font-size: 2em;
}

.coloricon {
  color: #CCCCCC !important;
}

.coloricon.active {
  color: #d5e046 !important;
}

.centered {
  align-items: center;
  display: block;
  text-align: center;
  width: 100%;
}

.link-text {
  text-decoration: none;
  color: inherit;
}

</style>