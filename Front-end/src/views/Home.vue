<template>
  <div class="home">
    <div class="container p-4">
      <div class="head-box">
        <div class="head-box-1">
          <div class="information">
            <p>Hi {{ $store.getters.user.name }} &#128075;</p>
            <h4>Welcome to Plasty</h4>
          </div>
        </div>
        <div class="head-box-2">
          <img src="img/logo/homepageicon.png" width="84px" height="84px">
        </div>
      </div>
      <div class="recently-scanned">
        <div class="text-center">
          <h5>Recently scanned products</h5>
        </div>
        <div class="row justify-content-between">
          <div class="col-6" v-for="user in SlicedScannedProducts" :key="user">
            <div class="row g-0">
              <div class="scanned-product-col col-11">
                <img src="img/logo/icon2.png" width="60px" height="60px">
                <h1>{{ user.name }}</h1>
                <h1>+ 250xp</h1>
              </div>
            </div>
            <div class="col-1"></div>
          </div>
          <div class="container">
            <div class="row" v-for="scan in SlicedScannedProducts" :key="scan">

              <div class="col-6">
                <div class="scanned-product-col py-3">
                  <img src="img/logo/icon2.png" width="60" height="60" alt="">
                  <h1>{{ scan.name }}</h1>
                  <h1>{{ scan.barcode }}}</h1>
                </div>
              </div>

            </div>
          </div>
        </div>
        <div class="row justify-content-center">
          <div class="d-grid gap-2 col-6 mx-auto">
            <form action="./recently-scanned" class="mx-auto">
            <button type="submit" class="btn btn-default btn-block text-nowrap view-all">View all</button>
            </form>
          </div>
        </div>
        <hr class="separation-line">
        <div class="text text-center" id="section1">
          <h5>Top 5 worst companies</h5>
          <p class="subtitle mono">which use the most excess<br>packaging plastic</p>
        </div>
        <table class="rank-list select" v-for="(company, index) in TopCompanies" :key="index">
          <tbody>
          <tr>
            <th>{{ index + 1}}</th>
            <td colspan="2">{{ company.name }}</td>
          </tr>
          <tr v-for="(product, index) in company.products" :key="index">
            <td class="empty"></td>
            <th>{{ index + 1 }}</th>
            <td>{{ product.name }} - {{ product.total_complaints }}</td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
    <Footer activepage="home"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Footer from "../components/Layout/Footer";
import { mapActions } from 'vuex';

export default {
  data () {
        return {
            company: this.$store.getters.companyRead,
            product: this.$store.getters.productRead,
            // complaint: this.$store.getters.complaintRead
        }
    },
    methods: {
      ...mapActions(['companyRead']),
      ...mapActions(['productRead']),
      // ...mapActions(['complaintRead'])
    },
    created () {
        // this.$store.dispatch('company/get', { id: 1 })
        // this.$store.dispatch('company/get', { id: 2 })

        // this.$store.state.company = await fetch(
        //     'http://127.0.0.1:5000/api/company'
        // ).then(res => res.json())

        this.$store.dispatch('companyRead')
        this.$store.dispatch('productRead')
        // this.$store.dispatch('complaintRead')
    },
    computed: {
      SlicedScannedProducts: function () {
        const user = this.$store.getters.user
        const output= []
        console.log(output)
        if (!user?.scanned_products) {
          user.scanned_products = []
        }
        Object.values(user.scanned_products).forEach(scanned_products => {
          output.push(scanned_products)
        });
        return output.slice(0, 4);
      },
      TopCompanies () {
        const companies = this.$store.getters.companyRead
        const products = this.$store.getters.productRead
        const output = []
        console.log(output)
        Object.values(companies).forEach(company => {
            
            if (!company?.products) {
                company.products = []
            }
            Object.values(products).forEach(product => {
                if (product.company_id === company.id) {
                    company.products.push(product)
                }
            })
            // company.products.orderBy(products, 'total_complaints', 'desc')
            output.push(company)
        });
        // for (var i = 0; i < output.length; i++) {
        //   ouput.i.products.orderBy(products, 'total_complaints')
        // }
        // output.orderBy(products, 'total_complaints')
        return output.slice(0, 5);
      }
    },
  name: "Home",
  components: {
    Footer,
  },
};
</script>

<style>
.subtitle {
  font-size: 0.8em;
}

.rank-list .empty {
  border: none;
}

.rank-list {
  border-collapse: separate;
  border-spacing: 8px;
  width: 100%;
}

.rank-list th {
  background-color: #d5e046;
  border-radius: 8px;
  margin: 0 8px;
  padding: 4px 20px;
  font-size: 0.9em;
  width: 32px;
  border: none;
  color: #fff;
}

.rank-list td {
  border-radius: 8px;
  border: 1px solid #707070;
  padding: 8px 12px;
  text-align: left;
  font-size: 0.9em;
}

.button-size {
  width: 50px;
  height: 50px;
  border-radius: 8px;
  line-height: 40px;
  margin-right: 20px;
  margin-bottom: 20px;
}

.btn-green {
  background: #d5e046;
  border: 1px solid #bbc441;
  color: #ffffff;
}

.head-box {
  display: flex;
}

.head-box-1 {
  flex: 5;
}

.head-box-2 {
  flex: 1;
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

.recently-scanned {
  font-size: 17px;
  font-weight: 400;
  margin-top: 20px;
  margin-bottom: 55px;
}

.recently-scanned h1 { 
  font-size: 17px;
  font-weight: 400;
}

.scanned-product-col {
  background: #F5F5F5;
  border-radius: 15px;
  padding: 7px;
  text-align: center;
  margin-top: 10px;
}

.scanned-product-col h1{
  font-size: 13px;
  margin-bottom: 4px;
}

.scanned-product-col img {
  border-radius: 50%;
  margin-bottom: 5px;
  border: 1px solid rgb(160, 160, 160);
}

.view-all {
  background: #d5e046;
  margin-top: 10px;
  color: #ffffff;
  font-weight: 600;
  border-radius: 8px;
}

.text h1 {
  font-size: 18px;
  text-align: center;
  margin-bottom: 5px;
  font-weight: 600;
}

/* .list {
} */

.list-number {
  background: #d5e046;
  text-align: center;
  border-radius: 10px;
  padding-top: 2px;
  margin-bottom: 5px;
  margin-top: 15px;
}

.list-number h1 {
  font-size: 15px;
  font-weight: 600;
  color: #ffffff;
  padding-top: 5px;
}

.list-company {
  text-align: left;
  border: 1px solid #707070;
  border-radius: 10px;
  margin-bottom: 5px;
  margin-top: 15px;
}

.list-company h1 {
  font-size: 15px;
  font-weight: 600;
  padding-top: 5px;
}

.list-number-item {
  background: #d5e046;
  text-align: center;
  border-radius: 10px;
  padding-top: 2px;
  padding-left: 10px;
  margin-bottom: 5px;
}

.list-number-item h1 {
  font-size: 10px;
  font-weight: 600;
  color: #ffffff;
  padding-top: 5px;
}

.list-company-item {
  text-align: left;
  border: 1px solid #707070;
  border-radius: 10px;
  margin-bottom: 5px;
}

.list-company-item h1 {
  font-size: 10px;
  font-weight: 600;
  padding-top: 5px;
}


</style>
