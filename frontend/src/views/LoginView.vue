<script setup lang='ts'>
import { RouterLink } from 'vue-router'

</script>

<template>
  <h1 class="text-3xl font-bold underline">Login Page</h1>
  
  <form class="my-8 flex flex-col justify-between h-28">
    <label class="input input-bordered border-black flex items-center gap-2">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70"><path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM12.735 14c.618 0 1.093-.561.872-1.139a6.002 6.002 0 0 0-11.215 0c-.22.578.254 1.139.872 1.139h9.47Z" /></svg>
      <input type="text" class="grow" placeholder="Username" />
    </label>
    <label class="input input-bordered border-black flex items-center gap-2">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70"><path d="M14 6a4 4 0 0 1-4.899 3.899l-1.955 1.955a.5.5 0 0 1-.353.146H5v1.5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1-.5-.5v-2.293a.5.5 0 0 1 .146-.353l3.955-3.955A4 4 0 1 1 14 6Zm-4-2a.75.75 0 0 0 0 1.5.5.5 0 0 1 .5.5.75.75 0 0 0 1.5 0 2 2 0 0 0-2-2Z" clip-rule="evenodd" /></svg>
      <input type="password" class="grow" placeholder="password" />
    </label>

  </form>

  <nav class="w-64 flex justify-between mt-8">
    <RouterLink class="btn btn-outline" to="/">Home</RouterLink>
    <RouterLink class="btn btn-outline" to="/signup">Signup</RouterLink>
    <RouterLink class="btn btn-outline" to="/profile">Profile</RouterLink>
  </nav>
</template>
