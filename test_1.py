import streamlit as st
import pandas as pd
import numpy as np

st.title("Various Charts using Vega-Lite in Streamlit")

# Sample Data
np.random.seed(42)
df = pd.DataFrame({
    'x': np.arange(1, 11),
    'y': np.random.randint(1, 100, 10),
    'category': ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']
})

# Line Chart
st.subheader("Line Chart")
st.vega_lite_chart(df, {
    'mark': 'line',
    'encoding': {
        'x': {'field': 'x', 'type': 'quantitative'},
        'y': {'field': 'y', 'type': 'quantitative'},
    }
})

# Bar Chart
st.subheader("Bar Chart")
st.vega_lite_chart(df, {
    'mark': 'bar',
    'encoding': {
        'x': {'field': 'category', 'type': 'nominal'},
        'y': {'aggregate': 'sum', 'field': 'y', 'type': 'quantitative'}
    }
})

# Scatter Plot
st.subheader("Scatter Plot")
st.vega_lite_chart(df, {
    'mark': 'circle',
    'encoding': {
        'x': {'field': 'x', 'type': 'quantitative'},
        'y': {'field': 'y', 'type': 'quantitative'},
        'color': {'field': 'category', 'type': 'nominal'}
    }
})

# Histogram
st.subheader("Histogram")
st.vega_lite_chart(df, {
    'mark': 'bar',
    'encoding': {
        'x': {'bin': True, 'field': 'y', 'type': 'quantitative'},
        'y': {'aggregate': 'count', 'type': 'quantitative'}
    }
})

# Pie Chart (Workaround using mark_arc)
st.subheader("Pie Chart")
pie_data = df.groupby('category').sum().reset_index()
st.vega_lite_chart(pie_data, {
    'mark': {'type': 'arc', 'innerRadius': 50},
    'encoding': {
        'theta': {'field': 'y', 'type': 'quantitative'},
        'color': {'field': 'category', 'type': 'nominal'}
    },
    'view': {'stroke': None}
})
