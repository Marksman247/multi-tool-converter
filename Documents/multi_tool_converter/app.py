import streamlit as st

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
                result = round(float(amount) * 2, 2)  # Dummy multiply by 2
                st.success(f"{amount} {from_currency} = {result} {to_currency}")
            except:
                st.error("Invalid input. Enter a numeric value.")

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
                result = round(float(value) * 3, 2)  # Dummy multiply by 3
                st.success(f"{value} {from_unit} = {result} {to_unit}")
            except:
                st.error("Invalid input. Enter a numeric value.")

# Temperature converter
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
                result = round(float(temp_value) + 10, 2)  # Dummy +10
                st.success(f"{temp_value}° {from_temp} = {result}° {to_temp}")
            except:
                st.error("Invalid input. Enter a numeric value.")

# Footer
st.markdown("""
<hr>
<center style='color: gray;'>Built with ❤️ using Streamlit</center>
""", unsafe_allow_html=True)

