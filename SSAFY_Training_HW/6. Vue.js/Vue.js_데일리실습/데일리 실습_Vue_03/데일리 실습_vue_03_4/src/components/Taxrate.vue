<template>
  <div>
    <div>
      <h2>산출세액 : {{tax_calculator}}만원</h2>
      <h2>세액감면 : (-) {{taxreductionProps}}만원</h2>
    </div>

    <hr>

    <div>
      <FinalTax :taxcalculator-props="tax_calculator" :taxreduction-props="taxreductionProps"/>
    </div>
  </div>
</template>

<script>
import FinalTax from '@/components/Finaltax'

export default {
  name: 'TaxRate',
  data : function() {
    return {
    }
  },
  components:{
    FinalTax,
  },
  props:{
    taxbaseProps : Number,
    taxreductionProps : Number,
  },
  computed:{
    tax_calculator: function() {
      if (this.taxbaseProps - 150 > 100000) {
        return Math.round((this.taxbaseProps-150) * 0.45) - 6540
      }else if (this.taxbaseProps - 150 >50000) {
        return Math.round((this.taxbaseProps-150) * 0.42) - 3540
      }else if (this.taxbaseProps - 150 >30000) {
        return Math.round((this.taxbaseProps-150) * 0.4) - 2540
      }else if (this.taxbaseProps - 150 >15000) {
        return Math.round((this.taxbaseProps-150) * 0.38) - 1940
      }else if (this.taxbaseProps - 150 >8800) {
        return Math.round((this.taxbaseProps-150) * 0.35) - 1490
      }else if (this.taxbaseProps - 150 >4600) {
        return Math.round((this.taxbaseProps-150) * 0.24) - 522
      }else if (this.taxbaseProps - 150 >1200) {
        return Math.round((this.taxbaseProps-150) * 0.15) - 108
      }else if (this.taxbaseProps - 150 >0) {
        return Math.round((this.taxbaseProps-150) * 0.06)
      }else{
        return 0
      }
    }
  }
}
</script>

<style>

</style>