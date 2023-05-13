<template>
  <div class="nocolor">
    <h2>2단계</h2>
    <div class='main'>
      <i class="fa-sharp fa-solid fa-circle-chevron-left fa-xl" @click="noBack"></i>
      <img class="image" src="../assets/happlossome.png" alt="">
      <i class="fa-sharp fa-solid fa-circle-chevron-right fa-xl" @click="toSsaflower"></i>
    </div>
    <h2>해플라썸</h2>
  </div>
</template>

<script>
export default {
  name:"SsafleafView",
  methods :{
    noBack () {
      alert('이전 진화 단계로 돌아갈 수 없습니다.')
    },
    toSsaflower() {
      this.$router.push({ name: 'Ssaflower'})
    }
  }
}
</script>

<style>

</style>