import streamlit as st
import pyodbc
import pandas as pd

# I am connecting to my database
def get_data():
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=(local)\\SQLEXPRESS;'
        'DATABASE=PipelineAutomation;'
        'Trusted_Connection=yes;'
    )
    
    # I am reading all test results
    query = "SELECT * FROM TestResults ORDER BY RunAt DESC"
    df = pd.read_sql(query, connection)
    connection.close()
    return df

# I am creating the dashboard
st.title("Test Results Dashboard")

# I am loading the data
df = get_data()

# I am showing numbers
st.metric("Total Tests Run", len(df))

# I am showing pass rate
if len(df) > 0:
    pass_rate = df['Passed'].sum() / len(df) * 100
    st.metric("Pass Rate", f"{pass_rate:.1f}%")

# I am showing the table
st.subheader("Recent Test Results")
st.dataframe(df)

# I am showing a chart
if len(df) > 0:
    st.subheader("Pass/Fail Over Time")
    st.bar_chart(df.groupby(df['RunAt'].dt.date)['Passed'].mean())