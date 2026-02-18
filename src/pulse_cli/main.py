#!/usr/bin/env python3
"""
Pulse CLI - Main entry point.

Usage:
    pulse login                           # Authenticate with Pulse
    pulse extract path/to/document.pdf    # Parse document to markdown
    pulse schema doc.pdf -s schema.json   # Extract structured data
    pulse jobs <job_id>                   # Check job status
"""

import argparse
import sys
from typing import Optional

from .commands import extract, jobs, login, schema
from . import __version__


def create_parser() -> argparse.ArgumentParser:
    """Create the main argument parser with all subcommands."""
    parser = argparse.ArgumentParser(
        prog="pulse",
        description="Parse, extract, and process documents from the command line.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  pulse extract document.pdf              # Parse a single file
  pulse extract ./docs                    # Parse an entire folder
  pulse schema invoice.pdf -s schema.json # Extract with a schema
  pulse jobs abc123                       # Check job status

Supported file types:
  PDF:       .pdf
  Images:    .png, .jpg, .jpeg
  Office:    .doc, .docx, .ppt, .pptx
  Sheets:    .xls, .xlsx
        """,
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "--api-key",
        help="Pulse API key (overrides stored credentials and PULSE_API_KEY env var)",
        dest="api_key",
    )
    parser.add_argument(
        "--base-url",
        help="Override the default API base URL",
        dest="base_url",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Login command
    login_parser = subparsers.add_parser(
        "login",
        help="Authenticate your CLI session",
        description="Opens Pulse Studio in your browser for secure authentication.",
    )
    login_parser.add_argument(
        "--token",
        help="Directly provide an API token instead of browser auth",
    )
    login_parser.set_defaults(func=login.run)

    # Extract command (equivalent to reducto parse)
    extract_parser = subparsers.add_parser(
        "extract",
        help="Parse documents into structured markdown",
        description="Convert documents into structured markdown output. Outputs are written as <filename>.extract.md",
    )
    extract_parser.add_argument(
        "path",
        help="Path to a file or directory. Directories are scanned recursively.",
    )
    extract_parser.add_argument(
        "--agentic",
        action="store_true",
        help="Enable all agentic options for enhanced accuracy (increases latency)",
    )
    extract_parser.add_argument(
        "--figures",
        action="store_true",
        help="Extract figures from the document",
    )
    extract_parser.add_argument(
        "--figure-description",
        action="store_true",
        help="Generate descriptive captions for extracted figures",
        dest="figure_description",
    )
    extract_parser.add_argument(
        "--html",
        action="store_true",
        help="Include HTML representation alongside markdown",
    )
    extract_parser.add_argument(
        "--pages",
        help="Page range filter (e.g., '1-2' or '1-2,5')",
    )
    extract_parser.add_argument(
        "--chunking",
        help="Chunking strategies (e.g., 'semantic,header,page,recursive')",
    )
    extract_parser.add_argument(
        "--chunk-size",
        type=int,
        help="Maximum characters per chunk when chunking is enabled",
        dest="chunk_size",
    )
    extract_parser.add_argument(
        "--async",
        action="store_true",
        help="Submit as async job and return immediately",
        dest="use_async",
    )
    extract_parser.add_argument(
        "--output-dir",
        "-o",
        help="Output directory for extracted files (default: same as input)",
        dest="output_dir",
    )
    extract_parser.add_argument(
        "--no-storage",
        action="store_true",
        help="Disable cloud storage of extraction artifacts",
        dest="no_storage",
    )
    extract_parser.set_defaults(func=extract.run)

    # Schema command (equivalent to reducto extract)
    schema_parser = subparsers.add_parser(
        "schema",
        help="Extract structured data according to a JSON Schema",
        description="Pull structured data from documents according to a JSON Schema. Outputs are written as <filename>.schema.json",
    )
    schema_parser.add_argument(
        "path",
        help="Path to a file or directory. Directories are scanned recursively.",
    )
    schema_parser.add_argument(
        "--schema",
        "-s",
        required=True,
        help="JSON Schema file path or inline JSON string",
        dest="schema_file",
    )
    schema_parser.add_argument(
        "--prompt",
        "-p",
        help="Natural language prompt to guide schema extraction",
    )
    schema_parser.add_argument(
        "--pages",
        help="Page range filter (e.g., '1-2' or '1-2,5')",
    )
    schema_parser.add_argument(
        "--async",
        action="store_true",
        help="Submit as async job and return immediately",
        dest="use_async",
    )
    schema_parser.add_argument(
        "--output-dir",
        "-o",
        help="Output directory for schema files (default: same as input)",
        dest="output_dir",
    )
    schema_parser.add_argument(
        "--reuse-extract",
        action="store_true",
        help="Reuse existing .extract.md files if available",
        dest="reuse_extract",
    )
    schema_parser.set_defaults(func=schema.run)

    # Jobs command
    jobs_parser = subparsers.add_parser(
        "jobs",
        help="Check status of async jobs",
        description="Check the status and retrieve results of asynchronous jobs.",
    )
    jobs_parser.add_argument(
        "job_id",
        help="Job ID to check status for",
    )
    jobs_parser.add_argument(
        "--wait",
        action="store_true",
        help="Wait for job completion",
    )
    jobs_parser.add_argument(
        "--cancel",
        action="store_true",
        help="Cancel the job instead of checking status",
    )
    jobs_parser.set_defaults(func=jobs.run)

    return parser


def main(args: Optional[list] = None) -> int:
    """Main entry point for the CLI."""
    parser = create_parser()
    parsed_args = parser.parse_args(args)

    if parsed_args.command is None:
        parser.print_help()
        return 0

    try:
        return parsed_args.func(parsed_args)
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        return 130
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

