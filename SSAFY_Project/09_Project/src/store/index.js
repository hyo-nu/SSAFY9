import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

const API_URL = "https://api.themoviedb.org/3/movie/top_rated?api_key=3e522bb11d9503474e85e9a710de1de4&language=ko-kr&page=1"
const API_KEY = "3e522bb11d9503474e85e9a710de1de4"
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
    likeMovieList: [],
    
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state,movies){
      movies.forEach(elem => {
        state.movies.push(elem)
      })
      
    },
    //WatchListForm
    ADD_MOVIE_LIST(state,inputItem){
      // console.log(inputItem)
      state.likeMovieList.push(inputItem)
    
    },
    COMPLETED_MOVIE(state,movie){
      state.likeMovieList = state.likeMovieList.map((likeMovie) => {
        if(likeMovie === movie) {
          likeMovie.isCompleted = !likeMovie.isCompleted 
        }
        return likeMovie
      })
    }
  },
  actions: {
    getMovies(context) {
      for (let i=1; i<21; i++){
      axios({
        url: API_URL,
        method: 'get',
        params: {
          api_key: API_KEY,
          language: 'ko-KR',
          page: i
        }
      })
      .then(res =>
        // console.log(res.data.results[0].backdrop_path,context)
        context.commit('GET_MOVIES',res.data.results)
        )
      .catch(err =>
        console.log(err)
        )
      }
    },
    //----------------------------------------
    //WatchListView를 부모로 가짐
    addMovieList(context,inputMovie) {
      // console.log(inputMovie)
      const inputItem = {
        title: inputMovie,
        isCompleted: false
      }
      context.commit('ADD_MOVIE_LIST',inputItem)
    },
    completedMovie(context,movie){
      context.commit("COMPLETED_MOVIE",movie)
    }


  },
  modules: {
  }
})
