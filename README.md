# Market Data Service

Market Data Service provides APIs for weather, electricity prices, and DUoS (Distribution Use of System) data management.

## Features

- Weather data API
- Wholesale/Retail electricity prices API
- DUoS charge data API
- Swagger UI documentation

## Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL 15+

### Installation

```bash
# Clone repository
git clone https://github.com/Colin-Bao/market-data-service.git
cd market-data-service

# Install dependencies (using uv)
uv sync

# Or using pip
pip install -r requirements.txt
```

### Running

```bash
# Using uv
uv run python run.py

# Or using Flask
flask run
```

### Health Check

```bash
curl http://localhost:5000/health
# Response: {"status": "ok"}
```

### API Documentation

Access Swagger UI at: http://localhost:5000/apidocs

## Testing

```bash
uv run pytest tests/ -v
```

## Project Structure

```
market-data-service/
├── app/
│   ├── __init__.py       # Flask factory
│   ├── routes/           # API endpoints
│   ├── models/           # Data models
│   └── services/         # Business logic
├── tests/                # Test suite
├── run.py                # Entry point
└── README.md             # This file
```

## License

MIT