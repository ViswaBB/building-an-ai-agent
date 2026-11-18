# building-an-ai-agent

A Python project for building an AI agent with the OpenAI SDK.

## Requirements

- Python 3.13+
- [`uv`](https://docs.astral.sh/uv/getting-started/installation/)
- An OpenAI API key

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/ViswaBB/building-an-ai-agent.git
   cd building-an-ai-agent
   ```

2. **Install dependencies**

   ```bash
   uv sync
   ```

   This creates a virtual environment and installs the packages from `pyproject.toml` and `uv.lock`.

3. **Configure environment variables**

   Create a `.env` file in the project root:

   ```bash
   touch .env
   ```

   Add your API key:

   ```dotenv
   OPENAI_API_KEY=sk-your-key-here
   ```

4. **Run the project**

   ```bash
   uv run main.py
   ```

   Expected output:

   ```text
   Hello from ai-agent!
   ```

## Project structure

```text
.
├── main.py          # Entrypoint
├── pyproject.toml   # Project metadata and dependencies
├── uv.lock          # Locked dependency versions
├── .env             # Local secrets (not committed)
└── README.md
```

## Dependencies

- [`openai`](https://pypi.org/project/openai/) — OpenAI API client
- [`python-dotenv`](https://pypi.org/project/python-dotenv/) — loads variables from `.env`

To add another dependency:

```bash
uv add <package>
```

## Environment variables

| Variable         | Description                  |
| ---------------- | ---------------------------- |
| `OPENAI_API_KEY` | Your OpenAI API key          |

Keep secrets in `.env` and never commit that file.
