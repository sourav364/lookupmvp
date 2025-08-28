.PHONY: install api app worker test up

install:
pip install -r requirements.txt

api:
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

app:
streamlit run app/app.py --server.port 8501 --server.address 0.0.0.0

worker:
python worker/worker.py

test:
pytest -q

up:
docker compose -f infra/docker/docker-compose.yml up --build
