<script setup lang="ts">
import type { Recipe } from 'integrate-openapi-to-ts-app'
import { FoodyClient } from 'integrate-openapi-to-ts-app'

const recipes = ref<Recipe[]>([])
const errorLoading = ref<string | null>()

const app = new FoodyClient({
  BASE: '/api',
})

// const name = $ref('')

// const router = useRouter()
onBeforeMount(async () => {
  app.recipes.recipesList({}).then((res) => {
    recipes.value = res.recipes
  }).catch((err) => {
    errorLoading.value = err
  })
})
// const goToRecipes = (id) => {
//   if (name)
//     router.push(`/recipes/${id}`)
// }

const simulateNotFound = async () => {
  console.log('not found')
}

const simulateUnauthorized = async () => {
  console.log('unauthorized')
}
</script>

<template>
  <div>
    <h1 class="text-3xl">
      <div class="i-carbon-restaurant inline-block" />
      Recipes
    </h1>
    <ul class="m-t-8">
      <li v-for="recipe in recipes" :key="recipe.id" class="m-t-2">
        <router-link :to="{ name: 'recipe-detail', params: { recipeId: recipe.id } }">
          {{ recipe.name }}
        </router-link>
      </li>
    </ul>

    <div class="m-t-12">
      <p class="m-b-2 text-sm">
        Handling api error calls:
      </p>
      <button class="btn text-sm m-r-4" @click="simulateNotFound">
        Not found call
      </button>

      <button class="btn text-sm" @click="simulateUnauthorized">
        Unauthorized call
      </button>
    </div>
  </div>
</template>
