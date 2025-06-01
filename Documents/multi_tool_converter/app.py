import streamlit as st
from pint import UnitRegistry

# Initialize Pint unit registry
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

# Reset button (works by rerunning the script)
if st.button("🔄 Reset"):
    st.experimental_rerun()

# Select converter type
option = st.sidebar.radio("Select Converter", ["Currency", "Unit", "Temperature"])

# Currency converter (keep your working code or replace dummy with actual forex-python later)
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
                result = round(float(amount) * 2, 2)  # Dummy multiply by 2
                st.success(f"{amount} {from_currency} = {result} {to_currency}")
            except:
                st.error("Invalid input. Enter a numeric value.")

# Unit converter with Pint
elif option == "Unit":
    st.subheader("📏 Unit Converter")
    value = st.text_input("Value", placeholder="Enter value")
    from_unit = st.selectbox("From Unit", ["meter", "kilometer", "mile"])
    to_unit = st.selectbox("To Unit", ["meter", "kilometer", "mile"])

    if st.button("Convert Unit"):
        if not value:
            st.warning("Please enter a value.")
        else:
            try:
                quantity = float(value) * ureg(from_unit)
                result = quantity.to(to_unit)
                st.success(f"{value} {from_unit} = {result:.2f}")
            except Exception as e:
                st.error(f"Conversion error: {e}")

# Temperature converter with formulas
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
                temp = float(temp_value)

                if from_temp == to_temp:
                    result = temp
                elif from_temp == "Celsius" and to_temp == "Fahrenheit":
                    result = (temp * 9/5) + 32
                elif from_temp == "Celsius" and to_temp == "Kelvin":
                    result = temp + 273.15
                elif from_temp == "Fahrenheit" and to_temp == "Celsius":
                    result = (temp - 32) * 5/9
                elif from_temp == "Fahrenheit" and to_temp == "Kelvin":
                    result = (temp - 32) * 5/9 + 273.15
                elif from_temp == "Kelvin" and to_temp == "Celsius":
                    result = temp - 273.15
                elif from_temp == "Kelvin" and to_temp == "Fahrenheit":
                    result = (temp - 273.15) * 9/5 + 32

                st.success(f"{temp_value}° {from_temp} = {round(result, 2)}° {to_temp}")
            except Exception as e:
                st.error(f"Conversion error: {e}")

# Footer
st.markdown("""
<hr>
<center style='color: gray;'>Built with ❤️ using Streamlit</center>
""", unsafe_allow_html=True)
