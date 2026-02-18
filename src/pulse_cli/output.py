"""
Output formatting utilities for Pulse CLI.
"""

import json
import sys
from typing import Any, Optional


# ANSI color codes
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"


def supports_color() -> bool:
    """Check if the terminal supports colors."""
    if not sys.stdout.isatty():
        return False
    import os
    if os.environ.get("NO_COLOR"):
        return False
    if os.environ.get("FORCE_COLOR"):
        return True
    return True


def colorize(text: str, color: str) -> str:
    """Apply color to text if supported."""
    if supports_color():
        return f"{color}{text}{Colors.RESET}"
    return text


def success(message: str) -> None:
    """Print a success message."""
    print(colorize(f"✓ {message}", Colors.GREEN))


def error(message: str) -> None:
    """Print an error message."""
    print(colorize(f"✗ {message}", Colors.RED), file=sys.stderr)


def warning(message: str) -> None:
    """Print a warning message."""
    print(colorize(f"⚠ {message}", Colors.YELLOW))


def info(message: str) -> None:
    """Print an info message."""
    print(colorize(f"ℹ {message}", Colors.BLUE))


def progress(current: int, total: int, filename: str) -> None:
    """Print a progress indicator."""
    prefix = colorize(f"[{current}/{total}]", Colors.DIM)
    print(f"{prefix} Processing {filename}...")


def print_json(data: Any, indent: int = 2) -> None:
    """Print JSON data with formatting."""
    print(json.dumps(data, indent=indent, default=str))


def format_status(status: str) -> str:
    """Format a job status with color."""
    status_colors = {
        "pending": Colors.YELLOW,
        "processing": Colors.BLUE,
        "completed": Colors.GREEN,
        "failed": Colors.RED,
        "canceled": Colors.DIM,
    }
    color = status_colors.get(status.lower(), Colors.RESET)
    return colorize(status, color)


def format_job_info(job_id: str, status: str, created_at: Optional[str] = None) -> str:
    """Format job information for display."""
    lines = [
        f"Job ID:    {colorize(job_id, Colors.CYAN)}",
        f"Status:    {format_status(status)}",
    ]
    if created_at:
        lines.append(f"Created:   {created_at}")
    return "\n".join(lines)

