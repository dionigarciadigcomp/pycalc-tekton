FROM python:3.12-slim

WORKDIR /app

# Primero las dependencias (se cachean si no cambian)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Después el código
COPY pycalc/ pycalc/

EXPOSE 8000
CMD ["python", "-m", "pycalc.app"]
