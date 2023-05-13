<template>
  <div class="box">
    <div class="random_box mt-2 mb-3">
      <h2>인기 영화를 추천 받아봐요!!</h2>
      <div class="shadow">    
      <img v-if="pickOne" id="image" :src="'https://image.tmdb.org/t/p/w500' + pickOne.poster_path" alt="">
      <h5 class="card-title mt-3 mb-2" ><b>{{pickOne.title}}</b></h5>
      </div>
      <button @click="randomBox" class="btn btn-primary mt-3">Suggestion</button>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name:"RandomView",
  data () {
    return {
      pickOne :'',
    }
  },
  created(){
    this.getMovies()
  },
  methods:{
    randomBox() {
      this.pickOne = _.sample(this.$store.state.movies)
      console.log(this.pickOne.poster_path)
    },
    getMovies(){
      this.$store.dispatch('getMovies')
    }
  }
}
</script>

<style>
.box{
  display: flex;
  justify-content: space-around;
}
.random_box{
  display: flex;
  flex-direction: column;
  align-items: center;
}
.shadow{
  box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;
}
#image{
  width: 350px;
  height: 400px;
}
</style>