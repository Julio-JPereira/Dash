import dash
from dash import Dash, html, dcc, Input, Output, dash_table
#import dash
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go




df = pd.read_excel("Vendas.xlsx")
df2 = pd.read_excel("Falhas.xlsx") #parse_dates=['Falhas'])
#print(df2['Falhas'])
df3 = pd.read_excel("MesxMes.xlsx")
df4 = pd.read_excel("Leitura.xlsx")

colors = {
    'background': '#27293d',
    'text': 'pink'
}


fig6 = px.pie(df2, values='Falhas', names='Sensores')
fig6.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

dash.register_page(__name__,external_stylesheets=[dbc.themes.MATERIA])

layout = html.Div(
    [
        html.H1('# Detalhamento ocorrências sensores',
            style={
            'textAlign': 'center',
            'color': 'white',

            }),
        html.Div([
        dcc.Graph(
            id='grafico_sensor',
            figure=fig6,

        ),
        html.Div([
            dcc.Link('pg1'+"  |  ", href=page['path'])
            for page in dash.page_registry.values()
        ]),
        ], style={'display': 'inline-block', 'width': '40%',  'margin-left': '30%'}), #'float': 'right',

        html.Div(
        [
        dash_table.DataTable(
        id='table',
        data=df.to_dict('records'),
        style_cell=dict(textAlign='center'),
        style_header=dict(backgroundColor="#001d38"),
        style_data=dict(backgroundColor="#27293d"),
        style_table={'height': '390px', 'overflowY': 'auto'}, #auto
        fixed_rows={'headers': True},
        style_as_list_view=True,
    )], style={'display': 'inline-block', 'width': '50%', 'height': '400px', 'margin-left': '25%', 'color': 'pink'}),

    ], style={'background-color': '#1e1e2f', 'margin': '0', 'padding': '0', "content": "width=device-width, initial-scale=1"}
)