<template>
  <div id="app">
    <p>Counter: {{ counter }}</p>
    <p>Counter x2: {{ counterDouble }}</p>
    <p></p>
    <button @click="increase">increase +</button>
    <button @click="decrease">decrease -</button>
  </div>
</template>

<script>

export default {
  name: 'App', 
  data: function() {
    return {
    }
  },
  methods: {
    increase: function () {
      // this.$store.commit('INCREASE')
      this.$store.dispatch('increase')
    },
    decrease: function () {
      // this.$store.commit('DECREASE')
      this.$store.dispatch('decrease')

    },
  },
  computed: {
    counter(){
      return this.$store.state.counter
    },
    counterDouble: function () {
      return this.$store.getters.counterDouble
    },
  },
}
</script>

<style>
</style>