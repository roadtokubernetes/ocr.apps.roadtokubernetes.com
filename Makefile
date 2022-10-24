build:
	docker build -t ocr.apps.roadtok8s.com -f Dockerfile .

stop:
	docker stop $$(docker ps | grep 'ocr.apps.roadtok8s.com')

run:
	docker run -p 8181:8181 -e PORT=8181 -e DEBUG=true -e SECRET_TOKEN=P3e5JGzKeGDMYkzJtSefA40ifBH_PKyMFFshE00piis ocr.apps.roadtok8s.com

local_run:
	venv/bin/uvicorn app.main:app --reload --port 8111

test_local:
	venv/bin/pytest . -s

py_secret:
	venv/bin/python -c "import secrets;print(secrets.token_urlsafe(32))"