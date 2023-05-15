// App.vue

export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  created: function () {
    this.isLogin = localStorage.get('jwt')? true:false
    }
  },