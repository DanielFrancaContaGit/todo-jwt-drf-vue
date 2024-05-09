import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '../stores/authentication'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/ProfileView.vue')
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('../views/SignupView.vue')
    },
  ]
})

router.beforeEach((to, from) => {
  const store = useAuthStore()

  if(to.name !== 'home' && to.name !== 'signup' && !store.isAuthenticate) {
    if(from.name == 'signup') {
      return {name: 'signup'}
    } else {
      return {name: 'home'}
    }
  } if (store.isAuthenticate && to.name !== 'profile') {
    return {name: 'profile'}
  }

})

export default router
