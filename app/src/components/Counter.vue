<script setup lang="ts">
import type { Item } from 'integrate-openapi-to-ts-app'
import { AppClient } from 'integrate-openapi-to-ts-app'

const props = defineProps<{
  initial: number
}>()

const app = new AppClient({})
const req: Item = {
  name: 'ok',
  price: 0,
}
app.default.updateItemItemsItemIdPut(0, req)
// app.default.readItemItemsItemIdGet

const { count, inc, dec } = useCounter(props.initial)
</script>

<template>
  <div>
    {{ count }}
    <button class="inc" @click="inc()">
      +
    </button>
    <button class="dec" @click="dec()">
      -
    </button>
  </div>
</template>
