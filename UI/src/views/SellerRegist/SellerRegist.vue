<template >
  <div>
    <SrTitle />
    <!-- 기본 정보 시작 영역 -->
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">기본 정보</i>
      </div>
      <div class="cmpTable">
        <v-simple-table>
          <template>
            <!-- 테이블 시작 영역 -->
            <tbody>
              <!-- 이미지박스 컨테이너 컴포넌트 생성 후 재사용 중, slot 이용 해당 내용 전달 -->
              <ImageBox>
                <template #thName>셀러프로필</template>
                <template #infoText01>
                  <i class="xi-info">셀러 프로필 확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다.</i>
                </template>
              </ImageBox>
            </tbody>
            <!-- 셀러 상태 테이블 -->
            <tbody>
              <tr>
                <th>셀러 상태</th>
                <td>{{baseInfo.seller_status}}</td>
              </tr>
            </tbody>
            <tbody v-if="role === 1">
              <tr>
                <th>셀러 속성</th>
                <td>
                  <div class="seller_att"
                  v-for="attributeList in baseInfo.seller_attributes.list"
                  :key="attributeList.id"> 
                    <input
                      v-model="baseInfo.seller_attributes.selected"
                      :value="attributeList.id"
                      type="radio"
                      name="attributeList.name"
                    />
                    <label for="shoppinglabel">{{attributeList.name}}</label>
                  </div>
                   </td>
              </tr>
            </tbody>
            <tbody>
              <tr>
                <th>셀러 한글명</th>
                
                <td v-if="role ===1">
                  <input
                      v-model="baseInfo.seller_name"
                      type="text"
                     />
                </td>
                <td v-else>
                  {{baseInfo.seller_name}}
                </td>

              </tr>
            </tbody>


            <!-- 셀러 영문명 -->
            <tbody>
              <tr>
                <th>셀러 영문명</th>
                 <td v-if="role ===1">
                  <input
                      v-model="baseInfo.seller_name_eng"
                      type="text"                 
                    />
                </td>
                <td v-else>
                  {{baseInfo.seller_name_eng}}
                </td>
                
              </tr>
            </tbody>
            <!-- 셀러 계정 -->
            <tbody>
              <tr>
                <th>셀러 계정</th>
                <td>{{baseInfo.seller_account}}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </div>
    </div>
    <!-- 상세 정보 시작 -->
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">상세 정보</i>
      </div>
      <div class="cmpTable">
        <v-simple-table>
          <template>
            <!-- 테이블 시작 영역 -->
            <tbody>
              <!-- 셀러페이지 배경이미지 -->
              <ImageBox>
                <template #thName>셀러페이지 배경 이미지</template>
                <template #infoText01>
                  <i class="xi-info">셀러 프로필 확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다.</i>
                </template>
                <template #infoText02>
                  <i class="xi-info">배경이미지는 1200 * 850 사이즈 이상으로 등록해주세요.</i>
                </template>
                <template #infoText03>
                  <i class="xi-info">확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다.</i>
                </template>
              </ImageBox>
            </tbody>
            <!-- 셀러 한줄 소개 -->
            <tbody>
              <InputBox v-model="detailInfo.introduction_short" placeholder="셀러 한줄 소개">
                <template #thName>
                  셀러 한줄 소개
                  <i class="xi-pen" />
                </template>
              </InputBox>
            </tbody>
            <!-- 셀러 상세 소개 -->
            <tbody>
              <TextAreaBox v-model="detailInfo.introduction_detail" placeholder="셀러 상세 소개">
                <template #thName>셀러 상세 소개</template>
                <template #infoText01>
                  <i class="xi-info">셀러 상세 소개 글은 최소10자 이상 입니다.</i>
                </template>
              </TextAreaBox>
            </tbody>
            <!-- 셀러 사이트 URL -->
            <tbody>
              <InputBox v-model="detailInfo.site_url" placeholder="셀러 사이트 URL">
                <template #thName>
                  셀러 사이트 URL
                  <i class="xi-pen" />
                </template>
              </InputBox>
            </tbody>
            <!-- 담당자 정보 -->
            <tbody>
              <tr>
                <th>
                  담당자정보
                  <i class="xi-pen" />
                </th>
                <td></td>
                <td class="threeInput">
                  <input
                    type="text"
                    v-model="detailInfo.managers[0].name"
                    @input="detailInfo.managers[0].name = $event.target.value"
                    placeholder="담당자명"
                  />
                  <input
                    type="text"
                    v-model="detailInfo.managers[0].phone"
                    @input="detailInfo.managers[0].phone = $event.target.value"
                    placeholder="담당자 번호"
                  />
                  <div style="display: flex">
                    <input
                      type="text"
                      v-model="detailInfo.managers[0].email"
                      @input="detailInfo.managers[0].email = $event.target.value"
                      placeholder="담당자 이메일"
                    />
                    <div
                      v-if="tableCount == 1"
                      @click="() => managerPlus()"
                      class="supervisorsBtn plusBtn"
                    >
                      <i class="xi-plus"></i>
                    </div>
                  </div>
                </td>
                <td class="threeInput" v-if="tableCount > 1">
                  <input
                    type="text"
                    v-model="detailInfo.managers[1].name"
                    @input="detailInfo.managers[1].name = $event.target.value"
                    placeholder="담당자명"
                  />
                  <input
                    type="text"
                    v-model="detailInfo.managers[1].phone"
                    @input="detailInfo.managers[1].phone = $event.target.value"
                    placeholder="담당자 번호"
                  />
                  <div style="display: flex">
                    <input
                      type="text"
                      v-model="detailInfo.managers[1].email"
                      @input="detailInfo.managers[1].email = $event.target.value"
                      placeholder="담당자 이메일"
                    />
                    <div
                      v-if="tableCount == 2"
                      @click="() => managerPlus()"
                      class="supervisorsBtn plusBtn"
                    >
                      <i class="xi-plus"></i>
                    </div>
                    <div
                      v-if="tableCount == 2"
                      @click="() => supervisorsMinus(1)"
                      class="supervisorsBtn minusBtn"
                    >
                      <i class="xi-minus"></i>
                    </div>
                  </div>
                </td>

                <td class="threeInput" v-if="tableCount > 2">
                  <input
                    type="text"
                    v-model="detailInfo.managers[2].name"
                    @input="detailInfo.managers[2].name = $event.target.value"
                    placeholder="담당자명"
                  />
                  <input
                    type="text"
                    v-model="detailInfo.managers[2].phone"
                    @input="detailInfo.managers[2].phone = $event.target.value"
                    placeholder="담당자 번호"
                  />
                  <div style="display: flex">
                    <input
                      type="text"
                      v-model="detailInfo.managers[2].email"
                      @input="detailInfo.managers[2].email = $event.target.value"
                      placeholder="담당자 이메일"
                    />
                    <div
                      v-if="tableCount == 3"
                      @click="() => supervisorsMinus(2)"
                      class="supervisorsBtn minusBtn"
                    >
                      <i class="xi-minus"></i>
                    </div>
                  </div>
                </td>
              </tr>
            </tbody>
            <!-- 고객센터 -->
            <tbody>
              <InputBox v-model="detailInfo.cs_phone" placeholder="고객센터 전화번호">
                <template #thName>
                  고객센터
                  <i class="xi-pen" />
                </template>
              </InputBox>
            </tbody>
            <!-- 택배 -->
            <!-- npm install --save vuejs-daum-postcode -->
            <tbody>
              <th>
                택배주소
                <i class="xi-pen" />
              </th>
              <td class="addressBox">
                <div class="addressBtn">
                  <input
                    class="disabledInput"
                    type="text"
                    v-model="detailInfo.zip_code"
                    placeholder="우편번호"
                    disabled
                  />
                  <div class="searchZip" @click="addressModalOpen()">우편번호 찾기</div>
                </div>
                <input
                  class="disabledInput"
                  type="text"
                  v-model="detailInfo.address"
                  placeholder="주소(택배 수령지)"
                  disabled
                />
                <input
                  type="text"
                  v-model="detailInfo.address_detail"
                  placeholder="상세주소(택배 수령지)"
                />
              </td>
            </tbody>
            <!-- 고객센터 운영시간(주중)-->
            <tbody>
              <th>
                고객센터 운영시간(주중)
                <i class="xi-pen" />
              </th>
              <td>
                <v-app id="inspire">
                  <v-row>
                    <v-col cols="1">
                      <v-text-field
                        :value="detailInfo.weekday_start_time"
                        @input="detailInfo.weekday_start_time = $event"
                        type="time"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-app>
                <v-app id="inspire">
                  <v-row>
                    <v-col cols="1">
                      <v-text-field
                        :value="detailInfo.weekday_end_time"
                        @input="detailInfo.weekday_end_time = $event"
                        type="time"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-app>
              </td>
            </tbody>
            <!-- 고객센터 운영시간(주중)-->
            <tbody>
              <th>고객센터 운영시간(주말)</th>
              <td>
                <v-app id="inspire">
                  <v-row>
                    <v-col cols="1">
                      <v-text-field
                        :value="detailInfo.weekend_start_time"
                        @input="detailInfo.weekend_start_time = $event"
                        type="time"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-app>
                <v-app id="inspire">
                  <v-row>
                    <v-col cols="1">
                      <v-text-field
                        :value="detailInfo.weekend_end_time"
                        @input="detailInfo.weekend_end_time = $event"
                        type="time"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-app>
              </td>
            </tbody>
            <!-- 정산정보 입력 -->
            <tbody>
              <tr>
                <th>
                  정산정보 입력
                  <i class="xi-pen" />
                </th>
                <td class="threeInput">
                  <input type="text" v-model="detailInfo.bank" placeholder="정산은행" />
                  <input type="text" v-model="detailInfo.bank_account_name" placeholder="계좌주" />
                  <input type="text" v-model="detailInfo.bank_account_number" placeholder="계좌번호" />
                </td>
              </tr>
            </tbody>

           <!-- 셀러상태 변경기록 -->
            <tbody>
              <th>셀러상태 변경기록</th>
              <td
                class="historyBox"

              >
                <tbody>
                  <tr>
                    <th>셀러상태 변경 적용일시</th>
                  </tr>
              
                </tbody>
                <tbody>
                  <tr>
                    <th>셀러상태</th>
                  </tr>
                  
                </tbody>
                <tbody>
                  <tr>
                    <th>변경 실행자</th>
                  </tr>
                </tbody>
                <td
                v-for="history in detailInfo.seller_status_history"
                :key="history.account" class="historyTr3"
                >
                <tr class="historyTr">
                    <td>{{history.startdate}}</td>
                </tr>
                <tr class="historyTr">
                    <td>{{history.name}}</td>
                </tr>
                <tr class="historyTr2">
                    <td>{{history.account}}</td>
                </tr>
                </td>
              
            </tbody>
          </template>
        </v-simple-table>
      </div>
    </div>
 
    <!-- 관리브랜드 정보 -->
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">관리브랜드 정보</i>
      </div>
      <div class="cmpTable">
        <v-simple-table>
          <!-- 테이블 시작 영역 -->
          <tbody>
            <tr>
              <th>관리 브랜드</th>
              <td></td>
            </tr>
          </tbody>
        </v-simple-table>
      </div>
    </div>
    <!-- 셀러 모델 사이즈 정보 -->
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">셀러 모델 사이즈 정보</i>
      </div>
      <div class="cmpTable">
        <v-simple-table>
          <!-- 테이블 시작 영역 -->
          <tbody>
            <InputBox v-model="modelSize.height" placeholder="키">
              <template #thName>키</template>
              <template #infoText01>
                <i class="xi-info">ex) 160cm => 160</i>
              </template>
            </InputBox>
          </tbody>
          <tbody>
            <InputBox v-model="modelSize.top_size" placeholder="상의 사이즈">
              <template #thName>상의 사이즈</template>
              <template #infoText01>
                <i class="xi-info">ex) 55사이즈 => 55</i>
              </template>
            </InputBox>
          </tbody>
          <tbody>
            <InputBox v-model="modelSize.bottom_size" placeholder="하의 사이즈">
              <template #thName>하의 사이즈</template>
              <template #infoText01>
                <i class="xi-info">ex) 27사이즈 => 27</i>
              </template>
            </InputBox>
          </tbody>
          <tbody>
            <InputBox v-model="modelSize.foot_size" placeholder="발 사이즈">
              <template #thName>발 사이즈</template>
              <template #infoText01>
                <i class="xi-info">ex) 240mm => 240</i>
              </template>
            </InputBox>
          </tbody>
        </v-simple-table>
      </div>
    </div>
    <!-- 쇼핑 업데이트 메시지 -->
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">쇼핑 업데이트 메시지</i>
      </div>
      <div class="cmpTable">
        <v-simple-table>
          <!-- 테이블 시작 영역 -->
          <tbody>
            <tr>
              <td class="infoTd">
                <i class="xi-info">신상품 업데이트 시 / 내 스토어를 팔로잉하는 회원의 쇼핑피드에 자동으로 노출됩니다.</i>
                <i class="xi-info">아래 메시지를 기재하시면 노출될 때 해당 메시지를 회원의 쇼핑피드에 함께 노출할 수 있습니다.</i>
                <i class="xi-info">해당 메시지 미 기재 시 디폴트로 다음의 문구가 출력됩니다.</i>
                <span>"000 스토어에 신상이 올라왔어요"</span>
              </td>
            </tr>
          </tbody>
          <tbody>
            <tr>
              <td>
                <textarea
                  v-model="feed"
                  placeholder="ex) 안녕하세요 000에요!! 봄에 어울리는 신상이 입고 되었습니다."
                ></textarea>
              </td>
            </tr>
          </tbody>
        </v-simple-table>
      </div>
    </div>
    <div class="daumAddress" v-if="addressModal">
      <div id="app">
        <DaumPostcode :on-complete="handleAddress" />
      </div>
      <div @click="addressModalOpen()" class="appCancel">
        <i class="xi-close"></i>
      </div>
    </div>
    <!-- 신청 클릭 하면 패치로 포스트 해보자 -->
    <div class="btnBox">
      <!-- 신청 클릭 하면 패치로 포스트 해보자 -->
      <div class="editBtn" @click="putInfoDatas">수정</div>
      <div class="cancelBtn" @click="cancelEdit">취소</div>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import { eventBus } from "../../main";
