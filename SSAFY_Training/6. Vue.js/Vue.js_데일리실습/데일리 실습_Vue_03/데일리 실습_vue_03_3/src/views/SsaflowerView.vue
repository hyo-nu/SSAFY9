<template>
  <div class="nocolor">
    <h2>3단계</h2>
    <div class='main'>
      <i class="fa-sharp fa-solid fa-circle-chevron-left fa-xl" @click="noBack"></i>
      <img class="image" src="../assets/happlower.png" alt="">
      <i class="fa-sharp fa-solid fa-circle-chevron-right fa-xl" @click="toHome"></i>
    </div>
    <h2>해플라썸</h2>
  </div>
</template>

<script>
export default {
  name:"SsaflowerView",
  methods :{
    noBack () {
      alert('이전 진화 단계로 돌아갈 수 없습니다.')
    },
    toHome() {
      this.$router.push({ name: 'home'})
      alert('Home으로 돌아갑니다!')

    },
    
  }
}
</script>

<style>

</style>