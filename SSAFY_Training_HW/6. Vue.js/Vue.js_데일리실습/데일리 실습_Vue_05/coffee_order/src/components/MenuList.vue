<template>
  <div class="menu-board">
    <h1 id="beverage">음료를 고르세요</h1>
    <MenuListItem :menu-props="menuList"/>
  </div>
</template>

<script>
import MenuListItem from '@/components/MenuListItem'

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

<style>
.menu-board{
  background-color: white;
  margin: 9px;
  border: 5px solid gainsboro;
  border-radius: 20px;
  width: 670px;
  height: 380px;
  padding: 10px;
}
#beverage{
  text-align: center;
  margin-top: 8px;
}

</style>