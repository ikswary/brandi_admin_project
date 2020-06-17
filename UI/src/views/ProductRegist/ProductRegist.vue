<template>
  <div class="prWrap">
    <div v-if="colorModal" class="wrap"></div>
    <div v-if="sellersModal" class="wrap"></div>
    <div class="slTitleBox">
      <div class="slTitle">상품 등록</div>
      <div class="slSubTitle">상품 정보 등록</div>
    </div>
    <div class="slCategory">
      <i class="xi-home">
        상품 관리
        <i class="xi-angle-right-min">상품 관리</i>
        <i class="xi-angle-right-min">상품 등록</i>
      </i>
    </div>
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">기본 정보</i>
      </div>
      <div class="cmpTable">
        <!-- 셀러검색모달 -->
        <div v-if="sellersModal === true" class="sellersModal">
          <div class="slTitleBox">
            <div class="slTitle">셀러 선택</div>
            <div class="titleLine"></div>
            <i class="xi-info">상품을 등록할 셀러를 선택해주세요. (검색 10건)</i>
            <div class="inputBox">
              <div class="text">셀러검색</div>
              <div>
                <div @click="sellersInputModal = !sellersInputModal" class="inputSelect">
                  {{sellerInfo.name? sellerInfo.name: "Select..."}}
                  <input
                    v-if="sellersInputModal === true"
                    type="text"
                    @input="searchSellerList($event.target.value)"
                    @click="$event.stopPropagation()"
                  />
                  <div v-if="sellersInputModal === true" class="searchResult">
                    <div v-for="seller in sellerList" :key="seller.id">
                      <div
                        class="sellerlist"
                        @click="selectSeller(seller.id, seller.name)"
                      >{{searchSeller.length ? seller.name : ""}}</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="titleLine02"></div>
            <div class="sellersBtn">
              <div class="cancel" @click="sellersModal = !sellersModal">닫기</div>
              <div class="selected" @click="sellersModal = !sellersModal">셀러 선택하기</div>
            </div>
          </div>
        </div>
        <!-- 컬러필터모달 -->
        <div v-if="colorModal === 1" class="colorModal">
          <div class="slTitle">색상 선택</div>
          <div class="titleLine"></div>
          <div class="colorBox" v-for="color in colors" :key="color.id">
            <div @click="selectColor(color.id, color.image, color.name)">
              <img :src="color.image_url" />
              <div v-model="productDatas.color_filter_id">{{color.name}}</div>
              <div>({{color.name_eng}})</div>

              <div
                v-if="productDatas.color_filter_id === color.id && color.id != 13 || productDatas.color_filter_id === color.id &&  color.id != 16 || productDatas.color_filter_id === color.id &&  color.id != 17 || productDatas.color_filter_id === color.id &&  color.id != 18"
              >
                <i class="xi-check" style="color: white"></i>
              </div>

              <div
                v-if="productDatas.color_filter_id === color.id && productDatas.color_filter_id === color.id &&  color.id === 13 || productDatas.color_filter_id === color.id &&  color.id === 16 || productDatas.color_filter_id === color.id &&  color.id === 17 || productDatas.color_filter_id === color.id &&  color.id === 18"
              >
                <i class="xi-check" style="color: black"></i>
              </div>
            </div>
          </div>
          <div class="titleLine"></div>
          <div style="text-align:center">
            <div class="selected" @click="colorModal = 0">적용</div>
            <div class="cancel" @click="colorModal = 0; productDatas.color_filter_id = 0">취소</div>
          </div>
        </div>
        <v-simple-table>
          <template>
            <!-- 테이블 시작 영역 -->
            <!-- 셀러 상태 테이블 -->

            <tr class="sellerSelect">
              <th>
                셀러 선택
                <i class="xi-pen" />
              </th>
              <td>
                <input
                  type="text"
                  placeholder="셀러검색을 해주세요."
                  v-model="sellerInfo.name"
                  style="cursor: not-allowed !important;"
                  disabled
                />
                <div @click="sellersModal = !sellersModal" class="btn">셀러검색</div>
              </td>
            </tr>

            <!-- 판매여부 -->

            <tr>
              <th>판매여부</th>
              <td class="onSaleBox">
                <div>
                  <input
                    v-model="productDatas.on_sale"
                    type="radio"
                    id="onSale"
                    :value="1"
                    name="saleStatus"
                  />
                  <label for="onSale">판매</label>
                  <input
                    v-model="productDatas.on_sale"
                    type="radio"
                    id="noSale"
                    :value="0"
                    name="saleStatus"
                  />
                  <label for="noSale">미판매</label>
                </div>
                <div>
                  <i class="xi-info">미판매 선택시 앱에서 Sold Out으로 표시됩니다.</i>
                </div>
              </td>
            </tr>

            <!--진열 여부 -->

            <tr>
              <th>진열여부</th>
              <td class="onSaleBox">
                <div>
                  <input
                    v-model="productDatas.on_list"
                    type="radio"
                    id="displayed"
                    :value="1"
                    name="displayStatus"
                  />
                  <label for="displayed">진열</label>
                  <input
                    v-model="productDatas.on_list"
                    type="radio"
                    id="nodisplayed"
                    :value="0"
                    name="displayStatus"
                  />
                  <label for="nodisplayed">미진열</label>
                </div>
                <div>
                  <i class="xi-info">미진열 선택시 앱에서 노출되지 않습니다.</i>
                </div>
              </td>
            </tr>

            <!-- 카테고리 -->

            <tr>
              <th>
                카테고리
                <i class="xi-pen" />
              </th>
              <td class="categoryBox">
                <tr>
                  <th>1차 카테고리</th>
                  <td>
                    <select
                      v-model="firstCateSelected"
                      @change="getSecondCategory(firstCateSelected)"
                    >
                      <option value="">1차 카테고리를 선택해주세요.</option>
                      <option
                        :value="index"
                        v-for="(list,index) in firstCate"
                        :key="list.id"
                      >{{list.name}}</option>
                    </select>
                  </td>
                </tr>
                <tr>
                  <th>2차 카테고리</th>
                  <td>
                    <select 
                    v-model="secondCateId"
                    >
                      <option value="">1차 카테고리를 먼저 선택해 주세요.</option>
                      <option
                        :value="list.id"
                        v-for="list in secondCate"
                        :key="list.id"
                      >{{list.name}}</option>
                    </select>
                  </td>
                </tr>
              </td>
            </tr>

            <!-- 상품 정보 고시 -->

            <tr>
              <th>
                상품 정보 고시
                <i class="xi-pen" />
              </th>
              <td class="onSaleBox">
                <div>
                  <input
                    v-model="productDatas.is_detail_reference"
                    type="radio"
                    id="detailInfo"
                    :value="1"
                    name="infoState"
                    @click="productInforClick()"
                  />
                  <label for="detailInfo">상품상세 참조</label>
                  <input
                    v-model="productDatas.is_detail_reference"
                    type="radio"
                    id="writeInfo"
                    :value="0"
                    name="infoState"
                  />
                  <label for="writeInfo">직접입력</label>
                  <div v-if="productDatas.is_detail_reference === 0" class="detailBox">
                    <div class="inputBox">
                      <div class="inputTitle">제조사(수입사):</div>
                      <input v-model="productDatas.manufacture.manufacturer" type="text" />
                    </div>
                    <div class="inputBox">
                      <div class="inputTitle">제조일자:</div>
                      <!-- <input v-model="productDatas.manufacture.manufacture_date" type="text" /> -->
                          <b-form-datepicker
                            id="datepicker-placeholder"
                            v-model="productDatas.manufacture.manufacture_date"
                            placeholder="클릭해주세요"
                            local="kr"
                            style="width:250px">
                            </b-form-datepicker>
                    </div>
                    <div class="inputBox">
                        <div class="inputTitle">원산지:</div>
                          <select
                          v-model="manufacture_country_id"
                          >
                            <!-- <option value="0">원산지</option> -->
                            <option

                              :value="list.id"
                              v-for="list in informs[0].country"
                              :key="list.id"
                            >{{list.name}}</option>
                      </select>
                    </div>
                  </div>
                </div>
              </td>
            </tr>

            <!-- 상품명 -->

            <tr>
              <th>
                상품명
                <i class="xi-pen" />
              </th>
              <td>
                <div class="box">
                  <input type="text" v-model="productDatas.name" />
                  <div>
                    <i class="xi-info">미진열 선택시 앱에서 노출되지 않습니다.</i>
                  </div>
                </div>
              </td>
            </tr>

            <!-- 한줄 상품 설명 -->

            <tr>
              <th>한줄 상품 설명</th>
              <td>
                <input type="text" v-model="productDatas.simple_description" />
              </td>
            </tr>
            <!-- 이미지 등록 -->
              <!-- <tr>
                <th>이미지 등록</th>
                <td>
                  <input type="text" placeholder="이미지 url" v-model="productDatas.description_short" />
                </td>
              </tr> -->
            <!-- 상세 상품 설명 -->
            <tr>
              <th>
                상세 상품 정보
                <i class="xi-pen" />
              </th>
              <td class="editorBox">
                <vue-editor v-model="productDatas.description_detail"></vue-editor>
              </td>
            </tr>
            <!-- 색상필터(썸네일 이미지) -->
          </template>
        </v-simple-table>
      </div>
    </div>
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">태그 정보</i>
      </div>
      <div class="cmpTable">
        <!-- 셀러검색모달 -->
        <!-- 컬러필터모달 -->
        <v-simple-table>
          <template>
            <tr>
              <th>
                색상필터(썸네일 이미지)
                <i class="xi-pen" />
              </th>
              <td class="onSaleBox">
                <div style="width: 100%">
                  <input
                    v-model="colorModal"
                    :value="0"
                    type="radio"
                    id="unuse"
                    name="colorFilter"
                    checked
                  />
                  <label for="unuse">사용안함</label>
                  <input
                    @click="getColors()"
                    v-model="colorModal"
                    :value="1"
                    type="radio"
                    id="using"
                    name="colorFilter"
                  />
                  <label @click="getColors()" for="using">사용</label>
                  <input class="colorInput" type="text" disabled :value="selectedColor[2]" />
                  <div>
                    <i
                      class="xi-info"
                    >베스트 탭, 카테고리 페이지 및 검색페이지의 필터에 적용되며, 선택하지 않으실 경우 색상필터를 사용한 검색결과에 노출되지 않습니다.</i>
                  </div>
                  <div>
                    <i class="xi-info">썸네일 이미지의 1개 색상만 선택 가능하며, 뷰티 및 다이어트 카테고리의 상품의 경우 선택하실 수 없습니다.</i>
                  </div>
                </div>
              </td>
            </tr>
            <!-- 색상필터 -->
            <!-- 스타일필터 -->            
              <tr>
                <th>
                  스타일필터
                  <i class="xi-pen" />
                </th>
                <td class="onSaleBox">
                  <div>
                    <input
                      v-model="productDatas.style_filter_id"
                      type="radio"
                      id="displayed"
                      @click="styleFilter()"
                    />
                    
                    <label for="displayed">선택안함</label>
                    <input
                      v-model="productDatas.style_filter_id"
                      type="radio"
                      id="nodisplayed"
                      v-bind:value="1"
                    />
                    <label for="nodisplayed">심플베이직</label>
                    <input
                      v-model="productDatas.style_filter_id"
                      type="radio"
                      id="nodisplayed"
                      v-bind:value="2"
                    />
                    <label for="nodisplayed">러블리</label>
                    <input
                      v-model="productDatas.style_filter_id"
                      type="radio"
                      id="nodisplayed"
                      v-bind:value="3"
                    />
                    <label for="nodisplayed">페미닌</label> 
                    <input
                      v-model="productDatas.style_filter_id"
                      type="radio"
                      id="nodisplayed"
                      v-bind:value="4"
                    />
                    <label for="nodisplayed">캐주얼</label>  
                    <input
                      v-model="productDatas.style_filter_id"
                      type="radio"
                      id="nodisplayed"
                      v-bind:value="5"
                    />
                    <label for="nodisplayed">섹시글램</label>                                                                                
                  </div>
                  <div>
                    <i class="xi-info">베스트 탭, 카테고리 페이지 및 검색페이지의 필터에 적용되며, 선택하지 않으실 경우 스타일필터를 사용한 검색결과에 노출되지 않습니다.</i>
                  </div>
                </td>
              </tr>           
            <!-- 상품 태그 관리 -->
              <tr>
                <th>
                    상품 태그 관리
                    <i class="xi-pen" />
                </th>
                <td>
                  <div class="box">
                    <b-form-tags
                      value="value"
                      input-id="tags-separators"
                      v-model="tag"
                      @input="inputTag()"
                      separator=","

                      placeholder="입력해 주세요"
                      class="mb-2"
                      tag-variant="primary"
                      ></b-form-tags> 
                  </div>           
                </td>           
              </tr>          
          </template>
        </v-simple-table>
      </div>
    </div>
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">옵션 정보</i>
      </div>
      <div class="cmpTable">
        <v-simple-table>
          <template v-slot:default>
            <tr>
              <th>
                옵션설정
                <i class="xi-pen" />
              </th>
              <td>
                <input style="width: 10px; margin-right: 10px" type="radio" id="option" checked />
                <label for="option">기본옵션</label>
              </td>
            </tr>

            <!-- 옵션정보 테이블 시작 -->

            <tr class="optionTable" style="background-color: white !important">
              <th>옵션정보</th>
              <td class="tdBox">
                <v-simple-table>
                  <template v-slot:default>
                    <thead>
                      <tr class="headColor">
                        <th class="headTh" style="width: 20%;">옵션 항목</th>
                        <th class="headTh">상품 옵션명</th>
                        <th class="headTh" style="width: 20%;">옵션값 추가/삭제</th>
                      </tr>
                    </thead>

                    <tr class="thColor" style="background-color: white !important">
                      <th class="thLine">색상</th>
                      <td v-for="(color, index) in invenColorsCount" :key="color.id">
                        <div class="optionModal">
                          <div class="textDiv" @click="colorModalHandle(index)">
                            <div
                              class="textBox"
                            >{{allOptions.color[index]?allOptions.color[index] : "색상 옵션을 선택해 주세요."}}</div>
                            <input
                              @click=" $event.stopPropagation()"
                              v-if="invenColorsCount[index].state === true"
                              type="text"
                            />
                            <div v-if="invenColorsCount[index].state === true" class="optionList">
                              <p
                                class="listText"
                                @click="selectOptionColor(optionColor.name,'color',index)"
                                v-for="optionColor in informs[0].option_color"
                                :key="optionColor.id"
                              >{{optionColor.name}}</p>
                            </div>
                          </div>
                        </div>
                      </td>
                      <th class="thLine">
                        <div
                          v-if="invenColorsCount.length > 1"
                          class="icon"
                          @click="minusColorOption()"
                        >
                          <i class="xi-minus"></i>
                        </div>
                        <div class="icon" @click="plusColorOption()">
                          <i class="xi-plus"></i>
                        </div>
                      </th>
                    </tr>
                    <tr class="thColor" style="background-color: white !important">
                      <th>사이즈</th>
                      <td
                        style="border-bottom: 1px solid lightgray; border-top-width: 0;"
                        v-for="(size, index) in invenSizesCount"
                        :key="size.id"
                      >
                        <div class="optionModal">
                          <div class="textDiv" @click="sizeModalHandle(index)">
                            <div
                              class="textBox"
                            >{{allOptions.size[index]?allOptions.size[index] : "사이즈 옵션을 선택해 주세요."}}</div>
                            <input v-if="invenSizesCount[index].state === true" type="text" />
                            <div v-if="invenSizesCount[index].state === true" class="optionList">
                              <p
                                class="listText"
                                @click="selectOptionColor(optionSize.name,'size',index)"
                                v-for="optionSize in informs[0].option_size"
                                :key="optionSize.id"
                              >{{optionSize.name}}</p>
                            </div>
                          </div>
                        </div>
                      </td>
                      <th>
                        <div
                          class="icon"
                          v-if="invenSizesCount.length > 1"
                          @click="minusSizeOption()"
                        >
                          <i class="xi-minus"></i>
                        </div>
                        <div class="icon" @click="plusSizeOption()">
                          <i class="xi-plus"></i>
                        </div>
                      </th>
                    </tr>
                  </template>
                </v-simple-table>
              </td>
              <!-- <td>
                    <tr>
                      <th>재고관리여부</th>
                    </tr>
                    <tr>
                      <td>
                        <input
                          v-model="productDatas.is_displayed"
                          type="radio"
                          id="noinventory"
                          :value="1"
                          name="inventory"
                        />
                        <label for="noinventory">재고 수량 관리 안함</label>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <input
                          v-model="productDatas.is_displayed"
                          type="radio"
                          id="inventroy"
                          :value="1"
                          name="inventory"
                        />
                        <label for="inventroy">재고 수량 관리</label>
                      </td>
                    </tr>
              </td>-->
              <div class="optionSelected" @click="makingOptions()">
                <i class="xi-check">적용</i>
              </div>
              <v-simple-table class="reusltTableWrap">
                <template v-slot:default>
                  <tr class="resultTable">
                    <th class="resultTableTh">
                      <v-simple-table>
                        <template v-slot:default>
                          <tr>
                            <th class="headTh" style="background-color:#eee;" colspan="2">상품 정보 옵션</th>
                            <th class="headTh" style="background-color:#eee;" rowspan="2">일반 재고</th>
                            <th class="headTh" style="background-color:#eee;" rowspan="2"></th>
                          </tr>
                          <tr>
                            <th class="headTh">색상</th>
                            <th class="headTh">사이즈</th>
                          </tr>
                          <tr
                            style="background-color:#eee"
                            v-for="(option, index) in makingOptionsData"
                            :key="option.id"
                          >
                            <th>{{option.color_name}}</th>
                            <th>{{option.size_name}}</th>
                            <th class="invenControl">
                              <input :name="`inven${index}`" id="noInven" type="radio" />
                              <label :for="`inven${index}`">재고관리 안함</label>

                              <input :name=" `inven${index}`" id="inven" type="radio" />

                              <label :for="`inven${index}`">
                                <input v-model="makingOptionsData[index].stock" type="text" />개
                              </label>
                            </th>
                            <th class="optionMinusBox">
                              <div class="optionMinus" @click="minusMakingOptions(index)">
                                <i class="xi-minus"></i>
                              </div>
                            </th>
                          </tr>
                        </template>
                      </v-simple-table>
                    </th>
                  </tr>
                  <div style="background-color:white;">
                    <i class="xi-info">도매처옵션명 조합은 최대 100자까지 표시됩니다.</i>
                  </div>
                </template>
              </v-simple-table>
            </tr>
          </template>
        </v-simple-table>
      </div>
    </div>
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">판매 정보</i>
      </div>
      <div class="cmpTable">
        <v-simple-table>
          <template>
            <tr class="originPriceTable">
              <th>
                판매가
                <i class="xi-pen" />
              </th>
              <td>
                <input v-model="productDatas.price" type="text" />
                <div class="wonBox">원</div>
              </td>
              <div>
                <i class="xi-info">판매가는 원화기준 10원 이상이며 가격 입력 시 10원 단위로 입력해 주세요.</i>
              </div>
            </tr>

            <tr class="originPriceTable">
              <th>할인 정보</th>

              <td class="discountTable">
                <v-simple-table>
                  <template>
                    <tr>
                      <th>할인율</th>
                      <th>할인가</th>
                    </tr>
                    <tr>
                      <th>
                        <input
                          class="discountInput"
                          v-model="productDatas.discount_rate"
                          type="text"
                        />
                        <div class="wonBox">%</div>
                      </th>
                      <th>
                        <div>{{discountPrice > 0 ? discountPrice : ""}}</div>
                        <div class="discountBtn" @click="discountClick">할인 판매가 적용</div>
                      </th>
                    </tr>
                    <tr>
                      <th>할인판매가</th>
                      <th>{{changedPrice > 0 ? changedPrice : ""}}</th>
                    </tr>
                    <tr>
                      <th>할인기간</th>
                      <th>
              <td class="onSaleBox">
                <div>
                  <input
                    v-model="productDatas.is_detail_reference_2"
                    type="radio"
                    id="detailInfo"
                    :value="1"
                    name="infoState"
                    @click="discountDateClick()"
                  />
                  <label for="detailInfo">무기한</label>
                  <input
                    v-model="productDatas.is_detail_reference_2"
                    type="radio"
                    id="writeInfo"
                    :value="0"
                    name="infoState"
                  />
                  <label for="writeInfo">기간설정</label>
                  <div v-if="productDatas.is_detail_reference_2 === 0" class="detailBox"
                  >
                    <div class="inputBox">
                        <div class="inputTitle"></div>
                            <b-form-datepicker
                              id="datepicker-placeholder2"
                              v-model="discount_start"
                              placeholder="클릭해주세요"
                              local="kr"
                              ></b-form-datepicker>
                            <span class="span-input-group"> ~ </span>
                            <b-form-datepicker
                              id="datepicker-placeholder3"
                              v-model="discount_end"
                              placeholder="클릭해주세요"
                              local="kr"
                              >
                            </b-form-datepicker>                        
                    </div>
                  </div>
                </div>
              </td>
                      </th>
                    </tr>
                  </template>
                </v-simple-table>
              </td>
              <div>
                <i class="xi-info">할인판매가 = 판매가 * 할인율</i>
              </div>
              <div>
                <i class="xi-info">할인 판매가 적용 버튼을 클릭 하시면 판매가 정보가 자동 계산되어집니다.</i>
              </div>
              <div>
                <i class="xi-info">할인 판매가는 원화기준 10원 단위로 자동 절사됩니다.</i>
              </div>
            </tr>
            <tr class="originPriceTable test">
              <th>최소 판매 수량</th>      
              <td>
                <input v-model="min_sales_unit" name="minQuantity" class="radioBtn" :value ="1" type="radio"/>
                <label class="radioLabel">1개 이상</label>
                <input class="radioBtn" name="minQuantity" type="radio" />
                <label class="radioLabel">
                  <input v-model="min_sales_unit" type="text" class="radioInput" /> 
                  개 이상</label>
                <span>(20개를 초과하여 설정하실 수 없습니다)</span>
              </td>
            </tr>
            <tr class="originPriceTable test">
              <th>최대 판매 수량</th>
              <td>
                <input v-model="max_sales_unit" class="radioBtn" name="maxQuantity" :value="20" type="radio">
                <label class="radioLabel">20개</label>
                <input class="radioBtn" name="maxQuantity" type="radio" />
                <label class="radioLabel">
                  <input v-model="max_sales_unit" class="radioInput" type="text" />
                  개 이하</label>
                <span>(20개를 초과하여 설정하실 수 없습니다)</span>
              </td>
            </tr>

          </template>
        </v-simple-table>
      </div>
    </div>

    <!-- 판매정보 시작 -->

    <!-- 등록 취소 버튼 -->
    <v-col class="text-center">
      <div class="my-2">
        <v-btn
          class="enroll-button"
          @click="test01()"
          >등록</v-btn>
      </div>
      <div class="my-2">
        <v-btn class="cancle-button">취소</v-btn>
      </div>
    </v-col>
  </div>
