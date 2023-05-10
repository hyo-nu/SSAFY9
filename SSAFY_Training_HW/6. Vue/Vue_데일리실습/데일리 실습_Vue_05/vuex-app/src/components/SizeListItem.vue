<template>
  <div>
    <div v-for="(size_type,index) in size" :key="index">
      <p>{{size_type.name}}</p>
      <p>{{size_type.price}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
}
</script>

<style>
</style>