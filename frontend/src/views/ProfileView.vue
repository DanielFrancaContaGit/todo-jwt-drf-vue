<script setup lang='ts'>
import { ref } from 'vue';
import { RouterLink } from 'vue-router'

const todoContent = ref('')
const acssesToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1MDUwODc3LCJpYXQiOjE3MTQ5NjQ0NzcsImp0aSI6IjdlMDYyZTRmMzE0MzRkODg5MWQ4M2U4NjAwNWMwNmE3IiwidXNlcl9pZCI6MX0.8nWAEG6Ww7cFGiCtzS8O5F8OhyWcqMyfsaz5pri2SaQ"

const url = new URL("http://127.0.0.1:8000/todo/list/")

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
    console.log(response.ok)
    console.log(response.json())
  })

}

getTodoList()
</script>

<template>
  <h1 class="text-3xl font-bold underline mb-8">Seja bem vindo Usuario</h1>
  <form class="flex justify-center w-1/2">
    <label class="input input-bordered border-black flex items-center gap-2 w-2/3">
      <input placeholder="Nova tarefa" class="grow" type="text">
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
    <tbody>
      <tr>
        <th>1</th>
        <td>Primeira atividade</td>
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
      <tr>
        <th>2</th>
        <td>Segunda atividade atividade</td>
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
        <td>

        </td>
      </tr>
      <tr>
        <th>3</th>
        <td>terceira atividade atividade</td>
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
