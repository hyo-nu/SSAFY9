<template >
  <div id="app">
    <nav>
      <router-link :to="{name: 'MovieView'}"><img id="nav_logo" src="./assets/nav_logo.png" alt=""></router-link>
      <router-link :to="{name: 'MovieView'}"><h1>CINEMA</h1></router-link>
      <div class="nav_box">
        <h6><router-link :to="{name: 'MovieView'}">Main</router-link></h6>
        <h6><router-link :to="{name: 'RandomView'}">Ramdombox</router-link></h6>
        <h6><router-link :to="{name: 'WatchListView'}">WatchList</router-link></h6>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  /* font-family: 'Dancing Script'; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  display: flex;
  margin-top: 10px;
  height: 80px;
  /* background-color: #B0E0E6; */
  margin-bottom: 20px;
  justify-content: space-between;
  align-items: center;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  margin-right: 15px;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #C71585;
}
#nav_logo{
  width: 60px;
  height: 60px;
  text-align: left;
  margin-left: 25px;
  margin-right: 150px;
}
.nav_box{
  display: flex;
}
body{
  background-color: #FFE4E1;
}
</style>
