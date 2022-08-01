<template>
  <div>
    <h1 class="text-3xl">
      <div class="i-carbon-gateway-user-access inline-block" />
      Login
    </h1>
    <p class="m-t-4">
      Please login to read recipes !
    </p>

    <div class="m-t-12">
      <router-link :to="{ name: 'recipes' }" class="btn">
        login
      </router-link>
    </div>
  </div>
</template>

<route lang="yaml">
name: login
</route>
