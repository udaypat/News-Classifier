import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Home.vue'
import PredctionView from '../views/Predction.vue'

const routes = [
  {
    path: '/',
    component: HomeView
  },
  {
    path: '/predction',
    component: PredctionView
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
