<script setup lang='ts'>
import { RouterLink } from 'vue-router'

</script>

<template>
  <h1 class="text-3xl font-bold underline mb-8">Seja bem vindo Usuario</h1>

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
            <input type="checkbox" checked="checked" class="checkbox checkbox-success" />
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
            <input type="checkbox" checked="checked" class="checkbox checkbox-success" />
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
            <input type="checkbox" checked="checked" class="checkbox checkbox-success" />
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
