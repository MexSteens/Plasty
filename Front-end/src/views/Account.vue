<template>
    <div class="account">
        <Accountcomponent activepage="challenges"/>
        <div class="container p-4">
            <div class="progressbar">
                <h1>Level {{ $store.getters.user.level }}</h1>
                <div class="row g-0">
                    <div class="container-progress-bar col-8">
                        <div class="progress-bar" id="progress-bar" :style="{width: ($store.getters.user.experience/10) + '%'}"></div>
                    </div>
                    <div class="progress-bar-total col-4">
                        <p>{{ $store.getters.user.experience }} / 1000xp</p>
                    </div>
                </div>
            </div>
            <hr>
            <div class="challenges">
                <div class="challenge" @click="hide1 = !hide1; hide2 = false; hide3 = false; hide()">
                    <div class="row">
                        <div class="picture col-3">
                           <img src="img/logo/icon2.png" class="imagee mx-auto d-block" width="60px" height="60px">
                        </div>
                        <div class="info col-6">
                            <h1>Get a streak</h1>
                            <p>1 / 6</p>
                            <p>get a 3 day streak</p>
                        </div>
                        <div class="xp col-3">
                            <p>+300xp</p>
                        </div>
                    </div>
                </div>
                <div class="card1" id="showOrHide1">
                    <div class="row g-0">
                        <div class="progressbarcol col-1">
                            <ul id="progressbar" class="text-center">
                                <li class="active step0"></li>
                                <li class="step0"></li>
                                <li class="step0"></li>
                                <li class="step0"></li>
                                <li class="step0"></li>
                            </ul>
                        </div>
                        <div class="minichallenges col-11">
                            <div class="row row-minichallenges g-0">
                                <div class="mini-info col-8">
                                    <p>get a 3 day streak</p>
                                </div>
                                <div class="mini-xp col-4">
                                    <p>+300xp</p>
                                </div>
                            </div>
                            <div class="row row-minichallenges g-0">
                                <div class="mini-info col-8">
                                    <p>get a 5 day streak</p>
                                </div>
                                <div class="mini-xp col-4">
                                    <p>+500xp</p>
                                </div>
                            </div>
                            <div class="row row-minichallenges g-0">
                                <div class="mini-info col-8">
                                    <p>get a 10 day streak</p>
                                </div>
                                <div class="mini-xp col-4">
                                    <p>+1000xp</p>
                                </div>
                            </div>
                            <div class="row row-minichallenges g-0">
                                <div class="mini-info col-8">
                                    <p>get a 20 day streak</p>
                                </div>
                                <div class="mini-xp col-4">
                                    <p>+2000xp</p>
                                </div>
                            </div>
                            <div class="row row-minichallenges g-0">
                                <div class="mini-info col-8">
                                    <p>get a 100 day streak</p>
                                </div>
                                <div class="mini-xp col-4">
                                    <p>+1000xp</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="challenge" @click="hide1 = false; hide2 = !hide2; hide3 = false; hide()">
                    <div class="row">
                        <div class="picture col-3">
                           <img src="img/logo/icon2.png" class="imagee mx-auto d-block" width="60px" height="60px">
                        </div>
                        <div class="info col-6">
                            <h1>Scan your products</h1>
                            <p>2 / 7</p>
                            <p>Scan 5 unique products</p>
                        </div>
                        <div class="xp col-3">
                            <p>+500xp</p>
                        </div>
                    </div>
                </div>
                <div class="card1" id="showOrHide2">
                    <div class="row g-0">
                        <div class="progressbarcol col-1">
                            <ul id="progressbar" class="text-center">
                                <li class="active step0"></li>
                                <li class="active step0"></li>
                                <li class="step0"></li>
                                <li class="step0"></li>
                                <li class="step0"></li>
                                <li class="step0"></li>
                                <li class="step0"></li>
                            </ul>
                        </div>
                        <div class="minichallenges col-11">
                            <div class="row row-minichallenges g-0">
                                <div class="mini-info col-8">
                                    <p>Scan your first product</p>
                                </div>
                                <div class="mini-xp col-4">
                                    <p>+100xp</p>
                                </div>
                            </div>
                            <div class="row row-minichallenges g-0">
                                <div class="mini-info col-8">
                                    <p>Scan 5 unique products</p>
                                </div>
                                <div class="mini-xp col-4">
                                    <p>+500xp</p>
                                </div>
                            </div>
                            <div class="row row-minichallenges g-0">
                                <div class="mini-info col-8">
                                    <p>Scan 10 unique products</p>
                                </div>
                                <div class="mini-xp col-4">
                                    <p>+1000xp</p>
                                </div>
                            </div>
                            <div class="row row-minichallenges g-0">
                                <div class="mini-info col-8">
                                    <p>Scan 20 unique products</p>
                                </div>
                                <div class="mini-xp col-4">
                                    <p>+2000xp</p>
                                </div>
                            </div>
                            <div class="row row-minichallenges g-0">
                                <div class="mini-info col-8">
                                    <p>Scan 50 unique products</p>
                                </div>
                                <div class="mini-xp col-4">
                                    <p>+5000xp</p>
                                </div>
                            </div>
                            <div class="row row-minichallenges g-0">
                                <div class="mini-info col-8">
                                    <p>Scan 100 unique products</p>
                                </div>
                                <div class="mini-xp col-4">
                                    <p>+10000xp</p>
                                </div>
                            </div>
                            <div class="row row-minichallenges g-0">
                                <div class="mini-info col-8">
                                    <p>Scan 1000 unique products</p>
                                </div>
                                <div class="mini-xp col-4">
                                    <p>+100000xp</p>
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
// @ is an alias to /src
import Footer from "../components/Layout/Footer";
import Accountcomponent from "../components/Account/Account.vue";

