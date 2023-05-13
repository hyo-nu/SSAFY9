<template>
  <div>
    <div>
    <p>연봉 입력 (만 원): <input type="number" v-model="totalSalay"></p>
    <p>세액감면액 (만 원): <input type="number" v-model="taxReduction"></p>
    </div>
    
    <hr>

    <div>
      <h2>종합소득금액 : {{totalSalay}} 만원</h2>
      <h2>종합소득공제 : (-) 150 만원</h2>
      <h2 v-if="totalSalay <= taxBase">과세표준 : 0 만원</h2>
      <h2 v-if="totalSalay > taxBase">과세표준 : {{totalSalay - taxBase}}만원</h2>
    </div>

    <hr>

    <div>
      <TaxRate :taxbase-props="totalSalay"
      :taxreduction-props="taxReduction"
      />
    </div>
  </div>
</template>

<script>
import TaxRate from '@/components/Taxrate'

export default {
  name:'InCome',
  components:{
    TaxRate,
  },
  data : function() {
    return {
      taxBase : 150,
      totalSalay : 0,
      taxReduction : 0,
    }
  }
}
</script>

<style>

</style>