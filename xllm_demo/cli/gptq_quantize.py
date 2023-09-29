from xllm.cli.gptq_quantize import cli_run_gptq_quantize
from xllm.datasets.registry import datasets_registry

from xllm_demo.core.constants import DATASET_KEY
from xllm_demo.core.config import DemoXLLMConfig
from xllm_demo.core.dataset import AntropicDataset

if __name__ == "__main__":
    datasets_registry.add(key=DATASET_KEY, item=AntropicDataset)
    cli_run_gptq_quantize(config_cls=DemoXLLMConfig)
