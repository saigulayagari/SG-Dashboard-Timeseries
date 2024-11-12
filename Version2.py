import streamlit as st
import pandas as pd
import plotly.express as px

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title { text-align: center; color: #3E64FF; font-size: 40px; }
    .subtitle { text-align: center; color: #00C897; font-size: 24px; }
    .section-header { color: #FF6363; font-size: 30px; margin-top: 40px; }
    .divider { border-top: 3px solid #FF6363; margin-top: 20px; margin-bottom: 20px; }
    </style>
    """, 
    unsafe_allow_html=True
)

# Title and Introduction
st.markdown("<h1 class='title'>📊 Business Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitle'>Insightful analytics on sales, customer demographics, and product performance</h2>", unsafe_allow_html=True)

# Data Input
st.sidebar.header("📂 Upload CSV File")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# Load data and preview it
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("<h3 class='section-header'>Data Preview</h3>", unsafe_allow_html=True)
    st.write(data.head())

    # Sales Insights
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("<h3 class='section-header'>📈 Sales Insights</h3>", unsafe_allow_html=True)
    fig = px.line(
        data, 
        x='sales_date', 
        y='sales_amount', 
        title='Sales Over Time',
        line_shape='spline',
        color_discrete_sequence=["#3E64FF"]
    )
    st.plotly_chart(fig)

    # Customer Segmentation by Region
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("<h3 class='section-header'>🗺️ Customer Segmentation by Region</h3>", unsafe_allow_html=True)
    fig = px.pie(
        data, 
        names='region', 
        values='sales_amount', 
        title="Customer Segmentation by Region",
        color_discrete_sequence=px.colors.sequential.Tealgrn
    )
    st.plotly_chart(fig)

    # Product Analysis
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("<h3 class='section-header'>📊 Top Products By Sales</h3>", unsafe_allow_html=True)
    top_products_df = data.groupby('product').sum()['sales_amount'].nlargest(10)
    fig = px.bar(
        top_products_df, 
        x=top_products_df.index, 
        y='sales_amount', 
        title="Top Products By Sales",
        color=top_products_df.index,
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    st.plotly_chart(fig)

    # Footer
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #00C897;'>This business dashboard template is flexible. Expand upon it based on your specific business needs.</p>", unsafe_allow_html=True)

else:
    st.write("Please upload a CSV file to proceed.")
