# IMAGE_DIR := $(shell pwd)/images
# OUTPUT_DIR := $(shell pwd)/output
IMAGE_DIR := images
OUTPUT_DIR := output


install:
	python -m venv venv
	source venv/bin/activate && pip install -r requirements.txt

lint:
	source venv/bin/activate && pylint script.py

test:
	source venv/bin/activate && python -m unittest discover tests

run:
	docker run -d \
		--rm \
		-v .:/app \
		-v ./images/source:/app/images/source \
		-v ./images/temp:/app/images/temp \
		-v ./images/output:/app/images/output \
		--name python-ocr \
		python-ocr

build:
	docker build -t python-ocr .

logs:
	docker logs python-ocr

shell:
	docker exec -it python-ocr /bin/bash

stop:
	docker stop python-ocr

remove:
	docker rm python-ocr

volumes:
	docker volume ls

clear:
	make stop && make remove && make volumes