# Use an official node image as the base
FROM node:22-slim AS builder

# Set the working directory in the container
WORKDIR /app/frontend/

# Copy the frontend directory into the container
COPY ./ ./

# Install fiab dependencies, with caching
# --mount=type=cache,mode=0755,target=/app/frontend/node_modules \
RUN yarn install
RUN yarn add vite

ENV VITE_API_BASE="http://backend:8000"

RUN yarn prodbuild

CMD ["yarn", "preview"]
EXPOSE 3000
