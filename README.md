# Dockerized Python API 


This repo demonstrates a small CI pipeline that builds a simple Flask API and a PostgreSQL database using Docker Compose, then runs integration tests inside the running API container via GitHub Actions.


## Files
- `app.py` — Minimal Flask application
- `requirements.txt` — Python dependencies
- `Dockerfile` — Container image for the API
- `docker-compose.yml` — Orchestration for API + PostgreSQL
- `test_app.py` — Integration test run against `/health`
- `.github/workflows/ci.yml` — GitHub Actions pipeline


## Local development
1. Build and run locally:


```bash
# start services
docker compose up --build -d


# view API
curl http://localhost:5000/health


# run tests locally (from host) - ensure Python and requests are installed
python3 test_app.py


# stop and remove
docker compose down -v
