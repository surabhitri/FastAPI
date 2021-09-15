install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		pip3 install --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint

test:
	python -m pytest -vv test.py

format:
	black *.py

run:
	python main.py

run-uvicorn:
	uvicorn main:app --reload

killweb:
	sudo killall uvicorn


all: install test