export default {
  name: "Account",
  components: {
    Footer,
    Accountcomponent
  },
  data: function () {
        return {
            width: this.$store.getters.user.experience,
            level: this.$store.getters.user.level,
            hide1: false,
            hide2: false,
            hide3: false
        }
    },
    methods: {
        move: function () {
            if (this.width < 1000) {
                this.width+=100
            }
            if (this.width == 1000) {
                this.level+= 1
                this.width = 0
            }
        },
        hide: function() {
            var x1 = document.getElementById("showOrHide1");
            var x2 = document.getElementById("showOrHide2");
            var x3 = document.getElementById("showOrHide3");
            var marginChallenge = document.getElementById("lastChallenge");
            if (this.hide1 == true) {
                x1.style.display = "block";
                x2.style.display = "none";
                x3.style.display = "none";
                marginChallenge.style.marginBottom = "60px"
            }
            if (this.hide2 == true) {
                x1.style.display = "none"
                x2.style.display = "block"
                x3.style.display = "none"
                marginChallenge.style.marginBottom = "60px"
            }
            else if (this.hide3 == true) {
                x1.style.display = "none"
                x2.style.display = "none"
                x3.style.display = "block"
                marginChallenge.style.marginBottom = "0px"
            }
        }
    }
};

</script>

<style>

.float-right {
  float: right
}

.float-left {
  float: left;
}

.progressbar h1 {
    font-size: 15px;
    font-weight: 600;
}

.container-progress-bar {
    height: 15px;
    background-color: #CCC;
    position: relative;
    border-radius: 8px;
    padding: 0;
}

.progress-bar {
    position: absolute;
    height: 100%;
    border-radius: 8px;
    background-color: #d5e046;
}

.progress-bar-total {
    padding: 0;
}

.progress-bar-total p {
    font-size: 10px;
    margin-left: 5px;
}

.challenge {
    background: #F5F5F5;
    border-radius: 15px;
    padding: 10px;
    margin-top: 20px;
}

.challenge p {
    font-size: 14px;
}

.imagee {
    border-radius: 15px;
    margin-top: 5px;
}

.info h1 {
    margin-top: 5px;
    font-size: 20px;
    margin-bottom: 0;
}

.info p {
    font-size: 13px;
    font-weight: 400;
    padding: 0;
    margin: 0;
}

.xp p {
    font-size: 13px;
    text-align: center;
    position: relative;
    top: 50%;
    -ms-transform: translateY(-50%);
    -webkit-transform: translateY(-50%);
    transform: translateY(-50%);
    color: rgb(0, 212, 0);
}

.card1 {
    /*margin-left: 60px;*/
    z-index: 0;
    border-right: 1px solid #F5F5F5;
    margin-bottom: 20px;
}

#showOrHide2 {
    display: none;
}

#showOrHide3 {
    display: none;
}

#lastChallenge {
    margin-bottom: 60px;
}

#progressbar {
    position: absolute;
    overflow: hidden;
    color: #d5e046;
    left: 4%;
    padding-bottom: 150px;
    margin-top: 20px;
}

#progressbar li {
    list-style-type: none;
    font-size: 8px;
    font-weight: 400;
    margin-bottom: 18px;
}

#progressbar .step0:before {
    content: "";
    color: #fff
}

#progressbar li:before {
    width: 30px;
    height: 30px;
    line-height: 30px;
    display: block;
    font-size: 20px;
    background: #fff;
    border: 2px solid #d5e046;
    border-radius: 50%;
    margin: auto
}

#progressbar li:after {
    content: '';
    width: 3px;
    height: 36px;
    background: #BDBDBD;
    position: absolute;
    left: 46px;
    top: 15px;
    z-index: -1
}

#progressbar li:last-child:after {
    top: 110px;
    height: 40px
}

#progressbar li:nth-child(3):after {
    top: 70px
}

#progressbar li:nth-child(2):after {
    top: 15px
}

#progressbar li:first-child:after {
    position: absolute;
    top: -81px
}

#progressbar li.active:after {
    background: #d5e046
}

#progressbar li.active:before {
    background: #d5e046;
    font-family: FontAwesome;
    content: "\f00c"
}

.row-minichallenges {
    background: #F5F5F5;
    border-radius: 8px;
    padding: 5px;
    margin-top: 20px;
}

.mini-info p {
    font-size: 12px;
    padding: 0;
    margin: 0;
}

.mini-xp p {
    font-size: 12px;
    padding: 0;
    margin: 0;
    color: rgb(0, 212, 0);
}
</style>