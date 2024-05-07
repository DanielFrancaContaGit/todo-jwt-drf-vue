<script setup lang='ts'>
import router from '@/router';
import { ref, type Ref } from 'vue';
import { RouterLink } from 'vue-router'
import { useAuthStore } from '../stores/authentication'

interface Todo {
  id: number,
  content: string,
  completed: boolean,
  owner: number,
}

const { token, userId } = useAuthStore()

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

getTodoList()
</script>

<template>
  <h1 class="text-3xl font-bold underline mb-8">Seja bem vindo Usuario</h1>
  <form v-on:submit.prevent="createNewTodo" class="flex justify-center w-1/2">
    <label class="input input-bordered border-black flex items-center gap-2 w-2/3">
      <input v-model="todoContent" placeholder="Nova tarefa" class="grow" type="text">
    </label>
    <button type="submit" class="btn bg-green-600 ml-3">Criat nova tarefa</button>
  </form>
  <table class="table w-1/2 my-8">
    <thead>
      <tr>
        <th></th>
        <th>Content</th>  
        <th>Complete</th>
        <th>Ações</th>
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
        <td class="flex justify-between w-52">
          <button class="btn btn-warning">Editar</button>
          <button class="btn btn-error">Deletar</button>
        </td>
      </tr>
    </tbody>  
    
  </table>

  <nav class="w-64 flex justify-between mt-8">
    <RouterLink class="btn btn-outline" to="/">Home</RouterLink>
    <RouterLink class="btn btn-outline" to="/signup">Signup</RouterLink>
    <RouterLink class="btn btn-outline" to="/profile">Profile</RouterLink>
  </nav>
</template>
