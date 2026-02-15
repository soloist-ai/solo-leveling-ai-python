# =============================================================================
# Build stage - устанавливаем зависимости
# =============================================================================
FROM python:3.11-slim AS builder

# Устанавливаем системные зависимости (одним слоем, без кеша)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV POETRY_VERSION=2.2.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -sf /opt/poetry/bin/poetry /usr/local/bin/poetry

WORKDIR /app

COPY pyproject.toml poetry.lock* ./
RUN poetry install --only main --no-root --no-directory \
    && rm -rf $POETRY_CACHE_DIR

COPY src ./src
RUN poetry install --only main \
    && rm -rf $POETRY_CACHE_DIR

# Очистка venv: кеш байткода и тесты пакетов
RUN find /app/.venv -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true \
    && find /app/.venv -type f -name "*.pyc" -delete 2>/dev/null || true \
    && find /app/.venv -type f -name "*.pyo" -delete 2>/dev/null || true \
    && find /app/.venv -path "*/site-packages/*" -type d -name "tests" -exec rm -rf {} + 2>/dev/null || true \
    && find /app/.venv -path "*/site-packages/*" -type d -name "test" -exec rm -rf {} + 2>/dev/null || true

# =============================================================================
# Runtime stage - минимальный образ
# =============================================================================
FROM python:3.11-slim AS runtime

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN groupadd -r appuser \
    && useradd -r -g appuser -u 1000 appuser \
    && mkdir -p /app \
    && chown -R appuser:appuser /app

WORKDIR /app

COPY --from=builder --chown=appuser:appuser /app/.venv /app/.venv
COPY --from=builder --chown=appuser:appuser /app/src /app/src

USER appuser

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app \
    APP_ENV=prod

EXPOSE 8080
CMD ["python", "-m", "src.app.main"]
