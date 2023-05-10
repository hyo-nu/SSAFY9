<template>
  <div class='menu_List'>
    <div @click="menuSelect(index)" :class="{selecting:coffee.selected}" 
    class="menu_units" v-for="(coffee,index) in menuProps" :key="index" >

      <h2  id="menu_title" >{{coffee.title}}</h2>
      <img :src="coffee.image">
      <p id="menu_price">{{coffee.price}} 원</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menuProps: Array,
  },
  data () {
    return {
      select : false,
    }
  },
  methods:{
    menuSelect (index) {
      this.$store.state.menuList[index].selected = !this.$store.state.menuList[index].selected
    }
  },
}
</script>

<style >
img{
  width: 100px;
  height: 150px;
  margin: 15px;
  border-radius: 5px;

}
.menu_List{
  display: flex;
  justify-content: space-around;
  margin: 20px;
}
.menu_units{
  display: flex;
  flex-direction: column;
  box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 2px 6px 2px;
  border-radius: 10px;
  width: 140px;
  align-items: center;
}
#menu_title{
  margin-top: 10px;
}
#menu_price{
  margin-bottom: 8px;
}
.selecting{
  background-color: wheat;
}
</style>>