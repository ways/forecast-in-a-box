# Use an official node image as the base
FROM node:22-slim

# Set the working directory in the container
WORKDIR /app/frontend/

# Copy the frontend directory into the container
COPY ./ ./

# Install fiab dependencies, with caching
RUN --mount=type=cache,mode=0755,target=/app/frontend/node_modules yarn install
RUN --mount=type=cache,mode=0755,target=/app/frontend/node_modules yarn add vite

ENV VITE_API_BASE="http://localhost:8000"

RUN yarn prodbuild

CMD ["yarn", "preview"]
EXPOSE 3000
