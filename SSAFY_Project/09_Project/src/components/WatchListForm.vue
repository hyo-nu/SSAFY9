<template>
  <div>    
    <input type="text" v-model.trim='content'
      @keyup.enter="addMovieList">
    <button @click="addMovieList">Add</button>
  </div>
</template>

<script>
export default {
  name: "WatchListForm",
  data () {
    return {
      content : null,
    }
  },
  methods:{
    addMovieList() {
      if (this.content) {
        this.$store.dispatch('addMovieList',this.content)
      }else{
        alert('영화를 입력해주세요')
      }
      this.content = null
      return 
    }
  }
  
} 
</script>

<style>

</style>