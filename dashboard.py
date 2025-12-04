import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------
# Load and prepare data
# ---------------------------
df = pd.read_csv('sales_data.csv')
df['conversion_rate'] = (df['conversions'] / df['users']) * 100

# Top Product
top_product_row = df.groupby('product')['revenue'].sum().reset_index().sort_values('revenue', ascending=False).iloc[0]
top_product = top_product_row['product']
top_product_revenue = top_product_row['revenue']

# Week of Highest Revenue
top_week_row = df.groupby('date')['revenue'].sum().reset_index().sort_values('revenue', ascending=False).iloc[0]
top_week = top_week_row['date']
top_week_revenue = top_week_row['revenue']

# Region with Lowest Conversion Rate
top_region_row = df.groupby('region')['conversion_rate'].mean().reset_index().sort_values('conversion_rate').iloc[0]
top_region_low_conversion = top_region_row['region']
top_region_conversion = round(top_region_row['conversion_rate'], 2)

# ---------------------------
# Charts
# ---------------------------
revenue_by_product = df.groupby('product')['revenue'].sum().reset_index()
fig1 = px.bar(revenue_by_product, x='product', y='revenue', title='Total Revenue by Product')

revenue_by_region = df.groupby('region')['revenue'].sum().reset_index()
fig2 = px.pie(revenue_by_region, names='region', values='revenue', title='Revenue by Region')

daily_revenue = df.groupby('date')['revenue'].sum().reset_index()
fig3 = px.line(daily_revenue, x='date', y='revenue', title='Daily Revenue Trend')

conversion_by_product = df.groupby('product')['conversion_rate'].mean().reset_index()
fig4 = px.bar(conversion_by_product, x='product', y='conversion_rate', title='Average Conversion Rate by Product')


# ---------------------------
# Streamlit Layout
# ---------------------------
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.markdown("<h1 style='text-align:center;'>SALES DASHBOARD</h1>", unsafe_allow_html=True)
st.write("")

# ---------------------------
# Card Component
# ---------------------------
def card(title, value, tooltip, color):
    st.markdown(
        f"""
        <div style="
            background-color:{color};
            padding:20px;
            border-radius:10px;
            text-align:center;
            min-width:200px;
            cursor:pointer;
        "
        title="{tooltip}">
            <h3 style="margin:0;">{title}</h3>
            <p style="font-size:22px;margin:0;">{value}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------------------
# Cards Row
# ---------------------------
col1, col2, col3 = st.columns(3)

with col1:
    card(
        "Top Product",
        top_product,
        f"Revenue: ${top_product_revenue:,.2f}",
        "#d4edda"
    )

with col2:
    card(
        "Week of Highest Revenue",
        top_week,
        f"Revenue: ${top_week_revenue:,.2f}",
        "#fff3cd"
    )

with col3:
    card(
        "Region with Lowest Conversion Rate",
        top_region_low_conversion,
        f"Conversion Rate: {top_region_conversion}%",
        "#f8d7da"
    )

st.write("")

# ---------------------------
# First row of charts
# ---------------------------
colA, colB = st.columns(2)
with colA:
    st.plotly_chart(fig1, use_container_width=True)
with colB:
    st.plotly_chart(fig4, use_container_width=True)

# ---------------------------
# Second row of charts
# ---------------------------
colC, colD = st.columns(2)
with colC:
    st.plotly_chart(fig2, use_container_width=True)
with colD:
    st.plotly_chart(fig3, use_container_width=True)
