<template>
  <div class="size-board">
    <h1 id="size"> 사이즈를 고르세요.</h1>
    <SizeListItem :size-props="sizeList"/>
  </div>
</template>

<script>
import SizeListItem from '@/components/SizeListItem'

export default {
  name: 'SizeList',
  components: {
    SizeListItem
  },
  methods: {
    onSelectMenu: function () {},
  },
  computed: {
    sizeList: function () {
      return this.$store.state.sizeList
    },
  },
}
</script>

<style>
.size-board{
  background-color: white;
  margin-bottom: 13px;
  margin-left: 10px;
  border: 5px solid gainsboro;
  border-radius: 20px;
  width: 670px;
  height: 180px;
}
#size{
  text-align: center;
  margin-top: 10px;
}
</style>