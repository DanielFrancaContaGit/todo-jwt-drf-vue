<script setup lang='ts'>
import router from '@/router';
import { ref } from 'vue';
import { RouterLink } from 'vue-router'
import { useAuthStore } from '../stores/authentication'

const username = ref('')
const password = ref('')
const email = ref('')

const { token, userId } = useAuthStore()

async function formSubmit() {
   const body = new FormData

   body.set('username', username.value)
   body.set('password', password.value)
   body.set('email', email.value)
   body.set('is_staff', "true")

   const url = new URL('http://localhost:8000/user/create/')

   await fetch(url, {
      method: 'POST',
      body
   })
   .then((response) => {
      if(response.ok) {
         return(response.json())
      } else {
         return response.ok
      }
   })
   .then((data) => {
      if(data) {
         return router.push('/')
      } else {
         alert('Cadastro invalido')
      }
   })

} 

</script>

<template>
  
  <h1 class="text-3xl font-bold underline">Signup Page</h1>
  <form v-on:submit.prevent="formSubmit" class="my-8 flex flex-col justify-between">

   <label class="input input-bordered border-black flex items-center gap-2">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70"><path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM12.735 14c.618 0 1.093-.561.872-1.139a6.002 6.002 0 0 0-11.215 0c-.22.578.254 1.139.872 1.139h9.47Z" /></svg>
      <input v-model="username" type="text" class="grow" placeholder="Username" />
   </label>

   <label class="input input-bordered border-black flex items-center gap-2 my-3">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70"><path d="M2.5 3A1.5 1.5 0 0 0 1 4.5v.793c.026.009.051.02.076.032L7.674 8.51c.206.1.446.1.652 0l6.598-3.185A.755.755 0 0 1 15 5.293V4.5A1.5 1.5 0 0 0 13.5 3h-11Z" /><path d="M15 6.954 8.978 9.86a2.25 2.25 0 0 1-1.956 0L1 6.954V11.5A1.5 1.5 0 0 0 2.5 13h11a1.5 1.5 0 0 0 1.5-1.5V6.954Z" /></svg>
      <input v-model="email" type="text" class="grow" placeholder="Email" />
   </label>

   <label class="input input-bordered border-black flex items-center gap-2">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70"><path fill-rule="evenodd" d="M14 6a4 4 0 0 1-4.899 3.899l-1.955 1.955a.5.5 0 0 1-.353.146H5v1.5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1-.5-.5v-2.293a.5.5 0 0 1 .146-.353l3.955-3.955A4 4 0 1 1 14 6Zm-4-2a.75.75 0 0 0 0 1.5.5.5 0 0 1 .5.5.75.75 0 0 0 1.5 0 2 2 0 0 0-2-2Z" clip-rule="evenodd" /></svg>
      <input v-model="password" type="password" class="grow" placeholder="password" />
   </label>
   <button class="btn w-full bg-blue-600 mt-3" type="submit">Cadastrar</button>
  </form>
  <nav class="w-44 flex justify-between mt-4">
    <RouterLink class="btn btn-outline" to="/">Home</RouterLink>
    <RouterLink class="btn btn-outline" to="/signup">Signup</RouterLink>
  </nav>
</template>
