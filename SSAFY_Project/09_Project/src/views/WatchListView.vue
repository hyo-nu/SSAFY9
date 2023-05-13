<template>
  <div>
    <div class="watch_box m-5 p-5">
    <h1>보고싶은 영화</h1>
    <WatchListForm/>
    </div>
    <WatchList/>
  </div>
</template>

<script>
import WatchListForm from '@/components/WatchListForm'
import WatchList from '@/components/WatchList'

export default {
  name:"WatchListView",
  components: {
    WatchListForm,
    WatchList,
  }
}
</script>

<style>
.watch_box{
  border-radius: 15px;
  background-color: white;
}
</style>