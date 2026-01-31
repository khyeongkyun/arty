# src/config/settings.py
from pathlib import Path
import yaml

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_CONFIG_PATH = _PROJECT_ROOT / "config" / "local.yaml"

def load_config() -> dict:
    if not _CONFIG_PATH.exists():
        raise FileNotFoundError(f"Config file not found: {_CONFIG_PATH}")

    with _CONFIG_PATH.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

CONFIG = load_config()
