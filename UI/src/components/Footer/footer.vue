<template>
  <div class="footer">
    <div class="footer-inner">
      <div>{{ title }}</div>
      <div>{{ subtitle }}</div>
      <div>{{ subtitle2 }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'footer',
  data() {
    return {
      title:
        '| 상호 : (주)브랜디 | 주소 : (06223) 서울특별시 강남구 테헤란로 32길 26 청송빌딩',
      subtitle:
        '사업자등록번호 : 220-88-93187 | 통신판매업신고 : 2016-서울강남-00359호',
      subtitle2: '| 이메일 : help@brandi.co.kr 2018 © brandi inc.    ',
    };
  },
};
</script>

<style>
.footer {
  width: 1540px;
  position: relative;
  right: 0;
  bottom: 0;
  left: 0;
  text-align: center;
  background-color: #35363a !important;
  color: white;
  padding: 20px 20px 20px 20px;
  font-size: 11px;

  .footer-inner {
    color: #999ba2;
    float: left;
    display: inline-block;
    font-size: 11px;
  }
}
</style>
