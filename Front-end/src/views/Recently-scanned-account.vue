<template>
    <div class="Recently-scanned-account">
        <Accountcomponent activepage="scanned_products"/>
        <div class="container p-4">
            <div v-for="user in $store.getters.user.scanned_products" :key="user">
                <div class="row product">
                    <div class="rounded-picture col-4">
                        <img src="../../public/img/logo/icon2.png" class="round">
                    </div>
                    <div class="info col-8">
                        <div class="row">
                            <div class="top-info">
                                <h1>{{ user.name }}</h1>
                                <p>Dit product is {8} keer eerder gescand</p>
                            </div>
                            <div class="row bottom">
                                <div class="bottom-info-left col-6">
                                    <p>Barcode:</p>
                                    <p>Gescand op:</p>
                                </div>
                                <div class="bottom-info-right col-6">
                                    <p>{{ user.barcode }}}</p>
                                    <p>{{ user.created_at }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <Footer activepage="account"/>
    </div>
</template>

<script>
import Footer from "../components/Layout/Footer";
import Accountcomponent from "../components/Account/Account.vue";

export default {
  name: "Recently-scanned-account",
  components: {
    Footer,
    Accountcomponent
  },
};
</script>

<style>

.product {
    background: #F5F5F5;
    border-radius: 15px;
    padding: 10px;
    margin-bottom: 15px;
}

.round {
    border-radius: 50%;
    width: 80px;
    height: 80px;
}

.top-info h1 {
    font-size: 10px;
}

.top-info p {
    font-size: 8px;
}

.bottom-info-left p {
    font-size: 8px;
    font-weight: 600;
    margin: 0;
}

.bottom-info-right p {
    font-size: 8px;
}

.bottom {
    margin-top: 20px;
}

.p-4 {
    padding-top: 0!important;
}
</style>