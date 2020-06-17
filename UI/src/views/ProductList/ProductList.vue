<template>
  <div class="plWrap">
    <div class="slTitleBox">
      <div class="slTitle">상품 관리</div>
    </div>
    <div class="slCategory">
      <i class="xi-home">
        상품관리 / 상품 관리
        <i class="xi-angle-right-min">상품관리 관리</i>
        <i class="xi-angle-right-min">리스트</i>
      </i>
    </div>
    <div class="filterBox">
      <div class="filterDiv">
        <div>조회 기간</div>
        <b-form-datepicker v-model="searchPeriod[0].value" id="datepicker-placeholder" placeholder="클릭해주세요" local="kr" style="width:180px"></b-form-datepicker>
          <span class="span-input-group"> ~ </span>
        <b-form-datepicker v-model="searchPeriod[1].value" id="datepicker-placeholder2" placeholder="클릭해주세요" local="kr" style="width:180px"></b-form-datepicker>

      </div>
      <div class="filterDiv">
        <div>셀러명</div>
        <div>
          <input type="text" v-model="inputBtn[0].state" placeholder="검색어를 입력하세요." />
          <select v-model="selectBtn[0].name">
            <option value>Select</option>
            <option value="product_name">상품명</option>
            <option value="product_id">상품번호</option>
            <option value="code">상품코드</option>
          </select>
          <input v-model="selectBtn[0].state" type="text" placeholder="검색어를 입력하세요." />
        </div>
      </div>
      <div class="filterDiv">
        <div>셀러속성 :</div>
        <div>
          <div></div>
          <div
            v-bind:class="{ btn: !attBtn[0].state, clickedBtn: attBtn[0].state}"
            @click="attAllClick()"
          >전체</div>
          <div
            v-bind:class="{ btn: !attBtn[1].state, clickedBtn: attBtn[1].state}"
            @click="() => attClickCheck(1)"
          >쇼핑몰</div>
          <div
            v-bind:class="{ btn: !attBtn[2].state, clickedBtn: attBtn[2].state}"
            @click="() => attClickCheck(2)"
          >마켓</div>
          <div
            v-bind:class="{ btn: !attBtn[3].state, clickedBtn: attBtn[3].state}"
            @click="() => attClickCheck(3)"
          >로드샵</div>
          <div
            v-bind:class="{ btn: !attBtn[4].state, clickedBtn: attBtn[4].state}"
            @click="() => attClickCheck(4)"
          >디자이너브랜드</div>
          <div
            v-bind:class="{ btn: !attBtn[5].state, clickedBtn: attBtn[5].state}"
            @click="() => attClickCheck(5)"
          >제너럴브랜드</div>
          <div
            v-bind:class="{ btn: !attBtn[6].state, clickedBtn: attBtn[6].state}"
            @click="() => attClickCheck(6)"
          >내셔널브랜드</div>
          <div
            v-bind:class="{ btn: !attBtn[7].state, clickedBtn: attBtn[7].state}"
            @click="() => attClickCheck(7)"
          >뷰티</div>
        </div>
      </div>
      <div class="flexFilter">
        <div class="filterDiv">
          <div>판매여부 :</div>
          <div>
            <div></div>
            <div
              @click="() => clickCheck(this.twoBtn[0], 3)"
              v-bind:class="{ btn: twoBtn[0].state != 3, clickedBtn: twoBtn[0].state === 3}"
            >전체</div>
            <div
              @click="() => clickCheck(this.twoBtn[0],1)"
              v-bind:class="{ btn: twoBtn[0].state != 1, clickedBtn: twoBtn[0].state === 1}"
            >판매</div>
            <div
              @click="() => clickCheck(this.twoBtn[0],0)"
              v-bind:class="{ btn: twoBtn[0].state != 0, clickedBtn: twoBtn[0].state === 0}"
            >미판매</div>
          </div>
        </div>
        <div class="filterDiv">
          <div>할인여부 :</div>
          <div>
            <div></div>
            <div
              @click="() => clickCheck(this.twoBtn[1], 3)"
              v-bind:class="{ btn: twoBtn[1].state != 3, clickedBtn: twoBtn[1].state === 3}"
            >전체</div>
            <div
              @click="() => clickCheck(this.twoBtn[1],1)"
              v-bind:class="{ btn: twoBtn[1].state != 1, clickedBtn: twoBtn[1].state === 1}"
            >할인</div>
            <div
              @click="() => clickCheck(this.twoBtn[1],0)"
              v-bind:class="{ btn: twoBtn[1].state != 0, clickedBtn: twoBtn[1].state === 0}"
            >미할인</div>
          </div>
        </div>
        <div class="filterDiv">
          <div>진열여부 :</div>
          <div>
            <div></div>
            <div
              @click="() => clickCheck(this.twoBtn[2], 3)"
              v-bind:class="{ btn: twoBtn[2].state != 3, clickedBtn: twoBtn[2].state === 3}"
            >전체</div>
            <div
              @click="() => clickCheck(this.twoBtn[2],1)"
              v-bind:class="{ btn: twoBtn[2].state != 1, clickedBtn: twoBtn[2].state === 1}"
            >진열</div>
            <div
              @click="() => clickCheck(this.twoBtn[2],0)"
              v-bind:class="{ btn: twoBtn[2].state != 0, clickedBtn: twoBtn[2].state === 0}"
            >미진열</div>
          </div>
        </div>
      </div>
      <div class="submitBox">
        <div class="Btn searchBtn" @click="search()">검색</div>
        <div class="Btn resetBtn" @click="reset()">초기화</div>
      </div>
    </div>
    <!-- <div class="select-button">
         <div>
    <b-form-select v-model="saled" :options="saleproduct" style="width:100px"></b-form-select>
         </div>
          <div>
    <b-form-select v-model="displayed" :options="displayproduct" style="width:100px"></b-form-select>
  </div>
            <div><b-button variant="warning">적용</b-button>
            </div>
          </div> -->

    <div class="count">전체 조회건 수 : {{infoDatas.quantity}}</div>
    <div class="tableBox">
      <!-- 테이블 시작 부분입니다.. -->
      <template>
        <v-simple-table>
          <template v-slot:default>
            <div class="tableIn">
              <thead>
                <tr>
                  <th class="text-left">등록일</th>
                  <th class="text-left">대표이미지</th>
                  <th class="text-left">상품명</th>
                  <th class="text-left">상품코드</th>
                  <th class="text-left">상품번호</th>
                  <th class="text-left">셀러속성</th>
                  <th class="text-left">셀러명</th>
                  <th class="text-left">판매가</th>
                  <th class="text-left">할인가</th>
                  <th class="text-left">판매여부</th>
                  <th class="text-left">진열여부</th>
                  <th class="text-left">할인여부</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="info in infoDatas.product" :key="info.id">
                  <td>{{info.created_at}}</td>
                  <td></td>
                  <td>{{info.product_name}}</td>
                  <td>{{info.product_code}}</td>
                  <td>{{info.product_id}}</td>
                  <td>{{info.seller_attribute}}</td>
                  <td>{{info.seller_name}}</td>
                  <td>{{info.price}}</td>
                  <td>
                    {{info.discount_price}}
                    <div class="discount">{{info.discount_rate ? `(${info.discount_rate}%)` : ""}}</div>
                  </td>
                  <td>{{info.on_sale ? "판매" : "미판매"}}</td>
                  <td>{{info.on_list ? "진열" : "미진열"}}</td>
                  <td>{{info.discount ? "할인" : "미할인"}}</td>
                </tr>
              </tbody>
            </div>
          </template>
        </v-simple-table>
      </template>
    </div>
    <div id="app">
  <v-app id="inspire">
    <div class="text-center">
      <v-pagination
        v-model="page"
        :length="maxPage"
        :total-visible="7"
        @input="search"
      ></v-pagination>
    </div>
  </v-app>
