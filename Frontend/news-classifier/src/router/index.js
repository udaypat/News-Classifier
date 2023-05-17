import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Home.vue'
import PredictionView from '../views/Prediction.vue'

const routes = [
  {
    path: '/',
    component: HomeView
  },
  {
    path: '/prediction',
    component: PredictionView
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
