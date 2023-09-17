from xllm.cli.fuse import cli_run_fuse

from demo_xllm.core.config import DemoXLLMConfig

if __name__ == "__main__":
    cli_run_fuse(config_cls=DemoXLLMConfig)
