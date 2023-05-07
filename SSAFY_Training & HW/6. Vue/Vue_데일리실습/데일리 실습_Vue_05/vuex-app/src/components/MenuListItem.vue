<template>
  <div>
    <div class="box_unit" v-for="(menu,index) in menus" :key="index" @click="updateMenuList(index)">
      <img class="unit_img" :src="menu.image">
      <span class="unit"><b>{{menu.title}}</b></span>
      <span class="unit"><b>{{menu.price}}원</b></span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  data(){
    return {
    }
  },
  props: {
    menus: Object,
  },
  methods:{
    updateMenuList (index){
      const selectedMenu = index
      this.$store.dispatch('updateMenuList',selectedMenu)
    }
  },
}
</script>

<style scoped>
  .unit {
    height: 50px;
    width: 80px;
    position: relative;
    margin-top:23px;    
    
  }
  .unit_img{
    height: 45px;
    width: 50px;
    border-radius: 10px;
    position: relative;
    margin-top: 13px;
    margin-left: 10px;   
  }
  .box_unit {
    display: flex;
    justify-content: space-between;
    width: 400px;
    border: 2px solid black;
    border-radius: 10px;
    margin-bottom: 15px;
  }
</style>