</template>

<script>
import axios from "axios";
import { VueEditor } from "vue2-editor";
import { URL, JA_URL } from "../../config/urlConfig";

export default {
  components: {
    VueEditor
  },
  data() {
    return {
      infoDatas: [],
      content: "",

      sellersModal: false,
      sellersInputModal: false,
      sellerList: [],
      sellerInfo: { id: "", name: "" },
      searchSeller: "",

      firstCate: [],
      firstCateSelected: "",
      firstCateId: "",

      secondCate: [],
      secondCateId: "", 

      colorModal: 0,
      colors: [],
      selectedColor: [],

      invenColorsCount: [{ state: false }],
      invenSizesCount: [{ state: false }],

      informs: [],

      optionColorModal: false,
      optionColors: [],
      optionSizes: [],
      allOptions: { color: [], size: [] },
      makingOptionsData: [],
      invenState: null,
      test: 0,

      discountPrice: "",
      changedPrice: "",

      manufacture_country_id: null,

      max_sales_unittag: [],
      postTag: [],
      min_sales_unit: "",
      max_sales_unit: "",
      discount_start : "",
      discount_end : "",
      productDatas: {
        seller_id: "",
        on_sale: 1,
        on_list: 1,
        first_category_id: "0",
        second_category_id: "",
        is_detail_reference: 1,
        manufacture: {
          manufacturer: null,
          manufacture_date: null
        },
        name: "",
        description_short: "",
        color_filter_id: 0,
        style_filter_id: "",
        description_detail: "",
        options: this.makingOptionsData,
        wholesale_price: "",
        price: "",
        dismax_sales_unitcount_rate: "",
        // discount_start: "2020-06-01 08:30:00",
        // discount_end: "2020-06-03 23:59:59",
        // max_sales_unit: "",
        // min_sales_unit: ""
        // tags: ["태그88", "태그97", "태그94"]
      }
    };
  },
  mounted: function() {
    // this.getListDatas();
    // this.getOptionColors();
    this.getInformations();
  },
  methods: {
    test01: function() {
      if (confirm("상품을 등록 하시겠습니까?") == true){
      axios
        .post(
          `${JA_URL}/product`,
          {
            seller_id: this.productDatas.seller_id,
            on_sale: this.productDatas.on_sale,
            on_list: this.productDatas.on_list,
            first_category_id: Number(this.firstCateId),
            second_category_id: Number(this.secondCateId),
            manufacturer: this.productDatas.manufacture.manufacturer,
            manufacture_date: this.productDatas.manufacture.manufacture_date,
            manufacture_country_id: this.manufacture_country_id,
            name: this.productDatas.name,
            images: [{
                    "url": "url"}],
            description_short: this.productDatas.description_short,
            description_detail: this.productDatas.description_detail,
            color_filter_id: this.productDatas.color_filter_id,
            style_filter_id: this.productDatas.style_filter_id,
            option: this.makingOptionsData,
            price: Number(this.productDatas.price),
            // max_sales_unitdiscount_rate: Numbermax_sales_unit(this.productDatas.discount_rate),
            discount_rate : Number(this.productDatas.discount_rate),
            discount_start: this.discount_start,
            discount_end: this.discount_end,
            max_sales_unit: this.max_sales_unit,
            min_sales_unit: this.min_sales_unit,
            tag: this.postTag
          },
          {
            headers: {
              Authorization: localStorage.Authorization
            }
          }
        )
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          if (error.response.data.message === "SUCCESS") {
              alert("상품이 등록되었습니다");
            }
          else
          alert("입력을 확인 해 주십시오")
          
        });}
    },
    inputTag: function() {
      let index = (this.tag.length-1);
      this.postTag.push({name:this.tag[index]})
    },
    styleFilter: function() {
      this.productDatas.style_filter_id = null
    },
    discountDateClick: function() {
      this.discount_start = null,
      this.discount_end = null
    },
    productInforClick: function() {
      this.productDatas.manufacture.manufacturer = null,
      this.productDatas.manufacture.manufacture_date = null,
      this.manufacture_country_id = null
    },
    discountClick: function() {
      this.discountPrice =
       Math.floor(this.productDatas.price * (this.productDatas.discount_rate/100));
      this.changedPrice = Math.floor(this.productDatas.price * ((100-this.productDatas.discount_rate)/100)/10)*10;
    },
    minusMakingOptions: function(index) {
      this.makingOptionsData.splice(this.makingOptionsData[index], 1);
    },
    sellersModalHandle: function() {
      this.sellersInputModal
        ? (this.sellersMdaol = false)
        : (this.sellersInputModal = false);
    },
    makingOptions: function() {
      this.makingOptionsData = [];
      for (let i = 0; i <= this.allOptions.color.length - 1; i++) {
        for (let j = 0; j <= this.allOptions.size.length - 1; j++) {
          this.makingOptionsData.push({
            color_name: this.allOptions.color[i],
            size_name: this.allOptions.size[j],
            stock: null
          });
        }
      }
    },
    selectOptionColor: function(name, option, index) {
      if (option === "color" && this.allOptions.color.length === 0) {
        this.allOptions.color.push(name);
      } else if (option === "color" && this.allOptions.color[index]) {
        const colorCheck = this.allOptions.color.filter(colorInfo => {c
          return colorInfo === name;
        });
        colorCheck.length != 0
          ? alert(`이미 선택된 옵션입니다.`)
          : (this.allOptions.color[index] = name);
      } else if (option === "color" && this.allOptions.color.length != 0) {
        const colorCheck = this.allOptions.color.filter(colorInfo => {
          return colorInfo === name;
        });
        colorCheck.length != 0
          ? alert(`이미 선택된 옵션입니다.`)
          : this.allOptions.color.push(name);
      }

      if (option === "size" && this.allOptions.size.length === 0) {
        this.allOptions.size.push(name);
      } else if (option === "size" && this.allOptions.size[index]) {
        const sizeCheck = this.allOptions.size.filter(sizeInfo => {
          return sizeInfo === name;
        });
        sizeCheck.length != 0
          ? alert(`이미 선택된 옵션입니다.`)
          : (this.allOptions.size[index] = name);
      } else if (option === "size" && this.allOptions.size.length != 0) {
        const sizeCheck = this.allOptions.size.filter(sizeInfo => {
          return sizeInfo === name;
        });
        sizeCheck.length != 0
          ? alert(`이미 선택된 옵션입니다.`)
          : this.allOptions.size.push(name);
      }
      // option === "color"
      //   ? this.allOptions.color.push(name)
      //   : this.allOptions.size.push(name);
    },
    colorModalHandle: function(index) {
      this.invenColorsCount[index].state = !this.invenColorsCount[index].state;
    },
    sizeModalHandle: function(index) {
      this.invenSizesCount[index].state = !this.invenSizesCount[index].state;
    },
    // getOptionColors: function() {
    //   // axios
    //   //   .get(`${YE_URL}/product-options`, {
    //   //     headers: {
    //   //       Authorization: localStorage.Authorization
    //   //     }
    //   //   })
    //   //   .then(response => {
    //   //     this.optionColors = response.data.option_color;
    //   //     this.optionSizes = response.data.option_size;
    //   //   });
    //   axios.get(`${URL}/test.json`).then(response => {
    //     console.log("here is test Data >>>>", response);
    //     this.optionSizes = response.data.size;
    //     this.optionColors = response.data.color;
    //   });
    // },
    minusSizeOption: function() {
      this.invenSizesCount.splice(this.invenSizesCount.length - 1, 1);
    },
    plusSizeOption: function() {
      this.invenSizesCount.push({ state: false });
    },
    minusColorOption: function() {
      this.invenColorsCount.splice(this.invenColorsCount.length - 1, 1);
    },
    plusColorOption: function() {
      this.invenColorsCount.push({ state: false });
    },

    selectColor: function(id, img, name) {
      this.productDatas.color_filter_id = id;
      this.selectedColor.push(id, img, name);
    },
    getInformations: function() {
      axios
        .get(`${JA_URL}/product/information`, {
          headers: {
            Authorization: localStorage.Authorization
          }
        })
        .then(response => {
          this.informs = response.data.data;
        });
    },  
    getColors: function() {
      axios
        .get(`${JA_URL}/product/information`, {
          headers: {
            Authorization: localStorage.Authorization
          }
        })
        .then(response => {
          this.colors = response.data.data[0].color_filter;
        });
    },

    //셀러 검색창에서 검색결과의 아이디를 클릭하면, 해당 아이디의 텍스트와 고유 id를 data에 저장합니다.
    //getFirstCategory라는 카테고리 리스트를 수신하는 함수에 셀러의 고유 id를 인자로 보내며 실행합니다.
    selectSeller: function(id, name) {
      this.sellerInfo.name = name;
      this.productDatas.seller_id = id;
      this.getFirstCategory(id);
      // event.stopPropagation();
    },
    //1차 카테고리를 선택하면 해당 옵션에 2차카테고리를 받아옵니다.
    getSecondCategory: function(index) {
      this.secondCate = this.firstCate[index].second_category;
      this.firstCateId = this.firstCate[index].id
     
    },
    //셀러 검색 후, 선택된 셀러의 속성에 따라 1차카테고리 리스트가 달라지므로,
    //selectSeller함수에서 셀러 고유 id를 받아 1차 카테고리 리스트를 받아옵니다.
    getFirstCategory: function(id) {
      axios
        .get(`${JA_URL}/product/category?seller_id=${id}`, {
          headers: {
            Authorization: localStorage.Authorization
          }
        })
        .then(response => {
          this.firstCate = response.data.data;
        });
    },
    //셀러 검색창에 입력된 텍스트들을 실시간으로 받아, 해당 텍스트가 포함된 셀러 리스트를 받아옵니다.
    searchSellerList: function(e) {
      this.searchSeller = e;
      axios
        .get(`${JA_URL}/product/seller?seller_name=${this.searchSeller}`, {
          headers: {
            Authorization: localStorage.Authorization
          }
        })
        .then(response => {
          this.sellerList = response.data.data;
        })
        .catch(error => {
          error.respons.status === 500 ? (this.sellerList = "") : "";
        });
    },
    //상품 수정페이지로 진입시, 기존의 상품 정보들을 받아옵니다.
    getListDatas: function() {
      axios
        .get(`${JA_URL}/product?code=${this.code}`, {
          headers: {
            Authorization: localStorage.Authorization
          }
        })
        .then(response => {
          this.infoDatas = response.data.data;
        });
    }
  }
};
</script>

