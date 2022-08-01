# syntax=docker/dockerfile:1.0.0-experimental
###############################################################################
# temporary layer, to build everything

FROM node:18.7.0-alpine as build

WORKDIR /app

RUN corepack enable && corepack prepare pnpm@7.9.3 --activate

COPY package.json pnpm-lock.yaml ./

RUN pnpm i

COPY index.html index.html
COPY tsconfig.json tsconfig.json
COPY unocss.config.ts unocss.config.ts
COPY vite.config.ts vite.config.ts
COPY src src
COPY public public

RUN pnpm run build

###############################################################################
# final layer

FROM nginx:1.23.1-alpine

COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html
