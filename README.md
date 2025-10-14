# TELCO Customer Churn MLE

A machine learning project for predicting customer churn in telecommunications companies.

## Project Structure

```
TELCO CUSTOMER CHURN MLE/
├── .github/workflows/     # GitHub Actions workflows
├── .gradio/              # Gradio UI configuration
├── .venv/                # Virtual environment
├── artifacts/            # Model artifacts and outputs
├── configs/              # Configuration files
├── data/                 # Data directory
│   ├── external/         # External data sources
│   ├── processed/        # Cleaned and processed data
│   └── raw/              # Original, unprocessed data
├── docker/               # Docker-related files
├── great_expectations/   # Data validation
├── mlruns/               # MLflow runs
├── notebooks/            # Jupyter notebooks
├── scripts/              # Utility scripts
├── src/                  # Source code
├── tests/                # Unit and integration tests
├── .dockerignore         # Docker ignore patterns
├── .gitignore           # Git ignore patterns
├── CLAUDE.md            # Claude AI documentation
├── dockerfile           # Docker configuration
└── README.md            # This file
```

## Getting Started

### Prerequisites

- Python 3.9+
- pip or conda
- Git

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd TELCO-CUSTOMER-CHURN-MLE
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

1. Place your raw data in the `data/raw/` directory
2. Run data preprocessing scripts from the `scripts/` directory
3. Execute model training and evaluation from the `notebooks/` or `src/` directory
4. View results in the `artifacts/` directory

## Data

- **Raw Data**: Place original datasets in `data/raw/`
- **Processed Data**: Cleaned and feature-engineered data in `data/processed/`
- **External Data**: Third-party data sources in `data/external/`

## Development

### Running Tests

```bash
pytest tests/
```

### Code Quality

```bash
# Linting
flake8 src/
black src/

# Type checking
mypy src/
```

## Docker

Build and run with Docker:

```bash
docker build -t telco-churn-ml .
docker run -p 8000:8000 telco-churn-ml
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is licensed under the MIT License.


