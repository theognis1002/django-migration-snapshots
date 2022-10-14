install:
	pip install -r requirements.txt -r requirements_dev.txt
	
package:
	python setup.py sdist

deploy:
	twine upload dist/*
