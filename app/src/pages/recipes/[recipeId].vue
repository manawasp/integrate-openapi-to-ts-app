<script setup lang="ts">
import type { Recipe, RecipeComment } from 'integrate-openapi-to-ts-app'
import { FoodyClient } from 'integrate-openapi-to-ts-app'
const route = useRoute()
const recipeId = parseInt(route.params.recipeId as string) || 0

const recipe = ref<Recipe | null>()
const comments = ref<RecipeComment[]>([])
const errorLoading = ref<string | null>()

const app = new FoodyClient({
  BASE: '/api',
})

onBeforeMount(() => {
  app.recipes.recipesRetrieve({ recipeId }).then((res) => {
    recipe.value = res
  }).catch((err) => {
    errorLoading.value = err
  })

  app.recipesComments.recipesCommentsList({ recipeId }).then((res) => {
    comments.value = res.comments
  }).catch((err) => {
    errorLoading.value = err
  })
})
</script>

<template>
  <div v-if="recipe">
    <h1 class="text-2xl">
      <div class="i-carbon-noodle-bowl inline-block" />
      {{ recipe.name }}
    </h1>
    <p class="m-y-8">
      Cupcake ipsum dolor sit amet pastry lemon drops pie. Sesame snaps sweet gummi bears cupcake jelly-o. Sugar plum
      jujubes chupa chups liquorice pudding soufflé. Cookie oat cake ice cream biscuit tiramisu tootsie roll gummi bears
      jelly beans jelly. Lemon drops tootsie roll cheesecake marshmallow candy pastry biscuit. Macaroon biscuit donut
      jelly-o shortbread croissant. Apple pie dragée cake icing marzipan candy canes brownie. Halvah sweet roll lollipop
      shortbread toffee. Jujubes tootsie roll candy canes lollipop muffin lollipop.
    </p>
    <h1 class="text-xl">
      Comments
    </h1>
    <ul>
      <li v-for="comment in comments" :key="comment.id" class="m-t-3 flex items-center">
        <div class="i-carbon-forum inline-block m-r-2" />
        <span>{{ comment.message }}</span>
      </li>
    </ul>

    <div>
      <router-link :to="{ name: 'recipes' }" class="btn text-sm mt-8">
        back
      </router-link>
    </div>
  </div>
  <div v-else>
    Loading...
  </div>
</template>

<route lang="yaml">
name: recipe-detail
</route>
