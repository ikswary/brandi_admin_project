<template>
  <div class="signUpBox">
    <p>셀러회원 가입</p>
    <hr />
    <img class="signUpBanner" src="http://sadmin.brandi.co.kr/include/img/seller_join_top_2.png" />
    <p>가입 정보</p>

    <!-- account check input -->
    <input
      v-model="account.value"
      v-bind:class="{ defaultInput: account.state, warningInput: !account.state }"
      placeholder="아이디"
      @keyup="() => regCheck(regs.idReg,this.account)"
    />
    <div
      v-bind:class="{ defaultText: account.state || account.value.length > 0, warningText: account.state || account.value.length == 0}"
    >필수 입력 항목입니다.</div>
    <div
      v-bind:class="{ defaultText: account.state || account.value.length == 0, warningText: !account.state && account.value.length >= 1}"
    >아이디는 5~20글자의 영문, 숫자, 언더바, 하이픈만 사용 가능하며 시작 문자는 영문 또는 숫자입니다.</div>

    <!-- password check input -->
    <input
      type="password"
      v-model="password.value"
      v-bind:class="{ defaultInput: password.state, warningInput: !password.state }"
      placeholder="비밀번호"
      @change="() => regCheck(regs.pwReg,this.password)"
      class="defaultInput"
    />
    <div
      v-bind:class="{ defaultText: password.state || password.value.length > 0, warningText: password.state || password.value.length == 0}"
    >필수 입력 항목입니다.</div>
    <div
      v-bind:class="{ defaultText: password.state || password.value.length == 0, warningText: !password.state && password.value.length >= 1}"
    >비밀번호는 8~20글자의 영문대소문자, 숫자, 특수문자를 조합해야 합니다.</div>

    <!-- rePw recheck input -->
    <input
      type="password"
      v-model="rePw.value"
      v-bind:class="{ defaultInput: rePw.state, warningInput: !rePw.state }"
      placeholder="비밀번호 재입력"
    />
    <div
      v-bind:class="{ defaultText: rePw.value.length == 0 || password.value === rePw.value, warningText: password.value !== rePw.value}"
    >비밀번호가 일치하지 않습니다.</div>

    <!-- manager_phone check input -->
    <div class="signUpManager">
      <p>담당자 정보</p>
      <p>(*실제 샵을 운영하시는 분)</p>
    </div>
    <input
      v-model="manager_phone.value"
      v-bind:class="{ defaultInput: manager_phone.state, warningInput: !manager_phone.state }"
      placeholder="핸드폰번호"
      @keyup="() => regCheck(regs.phReg,this.manager_phone)"
    />
    <div
      v-bind:class="{ defaultText: manager_phone.state, warningText: !manager_phone.state}"
    >올바른 정보를 입력해주세요.</div>
    <i class="xi-info">입점 신청 후 브랜디 담당자가 연락을 드릴 수 있으니 정확한 정보를 기입해주세요.</i>

    <!-- info check input -->
    <div class="radioList">
      <p>셀러정보</p>
      <v-radio-group class="radioBox" v-model="seller_attribute_id.value" :mandatory="false">
        <v-radio label="쇼핑몰" value="1"></v-radio>
        <v-radio label="마켓" value="2"></v-radio>
        <v-radio label="로드샵" value="3"></v-radio>
        <v-radio label="디자이너 브랜드" value="4"></v-radio>
        <v-radio label="제너럴 브랜드" value="5"></v-radio>
        <v-radio label="네셔널 브랜드" value="6"></v-radio>
        <v-radio label="뷰티" value="7"></v-radio>
      </v-radio-group>
    </div>

    <!-- seller_name check input -->
    <input
      v-model="seller_name.value"
      v-bind:class="{ defaultInput: seller_name.state, warningInput: !seller_name.state }"
      placeholder="셀러명(상호)"
      @keyup="() => regCheck(regs.nameReg,this.seller_name)"
    />
    <div
      v-bind:class="{ defaultText: seller_name.state || seller_name.value.length > 0 , warningText: seller_name.value.length == 0 || !seller_name.state}"
    >필수 입력 항목입니다.</div>
    <div
      v-bind:class="{ defaultText: seller_name.state || seller_name.value.length == 0, warningText: !seller_name.state}"
    >한글,영문,숫자만 입력해주세요.</div>

    <!-- seller_name_eng check input -->
    <input
      v-model="seller_name_eng.value"
      v-bind:class="{ defaultInput: seller_name_eng.state, warningInput: !seller_name_eng.state }"
      placeholder="영문 셀러명 (영문상호)"
      @keyup="() => regCheck(regs.engNameReg,this.seller_name_eng)"
    />
    <div
      v-bind:class="{ defaultText: seller_name_eng.state || seller_name_eng.value.length > 0 , warningText: seller_name_eng.value.length == 0 || !seller_name_eng.state}"
    >필수 입력 항목입니다.</div>
    <div
      v-bind:class="{ defaultText: seller_name_eng.state || seller_name_eng.value.length == 0, warningText: !seller_name_eng.state}"
    >셀러 영문명은 소문자만 입력가능합니다.</div>

    <!-- tel check input -->
    <input
      v-model="cs_phone.value"
      v-bind:class="{ defaultInput: cs_phone.state, warningInput: !cs_phone.state }"
      placeholder="고객센터 전화번호"
      @keyup="() => regCheck(regs.telReg,this.cs_phone)"
      class="defaultInput"
    />
    <div
      v-bind:class="{ defaultText: cs_phone.state || cs_phone.value.length > 0 , warningText: cs_phone.value.length == 0 || !cs_phone.state}"
    >필수 입력 항목입니다.</div>
    <div
      v-bind:class="{ defaultText: cs_phone.value >= 0 || cs_phone.state, warningText: !cs_phone.state}"
    >고객센터 전화번호는 숫자와 하이픈만 입력가능합니다.</div>

    <!-- url check input -->
    <input
      v-model="site_url.value"
      v-bind:class="{ defaultInput: site_url.state, warningInput: !site_url.state }"
      placeholder="사이트 URL"
      @keyup="() => regCheck(regs.urlReg,this.site_url)"
    />
    <div
      v-bind:class="{ defaultText: site_url.state || site_url.value.length > 0 , warningText: site_url.value.length == 0 || !site_url.state}"
    >필수 입력 항목입니다.</div>
    <div
      v-bind:class="{ defaultText: site_url.value >= 0 || site_url.state, warningText: !site_url.state}"
    >올바른 주소를 입력해주세요. (ex. http://www.brandi.co.kr)</div>

    <div class="signUpBtnBox">
      <!-- 신청 클릭 하면 패치로 포스트 해보자 -->
      <div class="signUpApply" @click="signUpClick()">신청</div>
      <div class="signUpCancel">
        <router-link to="/">취소</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { JH_URL } from "../../config/urlConfig";
import {
  idReg,
  pwReg,
  phReg,
  nameReg,
  engNameReg,
  telReg,
  urlReg
} from "../../config/reg";
export default {
  name: "SignUpBox",
  mounted: function() {
    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  },
  data() {
    return {
      regs: { idReg, pwReg, phReg, nameReg, engNameReg, telReg, urlReg },
      account: { value: "", state: true },
      password: { value: "", state: true },
      rePw: { value: "", state: true },
      manager_phone: { value: "", state: true },
      seller_attribute_id: { value: "", state: true },
      seller_name: { value: "", state: true },
      seller_name_eng: { value: "", state: true },
      cs_phone: { value: "", state: true },
      site_url: { value: "", state: true }
    };
  },
  methods: {
    regCheck: function(reg, inputName) {
      reg.test(inputName.value)
        ? (inputName.state = true)
        : (inputName.state = false);
    },

    signUpClick: function() {
      if (confirm("입력하신 정보로 셀러신청을 하시겠습니까?") == true) {
        axios
          .post(`${JH_URL}/user`, {
            method: "post",
            account: this.account.value,
            seller_attribute_id: this.seller_attribute_id.value,
            password: this.password.value,
            manager_phone: this.manager_phone.value,
            seller_name: this.seller_name.value,
            seller_name_eng: this.seller_name_eng.value,
            cs_phone: this.cs_phone.value,
            site_url: this.site_url.value,
            end_date: this.end_date
          })
          .then(res => {
            if (res.status === 200) {
              alert(
                "신청이 완료되었습니다.검토 후 연락드리겠습니다.감사합니다."
              );
              this.$router.push("/");
            }
          })
          .catch(error => console.log(error.response.data.message));

        // .catch(err => {
        //   alert("입력 내용을 확인해 주시기 바랍니다. 감사합니다.");
        //   console.log(err);
        // });
      }
    },
    radios: function() {}
  }
};
</script>

<style lang="scss">
.signUpBox {
  width: 470px !important;
  margin: 0 auto;
  padding: 20px 30px 15px 30px;
  background-color: #ffffff !important  ;
  display: flex;
  flex-direction: column;
  p:nth-of-type(1) {
    margin-top: 20px;
    font-size: 24px;
    font-weight: 300 !important;
    text-align: center;
    background-color: #ffffff;
  }
  hr {
    position: relative;
    margin: 20px 0;
  }
  .signUpBanner {
    width: 408px;
    height: 45px;
    margin: 0 auto 40px auto;
  }
  p:nth-of-type(2) {
    margin-bottom: 20px;
    font-size: 22px;
    font-weight: 300;
    background-color: #ffffff;
  }
  .signUpManager {
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    margin-bottom: 20px;
    p {
      margin: 0;
      font-weight: 300;
    }
    p:nth-of-type(1) {
      font-size: 22px;
      margin-right: 10px;
    }
    p:nth-of-type(2) {
      font-size: 16px;
      color: rgb(30, 144, 255);
    }
  }
  .xi-info {
    display: inline;
    font-size: 12px;
    font-weight: 500;
    color: rgb(30, 144, 255);
    letter-spacing: 1px;
    word-spacing: -7px;
    background-color: #ffffff;
  }

  .radioList {
    p {
      text-align: left;
      font-size: 24px;
      font-weight: 300 !important;
    }
    .radioBox {
      background-color: #ffffff;
      div {
        display: inline-block;
        margin-right: 10px;
      }
      label {
        font-size: 14px;
      }
    }
  }
  .signUpBtnBox {
    display: flex;
    flex-direction: row;
    justify-content: center;
    background-color: #ffffff;
    div {
      padding: 10px 10px;
      color: #ffffff;
      font-size: 14px;
      font-weight: 400;
      cursor: pointer;
    }
    .signUpApply {
      width: 50px;
      height: 35px;
      background-color: #31b1d5;
      border-top-left-radius: 4px;
      border-bottom-left-radius: 4px;
    }
    .signUpCancel {
      width: 50px;
      height: 35px;
      background-color: #c9302c;
      border-top-right-radius: 4px;
      border-bottom-right-radius: 4px;
      color: red;
    }
    a:visited {
      color: white;
    }
  }
}
</style>