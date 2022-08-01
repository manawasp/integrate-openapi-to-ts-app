<script setup lang="ts">
import type { Recipe } from 'integrate-openapi-to-ts-app'
import { ApiError, FoodyClient } from 'integrate-openapi-to-ts-app'

const router = useRouter()
const recipes = ref<Recipe[]>([])
const errorLoading = ref<string | null>()
const errorCallNotFound = ref<string | null>()

const app = new FoodyClient({
  BASE: '/api/',
})

// Load Data from the API
onBeforeMount(async () => {
  try {
    const listing = await app.recipes.recipesList({})
    recipes.value = listing.recipes
  } catch (err) {
    if (err instanceof ApiError) {
      errorLoading.value = err.message
    } else {
      console.error(err)
    }
  }
})

// Handle 404 error
const simulateNotFound = async () => {
  try {
    await app.custom.customNotFound()
    console.error('Not found returned 200')
  } catch (err) {
    if (err instanceof ApiError) {
      errorCallNotFound.value = err.message
    } else {
      console.error(err)
    }
  }
}

// Handle 401 unauthorized error with a redirects to the
const simulateUnauthorized = async () => {
  try {
    await app.custom.customUnauthorized()
    console.error('Unauthorized returned 200')
  } catch (err) {
    if (err instanceof ApiError) {
      if (err.status === 401) {
        router.push({ name: 'login' })
      }
    } else {
      console.error(err)
    }
  }
}
</script>

<template>
  <div>
    <h1 class="text-3xl">
      <div class="i-carbon-restaurant inline-block" />
      Recipes
    </h1>
    <div class="m-t-8">
      <ul v-if="!errorLoading">
        <li v-for="recipe in recipes" :key="recipe.id" class="m-t-2">
          <router-link :to="{ name: 'recipe-detail', params: { recipeId: recipe.id } }">
            {{ recipe.name }}
          </router-link>
        </li>
      </ul>
      <div v-else>
        Fail to load recipes: {{ errorLoading }}
      </div>
    </div>

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

      <p v-if="errorCallNotFound" class="text-sm m-t-4">
        {{ errorCallNotFound }}
      </p>
    </div>
  </div>
</template>
