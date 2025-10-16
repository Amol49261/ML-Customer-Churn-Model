# Telco Customer Churn Prediction

A comprehensive machine learning pipeline for predicting customer churn in telecommunications companies, featuring end-to-end MLOps practices, model serving, and production-ready deployment.

## Problem Statement

Customer churn is a critical business challenge across the technology sector, from telecommunications and SaaS platforms to e-commerce and fintech companies. With the tech industry's high customer acquisition costs and competitive landscape, predicting and preventing customer churn directly impacts revenue and growth. This project addresses the universal challenge of:

- **Identifying at-risk customers** before they churn across tech verticals
- **Reducing customer acquisition costs** by improving retention strategies
- **Optimizing business strategies** through data-driven customer insights
- **Scaling prediction capabilities** for real-time decision making in high-volume environments

While implemented on telecommunications data, the methodologies and MLOps practices developed here are directly applicable to SaaS churn, subscription cancellations, user engagement decline, and customer lifetime value optimization across the broader technology industry.

The goal is to build a robust, production-ready system that can accurately predict customer churn and provide actionable insights to business stakeholders in any customer-centric tech organization.

## Approach

### Data Science Methodology
- **Exploratory Data Analysis**: Comprehensive analysis of customer demographics, services, and billing patterns
- **Feature Engineering**: Creation of meaningful features from raw customer data
- **Model Selection**: Evaluation of multiple algorithms with XGBoost emerging as the optimal choice
- **Cross-validation**: 5-fold CV for robust model evaluation
- **Hyperparameter Tuning**: Systematic optimization of model parameters

### Machine Learning Pipeline
1. **Data Preprocessing**: Automated cleaning, encoding, and feature transformation
2. **Model Training**: XGBoost classifier with optimized hyperparameters
3. **Model Evaluation**: Comprehensive metrics including ROC-AUC, F1-score, precision, and recall
4. **Model Serving**: FastAPI REST API with Gradio web interface
5. **Monitoring**: MLflow integration for experiment tracking and model versioning

### MLOps Best Practices
- **Data Validation**: Great Expectations for data quality assurance
- **Experiment Tracking**: MLflow for model versioning and performance monitoring
- **API Development**: FastAPI with automatic OpenAPI documentation
- **Containerization**: Docker for consistent deployment environments
- **Testing**: Comprehensive test suite for data validation and model performance

## Results

### Model Performance
- **ROC-AUC Score**: 0.839 (Excellent discriminative ability)
- **F1-Score**: 0.615 (Balanced precision-recall performance)
- **Precision**: 0.488 (Low false positive rate)
- **Recall**: 0.832 (High sensitivity for churn detection)

### Business Impact
- **High Recall**: Captures 83.2% of customers who will churn
- **Actionable Predictions**: Enables targeted retention campaigns
- **Real-time Scoring**: FastAPI serving enables immediate decision-making
- **Scalable Architecture**: Docker containerization supports production deployment

### Key Insights
- Customer tenure and billing patterns are strong churn predictors
- Service usage patterns (internet, phone, streaming) significantly impact retention
- Demographics and contract types play crucial roles in churn likelihood

## Tools & Technologies Used

### Machine Learning & Data Science
- **Python 3.9+**: Core programming language
- **Pandas & NumPy**: Data manipulation and analysis
- **Scikit-learn**: Machine learning algorithms and utilities
- **XGBoost**: Gradient boosting classifier for optimal performance
- **Jupyter**: Interactive data analysis and visualization

### MLOps & Production
- **MLflow**: Experiment tracking, model versioning, and deployment
- **FastAPI**: High-performance REST API for model serving
- **Pydantic**: Data validation and automatic API documentation
- **Gradio**: User-friendly web interface for model demonstrations
- **Docker**: Containerization for consistent deployment

### Data Quality & Validation
- **Great Expectations**: Data quality validation and monitoring
- **Pytest**: Comprehensive testing framework
- **Joblib**: Efficient model serialization and loading

### Development & Deployment
- **Git**: Version control and collaboration
- **Uvicorn**: ASGI server for FastAPI applications
- **Python-dotenv**: Environment variable management

## Project Structure

```
TELCO CUSTOMER CHURN MLE/
├── src/                     # Source code
│   ├── app/                # FastAPI application
│   ├── data/               # Data processing modules
│   ├── features/           # Feature engineering
│   ├── models/             # Model training and evaluation
│   ├── serving/            # Model serving and inference
│   ├── tests/              # Unit and integration tests
│   └── utils/              # Utility functions
├── data/                   # Data directory
│   ├── raw/               # Original datasets
│   ├── processed/         # Cleaned and processed data
│   └── external/          # External data sources
├── notebooks/             # Jupyter notebooks for EDA
├── scripts/               # Pipeline execution scripts
├── mlruns/                # MLflow experiment tracking
├── artifacts/             # Model artifacts and outputs
├── docker/                # Docker configuration
├── great_expectations/    # Data validation
└── tests/                 # Test files
```

## Quick Start

### Prerequisites
- Python 3.9+
- Git
- Docker (optional)

### Installation

1. **Clone the repository**:
```bash
git clone <repository-url>
cd TELCO-CUSTOMER-CHURN-MLE
```

2. **Create virtual environment**:
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

### Usage

1. **Run the complete pipeline**:
```bash
python scripts/run_pipeline.py
```

2. **Start the API server**:
```bash
uvicorn src.app.main:app --host 0.0.0.0 --port 8000
```

3. **Access the web interface**: Navigate to `http://localhost:8000` for the FastAPI docs or `http://localhost:8000/gradio` for the Gradio interface

### Docker Deployment

```bash
docker build -t telco-churn-ml .
docker run -p 8000:8000 telco-churn-ml
```

## API Documentation

The FastAPI application provides comprehensive endpoints:
- `GET /`: Health check endpoint
- `POST /predict`: Customer churn prediction
- `GET /docs`: Interactive API documentation (Swagger UI)

## Model Serving

The production-ready serving solution includes:
- **REST API**: FastAPI with automatic validation
- **Web Interface**: Gradio for manual testing and demonstrations
- **Data Validation**: Pydantic models for input validation
- **Error Handling**: Comprehensive error responses and logging

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