import { JH_URL, URL } from "../../config/urlConfig";
import SrTitle from "./Components/SrTitle";
import ImageBox from "./Slots/ImageBox";
import InputBox from "./Slots/InputBox";
import TextAreaBox from "./Slots/TextAreaBox";
import DaumPostcode from "vuejs-daum-postcode";

// .get(`${URL}/seller_details`, {
export default {
  //첫 마운트가 되면 셀러의 기존 입력된 정보들을 불러오게 합니다.

  data() {
    return {
      masterURl : `${JH_URL}/user/${this.$route.params.id}`,
      userURl : `${JH_URL}/user`,
      baseInfo:{},
      detailInfo:{},
      modelSize:{},
      role: null,
      feed: null,
      addressModal: false,
      tableCount: null
    };
    e;
  },
  mounted: function() {

    axios
      .get(
        this.$route.params.id != null
          ? this.masterURl
          : this.userURl,
        {
          headers: {
            Authorization: localStorage.Authorization
          }
        }
      )
      .then(response => {
        this.baseInfo= response.data.base_info
        this.detailInfo= response.data.detail_info
        this.modelSize= response.data.model_size
        this.role= response.data.role,
        this.feed= response.data.feed
        this.tableCount = this.detailInfo.managers.length;
      });
      console.log(this.feed)
  },

  methods: {
    addressModalOpen: function() {
      this.addressModal = !this.addressModal;
    },
    timeInput: function(e) {
      this.time = e;
    },
    supervisorsMinus: function(index) {
      this.detailInfo.managers.pop()
      this.tableCount = this.detailInfo.managers.length
    },
    managerPlus: function() {
      this.detailInfo.managers.push({
        name: null,
        phone: null,
        email: null
      }),
      this.tableCount = this.detailInfo.managers.length
    },
    handleAddress: function(data) {
      let fullAddress = data.address;
      let extraAddress = "";
      if (data.addressType === "R") {
        if (data.bname !== "") {
          extraAddress += data.bname;
        }
        if (data.buildingName !== "") {
          extraAddress +=
            extraAddress !== "" ? `, ${data.buildingName}` : data.buildingName;
        }
        fullAddress += extraAddress !== "" ? ` (${extraAddress})` : "";
      }
      this.detailInfo.address = fullAddress;
      this.detailInfo.zip_code = data.zonecode;
      console.log(data); // e.g. '서울 성동구 왕십리로2길 20 (성수동1가)'
    },
    // 수정버튼을 누르면 백엔드로 인풋에 입력된 모든 내용을 보냅니다.
    putInfoDatas: function() {
      console.log(this.tableCount)
      console.log(this.detailInfo.managers)
      if (confirm("셀러정보를 수정 하시겠습니까?") == true) {
        axios
          .put(
            this.$route.params.id != null
              ? this.masterURl
              : this.userURl,
            {
              base_info:{
                profile_image: "url",
                seller_attribute_id: this.baseInfo.seller_attributes.selected,
                seller_name: this.baseInfo.seller_name,
                seller_name_eng: this.baseInfo.seller_name_eng

              },
              detail_info:{
                background_image: "url",
                introduction_short: this.detailInfo.introduction_short,
                introduction_detail: this.detailInfo.introduction_detail,
                site_url: this.detailInfo.site_url,
                managers: this.detailInfo.managers,
                cs_phone: this.detailInfo.cs_phone,
                zip_code: this.detailInfo.zip_code,
                address: this.detailInfo.address,
                address_detail: this.detailInfo.address_detail,
                buisness_hours: this.detailInfo.buisness_hours,
                weekday_start_time: this.detailInfo.weekday_start_time,
                weekday_end_time: this.detailInfo.weekday_end_time,
                weekend_start_time: this.detailInfo.weekend_start_time,
                weekend_end_time: this.detailInfo.weekend_end_time,
                bank: this.detailInfo.bank,
                bank_account_name: this.detailInfo.bank_account_name,
                bank_account_number: this.detailInfo.bank_account_number,
                feed: this.feed
              },
              model_size:{
                height: Number(this.modelSize.height),
                top_size: Number(this.modelSize.top_size),
                bottom_size: Number(this.modelSize.bottom_size),
                foot_size: Number(this.modelSize.foot_size),
              },
              
            },
            {
              headers: {
                Authorization: localStorage.Authorization
              }
            }
          )
          .then(res => {
            if (res.status === 200) {
              alert("셀러정보가 정상적으로 수정되었습니다.");
              window.location.reload();
            }
          })
          .catch(error => {
            console.log(error)
            alert("입력하지 않은 필수항목이 있습니다. 다시 확인해주세요.");
          });
      }
    },
    cancelEdit: function() {
      if (
        confirm("수정을 취소하겠습니까? 확인을 누르면 새로고침됩니다.") == true
      ) {
        window.location.reload();
      }
    }
  },

  components: {
    SrTitle,
    ImageBox,
    InputBox,
    TextAreaBox,
    DaumPostcode
  }
};
</script>
  <style lang="scss" >
