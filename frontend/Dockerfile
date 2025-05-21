# Use an official node image as the base
FROM node:22-slim AS builder

# Set the working directory in the container
WORKDIR /app/frontend/

# Copy the frontend directory into the container
COPY ./ ./

# Install fiab dependencies, with caching
RUN --mount=type=cache,mode=0755,target=/app/frontend/node_modules \
    npm install && \
    npm run prodbuild

# Switch to an unprivileged nginx prod image
FROM nginxinc/nginx-unprivileged:1-alpine-slim
COPY --from=builder /app/frontend/dist /usr/share/nginx/html
EXPOSE 8080
