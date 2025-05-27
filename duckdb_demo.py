import streamlit as st
import duckdb
import pandas as pd
import os

# --- Title ---
st.title("Streamlit + DuckDB Integration Demo")

# --- File uploader (CSV or Parquet) ---
uploaded_file = st.file_uploader("Upload a CSV or Parquet file", type=["csv", "parquet"])

if uploaded_file is not None:
    # Load file into DuckDB depending on type
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_parquet(uploaded_file)
    
    st.success(f"Loaded {uploaded_file.name} successfully!")
    st.dataframe(df.head())

    # Create an in-memory DuckDB connection
    con = duckdb.connect(database=':memory:')

    # Register the Pandas DataFrame as a DuckDB table
    con.register("uploaded_data", df)

    st.subheader("Run SQL on Your Data")
    query = st.text_area("Write your SQL query here", "SELECT * FROM uploaded_data LIMIT 10")

    if st.button("Execute SQL"):
        try:
            result = con.execute(query).df()
            st.write("Query Result:")
            st.dataframe(result)
        except Exception as e:
            st.error(f"Error executing query: {e}")

    # Example: Show DuckDB Aggregation Function
    st.subheader("Quick Stats (DuckDB SQL)")
    stats_query = """
    SELECT 
        COUNT(*) as row_count,
        AVG({col}) as average,
        MIN({col}) as min_value,
        MAX({col}) as max_value
    FROM uploaded_data
    """

    # Choose a numeric column
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if numeric_cols:
        selected_col = st.selectbox("Choose a numeric column", numeric_cols)
        result = con.execute(stats_query.format(col=selected_col)).df()
        st.write(result)
    else:
        st.warning("No numeric columns available for stats.")

else:
    st.info("Upload a CSV or Parquet file to begin.")

# --- Persistent Database Option ---
st.sidebar.header("DuckDB Persistent Mode")
use_persistent = st.sidebar.checkbox("Use Persistent DB (duckdb_file.duckdb)")

if use_persistent:
    persistent_con = duckdb.connect("duckdb_file.duckdb")
    st.sidebar.success("Connected to persistent DuckDB file.")

    if uploaded_file:
        persistent_con.register("uploaded_data", df)
        persistent_con.execute("CREATE TABLE IF NOT EXISTS uploaded_copy AS SELECT * FROM uploaded_data")
        st.sidebar.success("Data copied to persistent table 'uploaded_copy'")
