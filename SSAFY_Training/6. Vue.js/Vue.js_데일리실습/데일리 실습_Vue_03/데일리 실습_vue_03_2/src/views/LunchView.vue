<template>
  <div class="home">
    <div class="box">
      <h1>점심메뉴</h1>
      <button @click="randomMenu">Pick Lunch</button>
      <p v-if="pickOne">{{pickOne}}</p>
    </div>

    <div>
      <h1>로또</h1>
      <button @click="toLotto">Pick Lotto</button>
    </div>
  </div>
</template>
<script>
import _ from 'lodash'

export default {
  name: 'LunchView',
  components: {
  },
  data () {
    return {
      menus : ['국밥','텐동','피자','치킨'],
      pickOne :''
    }
  },
  methods:{
    randomMenu() {
      this.pickOne = _.sample(this.menus)
    },
    toLotto() {
    this.$router.push({name:'lotto'})  
    }
  }
}
</script>

<style>
.box{
  height: 150px;
}
</style>
