install_requirements:
	@pip install -r requirements.txt

install:
	@pip install .

install_dev:
	@pip install -e .

uninstall:
	@pip uninstall -y toto

test:
	@coverage run -m pytest tests/*.py
	@coverage report -m --omit=$(VIRTUAL_ENV)/lib/python*


say_hello:
	echo "creating empty file"
	touch text.txt


say_buy:
	echo "removing empty file"
	rm -rf *.txt
