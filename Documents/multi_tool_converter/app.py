import streamlit as st
from forex_python.converter import CurrencyRates
from pint import UnitRegistry

# Initialize unit registry
ureg = UnitRegistry()

# Set page config
st.set_page_config(page_title="🚀 Multi-Tool Converter", layout="centered")

# Custom CSS
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

# Reset button logic
if st.button("🔄 Reset"):
    st.experimental_rerun()

# Converter selection sidebar
option = st.sidebar.radio("Select Converter", ["Currency", "Unit", "Temperature"])

# Currency converter
if option == "Currency":
    st.subheader("💱 Currency Converter")
    amount = st.text_input("Amount", placeholder="Enter amount")
    from_currency = st.selectbox("From Currency", ["USD", "EUR", "NGN", "GBP"])
    to_currency = st.selectbox("To Currency", ["USD", "EUR", "NGN", "GBP"])

    if st.button("Convert Currency"):
        if not amount:
            st.warning("Please enter an amount.")
        else:
            try:
                amount_float = float(amount)
                c = CurrencyRates()
                rate = c.get_rate(from_currency, to_currency)
                result = round(amount_float * rate, 4)
                st.success(f"{amount_float} {from_currency} = {result} {to_currency}")
            except Exception as e:
                st.error(f"Conversion error: {e}")

# Unit converter
elif option == "Unit":
    st.subheader("📏 Unit Converter")
    value = st.text_input("Value", placeholder="Enter value")
    from_unit = st.selectbox("From Unit", ["meters", "kilometers", "miles"])
    to_unit = st.selectbox("To Unit", ["meters", "kilometers", "miles"])

    if st.button("Convert Unit"):
        if not value:
            st.warning("Please enter a value.")
        else:
            try:
                val_float = float(value)
                quantity = val_float * ureg(from_unit)
                converted = quantity.to(to_unit)
                st.success(f"{val_float} {from_unit} = {round(converted.magnitude, 4)} {to_unit}")
            except Exception as e:
                st.error(f"Conversion error: {e}")

# Temperature converter
elif option == "Temperature":
    st.subheader("🌡️ Temperature Converter")
    temp_value = st.text_input("Value", placeholder="Enter temperature")
    from_temp = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_temp = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

    def convert_temperature(value, from_unit, to_unit):
        # Convert input to Celsius first
        if from_unit == "Celsius":
            celsius = value
        elif from_unit == "Fahrenheit":
            celsius = (value - 32) * 5 / 9
        elif from_unit == "Kelvin":
            celsius = value - 273.15
        else:
            raise ValueError("Unsupported temperature unit")

        # Convert from Celsius to target
        if to_unit == "Celsius":
            return celsius
        elif to_unit == "Fahrenheit":
            return (celsius * 9 / 5) + 32
        elif to_unit == "Kelvin":
            return celsius + 273.15
        else:
            raise ValueError("Unsupported temperature unit")

    if st.button("Convert Temperature"):
        if not temp_value:
            st.warning("Please enter a value.")
        else:
            try:
                temp_float = float(temp_value)
                result = convert_temperature(temp_float, from_temp, to_temp)
                st.success(f"{temp_float}° {from_temp} = {round(result, 2)}° {to_temp}")
            except Exception as e:
                st.error(f"Conversion error: {e}")

# Footer
st.markdown("""
<hr>
<center style='color: gray;'>Built with ❤️ using Streamlit</center>
""", unsafe_allow_html=True)