</div>
  </div>
  
</template>

<script>
import axios from "axios";
import { JH_URL } from "../../config/urlConfig";
export default {
  data() {
    return {
      infoDatas: {
      },

      page: 1,
      maxPage: 1,

      searchPeriod: [
        { name: "start_period", value: null },
        { name: "end_period", value: null}
      ],

      searchDatas: [
        { name: "seller_name", state: "" },
        { name: "code", state: 3 },
        { name: "seller_attribute", state: 3 }
      ],

      twoBtn: [
        { name: "on_sale", state: 3 },
        { name: "discount", state: 3 },
        { name: "on_list", state: 3 }
      ],

      inputBtn: [{ name: "seller_name", state: "" }],

      selectBtn: [{ name: "", state: "" }],

      attBtn: [
        { name: "", state: 1 },
        { name: "seller_attribute", state: 0 },
        { name: "seller_attribute", state: 0 },
        { name: "seller_attribute", state: 0 },
        { name: "seller_attribute", state: 0 },
        { name: "seller_attribute", state: 0 },
        { name: "seller_attribute", state: 0 },
        { name: "seller_attribute", state: 0 }
      ],

      attAll: { state: true },
      attShop: { state: false },
      attMarket: { state: false },
      attLoad: { state: false },
      attDesigner: { state: false },
      attGeneral: { state: false },
      attBeauty: { state: false }
    };
  },
  mounted: function() {
    this.getListDatas();
  },
  methods: {
    search: function() {
      let queryString = [];

      this.twoBtn.filter(item => {
        item.state < 3 ? queryString.push(`${item.name}=${item.state}&`) : "";
      });
      this.inputBtn.filter(item => {
        item.state.length > 0
          ? queryString.push(`${item.name}=${item.state}&`)
          : "";
      });
      this.selectBtn.filter(item => {
        item.state.length > 0
          ? queryString.push(`${item.name}=${item.state}&`)
          : "";
      });
      this.searchPeriod.filter(item => {
        item.value
          ? queryString.push(`${item.name}=${item.value}&`)
          : "";
      });
      
      if (this.attBtn[0].state == 0){
        this.attBtn.filter(item => {
        item.state
        ? queryString.push(`${item.name}=${item.state}&`) 
        : "";
      });
      }
      

      axios
        .get(`${JH_URL}/product/list?limit=10&offset=${(this.page - 1) * 10}&${queryString.join("")}`, {
          headers: {
            Authorization: localStorage.Authorization
          }
        })
        .then(response => {
          this.infoDatas = response.data.data;
          this.maxPage = Math.ceil(this.infoDatas.quantity/10)
        });
      console.log("url=",`${JH_URL}/product/list?limit=10&offset=0&${queryString.join("")}`);
    },
    getListDatas: function() {
      axios
        .get(`${JH_URL}/product/list?limit=10&offset=0`, {
          headers: {
            Authorization: localStorage.Authorization
          }
        })
        .then(response => {
          this.infoDatas = response.data.data;
          this.maxPage = Math.ceil(this.infoDatas.quantity/10)
        });
    },
    reset: function() {
      this.searchDatas = [
        { name: "seller_name", state: "" },
        { name: "code", state: 3 },
        { name: "seller_attribute", state: 3 }
      ]
      this. twoBtn = [
        { name: "on_sale", state: 3 },
        { name: "discount", state: 3 },
        { name: "on_list", state: 3 }
      ]
      this.inputBtn = [{ name: "seller_name", state: "" }]
      this.selectBtn = [{ name: "", state: "" }]

      this.attBtn = [
        { name: "", state: 1 },
        { name: "seller_attribute", state: 0 },
        { name: "seller_attribute", state: 0 },
        { name: "seller_attribute", state: 0 },
        { name: "seller_attribute", state: 0 },
        { name: "seller_attribute", state: 0 },
        { name: "seller_attribute", state: 0 },
        { name: "seller_attribute", state: 0 }      ]
      
      this.searchPeriod= [
        { name: "start_period", value: null },
        { name: "end_period", value: null}
      ],

      this.getListDatas()
    },

    clickCheck: function(name, stateNumber) {
      if (name.state === stateNumber) {
        name.state = 3;
      } else {
        name.state = stateNumber;
      }
    },
    attAllClick: function() {
      if (!this.attBtn[0].state) {
        this.attBtn[0].state = 1;
        this.attBtn[1].state = 0;
        this.attBtn[2].state = 0;
        this.attBtn[3].state = 0;
        this.attBtn[4].state = 0;
        this.attBtn[5].state = 0;
        this.attBtn[6].state = 0;
        this.attBtn[7].state = 0;

      } else if (this.attBtn[0].state) {
        this.attBtn[0].state = 1;
      }
    },
    attClickCheck: function(index) {
      !this.attBtn[index].state
        ? this.attBtn[index].state = index
        : this.attBtn[index].state = 0

      if (this.attBtn.filter(item => item.state != 0).length === 7) {
        this.attBtn[0].state = 1;
        this.attBtn[1].state = 0;
        this.attBtn[2].state = 0;
        this.attBtn[3].state = 0;
        this.attBtn[4].state = 0;
        this.attBtn[5].state = 0;
        this.attBtn[6].state = 0;
        this.attBtn[7].state = 0;
      }
      if (this.attBtn.filter(item => item.state != 0).length > 1) {
        this.attBtn[0].state = 0;
      }
    }
  }
};
</script>

