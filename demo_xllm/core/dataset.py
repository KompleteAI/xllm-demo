from tqdm import tqdm
import datasets

from xllm.datasets.base import BaseDataset
from xllm.types import RawSample
from xllm import enums

from demo_xllm.core.config import DemoXLLMConfig


class AntropicDataset(BaseDataset):
    _HF_DATASET_ID = "Anthropic/hh-rlhf"

    @classmethod
    def download(cls, config: DemoXLLMConfig) -> tuple[list[RawSample], list[RawSample] | None]:
        rlhf_dataset = datasets.load_dataset(cls._HF_DATASET_ID)

        parsed_data: dict[str, list[RawSample]] = dict()

        for split in ["train", "test"]:

            parsed_data[split] = list()

            for sample in tqdm(rlhf_dataset[split], desc=f"Parsing {split}"):
                text_parts = sample[config.text_field].split("\n\n")[1:]

                parsed_data[split].append(text_parts)

        train = parsed_data["train"]
        evaluation = parsed_data["test"]

        return train, evaluation

    def get_sample(self, index: int) -> RawSample:
        sample = {
            enums.General.text_parts: self.data[index]
        }
        return sample
