<template>
  <div>
    <div class="units"  v-for="(coffe,index) in menu" :key="index">
      <img :src="coffe.image">
      <p>{{coffe.title}}</p>
      <p>{{coffe.price}}</p>

    </div>
    
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
}
</script>

<style scoped>
img{
  width: 50px;
  height: 50px;
}

</style>>