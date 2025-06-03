"""App for interactive dashboard."""

import pandas as pd
import plotly.express as px

from dash import Dash, Input, Output, dcc, html

# Load the data
suicide_data = pd.read_csv('data/who_suicide_latest.csv')
Nigerian_suicide_cases = suicide_data[
    suicide_data['GEO_NAME_SHORT'] == 'Nigeria'
].copy()


# Clean and rename
Nigerian_suicide_cases.rename(
    columns={
        'DIM_TIME': 'Suicide_Year',
        'DIM_SEX': 'Gender',
        'RATE_PER_100000_N': 'Suicide_Rate_N',
    },
    inplace=True,
)

# Initialize Dash app
app = Dash(__name__)
app.title = 'Suicide Rate Interactive Plot'

# Layout
app.layout = html.Div(
    [
        dcc.Dropdown(
            id='gender-dropdown',
            options=[
                {'label': 'TOTAL', 'value': 'TOTAL'},
                {'label': 'MALE', 'value': 'MALE'},
                {'label': 'FEMALE', 'value': 'FEMALE'},
            ],
            value='TOTAL',
            clearable=False,
            style={'width': '50%', 'margin': 'auto'},
        ),
        dcc.Graph(id='scatter-plot'),
    ]
)


# Callback for interactivity
@app.callback(
    Output('scatter-plot', 'figure'), Input('gender-dropdown', 'value')
)
def update_plot(selected_gender):
    """Update the dashboard."""
    if selected_gender == 'TOTAL':
        filtered_data = Nigerian_suicide_cases
    else:
        filtered_data = Nigerian_suicide_cases[
            Nigerian_suicide_cases['Gender'] == selected_gender
        ]

    fig = px.scatter(
        filtered_data,
        x='DIM_AGE',
        y='Suicide_Rate_N',
        color='Gender',
        labels={
            'DIM_AGE': 'Age Group',
            'Suicide_Rate_N': 'Suicide Rate per 100k',
        },
    )
    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
