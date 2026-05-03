# Movie Agent

An intelligent AI-powered movie recommendation agent that helps users discover movies tailored to their preferences.

## Overview

Movie Agent is a conversational AI assistant powered by OpenAI's language models and the TMDB (The Movie Database) API. The agent understands natural language queries, asks clarifying questions, and provides personalized movie recommendations based on user preferences like genre, release year, and cast members.

## Features

- **Conversational Interface**: Chat-based interaction with an AI expert named Jeff
- **Smart Recommendations**: Personalized movie suggestions based on user preferences
- **Multi-criteria Search**: Filter by genre, release year, certification, runtime, and more
- **Real-time Details**: Get in-depth information about specific movies
- **Genre Intelligence**: Automatic translation between genre IDs and human-readable names
- **Popular Trends**: Discover what's trending in movies currently

## Purpose

The Movie Agent simplifies the movie discovery process by:
- Eliminating decision fatigue through guided recommendations
- Understanding nuanced preferences through conversational context
- Providing detailed movie information without requiring multiple searches
- Offering a natural language interface to movie databases

## Architecture

### Technology Stack

- **LLM**: OpenAI (gpt-4-turbo) with Pydantic AI framework
- **Movie Data**: TMDB API integration
- **MCP**: Model Context Protocol (FastMCP) for tool integration
- **Runtime**: Python 3.12+ with async/await support

### Component Architecture

```
main.py (CLI Entry)
    ↓
MovieAgent (Orchestrator)
    ↓
├─ OpenAI Client (Language Model)
└─ FastMCP Server (Tools)
    ├─ list_popular_movies_tool
    ├─ discover_movies_tool
    ├─ movie_details_tool
    └─ genre_map_tool
        ↓
    TMDB Client (API Integration)
```

### Core Components

#### **Main (src/main.py)**
- Async CLI loop for user interaction
- Streams responses in real-time
- Maintains conversation history for context

#### **MovieAgent (src/agent/agent.py)**
- Wraps the Pydantic AI Agent
- Integrates FastMCP toolset for movie operations
- Provides streaming interface via `run()` method
- Uses system prompt to define "Jeff" persona and rules

#### **MCP Server (src/mcp/server.py)**
Exposes four tools to the language model:

1. **list_popular_movies_tool**: Returns currently popular movies for open-ended queries
2. **discover_movies_tool**: Searches movies with advanced filters (genre, year, runtime, etc.)
3. **movie_details_tool**: Retrieves detailed information about a specific movie
4. **genre_map_tool**: Maps TMDB genre IDs to human-readable names

#### **Clients**
- **OpenAIClient (src/clients/openai.py)**: Manages LLM interactions
- **TMDBClient (src/clients/tmdb.py)**: Handles all TMDB API calls

#### **Configuration (src/config.py)**
- `TMDBConfig`: Loads TMDB API credentials from environment
- `OpenAIConfig`: Loads OpenAI API credentials from environment

## Installation

### Prerequisites

- Python 3.12 or higher
- OpenAI API key
- TMDB API key

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/CymruLavis/movie_agent.git
   cd movie_agent
   ```

2. **Install dependencies** (using uv package manager)
   ```bash
   uv sync
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   
   TMDB_API_KEY=your_tmdb_api_key
   TMDB_API_READ_ACCESS_TOKEN=your_tmdb_read_access_token
   ```

   Get your keys from:
   - [OpenAI Platform](https://platform.openai.com/api-keys)
   - [TMDB Developer Settings](https://www.themoviedb.org/settings/api)

4. **Verify installation**
   ```bash
   uv run -m src.main
   ```

## Usage

### Running the Agent

```bash
uv run -m src.main
```

### Example Interactions

```
Welcome to the Movie Reccomendation Agent

> I want to watch something with action
Jeff: I'd love to help you find an action movie! Let me show you some popular action films...
[Lists recent action movies and asks for more details]

> Show me sci-fi movies from 2020
Jeff: Great choice! Here are some excellent sci-fi movies from 2020...

> Tell me more about Dune
Jeff: Dune is an epic space opera directed by Denis Villeneuve...

> /exit
Thank you for using the movie reccomendation agent!
```

### Commands

- `/exit` or `/quit`: Exit the application

## Development

### Running Linter and Formatter

```bash
just lint
```

This runs:
- `ruff check --fix` (Fix lint issues)
- `ruff format` (Format code)
- `ruff check` (Final validation)

### Running Tests

```bash
just test-all
```

Or directly:
```bash
python -m pytest -s
```

### Project Structure

```
movie_agent/
├── src/
│   ├── agent/
│   │   ├── agent.py              # MovieAgent class
│   │   └── system_prompt.txt     # Jeff's personality and rules
│   ├── clients/
│   │   ├── openai.py             # OpenAI API client
│   │   └── tmdb.py               # TMDB API client
│   ├── mcp/
│   │   ├── server.py             # FastMCP server and tools
│   │   └── tools/
│   │       ├── discover_movie.py  # Discover movies tool
│   │       ├── genre_map.py       # Genre mapping tool
│   │       ├── list_popular.py    # Popular movies tool
│   │       ├── movie_details.py   # Movie details tool
│   │       └── schemas.py         # Pydantic schemas
│   ├── config.py                 # Configuration classes
│   ├── dependencies.py           # Dependency injection
│   ├── main.py                   # CLI entry point
│   └── schemas.py                # Shared schemas
├── tests/
│   ├── integration/
│   └── unit/
├── pyproject.toml                # Project metadata
├── Justfile                      # Task runner
└── README.md
```

## Configuration

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key | sk-... |
| `TMDB_API_KEY` | TMDB API key | abcd1234... |
| `TMDB_API_READ_ACCESS_TOKEN` | TMDB read access token | eyJhbGc... |

## How It Works

1. **User Input**: User enters a natural language query
2. **Agent Processing**: The LLM analyzes the query and determines which tools to use
3. **Tool Execution**: MCP tools fetch data from TMDB API
4. **Response Generation**: LLM synthesizes a helpful response
5. **Streaming Output**: Response is streamed to the user in real-time
6. **History Management**: Conversation is maintained for contextual follow-ups

### Tool Selection Strategy

- **General requests** → `list_popular_movies_tool`
- **Specific filters** → `discover_movies_tool`
- **Movie details** → `movie_details_tool`
- **Genre references** → `genre_map_tool` (automatic translation)

## Dependencies

Key dependencies:
- `pydantic-ai-slim[openai]`: AI agent framework
- `fastmcp`: Model Context Protocol server
- `openai`: OpenAI API client
- `requests`: HTTP client
- `pydantic`: Data validation
- `python-dotenv`: Environment variable loading
- `rich`: Terminal formatting

See [pyproject.toml](pyproject.toml) for complete dependencies.
