import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from datetime import date

# Set up the Streamlit app
st.title('Stock Trend Prediction App')

# Sidebar for user input
st.sidebar.header('User Input')
selected_stock = st.sidebar.text_input('Stock Ticker', 'AAPL')
start_date = st.sidebar.date_input('Start Date', value=date(2010, 1, 1))
end_date = st.sidebar.date_input('End Date', value=date.today())

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, start=start_date, end=end_date)
    data.reset_index(inplace=True)
    return data

data = load_data(selected_stock)

st.subheader('Raw data')
st.write(data.tail())

# Plot raw data
def plot_raw_data():
    fig, ax = plt.subplots()
    ax.plot(data['Date'], data['Close'], label='Close Price')
    ax.set_xlabel('Date')
    ax.set_ylabel('Close Price')
    ax.set_title(f'{selected_stock} Close Price History')
    ax.legend()
    st.pyplot(fig)

plot_raw_data()

# Prepare data for prediction
def prepare_data(data):
    data['Date'] = data['Date'].map(pd.Timestamp.toordinal)
    X = data['Date'].values.reshape(-1, 1)
    y = data['Close'].values
    return X, y

X, y = prepare_data(data)

# Train a simple machine learning model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Plot prediction vs actual
st.subheader('Prediction vs Actual')
fig, ax = plt.subplots()
ax.scatter(X_test, y_test, color='blue', label='Actual Price')
ax.scatter(X_test, predictions, color='red', label='Predicted Price')
ax.set_xlabel('Date')
ax.set_ylabel('Close Price')
ax.set_title('Prediction vs Actual')
ax.legend()
st.pyplot(fig)
