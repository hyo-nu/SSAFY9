<template>
  <div id="appchild">
    <h1>AppChild</h1>
    <input type="text" v-model='childInputData' @input='childInputToParent'>
    <p>appData: {{appProps}}</p>
    <p>parentData: {{parentProps}}</p>
    <p>childData: {{childInputData}}</p>
  </div>
</template>

<script>
export default {
  name: 'AppChild',
  data : function (){
    return {
      childInputData:"",
    }
  },
  props:{
    appProps:String,
    parentProps:String,
  },
  methods:{
    childInputToParent: function(){
      this.$emit('child-input-to-parent', this.childInputData)
    }
  },
}
</script>

<style>
#appchild {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 30px;
  border: 1px solid blue;
}
</style>