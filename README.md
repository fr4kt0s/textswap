# Python Template

A minimal Python project structure with configuration, logging, and CLI parsing.

## Features

- Central logging setup (console + file)  
- YAML configuration via `ConfigReader` with dot notation  
- Simple CLI with `--config` flag  
- Uses `pathlib.Path` throughout  
- PEP 8–compliant code

## Quick Start

1. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt

project_root/
├── main.py              # Entry point
├── config/
│   ├── config.yaml      # Main config
│   └── config.example.yaml
├── logs/
│   └── app.log          # Auto-created
├── python_template/
│   └── utils/
│       ├── logging_setup.py
│       ├── config.py
│       └── cli.py
└── pyproject.toml
