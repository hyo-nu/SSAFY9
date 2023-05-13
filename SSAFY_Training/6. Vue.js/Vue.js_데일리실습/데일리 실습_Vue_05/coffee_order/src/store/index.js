import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [
      {
        menu :
        {
          title : '아메리카노',
          price : '3000',
          selected : false,
          image : 'https://source.unsplash.com/featured/?americano'
        },
        size :
        {
          name : 'grande',
          price : 1000,
          selected : false,
        }
      }
    ],
    menuList: [
      {
        title : '아메리카노',
        price : '3000',
        selected : false,
        image : 'https://source.unsplash.com/featured/?americano'
      },
      {
        title : '카페라떼',
        price : '4000',
        selected : false,
        image : 'https://source.unsplash.com/featured/?cafelatte'
      },
      {
        title : '콜드브루',
        price : '3500',
        selected : false,
        image : 'https://source.unsplash.com/featured/?coldbrew'
      }
    ],
    sizeList: [
      {
        name : 'Tall',
        price : 500,
        selected : false,
      },
      {
        name : 'Grande',
        price : 1000,
        selected : false,
      },
      {
        name : 'Venti',
        price : 1500,
        selected : false,
      }
    ],
  },
  getters: {
  },
  mutations: {
    addOrder: function () {},
    updateMenuList: function () {},
    updateSizeList: function () {},
  },
  actions: {
  },
  modules: {
  }
})
