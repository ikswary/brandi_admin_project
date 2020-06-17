<template>
  <div id="app">
    <div class="ProductRegist">
      <div class="page_content">
        <!-- 상품등록 테이블 -->
        <h3 class="page_title">
          상품등록
          <small>상품 정보 등록</small>
        </h3>
        <div class="page_bar">
          <ul class="page_ul">
            <div class="h2 mb-0">
              <i class="xi-home-o"  />
            </div>
            <li class="li-tag">상품관리 ></li>
            <li class="li-tag">상품 관리 ></li>
            <li class="li-tag">상품 등록</li>
          </ul>
        </div>
        <div class="portlet">
          <div class="portlet-title">
            <div class="caption">
              <i class="xi-pen-o" />
              <span>기본정보</span>
            </div>
          </div>

          <div class="row">
            <div class="col-md-12">
              <table class="table-in-portlet">
                <tbody>
                  <!-- 셀러선택 테이블 -->
                  <tr>
                    <td class="default-info-left td-border" width="15%">
                      셀러선택
                      <span class="font-color-red">*</span>
                    </td>
                    <td class="seller-search td-border">
                      <b-form-input                    
                        placeholder="셀러를 검색해주세요"
                        class="seller-search2"
                      />
                      <!-- 셀 러 검 색   모 달 창  시작하는곳 -->
                      <v-app id="inspire" >
                        <v-row>
                          <v-dialog v-model="dialog" persistent max-width="500">
                            <template v-slot:activator="{ on }">
                              <v-btn color="green" dark v-on="on" >셀러 검색</v-btn>
                            </template>
                            <v-card>
                              <v-card-title class="headline">셀러 선택</v-card-title>
                            </v-card>
                            <v-card-text class="modal-color"
                            >상품을 등록할 셀러를 선택해주세요. (검색 10건)</v-card-text>
                            <form class="modal-form"
                            >
                            <!-- 셀러 검색 인풋라인 -->
                              <v-card-text class="seller-search-input">
                                <span>셀러 검색</span>
                              </v-card-text>
                              <!-- 모달 내 셀러 검색 인풋태그 창 -->
                              <v-card-text>
                                <input type="text" v-model="seller_id" class="modal-input" />
                              </v-card-text>
                            </form>
                            <v-card-actions class="modal-color">
                              <v-spacer></v-spacer>
                              <v-btn color="outline-dark" text @click="dialog = false">닫기</v-btn>
                              <b-button variant="primary" text @click="dialog = false">셀러 선택하기</b-button>
                            </v-card-actions>
                          </v-dialog>
                        </v-row>
                      </v-app>
                    </td>
                  </tr>
                  <!-- 판매 여부-->
                  <tr>
                    <td class="sold-status default-info-left td-border">판매여부</td>
                    <td class="td-border" >

                    <div class="radio-list">
                        <label>
                          <div class="radio">
                            <button>
                              <input
                                v-model="on_sale"
                                type="radio"
                                value="1"
                                 v-on:click="thisisHidden = true"
                              />
                             판매
                            </button>
                          </div>
                        </label>

                        <label>
                          <button>
                            <input
                              type="radio"
                              v-model="on_sale"
                               value="0"
                              v-on:click="thisisHidden = !thisisHidden"
                            />
                            미판매
                          </button>
                        </label>
                      </div>
                   
                      <span class="font-color-blue style-filter-span" >
                        <i class="xi-caret-up"></i> 미판매 선택시 앱에서 Sold Out으로 표시됩니다.
                      </span>
                    </td>
                  </tr>
                  <!-- 진열 여부 -->
                  <tr>
                    <td class="display-status default-info-left">진열여부</td>
                    <td>
                      <div class="radio-list">
                        <label >
                          <div class="radio">
                            <span class="checked">
                              <input v-model="on_list" type="radio" value="1"  checked="checked" />
                            </span>
                          </div>판매
                        </label>
                        <label >
                          <div class="radio">
                            <span>
                              <input v-model="on_list" type="radio"  value="0" />
                            </span>
                          </div>미판매
                        </label>
                      </div>
                      <span class="font-color-blue style-filter-span">
                        <i class="xi-caret-up"></i> 미판매 선택시 앱에서 Sold Out으로 표시됩니다.
                      </span>
                    </td>
                  </tr>

                  <!-- 카테 고리 -->
                  <tr>
                    <td class="default-info-left">
                      카테고리
                      <span class="font-color-red">*</span>
                    </td>
                    <td>
                      <table class="table-category seller-search" />
                      <thead>
                        <tr>
                          <th width=" 40%">1차 카테고리</th>
                          <th width=" 40%">2차 카테고리</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>
                            <input
                              type="hidden"
                              name="categoryNoArr"
                              value="NOT_SELECTED"
                            />
                            <div>
                              <b-form-select
                                v-model="first_category_id"
                                :options="options"
                                size="sm"
                                class="mt-3"
                              ></b-form-select>
                            </div>
                          </td>
                          <td>
                                <b-form-select 
                                size="sm"
                                class="mt-3"
                                v-model="second_category_id" 
                                :options="secondOptions">
                                </b-form-select>
                          </td>
                        </tr>
                      </tbody>
                      <span class="font-color-blue style-filter-span">
                        <i class="xi-caret-up"></i> 카테고리 변경 시 입력한 실측 사이즈 정보는 초기화 됩니다.
                      </span>
                    </td>
                  </tr>
                  <!-- 상품 정보 고시 -->
                  <tr>
                    <td class="product-info-explain default-info-left">상품 정보 고시</td>
                    <td >
                      <div class="radio-list">
                        <label>
                          <div class="radio">
                            <button>
                              <input
                                type="radio"
                                name="information"
                                value="Y"
                                checked
                                v-on:click="isHidden = false"
                              />
                              상품 상세 참조
                            </button>
                          </div>
                        </label>

                        <label>
                          <button>
                            <input
                              type="radio"
                              name="information"
                              v-on:click="isHidden = !isHidden"
                            />
                            직접 입력
                          </button>
                        </label>
                      </div>
                      <div class="input-directly" v-if="isHidden">
                        <div>
                          제조사(수입사) :
                          <input v-model="manufacturer" type="text" class="company-name" />
                        </div>
                        <br />
                        <div class="manufacture-day">
                          <span>제조일자 :</span>
                          <span>
                            <b-form-datepicker id="example-datepicker" v-model="manufacture_date" class="mb-2"></b-form-datepicker>
                          </span>
                        </div>
                        <br />
                        <span>원산지 :</span>
                        <span>
                          <b-form-select v-model="manufacture_country_id" :options="conturys" size="sm" class="mt-3"></b-form-select>
                        </span>
                      </div>
                    </td>
                  </tr>
                  <!-- 상품명 테이블 -->
                  <tr>
                    <td class="product-name default-info-left">
                      상품명
                      <span class="font-color-red">*</span>
                    </td>
                    <td class="product-name">
                      <input
                        type="text"
                        name="product_name"
                        class="form-control"
                        v-model="name"
                        maxlength="200"
                      />
                         <span class="font-color-blue style-filter-span">
                          <i class="xi-caret-up"></i> 상품명에는 쌍따옴표(") 또는 홑따옴표(')를 포함할 수 없습니다.
                        </span>
                        <br>
                        <span class="font-color-blue style-filter-span">
                          <i class="xi-caret-up"></i> 상품명에는 4byte 이모지를 포함할 수 없습니다.
                        </span>
                      
                    </td>
                  </tr>
                  <!-- 한줄 상품 설명 테이블 -->
                  <tr>
                    <td class="oneline-explain default-info-left">
                      한줄 상품 설명
                      <span class="font-color-red">*</span>
                    </td>
                    <td class="oneline-explain">
                      <input v-model="description_short" type="text" class="form-control" />
                    </td>
                  </tr>
                  <!-- 이미지 등록 테이블 -->
                  <tr>
                    <td class="image-upload default-info-left">
                      이미지 등록
                      <span class="font-color-red">*</span>
                    </td>
                    <td class="image-upload" >
                      <div id="preview">
                        <img v-if="url" :src="url" />
                      </div>
                      <input type="file" @change="onFileChange" accept="image/*" multiple />
                      <div class="font-color-blue style-filter-span">
                        <i class="xi-caret-up"></i> 640 * 720 사이즈 이상 등록 가능하며 확장자는 jpg 만 등록 가능합니다.
                      </div>

                      <div id="image_container"></div>
                    </td>
                  </tr>

                  <!-- 색상필터(썸네일 이미지) -->
                  <tr>
                    <td class="default-info-left">
                      색상필터(썸네일 이미지)
                      <span class="font-color-red">*</span>
                    </td>
                    <td>
                      <div class="col-md-12">
                        <div class="radio-list">
                          <label>
                            <div class="radio">
                              <span class="checked">
                                <input type="radio" name="colorCode" class="ui-control" checked />
                              </span>
                            </div>사용안함
                          </label>
                          <label >
                            <div class="radio">
                              <span>
                                <input type="radio" name="colorCode" class="ui-control" />
                              </span>
                            </div>사용함
                          </label>
                          <div class="picker-box">
                            <input type="text" class="color-filter" />
                            <span class="color-box"></span>
                          </div>
                          <v-row justify="center">
                            <v-dialog v-model="colordialog" scrollable max-width="450px">
                              <template v-slot:activator="{ on }">
                                <v-btn color="primary" dark v-on="on">적용 할 색상 찾기</v-btn>
                              </template>
                              <v-card>
                                <!-- 색상 선택 modal  -->
                                <v-card-title>색상 선택</v-card-title>
                                <v-divider></v-divider>
                                <v-card-text style="width:100%; height: 300px;">
                                  <tr>
                                    <td>
                                      <img
                                        style="width:35px; height:35px; border-radius:20px;"
                                        src="https://dbscthumb-phinf.pstatic.net/2512_000_1/20130825213031822_DAT75UGRE.jpg/i-c-18.jpg?type=m4500_4500_fst_n&wm=Y"
                                      />
                                      <br />
                                      <span>빨강</span>
                                      <br />
                                      <span>(Red)</span>
                                    </td>
                                    <td>
                                      <img
                                        style="width:35px; height:35px; border-radius:20px;"
                                        src="https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F2512_000_1%2F20130825213048883_MOHWHB1G3.jpg%2Fi-c-30.jpg%3Ftype%3Dm4500_4500_fst_n%26wm%3DY%22&twidth=352&theight=80&opts=17"
                                      />
                                      <br />
                                      <span>주황</span>
                                      <br />
                                      <span>(Orange)</span>
                                    </td>
                                    <td>
                                      <img
                                        style="width:35px; height:35px; border-radius:20px;"
                                        src="https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F2512_000_1%2F20130825213141805_R5CXRESO9.jpg%2Fi-c-68.jpg%3Ftype%3Dm4500_4500_fst_n%26wm%3DY%22&twidth=354&theight=80&opts=17"
                                      />
                                      <br />
                                      <span>노랑</span>
                                      <br />
                                      <span>(Yellow)</span>
                                    </td>
                                    <td>
                                      <img
                                        style="width:35px; height:35px; border-radius:20px;"
                                        src="https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F2512_000_1%2F20190711160628123_BB7XII6S4.jpg%2Fi-c-55.jpg%3Ftype%3Dm4500_4500_fst_n%26wm%3DY%22&twidth=500&theight=62&opts=17"
                                      />
                                      <br />
                                      <span>베이지</span>
                                      <br />
                                      <span>(Beige)</span>
                                    </td>
                                    <td>
                                      <img
                                        style="width:35px; height:35px; border-radius:20px;"
                                        src="https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F2512_000_1%2F20130825213102693_IKNCISY3I.jpg%2Fi-c-38.jpg%3Ftype%3Dm4500_4500_fst_n%26wm%3DY%22&twidth=352&theight=83&opts=17"
                                      />
                                      <br />
                                      <span>갈색</span>
                                      <br />
                                      <span>(Brown)</span>
                                    </td>
                                  </tr>
                                  <tr>
                                    <button>
                                      <td>
                                        <img
                                          style="width:35px; height:35px; border-radius:20px;"
                                          src="https://dbscthumb-phinf.pstatic.net/2512_000_1/20130825213031822_DAT75UGRE.jpg/i-c-18.jpg?type=m4500_4500_fst_n&wm=Y"
                                        />
                                        <br />
                                        <span>빨강</span>
                                        <br />
                                        <span>(Red)</span>
                                      </td>
                                    </button>
                                    <td>
                                      <img
                                        style="width:35px; height:35px; border-radius:20px;"
                                        src="https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F2512_000_1%2F20130825213048883_MOHWHB1G3.jpg%2Fi-c-30.jpg%3Ftype%3Dm4500_4500_fst_n%26wm%3DY%22&twidth=352&theight=80&opts=17"
                                      />
                                      <br />
                                      <span>주황</span>
                                      <br />
                                      <span>(Orange)</span>
                                    </td>
                                    <td>
                                      <img
                                        style="width:35px; height:35px; border-radius:20px;"
                                        src="https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F2512_000_1%2F20130825213141805_R5CXRESO9.jpg%2Fi-c-68.jpg%3Ftype%3Dm4500_4500_fst_n%26wm%3DY%22&twidth=354&theight=80&opts=17"
                                      />
                                      <br />
                                      <span>노랑</span>
                                      <br />
                                      <span>(Yellow)</span>
                                    </td>
                                    <td>
                                      <img
                                        style="width:35px; height:35px; border-radius:20px;"
                                        src="https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F2512_000_1%2F20190711160628123_BB7XII6S4.jpg%2Fi-c-55.jpg%3Ftype%3Dm4500_4500_fst_n%26wm%3DY%22&twidth=500&theight=62&opts=17"
                                      />
                                      <br />
                                      <span>베이지</span>
                                      <br />
                                      <span>(Beige)</span>
                                    </td>
                                    <td>
                                      <img
                                        style="width:35px; height:35px; border-radius:20px;"
                                        src="https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F2512_000_1%2F20130825213102693_IKNCISY3I.jpg%2Fi-c-38.jpg%3Ftype%3Dm4500_4500_fst_n%26wm%3DY%22&twidth=352&theight=83&opts=17"
                                      />
                                      <br />
                                      <span>갈색</span>
                                      <br />
                                      <span>(Brown)</span>
                                    </td>
                                  </tr>
                                  <tr>
                                    <button>
                                      <td>
                                        <img
                                          style="width:35px; height:35px; border-radius:20px;"
                                          src="https://dbscthumb-phinf.pstatic.net/2512_000_1/20130825213031822_DAT75UGRE.jpg/i-c-18.jpg?type=m4500_4500_fst_n&wm=Y"
                                        />
                                        <br />
                                        <span>빨강</span>
                                        <br />
                                        <span>(Red)</span>
                                      </td>
                                    </button>
                                    <td>
                                      <img
                                        style="width:35px; height:35px; border-radius:20px;"
                                        src="https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F2512_000_1%2F20130825213048883_MOHWHB1G3.jpg%2Fi-c-30.jpg%3Ftype%3Dm4500_4500_fst_n%26wm%3DY%22&twidth=352&theight=80&opts=17"
                                      />
                                      <br />
                                      <span>주황</span>
                                      <br />
                                      <span>(Orange)</span>
                                    </td>
                                    <td>
                                      <img
                                        style="width:35px; height:35px; border-radius:20px;"
                                        src="https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F2512_000_1%2F20130825213141805_R5CXRESO9.jpg%2Fi-c-68.jpg%3Ftype%3Dm4500_4500_fst_n%26wm%3DY%22&twidth=354&theight=80&opts=17"
                                      />
                                      <br />
                                      <span>노랑</span>
                                      <br />
                                      <span>(Yellow)</span>
                                    </td>
                                    <td>
                                      <img
                                        style="width:35px; height:35px; border-radius:20px;"
                                        src="https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F2512_000_1%2F20190711160628123_BB7XII6S4.jpg%2Fi-c-55.jpg%3Ftype%3Dm4500_4500_fst_n%26wm%3DY%22&twidth=500&theight=62&opts=17"
                                      />
                                      <br />
                                      <span>베이지</span>
                                      <br />
                                      <span>(Beige)</span>
                                    </td>
                                    <td>
                                      <img
                                        style="width:35px; height:35px; border-radius:20px;"
                                        src="https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F2512_000_1%2F20130825213102693_IKNCISY3I.jpg%2Fi-c-38.jpg%3Ftype%3Dm4500_4500_fst_n%26wm%3DY%22&twidth=352&theight=83&opts=17"
                                      />
                                      <br />
                                      <span>갈색</span>
                                      <br />
                                      <span>(Brown)</span>
                                    </td>
                                  </tr>
                                  <tr>
                                    <button>
                                      <td>
                                        <img
                                          style="width:35px; height:35px; border-radius:20px;"
                                          src="https://dbscthumb-phinf.pstatic.net/2512_000_1/20130825213031822_DAT75UGRE.jpg/i-c-18.jpg?type=m4500_4500_fst_n&wm=Y"
                                        />
                                        <br />
                                        <span>빨강</span>
                                        <br />
                                        <span>(Red)</span>
                                      </td>
                                    </button>
                                    <td>
                                      <img
                                        style="width:35px; height:35px; border-radius:20px;"
                                        src="https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F2512_000_1%2F20130825213048883_MOHWHB1G3.jpg%2Fi-c-30.jpg%3Ftype%3Dm4500_4500_fst_n%26wm%3DY%22&twidth=352&theight=80&opts=17"
                                      />
                                      <br />
                                      <span>주황</span>
                                      <br />
                                      <span>(Orange)</span>
                                    </td>
                                    <td>
                                      <img
                                        style="width:35px; height:35px; border-radius:20px;"
                                        src="https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F2512_000_1%2F20130825213141805_R5CXRESO9.jpg%2Fi-c-68.jpg%3Ftype%3Dm4500_4500_fst_n%26wm%3DY%22&twidth=354&theight=80&opts=17"
                                      />
                                      <br />
                                      <span>노랑</span>
                                      <br />
                                      <span>(Yellow)</span>
                                    </td>
                                  </tr>
                                </v-card-text>
                                <v-divider></v-divider>
                                <v-card-actions>
                                  <v-btn class="apply-button">적용</v-btn>
                                  <v-btn color="blue darken-1" text @click="colordialog = false">취소</v-btn>
                                </v-card-actions>
                              </v-card>
                            </v-dialog>
                          </v-row>
                        </div>
                        <br />
                        <span class="font-color-blue">
                          <i class="xi-caret-up"></i> 베스트 탭, 카테고리 페이지 및 검색페이지의 필터에 적용되며, 선택하지 않으실 경우 색상필터를 사용한 검색결과에 노출되지 않습니다.
                          <br />
                        </span>
                        <span class="font-color-blue">
                          <i class="xi-caret-up"></i> 썸네일 이미지의 1개 색상만 선택 가능하며, 뷰티 및 다이어트 카테고리의 상품의 경우 선택하실 수 없습니다.
                        </span>
                      </div>
                    </td>
                  </tr>

                  <!-- 스타일필터 -->

                  <tr>
                    <td class="style-filter default-info-left">
                      스타일필터
                      <span class="font-color-red">*</span>
                    </td>
                    <div class="style-filter-label">
                      <label>
                        <div class="radio">
                          <span class="checked">
                            <input
                              type="radio"
                              name="styleCode"
                              class="ui-control"
                              disabled="disabled"
                              checked
                            />
                          </span>
                        </div>선택안함
                      </label>
                      <label>
                        <div class="radio">
                          <span class="checked">
                            <input
                              type="radio"
                              name="styleCode"
                              class="ui-control"
                              disabled="disabled"
                            />
                          </span>
                        </div>심플베이직
                      </label>
                      <label >
                        <div class="radio">
                          <span class="checked">
                            <input
                              type="radio"
                              name="styleCode"
                              class="ui-control"
                              disabled="disabled"
                            />
                          </span>
                        </div>러블리
                      </label>
                      <label >
                        <div class="radio">
                          <span class="checked">
                            <input
                              type="radio"
                              name="styleCode"
                              class="ui-control"
                              disabled="disabled"
                            />
                          </span>
                        </div>페미닌
                      </label>
                      <label >
                        <div class="radio">
                          <span class="checked">
                            <input
                              type="radio"
                              name="styleCode"
                              class="ui-control"
                              disabled="disabled"
                            />
                          </span>
                        </div>캐주얼
                      </label>
                      <label >
                        <div class="radio">
                          <span class="checked">
                            <input
                              type="radio"
                              name="styleCode"
                              class="ui-control"
                              disabled="disabled"
                            />
                          </span>
                        </div>섹시글램
                      </label>
                    </div>
                    <span class="font-color-blue style-filter-span" >
                      <i class="xi-caret-up"></i> 베스트 탭, 카테고리 페이지 및 검색페이지의 필터에 적용되며, 선택하지 않으실 경우 색상필터를 사용한 검색결과에 노출되지 않습니다.
                    </span>
                      <br />
                        <span class="font-color-blue style-filter-span" >
                      <i class="xi-caret-up"></i> 1개 스타일만 선택 가능하며, 브랜드 및 뷰티&다이어트 카테고리 상품의 경우 선택하실 수 없습니다.
                    </span>
                  </tr>
                  <!-- 연령 필터 테이블 -->
                  <tr>
                    <td class="default-info-left">
                      연령필터
                      <span class="font-color-red">*</span>
                    </td>
                    <td>
                      <div class="col-md-12">
                        <button type="button" class="age-filter">--연령필터 데이터받을곳--</button>
                        <br />
                        <span class="font-color-blue">
                          <i class="xi-caret-up"></i> 베스트 탭, 카테고리 페이지 및 검색페이지의 필터에 적용되며, 셀러 정보 셀러태그정보의 연령대가 자동으로 적용됩니다.
                          <br />
                          <i class="xi-caret-up"></i> 브랜드 및 뷰티 다이어트 카테고리 상품의 경우 적용되지 않습니다.
                          <br />
                          <i class="xi-caret-up"></i> 해당 정보는 상품단위로 적용이 불가능하며(셀러 단위로만 가능), 수정을 원하실 경우 카카오 플러스친구 '브랜디셀러'로 연락 부탁드립니다.
                        </span>
                      </div>
                    </td>
                  </tr>
                  <!-- 상세 상품정보 테이블 -->
                  <tr>
                    <td class="default-info-left">
                      상세 상품정보
                      <span class="font-color-red">*</span>
                    </td>
                    <ckeditor
                      :editor="editor"
                      v-model="description_detail"
                      :config="editorConfig"
                      class="ckeditor"
                    ></ckeditor>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- 옵션정보 옵션 테이블 -->
          <div class="container">
            <div class="box">
              <div id="app">
                <div class="ProductRegist">
                  <div class="page_content">
                    <div class="portlet">
                      <div class="portlet-title">
                        <div class="caption">
                          <i class="xi-pen-o"></i>
                          <span>옵션정보</span>
                        </div>
                      </div>
                      <div
                        class="row"
                      >
                        <div class="col-md-12">
                          <table
                            class="table-in-portlet"
                          >
                            <tbody>
                              <tr>
                                <td width="15%" class="seller-choice default-info-left">
                                  옵션 설정
                                  <span class="font-color-red">*</span>
                                </td>
                                <td >
                                  <div class="radio-list">
                                    <label >
                                      <div class="radio">
                                        <span class="checked">
                                          <input type="radio" name="sell" value="Y" />
                                        </span>
                                      </div>기본 옵션
                                    </label>
                                  </div>
                                </td>
                              </tr>
                              <tr>
                                <td width="15%" class="seller-choice default-info-left">옵션 정보</td>
                                <td colspan="3">
                                  <div class="basic-option-wrap">
                                    <table class="table table-bordered">
                                      <thead>
                                        <tr class="heading">
                                          <th>옵션항목</th>
                                          <th>상품옵션명</th>
                                          <th>옵션값 추가/삭제</th>
                                          
                                        </tr>
                                      </thead>
                                      <tbody>
                                        <tr class="option-group-1">
                                          <td width="15%" rowspan="1">색상</td>
                                          <td>
                                                <b-form-select v-model="color_id" :options="optionColor" size="sm" class="mt-1"></b-form-select>

                                          </td>

                                          <td width="15%">
                                            <div class="text-center">
                                              <v-btn class="mx-2" fab dark small color="indigo">
                                                <v-icon dark>mdi-plus</v-icon>
                                              </v-btn>
                                              <v-btn class="mx-2" fab dark small color="primary">
                                                <v-icon dark>mdi-minus</v-icon>
                                              </v-btn>
                                            </div>
                                          </td>
                                        </tr>
                                        <tr class="option-group-2">
                                          <td width="15%" rowspan="1">사이즈</td>
                                          <td>
                                            <b-form-select v-model="size_id" :options="optionSize" size="sm" class="mt-1"></b-form-select>

                                          </td>

                                          <td width="15%">
                                            <div class="text-center">
                                              <v-btn class="mx-2" fab dark small color="indigo">
                                                <v-icon dark>mdi-plus</v-icon>
                                              </v-btn>
                                              <v-btn class="mx-2" fab dark small color="primary">
                                                <v-icon dark>mdi-minus</v-icon>
                                              </v-btn>
                                            </div>
                                          </td>
                                        </tr>
                                      </tbody>
                                      <tfoot>
                                        <tr class="heading">
                                          <td class="vertical-align-middle">재고관리여부</td>
                                          <td colspan="6" class="vertical-align-middle">
                                            <div class="stock-div">
                                              <label>
                                                <div class="radio">
                                                  <span class="checked">
                                                    <input
                                                    v-model="stock"
                                                    value="1"
                                                      type="radio"
                                                    />
                                                  </span>
                                                </div>재고 수량 관리 안함
                                              </label>
                                              <label class="stock-amount">
                                                <div class="radio">
                                                  <span>
                                                    <input 
                                                      v-model="stock"
                                                    value="0" 
                                                    type="radio" />
                                                  </span>
                                                </div>재고 수량 관리
                                              </label>
                                            </div>
                                          </td>
                                        </tr>
                                      </tfoot>
                                    </table>

                                    <v-btn class="apply-button"  v-on="on">적용</v-btn>

                                    <table class="table table-bordered">
                                   <tr>
                                      <td class="product-option-info"> 상품 옵션정보</td>
                                         <td class="product-option-info" rowspan="2"> 일반재고 </td>
                                     </tr>

                                     <tr>
                                      <td class="product-option-info"> 색상 / 사이즈 </td>
                                     </tr>
                                      <tbody>
                                        <tr>
                                          <td colspan="11">
                                            <label>옵션정보를 입력 후 [적용] 버튼을 눌러주세요.</label>
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>

                                    <div class="font-color-blue">
                                      <i class="xi-caret-up"></i>
                                      도매처옵션명 조합은 최대 100자까지 표시됩니다.
                                      <br />
                                    </div>
                                  </div>
                                </td>
                                <span class="font-color-blue"></span>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- 판매정보 옵션 테이블 -->
          <div class="container">
            <div class="box">
              <div id="app">
                <div class="ProductRegist">
                  <div class="page_content">
                    <div class="portlet">
                      <div class="portlet-title">
                        <div class="caption">
                          <i class="xi-pen-o"></i>
                          <span>판매정보</span>
                        </div>
                      </div>
                      <div class="row sell-info">
                        <div class="col-md-12">
                          <table class="table-in-portlet sell-info">
                            <tbody>
                              <tr>
                                <td
                                  width="15%"
                                  height="50px"
                                  class="seller-choice default-info-left "
                                >도매원가</td>
                                <td class="td-wholesale">
                                  <div class="input-group">
                                    <input
                                      class="wholesale seller-info-input"
                                      type="text"
                                      maxlength="8"
                                      placeholder="0"
                                    />
                                  </div>
                                  <span class="input-group-addon">원</span>
                                </td>
                              </tr>
                              <tr>
                                <td
                                  width="15%"
                                  height="50px"
                                  class="seller-choice default-info-left"
                                >
                                  판매가
                                  <span class="font-color-red">*</span>
                                </td>
                                <td class="td-wholesale">
                                  <div class="input-group">
                                    <input
                                      v-model="price"
                                      class="wholesale seller-info-input"
                                      type="text"
                                      maxlength="8"
                                      placeholder="0"
                                    />
                                  </div>
                                  <span class="input-group-addon">원</span>
                                    <span class="font-color-blue">
                                  <i class="xi-caret-up"></i>
                                  판매가는 원화기준 10원 이상이며 가격 입력 시 10원 단위로 입력해 주세요.
                                </span>
                                </td>
                              
                              </tr>
                              <tr>
                                <td
                                  width="15%"
                                  height="50px"
                                  class="seller-choice default-info-left"
                                >
                                  할인정보
                                  <span class="font-color-red">*</span>
                                </td>
                                <td colspan="3">
                                  <div class="col-md-6">
                                    <table>
                                      <tbody>
                                        <tr >
                                          <td >할인율</td>
                                          <td >할인가</td>
                                        </tr>
                                        <tr >
                                          <td class=" td-background">
                                            <div class="discount-rate">
                                              <input
                                              v-model="discount_rate"
                                                placeholder="0"
                                                class="discount-input"
                                                type="text"
                                              />
                                              <span class="discount-persent">%</span>
                                            </div>
                                          </td>
                                          <td class=" td-background">
                                            <div>
                                              <input
                                              v-model="discount_price"
                                                class="discount-input"
                                                type="text"
                                                placeholder="0"
                                                />원
                                              <button class="discount-button" type="button">할인판매가적용</button>
                                            </div>
                                          </td>
                                        </tr>

                                     
                                        <tr >
                                          <td class=" td-background">
                                           할인판매가
                                          </td>
                                          <td class=" td-background">
                                            <div>
                                              <input
                                              v-model="discount_price"
                                                class="discount-input"
                                                type="text"
                                                placeholder="0"
                                                />원
                                              
                                            </div>
                                          </td>
                                        </tr>
                                        <tr>
                                          <td>할인기간</td>
                                          <td class="product_info">
                                            <div class="radio-list">
                                              <label>
                                                <div class="radio">
                                                  <button>
                                                    <input
                                                      type="radio"
                                                      name="informationNo2"
                                                      value="Y"
                                                      checked="checked"
                                                      v-on:click="thatisHidden = false"
                                                    />
                                                    무기한
                                                  </button>
                                                </div>
                                              </label>

                                              <label>
                                                <button>
                                                  <input
                                                    type="radio"
                                                    name="informationNo2"
                                                    v-on:click="thatisHidden = true"
                                                  />
                                                  기간설정
                                                </button>
                                              </label>
                                            </div>
                                            <div class="input-directly" v-if="thatisHidden">
                                              <span>
                                                 <div>
                                                  <label for="datepicker-invalid"> 시작일 </label>
                                                  <b-form-datepicker v-model="discount_start" id="datepicker-invalid" :state="false" class="mb-2"></b-form-datepicker>
                                                  <label for="datepicker-valid"> 종료일 </label>
                                                  <b-form-datepicker v-model="discount_end" id="datepicker-valid" :state="true"></b-form-datepicker>
                                                </div>
                                              </span>
                                              <br>
                                              <span class="font-color-red">
                                                   * 할인기간을 설정시 기간만료되면 자동으로 정상가로 변경 됩니다. <br>
                                                </span>
                                            </div>
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
                                    <span class="font-color-blue">
                                      <i class="xi-caret-up"></i> 할인판매가 = 판매가 * 할인율
                                      <br />
                                      <i class="xi-caret-up"></i> 할인 판매가 적용 버튼을 클릭 하시면 판매가 정보가 자동 계산되어집니다.
                                      <br />
                                      <i class="xi-caret-up"></i> 할인 판매가는 원화기준 10원 단위로 자동 절사됩니다.
                                    </span>
                                  </div>
                                </td>
                              </tr>

                              <tr class="tr-wholesale default-info-left">
                                <td
                                  width="15%"
                                  class="seller-choice default-info-left"
                                >
                                  최소판매수량
                                  <span class="font-color-red">*</span>
                                </td>
                                <td>
                                  <div class="radio-list">
                                    <label>
                                      <div class="radio">
                                        <span class="checked">
                                          <input v-model="min_sales_unit" value ="1" type="radio"/>
                                        </span>
                                      </div>상
                                    </label>
                                    <label>
                                      <div class="radio">
                                        <span>
                                          <input class type="radio" disabled />
                                        </span>
                                      </div>
                                    </label>
                                    <input type="text" class="minimum-amount" /> 개 이상
                                    <span class="font-color-blue">(20개를 초과하여 설정하실 수 없습니다)</span>
                                  </div>
                                </td>
                              </tr>
                              <tr class="tr-wholesale default-info-left">
                                <td
                                  width="15%"
                                  height="50px"
                                  class="seller-choice default-info-left"
                                >
                                  최대판매수량
                                  <span class="font-color-red">*</span>
                                </td>
                                <td>
                                  <div class="radio-list">
                                    <label>
                                      <div class="radio">
                                        <span class="checked">
                                          <input v-model="max_sales_unit" value="20" type="radio"  />
                                        </span>
                                      </div>20개
                                    </label>
                                    <label>
                                      <div class="radio">
                                        <span>
                                          <input class type="radio"  />
                                        </span>
                                      </div>
                                    </label>
                                    <input type="text" v-model="max_sales_unit" value="0" /> 개 이상
                                    <span class="font-color-blue">(20개를 초과하여 설정하실 수 없습니다)</span>
                                  </div>
                                </td>
                              </tr>
                              <tr class="tr-wholesale default-info-left">
                                <td
                                  class="seller-choice default-info-left"
                                >
                                  상품 태그 관리
                                  <span class="font-color-red">*</span>
                                </td>
                                <td>
                                  <b-form-tags
                                    input-id="tags-separators"
                                    v-model="tag"
                                    separator=" ,;"
                                    placeholder="입력해 주세요"
                                    class="mb-2"
                                  ></b-form-tags>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- 등록 취소 버튼 -->
          <v-col class="text-center">
            <div class="my-2">
              <v-btn class="enroll-button" @click="postProduct()">등록</v-btn>
            </div>
            <div class="my-2">
              <v-btn class="cancle-button">취소</v-btn>
            </div>
          </v-col>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { JH_URL } from "../../config/urlConfig";
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import Datepicker from 'vuejs-datepicker';

export default {
  el: `#app`,
  components: {},
  data() {
    return {      
      text: '',
      colordialog: false,
      dialog: false,
      message: 'Default Message',
      isHidden: false,
      thatisHidden: false,
      thisisHidden : false,
      key: '',
      selected: null,
      // ----------상품등록 post 데이터----------------
      seller_id: "",      
      on_sale: "1",
      on_list: "1",
      first_category_id: "",
      second_category_id: "",
      manufacturer: "",
      manufacture_date: "",
      manufacture_country_id: "",
      name: "",
      description_short: "",
      description_detail:"",
      option: [
        {
          color_id: "",
          size_id: "",
          stock: "",
        },
      ],
      price: "",
      discount_rate: null,
      discount_price: null,
      discount_start: null,
      discount_end: null,
      min_sales_unit : "1",
      max_sales_unit : "20",
      tag : [],
      options: [
        { value: null, text: '1차 카테고리를 선택해주세요' },
        { value: '아우터', text: '아우터' },
        { value: '상의', text: '상의' },
        { value: '스커트', text: '스커트' },
        { value: '바지', text: '바지' },
        { value: '원피스', text: '원피스' },
        { value: '신발', text: '신발' },
        { value: '가방', text: '가방' },
        { value: '잡화', text: '잡화' },
        { value: '주얼리', text: '주얼리' },
        { value: '라이프웨어', text: '라이프웨어' },
        { value: '빅사이즈', text: '빅사이즈' },
      ],
        secondOptions: [
        { value: null, text: '2차 카테고리를 선택해주세요' },
        { value: '자켓', text: '자켓' },
        { value: '가디건', text: '가디건' },
        { value: '코트', text: '코트' },
        { value: '점퍼', text: '점퍼' },
        { value: '패딩', text: '패딩' },
        { value: '무스탕/퍼', text: '무스탕/퍼' },
        { value: '기타', text: '기타' },
      
      ],
      conturys: [
          { value: null, text: '국가를 선택해 주세요' },
          { value: '대한민국', text: '대한민국' },
          { value: '베트남', text: '베트남' },
          { value: '중국', text: '중국' },
          { value: '기타', text: '기타' },
        ]
      ,
        optionColor: [
          { value: null, text: '색상을 선택해 주세요' },
          { value: '검정', text: '검정' },
          { value: '초록', text: '초록' },
          { value: '노랑', text: '노랑' },
          { value: '기타', text: '기타' },
        ],
          optionSize: [
          { value: null, text: '사이즈을 선택해 주세요' },
          { value: 's', text: 's' },
          { value: 'm', text: 'm' },
          { value: 'l', text: 'l' },
          { value: '기타', text: '기타' },
        ],
      url: null,
      editor: ClassicEditor,
      editorConfig: {
      },
      date: null,
      date1: null,
      dateFormatted: null,
      value: [] ,
      // color_filter_id: "",
      // style_filter_id: "",
     };
  },
  computed: {
    computedDateFormatted() {
      return this.formatDate(this.date);
    },
      
  },
  watch: {
    date(val) {
      this.dateFormatted = this.formatDate(this.date);
    },
  },
  methods: {
    onChange(event) {
      console.log(event.target.value);
    },
    onFileChange(e) {
      const file = e.target.files[0];
      this.url = URL.createObjectURL(file);
    },
    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split('-');
      return `${month}/${day}/${year}`;
    },
    parseDate(date) {
      if (!date) return null;

      const [month, day, year] = date.split('/');
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`;
    },
    // 상품 등록 post 보내는 함수
    postProduct: function() {
      if (confirm('상품을 등록 하시겠습니까?') == true) {
        axios
          .post(`${JH_URL}/product`, {
            seller_id: this.seller_id,
            on_sale: this.on_sale,
            on_list: this.on_list,
            first_category_id: this.first_category_id,
            second_category_id: this.second_category_id,
            manufacturer: this.manufacturer,
            manufacture_date: this.manufacture_date,
            manufacture_country_id: this.manufacture_country_id,
            name: this.name,
            description_short: this.description_short,
            // color_filter_id: this.color_filter_id,
            // style_filter_id: this.style_filter_id,
            // images: [
            //   {
            //     url: 'url',
            //   },
            // ],
            description_detail: this.description_detail,
            option: [
              {
                color_id: this.color_id,
                size_id: this.size_id,
                stock: this.stock,
              },
            ],
            price: this.price,
            discount_rate: this.discount_rate,
            discount_price: this.discount_price,
            discount_start: this.discount_start,
            discount_end: this.discount_end,
            min_sales_unit  :this.min_sales_unit,
            max_sales_unit : this.max_sales_unit,
            tag : this.tag,
          },
          {
            headers: {
              Authorization: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlX2lkIjoyLCJ1c2VyX2lkIjoxMCwiZXhwIjoxNTkxOTAxMzI3fQ.vmFzC4RWoBZhSCn58i5C4UUc8gFb5gP2l1L9O1L8LVs"
              }
          })
          .then(res => {
            if (res.status === 200) {
              alert('상품이 정상적으로 등록되었습니다.');
            }
          })
          .catch(error => console.log("err", error.response.data))
      }
    },
  
  },
};
</script>
<style lang="scss" scoped>
.ProductRegist {
  
   tr th{
    // border : 1px solid #ddd;
    text-align: center;
   }
   td {
     padding : 10px;
     border:  0.3px solid #ddd;
     background-color: white;

    }
    .td-border {
      // border:  0.3px solid #ddd;
    }

  .page_content {
    width: 100%;
    height: 100%;
    background-color: white;
    margin-top: 20px;

    .page_title {
      background-color: #eee;
      padding: 10px 10px 2px 10px;
      font-size: 20px;
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
     

      .portlet-title {
        background-color: #eee;
        border-radius: 4px 4px 0 0;
        padding: 10px 10px 2px 10px;
        height: 50px;
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

  .modal-color{
    background-color: white;
    color : red;
  }

  .modal-form {
    display: flex;
    justify-content:center; 
    background-color: white;

  }
    
 
    label {
      display: flex;
      margin: 10px;
    }
    .seller-search {
      display: flex;
    
       
    .seller-search-input{
    background-color:white; 
    width:150px; 
    margin:auto;
    }

      .seller-search2 {
       cursor: not-allowed;
       background-color: #eeeeee;
       width:250px; 
       border:none;

     }
    }

   
    .row {
      margin-right: -15px;
      margin-left: -15px;

  
      .table-in-portlet {
        width: 100%;
      }
      .align-middle {
        background-color: #f9f9f9;
        .font-color-red {
          color: red !important;
        }
        input[type='button'] {
          -webkit-appearance: button;
          cursor: pointer;
        }
      }

      .radio-list {
        display: flex;
        align-items: center;
      
      }

      .font-color-blue {
        font-size: 13px;
        color: #1e90ff !important;
        margin-top: 5px;
      }
      .font-color-red {
        color: red !important;
      }
      .table-category {
        zoom: 1;
        position: static;
        width: 500px;
        background-color: #f9f9f9;
      }
      .radio {
        display: flex;
      }
      .input-directly {
        height: 300px;
      }
      .manufacture-day {
        display: flex;
        justify-content: flex-start;
        align-items: center;
      }
      
      .company-name {
        margin-top: 10px;
        background-color: white;
        border: 1px solid #888;
        width: 400px;
        background-color: white;
        border: 1px solid #888;
      }
      .origin {
        width: 400px;
      }
      .form-selectd {
        border: 1px solid #888;
        background-color: white;
        width: 300px;
      }
      .form-control {
        border: 1px solid #888;
      }
      .color-filter {
        // border: 1px solid #ddd;
        width: 200px;
      }
      .one-line {
        width: 100%;
        background-color: white;
        border: 1px solid #888;
      }
      #preview {
        display: flex;
        justify-content: center;
        align-items: center;
      }

      #preview img {
        max-width: 100%;
        max-height: 500px;
      }

      .picker-box {
        margin-right: 30px;
      }
    }
    .li-tag {
      margin-top: 15px;
    }
    .age-filter {
      background-color: white;
      width: 200px;
      height: 12px;
      border-radius: 15px;
    }
    .ckeditor {
      display: block;
      // border: 1px solid #ddd;
      border-radius: 4px;
      padding: 0 3px;
      background: #eee;
    }
    .vertical-align-middle {
      height: unset;
      background-color: #eee !important;
    }
    .bd-top {
      font-size: 14px;
      font-weight: 600;
      background-color: #eee !important;
    }

    .style-filter-label {
      display: flex;
      justify-content: flex-start;
    }

    .default-info-left {
      background-color: #eee;
      text-align: center;
    }

    .td-wholesale {
      display: flex;
    }

    .tr-wholesale {
      border: 1px solid rgb(221, 221, 221);
    }

    .input-group {
      width: 240px !important;
      background-color: white;
      border-radius: 10px;     
      margin-left : 10px 
    }

    .wholesale {
      position: relative;
      z-index: 2;
      float: left;
      width: 100%;
      margin-left: 10px;
    }

    .input-group-addon {
      margin-left: 10px;
      border-color: #e5e5e5;
      min-width: 39px;
      margin-top: 10px;
    }

    .seller-info-input {
      border: 1px solid #eee;
    }

    .td-background {
      background-color: white;
    }

    .discount-label {
      width: 120px;
    }
    .discount-div {
      background-color: #f9f9f9;
    }

    .discount-persent {
      background-color: #e5e5e5;
      }

    .discount-button {
      color: #fff;
      background-color: #3071a9;
      border-color: #285e8e;
      border-radius: 10px;
      width: 124px;
      height: 34px;
      margin: 15px;
    }

    .discount-input {
      width: 100px;
      margin-left: 10px;
       border: 1px solid #ddd;
    }

    .discount-rate {
      display: flex;
    
     
    }

    .minimum-amount {
      cursor: not-allowed;
      background-color: #eeeeee;
      width: 100px;
      height: 34px;
    }
    .stock-div{
      display: flex;
    }
    .stock-amount {
      margin-left: 20px;
    }

    .text-center {
      display: flex;
      justify-content: center;
    }
    

     .inspire {
       height : 50px;
     }
    .modal-input{
      border: 1px solid red;
    }

    .enroll-button {
      background-color: #5cb85c !important;
      color : white
    }
    .cancle-button {
      margin-left: 5px;
      background-color: #d9534f !important;
      color: white;
    }

    .apply-button{
      background-color: #5bc0de !important;
      color : white;
      margin-bottom: 10px;
    }

    .product-option-info{
      text-align: center;
    }

    .style-filter-span {
      margin-left: 20px;
    }
    // .seller_tr {
    //   height: 20px !important;
    // }
    // .seller_choice {
    //   height: 20px !important;
    //   margin: 0 10px;
    // }
    
  }
}
</style>