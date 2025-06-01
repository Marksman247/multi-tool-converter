import streamlit as st
from forex_python.converter import CurrencyRates
from pint import UnitRegistry

# Initialize
c = CurrencyRates()
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

# Reset button
if st.button("🔄 Reset"):
    st.experimental_rerun()

# Select converter type
option = st.sidebar.radio("Select Converter", ["Currency", "Unit", "Temperature"])

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
                rate = c.get_rate(from_currency, to_currency)
                result = round(amount_float * rate, 2)
                st.success(f"{amount} {from_currency} = {result} {to_currency}")
            except Exception as e:
                st.error(f"Conversion error: {e}")

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
                quantity = float(value) * ureg(from_unit)
                result = quantity.to(to_unit).magnitude
                st.success(f"{value} {from_unit} = {round(result, 4)} {to_unit}")
            except Exception as e:
                st.error(f"Conversion error: {e}")

elif option == "Temperature":
    st.subheader("🌡️ Temperature Converter")
    temp_value = st.text_input("Value", placeholder="Enter temperature")
    from_temp = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_temp = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

    if st.button("Convert Temperature"):
        if not temp_value:
            st.warning("Please enter a value.")
        else:
            try:
                val = float(temp_value)
                # Convert to Celsius first
                if from_temp == "Celsius":
                    celsius = val
                elif from_temp == "Fahrenheit":
                    celsius = (val - 32) * 5/9
                else:  # Kelvin
                    celsius = val - 273.15

                # Convert from Celsius to target
                if to_temp == "Celsius":
                    result = celsius
                elif to_temp == "Fahrenheit":
                    result = celsius * 9/5 + 32
                else:  # Kelvin
                    result = celsius + 273.15

                st.success(f"{temp_value}° {from_temp} = {round(result, 2)}° {to_temp}")
            except Exception as e:
                st.error(f"Conversion error: {e}")

# Footer
st.markdown("""
<hr>
<center style='color: gray;'>Built with ❤️ using Streamlit</center>
""", unsafe_allow_html=True)