<style lang="scss" scoped>
* {
  // border: 1px solid red;
}
.plWrap {
  padding-top: 35px;

  .slTitleBox {
    padding: 0 20px;
    display: flex;
    align-items: flex-end;
    margin-bottom: 20px;

    .slTitle {
      font-size: 28px;
      color: #666;
      margin-right: 10px;
      font-weight: 300;
    }
    .slSubTitle {
      font-size: 14px;
      color: #666;
      font-weight: 300;
    }
  }
  .slCategory {
    width: 100%;
    height: 44px;
    font-size: 13px;
    display: flex;
    align-items: center;
    background-color: #eee;
    padding-left: 20px;
    margin-bottom: 10px;
  }
  .filterBox {
    margin-top: 15px;
    width: calc(100vw - 335px);
    border: 3px solid #eee;
    margin: 10px;
    padding-left: 10px;
    margin-bottom: 20px;
    background-color: #fafafa;
  }
  .count {
    margin-left: 10px;
  }
  .discount {
    color: red;
    font-size: 12px;
  }
  .filterDiv {
    display: flex;
    padding: 10px 20px;
    font-size: 14px;

    div:first-child {
      margin-right: 30px;
      width: 100px;
      align-self: center;
    }
    .btn {
      display: inline-block;
      padding: 6px 12px;
      margin-right: 10px;
      font-size: 12px;
      font-weight: 400;
      line-height: 1.42857143;
      text-align: center;
      white-space: nowrap;
      vertical-align: middle;
      cursor: pointer;
      user-select: none;
      background-image: none;
      border: 1px solid transparent;
      border-radius: 4px;
      border: 1px solid #eee;
      background-color: white;

      &:hover {
        background-color: #eee;
      }
    }
    .clickedBtn {
      display: inline-block;
      padding: 6px 12px;
      margin-right: 10px;
      font-size: 12px;
      font-weight: 400;
      line-height: 1.42857143;
      text-align: center;
      white-space: nowrap;
      vertical-align: middle;
      cursor: pointer;
      user-select: none;
      background-image: none;
      border: 1px solid transparent;
      border-radius: 4px;
      border: 1px solid #357ebd;
      color: #fff;
      background-color: #428bca;
    }

    .span-input-group {
     width: 39px;
    background-color: #e5e5e5;
    color: #555555;
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
    font-weight: bold;
    }
  }

  input {
    border: 1px solid lightgray;
    border-radius: 3px;
    width: 180px;
    padding: 6px 12px 6px 33px;
    font-size: 12px;
    font-weight: 500;
    color: #333333;
    margin-right: 40px;
    background-color: white;
  }
  input:focus {
    outline: 1px solid #eee;
  }
  select {
    width: 180px;
    height: 100%;
    border: 1px solid lightgray;
    padding-left: 10px;
    margin-right: 5px;
    border-radius: 3px;
    vertical-align: middle;
    background-color: white;
    font-size: 12px;
  }
  .flexFilter {
    display: grid;
    grid-template-columns: 1fr 1fr;
    align-content: center;
  }
  .submitBox {
    display: flex;
    justify-content: center;

    .Btn {
      display: inline-block;
      padding: 6px 12px;
      margin-bottom: 0;
      font-size: 12px;
      font-weight: 400;
      line-height: 1.42857143;
      text-align: center;
      white-space: nowrap;
      vertical-align: middle;
      cursor: pointer;
      border: 1px solid transparent;
      border-radius: 4px;
      margin: 40px 0;
    }
    .searchBtn {
      color: #fff;
      background-color: #428bca;
      border-color: #357ebd;

      margin-right: 15px;
      &:hover {
        background-color: #357ebd;
      }
    }

    .resetBtn {
      color: black;
      background-color: white;
      border-color: #333;
      &:hover {
        background-color: #eee;
      }
    }
  }

  .tableBox {
    .tableIn {
      width: calc(100vw - 335px);
      overflow: auto;
      white-space: nowrap;
      margin: 10px;
      border: 1px solid lightgray;
      button {
        padding: 5px;
        color: #fff;
        border-radius: 3px;
        margin-left: 5px;
      }
    }
    th,
    td {
      text-align: left;
      height: 39px !important;
      padding: 12px 8px 8px 8px;
      border: 1px solid #ddd;
      border-left-width: 0 !important;
      border-bottom-width: 0 !important;
    }
    th {
      font-weight: 600;
      color: black !important;
      font-size: 13px !important;
      background-color: #eee;
    }
  }
}
</style>
