<template>
<div class="accounthead">
        <div class="container p-4">
            <div class="head-box">
                <div class="head-box-column-1">
                    <img src="img/logo/homepageicon.png" width="60px" height="60px">
                        </div>
                <div class="head-box-column-2">
                    <div class="information">
                    <p>{{ $store.getters.user.name }}</p>
                    <div class="row">
                      <div class="streak col-7"><h4>streak: {{ $store.getters.user.streaks }} days</h4></div>
<!--                      <div class="bonusxp col-5"><h4>+5% xp</h4></div>-->
                    </div>
<!--                    <button type="button" class="btn btn-outline-secondary">Edit profile</button>-->
                      <button type="button" class="btn btn-outline-secondary" @click="logout()">logout</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="account-view-options">
            <div class="row two-options">
                <div class="challenges-option col-6"><a href="./account">Challenges</a><hr :class="{scannedhr: true, active: activepage === 'challenges'}"></div>
                <div class="scanned-products-option col-6"><a href="./recently-scanned">Gescande Producten</a><hr :class="{scannedhr: true, active: activepage === 'scanned_products'}"></div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: "Account",
  props: {
    activepage: String
  },
  methods: {
    logout() {
      this.$store.commit('logout')
      this.$router.push('/')
    }
  }
}
</script>


<style>
.head-box {
  display: flex;
  margin-top: 20px;
}

.head-box-column-1 {
  flex: 1;
}

.head-box-column-2 {
  flex: 3;
  margin: 0;
  margin-left: 20px;
}

.information p {
  font-size: 20px;
  font-weight: 500;
  margin: 0;
  margin-bottom: 5px;
}

.information h4 {
  font-size: 15px;
  font-weight: 200;
}

.bonusxp h4 {
  color: rgb(0, 212, 0);
}

.information button {
  margin-top: 10px;
    padding: 2px;
    padding-right: 30px;
    padding-left: 30px;
    color: black;
    border-radius: 8px;
    font-size: 15px;
}

.challenges-option a {
  color: black;
  text-decoration: none;
  font-size: 13px;
}

.challenges-option, .scanned-products-option {
    text-align: center;
    padding: 0;
}

.scannedhr.active {
  color: #d5e046;
  background-color: #d5e046;
  border-color: #d5e046;
  border-top: 2px solid #d5e046;
  opacity: 1;
}

.scannedhr {
    color: #ccc;
    background-color: #ccc;
    border-color: #ccc;
    border-top: 2px solid #ccc;
    opacity: 1;
}

.scanned-products-option a {
  color: black;
  text-decoration: none;
  font-size: 13px;
}

.two-options {
    width: 100%;
    margin: 0;
}
</style>
