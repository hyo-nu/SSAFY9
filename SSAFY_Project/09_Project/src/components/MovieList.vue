<template>
  <div class="movie-list">
    <!-- <div class="row row-cols-1 row-cols-md-3 g-4"> -->
    <!-- <div class="row row-cols-1 row-cols-md-3 g-4"> -->
      <div class="row row-cols-xs-1 row-cols-md-3 row-cols-xxl-6 g-4">
      <MovieListItem
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
      />
      </div>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem'

export default {
  name: 'MovieList',
  components:{
    MovieListItem
  },
  computed:{
    movies() {
      return this.$store.state.movies
    }
  }
}
</script>

<style>
/* .movie-list{
  text-align: start;
} */

.row{
  margin-left: 100px;
  margin-right: 100px;
}

</style>