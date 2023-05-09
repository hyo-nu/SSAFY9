<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model="dynamicProps">
    <p>parentData:{{parentInputData}}</p>
    <p>childData:{{childInputData}}</p>
    
    <div>
      <AppParent :app-props='dynamicProps' @child-input-to-app="getDynamicChildData"
      @parent-input-to-app="getDynamicParentData"/>
    </div>
  </div>
</template>

<script>
import AppParent from '@/components/AppParent'

export default {
  name: 'App',
  components:{
    AppParent,
  },
  data: function() {
    return{
      dynamicProps : "",
      childInputData : '',
      parentInputData :'',
    }
  },
  methods:{
    getDynamicChildData(input){
      this.childInputData = input
    },
    getDynamicParentData(input){
      this.parentInputData = input
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 30px;
  border: 1px solid black;
}
</style>
