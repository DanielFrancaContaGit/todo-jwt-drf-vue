<script setup lang='ts'>
import router from '@/router';
import { ref } from 'vue';
import { RouterLink } from 'vue-router'

const todoContent = ref('')
const todoList = ref(false)
const acssesToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1MDk2NzAzLCJpYXQiOjE3MTUwMTAzMDMsImp0aSI6IjA0ODBiNWQzNzA2NDQ0ZTJhMjc1NDZiMjBhMTBlNThhIiwidXNlcl9pZCI6MX0.u93V80ctYF33PXzbr_Zv3hUJtQJcyHaDIxMBQvY_0AY"

// const url = new URL("http://127.0.0.1:8000/todo/all/")
const url = new URL("http://127.0.0.1:8000/todo/list/1/")


async function getTodoList() {
  const ownerId = '1'

  const body = new FormData()

  const headers = new Headers()

  headers.set('Authorization',  "Bearer " + acssesToken)

  body.set('id', ownerId)

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

  headers.set('Authorization',  "Bearer " + acssesToken)

  body.set("content", todoContent.value)
  body.set("completed", "false")
  body.set("owner", '1')

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
