# Use an official lightweight Python image as the base
# 3.11 required by mir
FROM python:3.11-slim

# Install system deps
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
    apt install -y --no-install-recommends git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app/backend

# Copy the backend directory into the container
COPY forecastbox /app/backend/forecastbox/
COPY pyproject.toml /app/backend/forecastbox/pyproject.toml

# Install UV
COPY --from=ghcr.io/astral-sh/uv:0.7.8 /uv /uvx /bin/

# Create a virtual env. Install fiab dependencies, with caching
RUN --mount=type=cache,mode=0755,target=/root/.cache/uv \
    uv venv --seed /app/.venv && \
    uv pip install --link-mode=copy /app/backend/forecastbox[all] && \
    uv pip install --link-mode=copy --prerelease allow fdb5lib mirlib --upgrade && \
    uv pip install --link-mode=copy fckitlib

ENV PATH="/app/.venv/bin/:$PATH"
ENTRYPOINT ["/app/.venv/bin/uvicorn", "forecastbox.entrypoint:app", "--log-level", "info"]
EXPOSE 8080
