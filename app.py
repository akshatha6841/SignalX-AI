import streamlit as st
import yfinance as yf

st.title("SignalX AI")

stock = st.text_input("Enter Stock Symbol (e.g. TCS.NS)")

if stock:
    data = yf.download(stock, period="1mo")
    st.line_chart(data["Close"])

    if data["Close"].iloc[-1] > data["Close"].mean():
        st.success("Bullish Signal Detected 🚀")
    else:
        st.warning("No strong signal")

    question = st.text_input("Ask AI about this stock")

    if question:
        st.write("AI Insight: This stock shows moderate momentum based on recent trends.")
