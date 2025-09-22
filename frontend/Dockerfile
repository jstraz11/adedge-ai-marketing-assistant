# frontend/Dockerfile
# Build stage
FROM node:20-alpine AS build
WORKDIR /app

# Install deps
COPY package.json package-lock.json* ./
RUN npm ci || npm install

# App source
COPY . .

# Build-time env (can be overridden by docker build args)
ARG VITE_BASE=/
ARG VITE_API_BASE=http://localhost:8000
ENV VITE_BASE=$VITE_BASE
ENV VITE_API_BASE=$VITE_API_BASE

# Build static site
RUN npm run build

# Serve stage
FROM nginx:1.27-alpine
# SPA routing fallback to index.html
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
