from xllm.cli.train import cli_run_train
from xllm.datasets.registry import datasets_registry

from demo_xllm.core.constants import DATASET_KEY
from demo_xllm.core.config import DemoXLLMConfig
from demo_xllm.core.dataset import AntropicDataset

if __name__ == "__main__":
    datasets_registry.add(key=DATASET_KEY, item=AntropicDataset)
    cli_run_train(config_cls=DemoXLLMConfig)