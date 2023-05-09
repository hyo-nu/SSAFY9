<template>
  <div>
    <h2>결정세액 : {{taxcalculatorProps-taxreductionProps}} 만원</h2>
  </div>
</template>

<script>
export default {
  name:'FinalTax',
  props:{
    taxcalculatorProps : Number,
    taxreductionProps : Number,
  },
}

</script>

<style>

</style>