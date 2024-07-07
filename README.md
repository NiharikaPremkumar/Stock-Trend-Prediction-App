---

# Stock Trend Prediction App

This web application predicts stock trends using machine learning models integrated with Django and Streamlit.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Project](#running-the-project)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Stock Trend Prediction App combines the power of Django for backend development and Streamlit for frontend visualization. It allows users to input a stock ticker symbol and view historical stock data, visualize trends, and see predictions using a simple machine learning model.

The application leverages Yahoo Finance (via `yfinance` library) to fetch historical stock data, `scikit-learn` for machine learning modeling, and `matplotlib` for plotting visualizations.

### Features

- **Input Form**: Users can enter a stock ticker symbol and select a date range to analyze.
- **Visualization**: Interactive charts display historical stock prices and predicted trends.
- **Prediction**: Machine learning model predicts future stock prices based on historical data.
- **Responsive**: Designed with Django templates and integrated Streamlit app for seamless user experience.

## Project Structure

The project structure follows a typical Django application setup with an integrated Streamlit app for data visualization.

```
stock_app/
├── stock_app/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── prediction/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── prediction/
│   │   │   ├── streamlit_app.html
│   ├── stock_trend_app.py
├── manage.py
├── README.md
```

- **`stock_app/`**: Django project settings and configurations.
- **`prediction/`**: Django app containing views, URLs, templates, and the Streamlit integration.
- **`prediction/templates/prediction/`**: HTML templates, including `streamlit_app.html` for embedding Streamlit app.

## Setup Instructions

Follow these steps to set up and run the Stock Trend Prediction App on your local machine.

### Prerequisites

- Python 3.x installed on your system.
- `pip` package manager.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/stock_trend_prediction.git
   cd stock_trend_prediction
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Project

1. **Run the Streamlit App**

   Open a terminal and navigate to the project directory. Run the Streamlit app:

   ```bash
   streamlit run prediction/stock_trend_app.py
   ```

   This will start the Streamlit app on `http://localhost:8501`.

2. **Run the Django Server**

   Open another terminal and navigate to the project directory. Run the Django server:

   ```bash
   python manage.py runserver
   ```

   The Django server will start on `http://localhost:8000`.

3. **Access the Application**

   Open a web browser and go to `http://localhost:8000/streamlit/`. You should see the Stock Trend Prediction App interface.

# Results
You now have a complete Django project integrated with a Streamlit app. Your project is ready to be uploaded to GitHub, showcasing your skills in prompt engineering with ChatGPT. This guide includes the necessary files and setup instructions to help others understand and run your project.


<img width="1440" alt="ss1" src="https://github.com/NiharikaPremkumar/Stock-Trend-Prediction-App/assets/147183384/d9e99447-09b3-446f-8737-e5d1145c03d2">


<img width="1440" alt="SCR-20240707-ovep" src="https://github.com/NiharikaPremkumar/Stock-Trend-Prediction-App/assets/147183384/c439fe51-9a0a-4498-9909-6b81de8b8f31">


## Usage

- Enter a stock ticker symbol (e.g., AAPL for Apple).
- Select a date range to analyze historical data.
- View plotted charts of historical stock prices and predicted trends.
- Analyze predictions made by the machine learning model.

## Technologies Used

- **Django**: Backend framework for web development.
- **Streamlit**: Frontend framework for interactive data visualization.
- **Python Libraries**: `yfinance`, `scikit-learn`, `matplotlib`, `pandas` for data fetching, machine learning modeling, and plotting.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

