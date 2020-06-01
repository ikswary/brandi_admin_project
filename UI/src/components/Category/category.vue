<template>
  <div class="category">
    <div class="category-inner">
      <div>{{ title }}</div>
      <div>{{ subtitle }}</div>
      <div>{{ subtitle2 }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'category',
  data() {
    return {
      title: '상품등록',
      subtitle: '상품관리',
      subtitle2: '상품22 ',
    };
  },
};
</script>

<style lang="scss" scoped>
.category {
  width: 215px;
  position: relative;
  right: 0;
  bottom: 0;
  left: 0;
  text-align: center;
  background-color: #35363a !important;
  color: white;
  font-size: 11px;
}
.category-inner {
  color: #999ba2;
  float: left;
  display: inline-block;
  font-size: 11px;
}
</style>
