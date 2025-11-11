# =============================================================================
# Build stage - устанавливаем зависимости
# =============================================================================
FROM python:3.11-slim AS builder

# Устанавливаем системные зависимости
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry 2.2.1
ENV POETRY_VERSION=2.2.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /opt/poetry/bin/poetry /usr/local/bin/poetry && \
    poetry --version

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock* ./

# Устанавливаем зависимости (только production)
RUN poetry install --only main --no-root --no-directory && \
    rm -rf $POETRY_CACHE_DIR

# Копируем исходный код
COPY src ./src

# Устанавливаем проект
RUN poetry install --only main && \
    rm -rf $POETRY_CACHE_DIR

# =============================================================================
# Runtime stage - минимальный образ для запуска
# =============================================================================
FROM python:3.11-slim AS runtime

# Устанавливаем только необходимые runtime зависимости
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Создаём непривилегированного пользователя
RUN groupadd -r appuser && \
    useradd -r -g appuser -u 1000 appuser && \
    mkdir -p /app && \
    chown -R appuser:appuser /app

WORKDIR /app

# Копируем виртуальное окружение из builder stage
COPY --from=builder --chown=appuser:appuser /app/.venv /app/.venv

# Копируем исходный код
COPY --from=builder --chown=appuser:appuser /app/src /app/src

# Копируем pyproject.toml для метаданных (опционально)
COPY --chown=appuser:appuser pyproject.toml poetry.lock* ./

# Переключаемся на непривилегированного пользователя
USER appuser

# Переменные окружения
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app \
    APP_ENV=prod


# Expose порты (если нужны)
EXPOSE 8080

# Запуск приложения
CMD ["python", "-m", "src.app.main"]
