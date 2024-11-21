PROJECT_NAME := python-ocr

install:
	python -m venv venv
	source venv/bin/activate && pip install -r requirements.txt

run:
	docker run -d \
		--rm \
		-v .:/app \
		--name ${PROJECT_NAME} \
		${PROJECT_NAME}

build:
	docker build -t ${PROJECT_NAME} .

logs:
	docker logs ${PROJECT_NAME}

shell:
	docker exec -it ${PROJECT_NAME} /bin/bash

stop:
	docker stop ${PROJECT_NAME}

remove:
	docker rm ${PROJECT_NAME}

volumes:
	docker volume ls

clear:
	make stop && make remove && make volumes