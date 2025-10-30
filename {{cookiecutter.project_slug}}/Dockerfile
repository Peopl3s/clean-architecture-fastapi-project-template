# =============================================================================
# Stage 1: Base image with system dependencies
# =============================================================================
FROM python:3.14-slim-bookworm AS base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYTHONPATH="/app/src"

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Create non-root user
RUN groupadd --gid 1000 appuser && \
    useradd --uid 1000 --gid appuser --shell /bin/bash --create-home appuser

# =============================================================================
# Stage 2: Dependencies installation
# =============================================================================
FROM base AS deps

# Set working directory
WORKDIR /app

# Copy dependency files and README (required by hatchling)
COPY pyproject.toml README.md ./

# Create virtual environment and install dependencies
RUN poetry config virtualenvs.create true && \
    poetry config virtualenvs.in-project true && \
    poetry env use python3.12 && \
    poetry install --no-root --only main --no-interaction --no-ansi

# =============================================================================
# Stage 3: Development dependencies (optional)
# =============================================================================
FROM deps AS deps-dev

# Install development dependencies
RUN poetry install --no-root --no-interaction --no-ansi

# =============================================================================
# Stage 4: Production image
# =============================================================================
FROM deps AS production

# Set working directory
WORKDIR /app

# Copy application code
COPY --chown=appuser:appuser src/ ./src/
COPY --chown=appuser:appuser alembic.ini ./

# Create necessary directories
RUN mkdir -p /app/logs /app/htmlcov && \
    chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/api/docs || exit 1

# Default command
CMD ["poetry", "run", "python", "-m", "{{cookiecutter.project_slug}}/main.py"]

# =============================================================================
# Stage 5: Development image
# =============================================================================
FROM deps-dev AS development

# Set working directory
WORKDIR /app

# Copy application code
COPY --chown=appuser:appuser src/ ./src/
COPY --chown=appuser:appuser alembic.ini ./
COPY --chown=appuser:appuser tests/ ./tests/
COPY --chown=appuser:appuser docs/ ./docs/
COPY --chown=appuser:appuser Makefile ./

# Create necessary directories
RUN mkdir -p /app/logs /app/htmlcov && \
    chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8000

# Default command for development
CMD ["poetry", "run", "uvicorn", "src.{{cookiecutter.project_slug}}.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# =============================================================================
# Stage 6: Testing image
# =============================================================================
FROM deps-dev AS testing

# Set working directory
WORKDIR /app

# Copy application code and tests
COPY --chown=appuser:appuser src/ ./src/
COPY --chown=appuser:appuser tests/ ./tests/
COPY --chown=appuser:appuser alembic.ini ./
COPY --chown=appuser:appuser Makefile ./

# Create necessary directories
RUN mkdir -p /app/logs /app/htmlcov && \
    chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Default command for testing
CMD ["poetry", "run", "pytest", "tests/", "-v", "--cov=src", "--cov-report=html", "--cov-report=term"]
