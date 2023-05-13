<template>
  <div class='size_List'>
    <div @click="sizeSelect(index)" :class="{selecting:size_type.selected}" 
    class="size_units" v-for="(size_type,index) in sizeProps" :key="index">
      <h3 class="size_title">{{size_type.name}}</h3>
      <p class="size_price">{{size_type.price}} 원</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    sizeProps: Array,
  },
  methods: {
    sizeSelect (index) {
      this.$store.state.sizeList[index].selected = !this.$store.state.sizeList[index].selected
    }
  }
}
</script>

<style>
.size_List{
  display: flex;
  justify-content: space-around;
  margin: 20px;
}
.size_units{
  display: flex;
  flex-direction: column;
  box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 2px 6px 2px;
  border-radius: 10px;
  width: 140px;
  height: 70px;
  align-items: center;
  justify-content: space-evenly;
}

#size_title{
  margin-top: 10px;
}
#size_price{
  margin-bottom: 8px;
}
</style>