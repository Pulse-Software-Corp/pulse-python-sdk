"""
Configuration and credential management for Pulse CLI.
"""

import json
import os
from pathlib import Path
from typing import Optional

# Supported file extensions
SUPPORTED_EXTENSIONS = {
    ".pdf",  # PDF
    ".png", ".jpg", ".jpeg",  # Images
    ".doc", ".docx", ".ppt", ".pptx",  # Office documents
    ".xls", ".xlsx",  # Spreadsheets
}


def get_config_dir() -> Path:
    """Get the configuration directory for Pulse CLI."""
    # Use XDG_CONFIG_HOME if available, otherwise ~/.config
    xdg_config = os.environ.get("XDG_CONFIG_HOME")
    if xdg_config:
        config_dir = Path(xdg_config) / "pulse"
    else:
        config_dir = Path.home() / ".config" / "pulse"
    
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir


def get_credentials_file() -> Path:
    """Get the path to the credentials file."""
    return get_config_dir() / "credentials.json"


def save_api_key(api_key: str) -> None:
    """Save the API key to the credentials file."""
    creds_file = get_credentials_file()
    creds = {}
    if creds_file.exists():
        try:
            creds = json.loads(creds_file.read_text())
        except json.JSONDecodeError:
            pass
    
    creds["api_key"] = api_key
    creds_file.write_text(json.dumps(creds, indent=2))
    # Set restrictive permissions
    creds_file.chmod(0o600)


def load_api_key() -> Optional[str]:
    """Load the API key from credentials file or environment."""
    # Priority: environment variable > credentials file
    env_key = os.environ.get("PULSE_API_KEY")
    if env_key:
        return env_key
    
    creds_file = get_credentials_file()
    if creds_file.exists():
        try:
            creds = json.loads(creds_file.read_text())
            return creds.get("api_key")
        except (json.JSONDecodeError, KeyError):
            pass
    
    return None


def get_api_key(args) -> Optional[str]:
    """Get API key from args, env, or stored credentials."""
    # Priority: CLI arg > env var > stored credentials
    if hasattr(args, "api_key") and args.api_key:
        return args.api_key
    return load_api_key()


def get_base_url(args) -> Optional[str]:
    """Get base URL from args or environment."""
    if hasattr(args, "base_url") and args.base_url:
        return args.base_url
    return os.environ.get("PULSE_BASE_URL")


def is_supported_file(path: Path) -> bool:
    """Check if a file has a supported extension."""
    return path.suffix.lower() in SUPPORTED_EXTENSIONS


def collect_files(path: Path) -> list[Path]:
    """Collect all supported files from a path (file or directory)."""
    if path.is_file():
        if is_supported_file(path):
            return [path]
        return []
    
    if path.is_dir():
        files = []
        for item in path.rglob("*"):
            if item.is_file() and is_supported_file(item):
                files.append(item)
        return sorted(files)
    
    return []

