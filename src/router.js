import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'
import Contact from './views/Contact.vue'
import Bitcoin from './views/Bitcoin.vue'

const routerHistory = createWebHistory()

const router = createRouter({
  history: routerHistory,
  routes: [
    {
      path: '/',
      component: Home
    },
    {
      path: '/contact',
      component: Contact
    },
    {
      path: '/bitcoin',
      component: Bitcoin
    }
  ]
})

export default router