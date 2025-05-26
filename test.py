import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.title(" Matplotlib Charts with Streamlit")

# Sample data
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = np.sin(x)
data = np.random.randn(100)
categories = ['A', 'B', 'C', 'D']
values = [15, 30, 45, 10]

# Line Chart
st.subheader("Line Chart")
fig1, ax1 = plt.subplots()
ax1.plot(x, y, label='sin(x)', color='blue')
ax1.set_title("Line Chart")
ax1.set_xlabel("x")
ax1.set_ylabel("sin(x)")
ax1.legend()
st.pyplot(fig1)

# Bar Chart
st.subheader("Bar Chart")
fig2, ax2 = plt.subplots()
ax2.bar(categories, values, color='green')
ax2.set_title("Bar Chart")
st.pyplot(fig2)

# Scatter Plot
st.subheader("Scatter Plot")
fig3, ax3 = plt.subplots()
ax3.scatter(x, np.random.randn(100), color='purple')
ax3.set_title("Scatter Plot")
ax3.set_xlabel("x")
ax3.set_ylabel("Random Values")
st.pyplot(fig3)

# Histogram
st.subheader("Histogram")
fig4, ax4 = plt.subplots()
ax4.hist(data, bins=10, edgecolor='black')
ax4.set_title("Histogram")
st.pyplot(fig4)

# Pie Chart
st.subheader("Pie Chart")
fig5, ax5 = plt.subplots()
ax5.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
ax5.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax5.set_title("Pie Chart")
st.pyplot(fig5)
