import streamlit as st
import requests
from pint import UnitRegistry

# Initialize Unit Registry for unit conversions
ureg = UnitRegistry()

# ExchangeRate-API config
API_KEY = "541335f3500f4529dc48dca9"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def get_exchange_rate(from_currency: str, to_currency: str) -> float | None:
    try:
        response = requests.get(BASE_URL + from_currency)
        data = response.json()
        if data['result'] == 'success':
            rates = data['conversion_rates']
            return rates.get(to_currency)
        else:
            return None
    except Exception:
        return None

# Streamlit page config and CSS
st.set_page_config(page_title="🚀 Multi-Tool Converter", layout="centered")

st.markdown("""
    <style>
        .main-header {
            background-color: #007bff;
            padding: 18px;
            border-radius: 12px;
            text-align: center;
            margin-bottom: 30px;
        }
        .main-header h1 {
            color: white;
            font-size: 36px;
            margin: 0;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5em 1.3em;
            cursor: pointer;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        input[type=number]::-webkit-inner-spin-button, 
        input[type=number]::-webkit-outer-spin-button {
            -webkit-appearance: none;
            margin: 0;
        }
        input[type=number] {
            -moz-appearance: textfield;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🚀 Multi-Tool Converter</h1>
</div>
""", unsafe_allow_html=True)

# Reset button (reruns the app)
if st.button("🔄 Reset"):
    st.experimental_rerun()

# Sidebar selection
option = st.sidebar.radio("Select Converter", ["Currency", "Unit", "Temperature"])

# Currency Converter
if option == "Currency":
    st.subheader("💱 Currency Converter")
    amount = st.text_input("Amount", placeholder="Enter amount", key="currency_amount")
    from_currency = st.selectbox("From Currency", ["USD", "EUR", "NGN", "GBP"])
    to_currency = st.selectbox("To Currency", ["USD", "EUR", "NGN", "GBP"])

    if st.button("Convert Currency"):
        if not amount:
            st.warning("Please enter an amount.")
        else:
            try:
                rate = get_exchange_rate(from_currency, to_currency)
                if rate:
                    result = round(float(amount) * rate, 2)
                    st.success(f"{amount} {from_currency} = {result} {to_currency}")
                    st.info(f"Exchange Rate: 1 {from_currency} = {rate} {to_currency}")
                else:
                    st.error("Conversion error: Could not fetch currency rates.")
            except ValueError:
                st.error("Invalid input. Enter a numeric value.")

# Unit Converter
elif option == "Unit":
    st.subheader("📏 Unit Converter")
    value = st.text_input("Value", placeholder="Enter value", key="unit_value")
    from_unit = st.selectbox("From Unit", ["meters", "kilometers", "miles"])
    to_unit = st.selectbox("To Unit", ["meters", "kilometers", "miles"])

    if st.button("Convert Unit"):
        if not value:
            st.warning("Please enter a value.")
        else:
            try:
                qty = float(value) * ureg(from_unit)
                result = qty.to(to_unit).magnitude
                st.success(f"{value} {from_unit} = {round(result, 4)} {to_unit}")
            except Exception as e:
                st.error(f"Conversion error: {str(e)}")

# Temperature Converter
elif option == "Temperature":
    st.subheader("🌡️ Temperature Converter")
    temp_value = st.text_input("Value", placeholder="Enter temperature", key="temp_value")
    from_temp = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_temp = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

    def convert_temperature(value, from_scale, to_scale):
        # Convert input value to Celsius first
        if from_scale == to_scale:
            return value
        if from_scale == "Celsius":
            celsius = value
        elif from_scale == "Fahrenheit":
            celsius = (value - 32) * 5/9
        elif from_scale == "Kelvin":
            celsius = value - 273.15

        # Convert Celsius to target scale
        if to_scale == "Celsius":
            return celsius
        elif to_scale == "Fahrenheit":
            return (celsius * 9/5) + 32
        elif to_scale == "Kelvin":
            return celsius + 273.15

    if st.button("Convert Temperature"):
        if not temp_value:
            st.warning("Please enter a temperature value.")
        else:
            try:
                temp_val = float(temp_value)
                result = convert_temperature(temp_val, from_temp, to_temp)
                st.success(f"{temp_val}° {from_temp} = {round(result, 2)}° {to_temp}")
            except ValueError:
                st.error("Invalid input. Enter a numeric value.")

# Footer
st.markdown("""
<hr>
<center style='color: gray;'>Built with ❤️ using Streamlit</center>
""", unsafe_allow_html=True)
