<template>
  <div id="app">
    <h1>캐릭터 진화 단계 가이드</h1>
    <nav>
      <router-link :to="{name: 'home'}">Home</router-link>
      <router-link :to="{name: 'nocolor'}">Start</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Noto Sans KR', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  flex-direction: column;
  text-align: center;
  justify-content: center;
  color: black;
}

nav {
  display: flex;
  justify-content: center;
}

nav a {
  text-decoration-line: none;
  line-height: 45px;
  width: 110px;
  height: 50px;
  border: 1px solid #F1A324;
  margin: 20px;
  font-weight: bold;
}

nav a.router-link-exact-active {
  font-size: 100;
  color :black
}
</style>
