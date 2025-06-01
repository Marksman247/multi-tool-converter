from pint import UnitRegistry

ureg = UnitRegistry()

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
                value = float(value)
                result = (value * ureg(from_unit)).to(to_unit)
                st.success(f"{value} {from_unit} = {result.magnitude:.2f} {to_unit}")
            except Exception as e:
                st.error(f"Error: {e}")
