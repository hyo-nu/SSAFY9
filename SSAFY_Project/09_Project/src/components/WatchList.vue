<template>
  <div>
    <WatchListItem v-for="(movie,index) in likeMovieList"
    :key="index" :movie=movie />
  </div>
</template>

<script>
import WatchListItem from '@/components/WatchListItem'

export default {
  name:'WatchList',
  components: {
    WatchListItem,
  },
  computed: {
    likeMovieList() {
      return this.$store.state.likeMovieList
    }
  }
}
</script>

<style>

</style>