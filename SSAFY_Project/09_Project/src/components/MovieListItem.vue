<template>
  <div class="col">
    <div class="card h-100" >
      <img class="card h-100"  :src="poster">
      <div class="card-body">
      <h5 class="card-title"><b>{{title}}</b></h5>
      </div>
    </div>
  </div>
</template>

<!-- <h1>MovieListItem</h1>
<h6>번호 : {{id}}</h6>
<h6>제목 : {{title}}</h6>
<img :src="poster"> -->
<!-- <img :src="backdrop" alt=""> -->

<script>
const make_img_URL = 'https://image.tmdb.org/t/p/w500'
export default {
  name: 'MovieListItem',
  data() {
    return{
      id: this.movie.id,
      title: this.movie.title,
      original_title: this.movie.original_title,
      poster: make_img_URL + this.movie.poster_path,
      // backdrop : make_img_URL + this.movie.backdrop_path,
    }
  },
  props:{
    movie: Object
  }
}
</script>

<style>
/* img{
  height: 500px;
} */

</style>