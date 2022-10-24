build:
	docker build -t ocr.apps.roadtok8s.com -f Dockerfile .


run:
	docker run -p 8181:8181 -e PORT=8181 ocr.apps.roadtok8s.com