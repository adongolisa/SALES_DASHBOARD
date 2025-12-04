from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px


df = pd.read_csv('sales_data.csv')
df['conversion_rate'] = (df['conversions'] / df['users']) * 100


top_product_row = df.groupby('product')['revenue'].sum().reset_index().sort_values('revenue', ascending=False).iloc[0]
top_product = top_product_row['product']
top_product_revenue = top_product_row['revenue']

top_week_row = df.groupby('date')['revenue'].sum().reset_index().sort_values('revenue', ascending=False).iloc[0]
top_week = top_week_row['date']
top_week_revenue = top_week_row['revenue']

top_region_row = df.groupby('region')['conversion_rate'].mean().reset_index().sort_values('conversion_rate').iloc[0]
top_region_low_conversion = top_region_row['region']
top_region_conversion = round(top_region_row['conversion_rate'], 2)

# Revenue by product
revenue_by_product = df.groupby('product')['revenue'].sum().reset_index()
fig1 = px.bar(revenue_by_product, x='product', y='revenue', title='Total Revenue by Product')

# Revenue by region
revenue_by_region = df.groupby('region')['revenue'].sum().reset_index()
fig2 = px.pie(revenue_by_region, names='region', values='revenue', title='Revenue by Region')

# Daily revenue trend
daily_revenue = df.groupby('date')['revenue'].sum().reset_index()
fig3 = px.line(daily_revenue, x='date', y='revenue', title='Daily Revenue Trend')

# Conversion rate per product
conversion_by_product = df.groupby('product')['conversion_rate'].mean().reset_index()
fig4 = px.bar(conversion_by_product, x='product', y='conversion_rate', title='Average Conversion Rate by Product')

# Dash app
app = Dash(__name__)

def create_card(title, main_text, tooltip_text, color):
    return html.Div(
        children=[
            html.H3(title),
            html.P(main_text, title=tooltip_text)  # Tooltip on hover
        ],
        style={
            'flex': '1',
            'minWidth': '200px',
            'padding': '20px',
            'backgroundColor': color,
            'borderRadius': '10px',
            'textAlign': 'center',
            'cursor': 'pointer'  
        }
    )

app.layout = html.Div(
    children=[
        html.H1("SALES DASHBOARD", style={'textAlign': 'center', 'marginBottom': '20px'}),

        # Top insights cards with tooltips
        html.Div(
            children=[
                create_card(
                    "Top Product",
                    top_product,
                    f"Revenue: ${top_product_revenue:,.2f}",
                    "#d4edda"
                ),
                create_card(
                    "Week of Highest Revenue",
                    top_week,
                    f"Revenue: ${top_week_revenue:,.2f}",
                    "#fff3cd"
                ),
                create_card(
                    "Region with Lowest Conversion Rate",
                    top_region_low_conversion,
                    f"Conversion Rate: {top_region_conversion}%",
                    "#f8d7da"
                )
            ],
            style={'display': 'flex', 'flexWrap': 'wrap', 'gap': '20px', 'marginBottom': '30px'}
        ),

        # Graphs row 1
        html.Div(
            children=[
                dcc.Graph(figure=fig1, style={'flex': '1', 'minWidth': '300px'}),
                dcc.Graph(figure=fig4, style={'flex': '1', 'minWidth': '300px'})
            ],
            style={'display': 'flex', 'flexWrap': 'wrap', 'gap': '20px'}
        ),

        # Graphs row 2
        html.Div(
            children=[
                dcc.Graph(figure=fig2, style={'flex': '1', 'minWidth': '300px'}),
                dcc.Graph(figure=fig3, style={'flex': '1', 'minWidth': '300px'})
            ],
            style={'display': 'flex', 'flexWrap': 'wrap', 'gap': '20px', 'marginTop': '20px'}
        )
    ],
    style={'padding': '20px'}
)

if __name__ == '__main__':
    app.run(debug=True)
