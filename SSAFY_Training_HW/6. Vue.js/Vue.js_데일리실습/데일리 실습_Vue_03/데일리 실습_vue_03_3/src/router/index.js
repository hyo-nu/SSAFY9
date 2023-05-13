import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import NocolorView from '../views/NocolorView.vue'
import SsaflingView from '../views/SsaflingView.vue'
import SsafleafView from '../views/SsafleafView.vue'
import SsaflowerView from '../views/SsaflowerView.vue'
import NotfoundView from '../views/NotfoundView.vue'

SsafleafView
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/nocolor',
    name: 'nocolor',
    component: NocolorView
  },
  {
    path: '/Ssafling',
    name: 'Ssafling',
    component: SsaflingView
  },
  {
    path: '/Ssafleaf',
    name: 'Ssafleaf',
    component: SsafleafView
  },
  {
    path: '/Ssaflower',
    name: 'Ssaflower',
    component: SsaflowerView
  },
  {
    path : '/notFound',
    name : 'notFound',
    component : NotfoundView
  },
  {
    path: '*',
    redirect : "/notFound"
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
