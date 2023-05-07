import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message:"message in store"
  },
  getters: {
    messageLength(state){
      return state.message.length
    },
    doubleLength(state,getters){
      return getters.messageLength * 2
    }
  },
  mutations: { // mutations은 state바꾸라고 태어난 아이죠
    CHANGE_MESSAGE(state, message){
      // console.log(state)
      // console.log(message)
      state.message = message
    }
    // CHANGE_MESSAGE(A, payload)
    // payload : actions에서 전달받은 message
    // A : state임
  },
  actions: {
    changeMessage(context, message) {
      context.commit('CHANGE_MESSAGE', message)
    }
  },
  modules: {
  }
})
