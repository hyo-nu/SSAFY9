<template>
  <div class="nocolor">
    <h2>1단계</h2>
    <div class='main'>
      <i class="fa-sharp fa-solid fa-circle-chevron-left fa-xl" @click="noBack"></i>
      <img class="image" src="../assets/happling.png" alt="">
      <i class="fa-sharp fa-solid fa-circle-chevron-right fa-xl" @click="toSsafleaf"></i>
    </div>
    <h2>해플링</h2>
  </div>
</template>

<script>
export default {
  name : 'SsaflingView',
  methods :{
    noBack () {
      alert('이전 진화 단계로 돌아갈 수 없습니다.')
    },
    toSsafleaf() {
      this.$router.push({ name: 'Ssafleaf'})
    }
  }
}
</script>

<style>

</style>