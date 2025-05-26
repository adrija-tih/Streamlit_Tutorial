import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Title
st.title("📊 Sales Dashboard")

# Sidebar filters
st.sidebar.header("Filter Data")

# Simulate some data
@st.cache_data
def load_data():
    np.random.seed(42)
    dates = pd.date_range("2023-01-01", periods=180)
    data = {
        "Date": dates,
        "Region": np.random.choice(["North", "South", "East", "West"], size=180),
        "Sales": np.random.randint(100, 1000, size=180)
    }
    return pd.DataFrame(data)

df = load_data()

# Sidebar region filter
region = st.sidebar.multiselect("Select Region", options=df["Region"].unique(), default=df["Region"].unique())

# Filter data
filtered_df = df[df["Region"].isin(region)]

# KPIs
total_sales = filtered_df["Sales"].sum()
average_sales = filtered_df["Sales"].mean()
max_sales = filtered_df["Sales"].max()

# Show KPIs
st.markdown("## Key Performance Indicators")
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,}")
col2.metric("Average Sales", f"${average_sales:,.2f}")
col3.metric("Max Sale", f"${max_sales:,}")

# Line Chart
st.markdown("## 📈 Sales Over Time")
sales_over_time = filtered_df.groupby("Date")["Sales"].sum()
st.line_chart(sales_over_time)

# Bar Chart by Region
st.markdown("## 🗺️ Sales by Region")
sales_by_region = filtered_df.groupby("Region")["Sales"].sum()
st.bar_chart(sales_by_region)

# Show raw data
with st.expander("Show Raw Data"):
    st.write(filtered_df)