<style lang="scss" scoped>
.prWrap {
  padding-top: 35px;

  .editorBox {
    display: block !important;
  }
  .quillWrapper {
    background-color: white;
  }
  td {
    padding: 20px !important;
  }
  .wrap {
    position: absolute;
    top: -100px;
    left: 0;
    width: 100vw;
    height: 200vh;
    opacity: 50%;
    background-color: gray;
    z-index: 5;
  }

  .v-data-table {
    background-color: #fafafa;
  }

  .sellersModal {
    position: fixed;
    background-color: white;
    top: 40%;
    left: 40%;
    z-index: 10;
    width: 450px;
    height: 240px;
    border-radius: 5px;

    .cancel {
      border: 1px solid lightgray;
      cursor: pointer;
      &:hover {
        background-color: lightgray;
      }
    }
    .selected {
      color: #fff;
      background-color: #5bc0de;
      border-color: #46b8da;
      cursor: pointer;
      &:hover {
        background-color: #46b8da;
      }
    }

    .slTitleBox {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
    }
    .slTitle {
      margin: 20px 0;
      font-size: 18px !important;
      color: black !important;
    }
    .titleLine {
      border: 1px solid lightgray;
      width: 100%;
      height: 1px;
    }

    .inputBox {
      display: flex;
      margin: 20px 0 0 0;
      width: 100%;
      height: 30px;
      z-index: 30;
      .text {
        display: inline-block;
        color: black;
        margin-right: 100px;
        font-size: 13px;
      }
      input {
        margin-top: 0px;
        width: 100%;
        z-index: 40;
      }
    }
    .v-data-table table {
      width: 100%;
    }

    .inputSelect {
      width: 240px;
      padding: 10px;
      border: 1px solid lightgray;
      border-radius: 5px;
      color: gray;
      background-color: white;
      z-index: 15;
    }
    .searchResult {
      height: 130px;
      border: 1px solid lightgray;
      overflow: auto;
      .sellerlist {
        &:hover {
          background-color: lightgray;
        }
      }
    }
  }
  .titleLine02 {
    margin-top: 20px;
    margin-bottom: 20px;
    border: 1px solid lightgray;
    width: 100%;
    height: 1px;
  }
  .sellersBtn {
    width: 100%;
    display: flex;
    justify-content: flex-end;
    font-size: 13px;
    font-weight: 600;
    div {
      margin: 0 15px;
      padding: 8px 10px;
      border-radius: 5px;
    }
  }

  .colorModal {
    position: fixed;
    top: 20%;
    left: 40%;
    width: 500px;
    height: 500px;
    background-color: white;
    padding: 40px;
    z-index: 10;
    .cancel {
      display: inline-block;
      border-radius: 5px;
      border: 1px solid lightgray;
      margin-top: 10px;
      padding: 8px 10px;
      cursor: pointer;
      &:hover {
        background-color: lightgray;
      }
    }
    .selected {
      display: inline-block;
      border-radius: 5px;
      color: #fff;
      background-color: #5bc0de;
      border-color: #46b8da;
      margin-top: 10px;
      padding: 8px 10px;
      margin-right: 10px;
      cursor: pointer;
      &:hover {
        background-color: #46b8da;
      }
    }

    .colorBox {
      position: relative;
      display: inline-block;
      width: 80px;
      text-align: center;
      margin: 1px;
      &:hover {
        background-color: lightgray;
      }
    }
    .slTitle {
      margin: 20px 0;
      font-size: 18px !important;
      color: gray !important;
    }
    .titleLine {
      border: 1px solid lightgray;
      width: 100%;
      height: 1px;
    }
    .xi-check {
      position: absolute;
      top: 10px;
      left: 32px;
    }
  }

  .categoryBox {
    margin-bottom: 10px;
    tr {
      width: 100%;
      height: 100%;
      border: 1px solid lightgray;
    }
    th {
      background-color: white;
      width: 100vw;
      text-align: left;
      font-size: 14px;
      font-weight: 600;
      border: unset;
    }
    select {
      background-color: white;
      border: 1px solid lightgray;
      padding-left: 3px;
      border-radius: 3px;
      width: 100%;
      height: 34px;
    }
  }

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
  }

  .sellerSelect {
    .btn {
      margin-left: 20px;
    }
  }
  .optionSelected {
    display: inline-block;

    color: #fff;
    background-color: #5bc0de;
    border-color: #46b8da;
    font-weight: 900;
    font-size: 15px;
    cursor: pointer;
    &:hover {
      background-color: #46b8da;
    }
    border-radius: 3px;
    padding: 8px 12px;
    margin-left: 20px;
    margin-bottom: 10px;
  }

  .onSaleBox {
    display: flex;
    flex-direction: column;
    div:first-child {
      margin-bottom: 20px;
    }

    input {
      width: 10px;
      margin-right: 10px;
    }
    label {
      margin-right: 10px;
    }
    i {
      color: #1e90ff;
      display: block;
    }
    .colorInput {
      width: 30%;
    }
  }

  .detailBox {
    .inputBox {
      display: flex;
      margin: 20px 0;
      .inputTitle {
        width: 100px;
      }
      input,
      select {
        width: 250px;
      }
      select {
        background-color: white;
        border: 1px solid lightgray;
        border-radius: 3px;
        padding-left: 5px;
      }
    }
  }
  .btn {
    color: #fff;
    background-color: #5cb85c;
    border-color: #4cae4c;

    display: inline-block;
    padding: 6px 12px;
    margin-bottom: 0;
    font-size: 14px;
    font-weight: 400;
    line-height: 1.42857143;
    text-align: center;
    white-space: nowrap;
    vertical-align: middle;
    cursor: pointer;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    background-image: none;
    border: 1px solid transparent;
    border-radius: 4px;
  }

  input:focus {
    outline: 1px solid gray;
  }
  select:focus {
    outline: 1px solid gray;
  }
  .box {
    width: 100%;
    .xi-info {
      font-size: 12px;
      margin-top: 10px;
      color: #1e90ff;
    }
  }
  .xi-info {
    font-size: 12px;
    margin-top: 10px;
    color: #1e90ff;
  }

  .optionTable {
    border: 1px solid lightgray;
    .tdBox {
      .v-data-table {
        border: 1px solid lightgray;
        border-radius: 3px;
      }
      .headTh:nth-child(2) {
        border: 1px solid lightgray !important;
        border-top-width: 0 !important;
        border-bottom-width: 0 !important;
      }
      .thColor {
        background-color: white;
        td {
          border: 1px solid lightgray !important;
          border-bottom-width: 0 !important;
        }
        .icon {
          display: inline-block;
          width: 25px;
          padding: 5px;
          text-align: center;
          margin-right: 20px;
          border: 1px solid lightgray;
          border-radius: 3px;
        }
        i {
          color: black;
          font-weight: 900;
          font-size: 13px;
          cursor: pointer;
          &:hover {
            color: gray;
          }
        }
      }
      .thLine {
        border: 1px solid lightgray !important;
        border-left-width: 0 !important;
        border-right-width: 0 !important;
      }
      th {
        border: 0 !important;
      }
      td {
        border: 0 !important;
      }
    }
    .optionModal {
      .textBox {
        text-align: center;
        width: 80%;
        margin: 0 !important;
        cursor: pointer;
      }
      input {
        width: 100%;
      }
      .optionList {
        margin: 0;
        display: inline-block;
        width: 100%;
        height: 100px;
        background-color: white;
        overflow: scroll;
        text-align: center;
        font-size: 14px;
        font-weight: 400;
        .listText {
          margin-top: 8px;
          height: 20px;
          cursor: pointer;
          &:hover {
            background-color: #eee;
          }
        }
      }
      .textBox {
        text-align: center;
        width: unset;
        font-size: 14px;
        margin-bottom: 10px !important;
      }
      .textDiv {
        border: 1px solid lightgray;
        padding: 10px;
        text-align: left;
        font-size: 13px;
      }
    }

    .reusltTableWrap {
      .v-data-table {
        margin: 20px 0;
        border: 1px solid lightgray !important;
      }
      .xi-info {
        margin-left: 20px;

        background-color: white;
      }
    }
    .resultTable {
      .resutlTableTh {
        border: 0 !important;
      }
      th {
        background-color: white;
      }
      .headTh {
        background-color: #eee;
      }
      .invenControl {
        display: flex;
        width: 100%;
        align-items: center;
        input {
          width: unset;
          margin-right: 5px;
        }
        label {
          margin: 0 30px 0 10px;
        }
      }
      .optionMinusBox {
        text-align: center;
        width: 20%;

        .optionMinus {
          margin-left: 43%;
          text-align: center;
          justify-self: center;
          width: 30px;
          height: 30px;
          font-size: 30px;
          font-weight: 900;
          color: #fff;
          background-color: #d9534f;
          border-color: #d43f3a;
          border-radius: 3px;
          cursor: pointer;
        }
      }
    }

    .headTh {
      font-size: 14px;
      font-weight: 600;
      color: black;
    }
    div:first-child {
      width: 100%;
    }
    .headColor {
      background-color: #eee;
    }
  }
  .originPriceTable {
    // border: 1px solid red;
    input {
      width: 15% !important;
      border-top-right-radius: 0px !important;
      border-bottom-right-radius: 0px !important;
    }
    .radioBtn {
      width: unset !important;
      margin-right: 20px;
    }
    .radioLabel {
      margin-right: 20px;
    }
    .radioInput {
      margin-right: 20px;
      width: 35% !important;
      border-radius: 3px !important;
    }
    span {
      color: #1e90ff;
    }
    .wonBox {
      width: 40px;
      height: 34px;
      background-color: #e5e5e5;
      border-top-right-radius: 3px;
      border-bottom-right-radius: 3px;

      text-align: center;
      padding: 8px;
    }
    .xi-info {
      padding-left: 20px;
    }
  }
  .discountTable {
    text-align: left;
    .discountInput {
      width: 40% !important;
    }
    .v-data-table {
      width: 70%;
      border-left: 1px solid lightgray;
      border-bottom: 1px solid lightgray;
    }
    .wonBox {
      display: inline;
      vertical-align: middle;
    }
    .discountBtn {
      font-size: 14px;
      padding: 6px 12px;
      display: inline-block;
      border-radius: 3px;
      margin-top: 5px;
      color: #fff;
      background-color: #428bca;
      border-color: #357ebd;
      cursor: pointer;
    }
  }

  * {
    // border: 1px solid red;
  }
}
</style>