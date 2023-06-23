import pandas as pd
import dash
from dash import dcc
from dash import html
from dash import dash_table
import plotly.graph_objects as go

# wczytanie danych
df = pd.read_csv('processed_AviationData.csv')

# czyszczenie danych pod wykres
df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')
df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')
df.dropna(subset=['Latitude', 'Longitude'], inplace=True)

trace = go.Scattergeo(
    lat=df['Latitude'],
    lon=df['Longitude'],
    mode='markers',
    marker=dict(
        size=5,
        color='red',
        opacity=0.7,
        symbol='circle'
    )
)

layout = go.Layout(
    title='Aviation Accidents Map',
    geo=dict(
        resolution=50,
        showland=True,
        showlakes=True,
        landcolor='rgb(204, 204, 204)',
        countrycolor='rgb(204, 204, 204)',
        lakecolor='rgb(255, 255, 255)',
        projection=dict(
            type='natural earth'
        ),
        coastlinewidth=0.5,
        lataxis=dict(
            range=[-90, 90],
            showgrid=True,
            dtick=10
        ),
        lonaxis=dict(
            range=[-180, 180],
            showgrid=True,
            dtick=20
        )
    )
)


fig = go.Figure(data=[trace], layout=layout)

# tworzenie aplikacji dash
app = dash.Dash(__name__)

# ustawienie layoutu
app.layout = html.Div([
    html.H1("Aviation Accidents Dashboard "),
    dash_table.DataTable(
        id='a',
        columns=[{'name': col, 'id': col} for col in df.columns],
        data=df.to_dict('records')
    ),
    html.H1('Aviation Accidents Dashboard'),
    dcc.Graph(figure=fig)
])


if __name__ == '__main__':
    app.run_server(debug=True)
