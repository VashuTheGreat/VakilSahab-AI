FROM python:3.12-slim

WORKDIR /app

# Force CPU Torch


COPY requirements.txt .
COPY pyproject.toml .
# Install uv
RUN pip install --no-cache-dir uv

# Install dependencies into system python (no venv needed)
RUN uv pip install --system .


# Copy project
COPY . .


CMD ["uv", "run", "main.py"]