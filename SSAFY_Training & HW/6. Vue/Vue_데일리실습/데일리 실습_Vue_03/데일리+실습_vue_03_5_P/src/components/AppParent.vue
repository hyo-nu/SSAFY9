<template>
  <div id="appparent">
    <h1>AppParent</h1>
    <input type="text" v-model="dynamicProps" @input='parentInputToApp'>
    <p>appData: {{appProps}}</p>
    <p>childData: {{childInputData}}</p>
    
    <div>
      <AppChild :app-props='appProps' :parent-props='dynamicProps' @child-input-to-parent="getDynamicData" 
      />
    </div>
  </div>
</template>

<script>
import AppChild from '@/components/AppChild'

export default {
  name: 'AppParent',
  components :{
    AppChild,
  },
  data : function(){
    return{
      dynamicProps:'',
      childInputData:'',
    }
  },
  props:{
    appProps:String,
  },
  methods:{
    getDynamicData(input){
      this.childInputData = input
      this.$emit('child-input-to-app',this.childInputData)
    },
    parentInputToApp() {
      this.$emit('parent-input-to-app', this.dynamicProps)
    },
  }
}
</script>

<style>
#appparent {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 30px;
  border: 1px solid red;
}
</style>