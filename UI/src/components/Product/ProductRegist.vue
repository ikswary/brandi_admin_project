<template>
  <div id="app">
    <div class="ProductRegist">
       <div class="page_content">
        <h3 class="page_title">상품등록 <small> 상품 정보 등록</small></h3>
        <div class="page_bar">
          <ul class="page_ul">
            <div class="h2 mb-0">
              <i class="xi-home-o" style="color: black;" />
            </div>
            <li>상품관리</li>
            >
            <li>상품 관리</li>
            >
            <li>상품 등록</li>
          </ul>
        </div>
        <div class="portlet">
          <div class="portlet-title">
            <div class="caption">
              <i class="xi-pen-o" style="color: black;" />
              <span> 기본정보 </span>
            </div>
          </div>

          <div class="row" style="border:1px solid gray">
            <div class="col-md-12">
              <table class="table-in-portlet" style="border:1px solid gray">
                <tbody>
                 <tr>
                   <td class="vertical-align-middle">
                        셀러선택 <span class="font-color-red">*</span>
                    </td>
                     <td style="width:300px">
                       <b-form-input
                        style="margim:20px 30px; width:250px; border:none"
                        v-model="text"
                        placeholder="셀러를 검색해주세요"
                        class="search_seller"
                        readonly
              />
                     </td>
                       <td>
              <v-app id="inspire" style="height:50px;">
                <v-row>
                  <v-dialog v-model="dialog" persistent max-width="500" >
                    <template v-slot:activator="{ on }">
                      <v-btn
                        color="green"
                        dark
                        v-on="on"
                        style="margin-left:30px;"
                        >셀러 검색</v-btn
                      >
                    </template>
                    <v-card>
                      <v-card-title class="headline">셀러 선택</v-card-title>
                    </v-card>
                    <v-card-text style='color:blue; background-color:white'>
                      상품을 등록할 셀러를 선택해주세요. (검색 10건)
                    </v-card-text>
                    <form
                      style="display:flex; justify-content:center; background-color: white;"
                    >
                      <v-card-text
                        style="background-color:white; width:150px; margin:auto"
                      >
                        <span> 셀러 검색 </span>
                      </v-card-text>
                   <v-card-text style="background-color:white">
                        <v-autocomplete
                          v-model="model"
                          :items="items"
                          :loading="isLoading"
                          :search-input.sync="search"
                          color="white"
                          hide-no-data
                          hide-selected
                          item-text="Description"
                          item-value="API"
                          placeholder="Select"
                          prepend-icon="mdi-database-search"
                          return-object
                        ></v-autocomplete>
                      </v-card-text>
                    </form>
                    <v-card-actions style="background-color:white">
                      <v-spacer></v-spacer>
                      <v-btn color="outline-dark" text @click="dialog = false"
                        >닫기</v-btn
                      >
                      <b-button variant="primary" text @click="dialog = false"
                        >셀러 선택하기</b-button
                      >
                    </v-card-actions>
                  </v-dialog>
                </v-row>
              </v-app>
            </td>
                    </tr>
                  <tr>
                     <td class="vertical-align-middle" width="15%">
                        판매여부
                    </td>
                       <td style="width:400px">
                    <div class="radio-list">
                      <label class="radio-inline">
                         <div class="radio"><span class="checked"><input type="radio" name="sell" value="Y" checked="checked"></span></div>
                            판매
                       </label>
                      <label class="radio-inline">
                           <div class="radio"><span><input type="radio" name="sell" value="N"></span></div>
                            미판매
                       </label>
                          </div>
                            <span class="font-color-blue">
                            <i class="xi-caret-up"></i>  미판매 선택시 앱에서 Sold Out으로 표시됩니다.
                           </span>
                        </td>
                    </tr>

                     <tr>
                     <td class="vertical-align-middle" width="15%">
                        진열여부
                    </td>
                      <td style="width:400px">
                    <div class="radio-list">
                      <label class="radio-inline">
                         <div class="radio"><span class="checked"><input type="radio" name="display" value="Y" checked="checked"></span></div>
                            판매
                       </label>
                      <label class="radio-inline">
                           <div class="radio"><span><input type="radio" name="display" value="N"></span></div>
                            미판매
                       </label>
                          </div>
                            <span class="font-color-blue">
                            <i class="xi-caret-up"></i>  미판매 선택시 앱에서 Sold Out으로 표시됩니다.
                           </span>
                        </td>
                    </tr>

                    <tr>
                       <td style="width=5%">
                         카테고리 <span class="font-color-red">*</span>
                      </td>
                         <td>
                           <table class="table-category" />
                            <thead>
                               <tr>
                                  <th width=" 40%">1차 카테고리</th>
                                  <th width=" 40%">2차 카테고리</th>
                               </tr>
                                 </thead>
                          <tbody>
                             <tr>
                               <td>
                                  <input type="hidden" name="categoryNoArr" value="NOT_SELECTED">
                                     <select name="first_category" class="form-control resetable select-category" data-tier="1">
                                    <option value="NOT_SELECTED">1차 카테고리를 선택해주세요.</option>
                                        <option value="1">             아우터         </option>
                                        <option value="2">             상의         </option>
                                        <option value="3">             스커트         </option>
                                        <option value="4">             바지         </option>
                                        <option value="5">             원피스         </option>
                                        <option value="6">             신발         </option>
                                        <option value="7">             가방         </option>
                                        <option value="8">             잡화         </option>
                                        <option value="9">             주얼리         </option>
                                        <option value="10">             라이프웨어         </option>
                                         <option value="11">             빅사이즈         </option>
                                         </select>
                                         </td>
                                          <td>
                                            <select name="second_category" class="form-control resetable select-category" data-tier="2">

                                    <option value="NOT_SELECTED">1차 카테고리를 먼저 선택해 주세요.</option>
                                </select>
                                </td>
                                </tr>
                               </tbody>
                                     <span class="font-color-blue" >
                                     <i class="fa fa-warning"></i> 카테고리 변경 시 입력한 실측 사이즈 정보는 초기화 됩니다.</span>
                                </td>
                          </tr>
                </tbody>
              </table>
            </div>
          </div>
          <!-- <tr class="seller_tr">
            <td class="seller_choice">
              셀러선택
            </td>
            <td>
              <b-form-input
                style="margim:20px 30px;"
                v-model="text"
                placeholder="셀러를 검색해주세요"
                class="search_seller"
                readonly
              />
              <!-- <div class="mt-2">Value: {{ text }}</div> -->
            <!-- </td>
            <td>
              <v-app id="inspire">
                <v-row>
                  <v-dialog v-model="dialog" persistent max-width="500">
                    <template v-slot:activator="{ on }">
                      <v-btn
                        color="green"
                        dark
                        v-on="on"
                        style="margin-left:30px;"
                        >셀러 검색</v-btn
                      >
                    </template>
                    <v-card>
                      <v-card-title class="headline">셀러 선택</v-card-title>
                    </v-card>
                    <v-card-text style="color:blue; background-color:white">
                      상품을 등록할 셀러를 선택해주세요. (검색 10건)
                    </v-card-text>
                    <form
                      style="display:flex; justify-content:center; background-color: white;"
                    >
                      <v-card-text
                        style="background-color:white; width:150px; margin:auto"
                      >
                        <span> 셀러 검색 </span>
                      </v-card-text>
                      <v-card-text style="background-color:white">
                        <v-autocomplete
                          v-model="model"
                          :items="items"
                          :loading="isLoading"
                          :search-input.sync="search"
                          color="white"
                          hide-no-data
                          hide-selected
                          item-text="Description"
                          item-value="API"
                          placeholder="Select"
                          prepend-icon="mdi-database-search"
                          return-object
                        ></v-autocomplete>
                      </v-card-text>
                    </form>
                    <v-card-actions style="background-color:white">
                      <v-spacer></v-spacer>
                      <v-btn color="outline-dark" text @click="dialog = false"
                        >닫기</v-btn
                      >
                      <b-button variant="primary" text @click="dialog = false"
                        >셀러 선택하기</b-button
                      >
                    </v-card-actions>
                  </v-dialog>
                </v-row>
              </v-app>
            </td>
          </tr> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      text: '',
      dialog: false,
      message: 'Default Message',
    };
  },
};


