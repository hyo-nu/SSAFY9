<template>
  <div id="app">
    <div>
      <nav><h1>Coffee Order App</h1></nav>
      <div class="box">
        <MenuList/>
      </div>
    </div>
  </div>
</template>

<script>
import MenuList from "@/components/MenuList"

export default {
  name: 'App',
  components :{
    MenuList,
  }
}
</script>

<style scoped>
#app {
  display: flex;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.box{
  background-color: gainsboro;
  border-radius: 10px;
}
ul {
  list-style: none;
}
</style>
