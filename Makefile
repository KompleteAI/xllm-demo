#* Poetry
.PHONY: poetry-download
poetry-download:  ## Download and install Poetry
	curl -sSL https://install.python-poetry.org | $(PYTHON) -

.PHONY: poetry-remove
poetry-remove:  ## Remove / uninstall Poetry
	curl -sSL https://install.python-poetry.org | $(PYTHON) - --uninstall
	
#* Run
.PHONY
download:  ## Download and prepare
	poetry run python demo_xllm/cli/download.py
	
.PHONY
train:  ## Train model
	poetry run python demo_xllm/cli/train.py
	
.PHONY
fuse:  ## Fuse model
	poetry run python demo_xllm/cli/fuse.py
	
.PHONY
fuse:  ## GPTQ quantization
	poetry run python demo_xllm/cli/gptq_quantization.py
