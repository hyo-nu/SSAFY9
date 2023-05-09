<template>
  <div class="about">
    <h1>로또</h1>
    <button @click="randomNumbers">Get Lucky Numbers</button>
    <p v-if ="number">{{number}}</p>
  </div>
</template>

<script>
import _ from "lodash"

export default {
  name : 'LottoView',
  data () {
    return {
      number : '',
    }
  },
  methods:{
    randomNumbers (){
      this.number = _.sortBy(_.sampleSize((_.range(1,46)),6))
    }
  }
}
</script>