.cmpWrap {
  border: 1px solid lightgray;
  border-radius: 3px;
  margin: 10px;

  .cmpTitle {
    height: 39px;
    background-color: #eee;
    color: #333;
    font-size: 18px;
    line-height: 16px;
    font-weight: 400;
    padding: 10px 20px;
  }
  .cmpTable {
    border-left: 1px solid lightgrey;
    border-right: 1px solid lightgrey;
    border-bottom: 1px solid lightgrey;

    border-radius: 3px;
    margin: 10px;

    th {
      border-right: 1px solid lightgray;
      border-top: 1px solid lightgray;
      vertical-align: middle;
      width: 149px;
    }
    td {
      display: flex;
      padding: 8px;
      height: 100%;
      vertical-align: middle;
    }
    td:first-of-type {
      border-top: 1px solid lightgray;
    }

    input {
      border: 1px solid lightgray;
      border-radius: 3px;
      width: 40%;
      padding: 6px 12px 6px 33px;
      font-size: 14px;
      font-weight: 500;
      color: #333333;
      background-color: white;
    }
    input:focus {
      outline: 1px solid #eee;
    }

    textarea {
      width: 531px;
      height: 100px;
      padding: 6px 12px;
      border: 1px solid lightgray;
      border-radius: 3px;
      background-color: white;
    }

    .infoTd {
      display: flex;
      flex-direction: column;
      padding: 0 10px 10px 10px;
      color: rgb(30, 144, 255);
      .xi-info {
        color: rgb(30, 144, 255);
      }
    }

    .option {
      input {
        width: 10px;
        height: 10px;
        margin-right: 10px;
        background-color: white;
      }
      label {
        margin-right: 10px;
      }
    }
    .threeInput {
      display: flex;
      flex-direction: column;
      input {
        margin-bottom: 20px;
      }
    }
  }
 .historyBox {
    width: 100%;
    th,
    td {
    width: 149px;
    border: 1px solid lightgray;
    }
    th {
      background-color: #eee;
    }
     padding: 8px 8px 0 8px !important;

    
  }
  .historyTr {
    width : 150px;
   border-left: 1px solid lightgray;
   

 }
 .historyTr2 {
   width : 149px;
   border-bottom: 1px solid lightgray;
   border-left: 1px solid lightgray;
   border-right: 1px solid lightgray;


     
 }

 .historyTr3 {
   padding: 0 0 0 8px !important;
 }
 .seller_att {

      display: flex;
      input {
        margin-top : 3px;
      }
       label {
      width:80px;
    }
    }
}

