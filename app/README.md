# App

This api is built using [Vitesse lite](https://github.com/antfu/vitesse-lite).

## Summary

- [App](#app)
  - [Summary](#summary)
  - [Run locally](#run-locally)
  - [Errors handling example](#errors-handling-example)
  - [CORS note](#cors-note)

## Run locally

```
$ nvm use
$ corepack enable && corepack prepare pnpm@7.9.3 --activate
$ pnpm i
$ pnpm run dev
```

_note: the api should serving as the app will call it_

![Recipe app](/app/images/app-example.png)

The app should appear and you should be able to take a tour.

## Errors handling example

You can find below an example on how to handle api communication error

**[app/src/pages/recipes/index.vue](/app/src/pages/recipes/index.vue)**

```ts
// Load Data from the API
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
```

## CORS note

We use a server proxy setup to communicate with the API and avoid CORS issue

**[app/vite.config.ts](/app/vite.config.ts)**

```ts
  proxy: {
    '/api': {
      target: 'http://localhost:8000',
      changeOrigin: true,
      rewrite: path => path.replace('/api', ''),
    },
  },
```

