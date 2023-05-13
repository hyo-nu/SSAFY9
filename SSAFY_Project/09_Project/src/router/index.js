import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView'
import WatchListView from '@/views/WatchListView'
import RandomView from '@/views/RandomView'

Vue.use(VueRouter)

const routes = [
  {
    path:'/Movies',
    name:'MovieView',
    component: MovieView
  },
  {
    path:'/WatchListView',
    name:'WatchListView',
    component: WatchListView
  },
  {
    path:'/RandomView',
    name:'RandomView',
    component: RandomView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
