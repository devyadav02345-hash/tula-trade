import streamlit as st

st.set_page_config(page_title="Tula Trade", page_icon="📈")
st.title("📈 Tula Trade - Trading Dashboard")

st.write("Welcome to Tula Trade App!")

balance = st.number_input("Enter Balance", value=10000)
risk = st.slider("Risk %", 1, 10, 2)

if st.button("Calculate"):
    result = balance * risk / 100
    st.success(f"Risk Amount: ₹{result}")

st.info("App successfully deployed!")
