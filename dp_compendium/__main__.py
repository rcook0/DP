"""
dp_compendium.__main__

Allows running the package directly:
    python -m dp_compendium <subcommand> [options]

This is equivalent to using the installed `dp-cli` entrypoint.
"""

from .cli import main

if __name__ == "__main__":
    main()
