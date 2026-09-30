# pycalc

Calculadora mínima con API web, pensada para practicar CI/CD con Tekton.

## Uso local

```bash
pip install -r requirements-dev.txt
ruff check .        # lint
pytest -v           # tests
python -m pycalc.app
curl localhost:8000/add/2/3
```

## Endpoints

| Ruta | Respuesta |
| --- | --- |
| `GET /` | Información de la app |
| `GET /add/<a>/<b>` | Suma |
| `GET /subtract/<a>/<b>` | Resta |
| `GET /multiply/<a>/<b>` | Multiplicación |
| `GET /divide/<a>/<b>` | División (400 si `b` es 0) |
