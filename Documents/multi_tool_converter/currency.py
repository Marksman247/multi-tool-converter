from forex_python.converter import CurrencyRates

c = CurrencyRates()

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
                result = c.convert(from_currency, to_currency, float(amount))
                result = round(result, 2)
                st.success(f"{amount} {from_currency} = {result} {to_currency}")
            except Exception as e:
                st.error(f"Error: {e}")
