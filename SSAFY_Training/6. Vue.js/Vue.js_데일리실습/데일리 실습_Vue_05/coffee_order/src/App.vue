<template>
  <div id="app">
    <h1>Coffee Order App</h1>
    <div class="board">
      <MenuList/>
      <SizeList/>
    </div>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList'
import SizeList from '@/components/SizeList'

export default {
  name: 'App',
  components :{
    MenuList,
    SizeList,
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}
#app{
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}
.board{
  display: flex;
  flex-direction: column;
  margin-top: 20px;
  background-color: gainsboro;
  border-radius: 10px;
}

ul {
  list-style: none;
}
</style>
