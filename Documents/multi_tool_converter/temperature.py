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
                temp_value = float(temp_value)
                temp = temp_value * ureg.degC  # Default

                if from_temp == "Fahrenheit":
                    temp = temp_value * ureg.degF
                elif from_temp == "Kelvin":
                    temp = temp_value * ureg.kelvin

                # Convert to target
                if to_temp == "Celsius":
                    result = temp.to('degC').magnitude
                    unit = "°C"
                elif to_temp == "Fahrenheit":
                    result = temp.to('degF').magnitude
                    unit = "°F"
                elif to_temp == "Kelvin":
                    result = temp.to('kelvin').magnitude
                    unit = "K"

                st.success(f"{temp_value}° {from_temp} = {result:.2f}{unit}")
            except Exception as e:
                st.error(f"Error: {e}")
