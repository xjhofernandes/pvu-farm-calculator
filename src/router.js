import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'

const routerHistory = createWebHistory()

const router = createRouter({
  history: routerHistory,
  routes: [
    {
      path: '/',
      component: Home
    }
  ]
})

export default router