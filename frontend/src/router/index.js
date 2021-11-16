import Vue from 'vue'
import VueRouter from 'vue-router'
import Card from '@/components/Card'

Vue.use(VueRouter)

const routes = [  
  {
    path: '/cards/lista',
    name: 'Card',
    component: Card
  },
]

const router = new VueRouter({
  routes: routes,
  mode: 'history',
})
export default router