.addressBox {
  display: flex;
  flex-direction: column;
  .disabledInput {
    cursor: not-allowed !important;
  }
  .addressBtn {
    display: flex;
    width: 40%;
    input {
      margin-right: 10px;
    }

    .searchZip {
      border-radius: 3px;
      width: 50%;
      margin-right: 10px;
      margin-bottom: 10px;
      text-align: center;
      vertical-align: middle;
      color: #fff;
      background-color: #5cb85c;
      border-color: #4cae4c;
      padding: 6px 12px;
      font-size: 16px;
      font-weight: 600;
      line-height: 1.42857143;
      white-space: nowrap;
      cursor: pointer;
    }
  }
  input {
    margin-bottom: 10px;
  }
}

.btnBox {
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
  .editBtn {
    width: 50px;
    height: 35px;
    background-color: rgb(92, 184, 92);
    border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
  }
  .cancelBtn {
    width: 50px;
    height: 35px;
    background-color: #eee;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    color: black;
  }
  a:visited {
    color: black;
  }
}

#inspire {
  margin-left: 50px;

  .v-application--wrap {
    min-height: unset;
  }
}
.daumAddress {
  background-color: white;
  position: fixed;
  display: flex;
  top: 30%;
  left: 55%;
  z-index: 10;
  border: 3px solid black;
  .appCancel {
    width: 30px;
    height: 25px;
    background-color: #eee;
    text-align: center;
    vertical-align: middle;
  }
}
.supervisorsBtn {
  margin-left: 20px;
  width: 40px;
  height: 33px;
  color: #fff;

  padding: 6px 12px;
  margin-bottom: 0;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.42857143;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 4px;
}
.plusBtn {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.minusBtn {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.xi-pen {
  color: red;
}
</style>;
