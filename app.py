import os
print("Current Directory:", os.getcwd())

import streamlit as st # pyright: ignore[reportMissingImports]
import pandas as pd # pyright: ignore[reportMissingModuleSource]
import plotly.express as px # type: ignore #used for creating charts
from utils.insights import generate_insight #belo wrong lines
# from insights import generate_insight #as if it is inside util folder

# 1. Page Configuration
st.set_page_config(page_title="Filtered Sales Dashboard", layout="wide")
st.title("📊 Filtered Sales Dashboard")

# 2. Load Data Safely
try:
    df = pd.read_csv("data/sales_data.csv")
    st.success("✅ CSV loaded successfully") #this is the output 

    # 3. Sidebar Filters
    st.sidebar.header("Filter Options")
    region = st.sidebar.selectbox("Choose Region", df['region'].unique())

    # 4. Filter Data
    filtered_df = df[df['region'] == region]

    # 5. Show Filtered Table
    st.subheader(f"Sales Data for Region: {region}")
    st.dataframe(filtered_df)

    # 6. Bar Chart: Total Sales by Product
    st.subheader("📦 Total Sales by Product")
    fig = px.bar(
        filtered_df,
        x='product',
        y='total_sales',
        color='status',
        title=f"Sales Breakdown by Product in {region}"
    )
    st.plotly_chart(fig, use_container_width=True)

    # 7. AI Insight Generation
    st.subheader("🔍 AI Insight")
    st.info(generate_insight(filtered_df))

except FileNotFoundError:
    st.error("❌ The file 'data/sales_data.csv' could not be found. Please check your filepath.")
except Exception as e:
    st.error(f"❌ Something went wrong while loading data: {e}")
# import streamlit as st
# import pandas as pd

# st.set_page_config(page_title="Filtered Sales Dashboard", layout="wide")
# st.title("📊 Filtered Sales Dashboard")

# # Load data
# try:
#     df = pd.read_csv("data/sales_data.csv")
#     st.success("✅ CSV loaded successfully")

#     # Region filter
#     st.sidebar.header("Filter Options")
#     region = st.sidebar.selectbox("Choose Region", df['region'].unique())

#     # Filter data
#     filtered_df = df[df['region'] == region]

#     # Show filtered table
#     st.subheader(f"Sales Data for Region: {region}")
#     st.dataframe(filtered_df)

# except Exception as e:
#     st.error(f"❌ Something went wrong: {e}")

# import plotly.express as px

# # Bar chart: total sales by product
# st.subheader("📦 Total Sales by Product")
# fig = px.bar(
#     filtered_df,
#     x='product',
#     y='total_sales',
#     color='status',
#     title=f"Sales Breakdown by Product in {region}"
# )
# st.plotly_chart(fig, use_container_width=True)

# from utils.insights import generate_insight

# st.subheader("🔍 AI Insight")
# st.info(generate_insight(filtered_df))