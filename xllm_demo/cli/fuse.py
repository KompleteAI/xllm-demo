from xllm.cli.fuse import cli_run_fuse

from xllm_demo.core.config import DemoXLLMConfig

if __name__ == "__main__":
    cli_run_fuse(config_cls=DemoXLLMConfig)
