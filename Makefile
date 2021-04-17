##############################
ENVIRONMENT_PREFIX=$(shell pwd)
ENVIRONMENT_NAME=venv
VENV_NAME=${ENVIRONMENT_PREFIX}/${ENVIRONMENT_NAME}
VENV_BIN=${VENV_NAME}/bin
VENV_PYTHON=${VENV_BIN}/python3

# Virtualenv for project
dev: requirements.txt
	echo "Creating virtual environment..."
	${VENV_BIN}/pip-sync requirements.txt

requirements.txt: venv
	${VENV_BIN}/pip-compile requirements.in --output-file requirements.txt

venv: requirements.in
	echo "Compiling requirements..."
	python3 -m venv ${ENVIRONMENT_NAME}
	${VENV_BIN}/pip3 install --upgrade 'pip'
	${VENV_BIN}/pip3 install pip-tools 'numpy' 'scipy' 'setuptools>=41.0.0' 'ipykernel'
	# python3 -m ipykernel install --user --name=${ENVIRONMENT_NAME}
