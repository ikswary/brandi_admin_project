<template>
  <div class="login">
    <Login login="샐러로그인" />
  </div>
</template>

<script>
// @ is an alias to /src
import Login from '@/views/Login/login';

export default {
  name: 'Login',
  components: {
    Login,
  },
};
</script>

<style lang="scss">
.home {
  background-color: red;
}
</style>
