<template>
  <div class="nocolor">
    <h2>시작</h2>
    <div class='main'>
      <i class="fa-sharp fa-solid fa-circle-chevron-left fa-xl" @click="toHome"></i>
      <img class="image" src="../assets/happeed.png" alt="">
      <i class="fa-sharp fa-solid fa-circle-chevron-right fa-xl" @click="toSsafling"></i>
    </div>
    <h2>해피드</h2>
  </div>
</template>

<script>
export default {
  name : "NocolorView",
  methods: {
    toHome() {
      this.$router.push({ name: 'home'})
    },
    toSsafling() {
      this.$router.push({ name: 'Ssafling'})
    }
  }
}
</script>

<style>
.nocolor{
  margin : auto;
  width: 600px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
}
.main{
  display: flex;
  align-items: center;
  justify-content: space-around;

}
.image {

  width: 400px;
}
</style>