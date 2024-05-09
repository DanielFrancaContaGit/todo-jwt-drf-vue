<script setup lang='ts'>
import { ref, type Ref } from 'vue';
import { RouterLink } from 'vue-router'
import { useAuthStore } from '../stores/authentication'
import router from '@/router';


interface Todo {
  id: number,
  content: string,
  completed: boolean,
  owner: number,
}

const { token, userId, cleanToken } = useAuthStore()

const todoContent = ref('')
const todoList: Ref<Todo[]> = ref([])

const url = new URL("http://127.0.0.1:8000/todo/list/" + userId +"/")

async function getTodoList() {
  const headers = new Headers()

  headers.set('Authorization',  "Bearer " + token)

  await fetch(url, {
    method: "GET",
    headers
  })
  .then((response) => {
    if(response.ok) {
      return response.json()
    } else {
      return response.ok
    }
  })
  .then((data) => {
    return todoList.value = data
  })

}

function createNewTodo() {
  const body = new FormData()

  const headers = new Headers()

  const url = new URL("http://127.0.0.1:8000/todo/create/")

  headers.set('Authorization',  "Bearer " + token)

  body.set("content", todoContent.value)
  body.set("completed", "false")
  body.set("owner", String(userId))

  fetch(url, {
    method: "POST",
    headers,
    body,
  })
  .then((request) => {
    getTodoList()
  })
}

function logout() {
  cleanToken()
  router.push('/')
}

getTodoList()
</script>

<template>
  <section class="w-screen flex justify-center items-center flex-col">

  <h1 class="text-3xl font-bold underline mb-8 mt-10">Seja bem vindo Usuario</h1>
  <form v-on:submit.prevent="createNewTodo" class="flex justify-center items-center flex-wrap">
    <label class="input input-bordered border-black flex items-center gap-2 w-2/3 ">
      <input v-model="todoContent" placeholder="Nova tarefa" class="grow" type="text">
    </label>
    <button type="submit" class="btn bg-green-600 mt-3 md:btn-wide">Criat nova tarefa</button>
  </form>
  <table class="table w-auto max-w-full my-8 bg-slate-200">
    <thead>
      <tr>
        <th></th>
        <th>Content</th>  
        <th>Complete</th>
        <th class="hidden md:block">Ações</th>
      </tr>
    </thead>
    <tbody v-for="(todo, index) in todoList" :key="todo.id">
      <tr>
        <th>{{ index + 1 }}</th>
        <td>{{ todo.content }}</td>
        <td>
          <div class="form-control ml-3">
          <label class="cursor-pointer label">
            <input type="checkbox" class="checkbox checkbox-success" />
          </label>
          </div>
        </td>
        <td class="hidden md:flex justify-between w-52">
          <button class="btn btn-warning">Editar</button>
          <button class="btn btn-error">Deletar</button>
        </td>
      </tr>
    </tbody>  
    
  </table>

  <nav class="flex justify-between mt-4 mb-10">
    <button class="btn btn-outline" v-on:click="logout">Logout</button>
  </nav>
</section>

</template>
