from dataclasses import dataclass, field

from xllm.core.config import HuggingFaceConfig

from xllm_demo.core.constants import DATASET_KEY


@dataclass
class DemoXLLMConfig(HuggingFaceConfig):
    text_field: str = field(default="chosen", metadata={
        "help": "Field for Antropic RLHF dataset",
    })
    dataset_key: str = field(default=DATASET_KEY, metadata={
        "help": "Dataset key",
    })
