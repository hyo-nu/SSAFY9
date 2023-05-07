<template>
  <div class="menu-list">
    <div class="box">
      <h3><b>1. 음료를 고르세요.</b></h3>
      <MenuListItem :menus="menuList"/>
    </div>
  </div>
</template>

<script>
import MenuListItem from "@/components/MenuListItem"

export default {
  name: 'MenuList',
  components: {
    MenuListItem
  },
  computed: {
    menuList: function () {
      return this.$store.state.menuList
    },
  },
  methods: {
    selectMenu: function () {},
  },
}
</script>

<style scoped>
  .menu-list {
    display: flex;
  }
  .box{
    margin: 20px;
    background-color: white;
    border-radius: 10px;
  }
  .title{
    position: relative;
  }

</style>