</script>

<style lang="scss">
.ProductRegist {
  display: flex;
}
.page_content {
  width: 100%;
  height: 100%;
  background-color: white;
  margin-top: 20px;

  .page_title {
    background-color: #eee;
    border-radius: 4px 4px 0 0;
    padding: 10px 10px 2px 10px;
    height: 38px;
    small {
      font-size: 14px;
      letter-spacing: 0px;
      font-weight: 300;
      color: #888;
    }
  }
  .page_bar {
    border: 0;
    padding: 0px;
    background-color: #eee;
    margin-bottom: 25px;
    margin-left: -20px;
    margin-right: -20px;
    padding-left: 10px;
    padding-right: 20px;
  }
  .page_ul {
    display: flex;
    justify-content: flex-start;
    padding: 8px;
    margin: 0;
    list-style: none;
  }

  .portlet {
    clear: both;
    margin-top: 0px;
    margin-bottom: 25px;
    padding: 0px;
    -webkit-box-shadow1: 0 1px 4px rgba(0, 0, 0, 0.07);
    border: 1px solid #ddd;
    border-radius: 4px;
    .portlet-title {
      background-color: #eee;
      border-radius: 4px 4px 0 0;
      padding: 10px 10px 2px 10px;
      height: 38px;
    }

    .caption {
      color: #333;
      display: flex;
      justify-content: flex-start;
      font-size: 16px;
      line-height: 16px;
      font-weight: 400;
      margin: 0;
      padding: 0;
      margin-top: 1px;
    }
  }

  .row {
        margin-right: -15px;
        margin-left: -15px;
        .col-md-12 {
           width: 100%;
        }
        .table-in-portlet{
          border: 1px solid #888;
           width: 100%;
        }
        .vertical-align-middle{
              background-color: #f9f9f9;
            .font-color-red {
                  color: red !important;
            }
            input[type=button]{
              -webkit-appearance: button;
              cursor: pointer;
            }
        }

        .radio-list {
          display: flex;
          align-items: center;
          .radio-inline{
            margin-right: 15px;
          }
        }

        .font-color-blue{
          font-size: 13px;
          color: #1e90ff !important;
        }
        .font-color-red{
          color: red !important;

        }
        .table-category{
          zoom: 1;
          position: static;
          width:500px;
        }
  }

  // .seller_tr {
  //   height: 20px !important;
  // }
  // .seller_choice {
  //   height: 20px !important;
  //   margin: 0 10px;
  // }
  // .search_seller {
  //   cursor: not-allowed;
  //   background-color: #eeeeee;
  //   margin-left: 20px;
  // }
}
</style>
