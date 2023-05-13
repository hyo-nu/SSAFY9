<template>
  <div id="app">
    <div class="container">
      <header class="text-center text-primary">
        <h1>SSAFY TUBE</h1>
      </header>
      <!-- null값일때 안되게 하기 위해 v-if를 해준당 -->
      <div class="ratio ratio-16x9" v-if="video">
        <iframe :src="videoUrl" frameborder="0"></iframe>
      </div>
        <p>{{title}}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'
export default {
  name: 'App',
  data() {
    return {
      video: null,
      title: ''
    }
  },
  computed: {
    videoUrl() {
      return `https://www.youtube.com/embed/${this.video.id.videoId}`
    }
  },
  created() {
    axios({
      url: YOUTUBE_URL,
      params: {
        // key, part는 찐 필수
        key: API_KEY,
        part: 'snippet',
        q: '정국',
        type: 'video'
      }
    })
    .then(res=> {
      console.log(res)
      this.video = res.data.items[0]
      this.title = res.data.items[0].snippet.title
    })
    .catch(err=> {
      console.log(err)
    })
  }
}
</script>

<style>
  * {
    font-family: 'Noto Sans KR', sans-serif;
  }
</style>