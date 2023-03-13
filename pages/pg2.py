import dash
from dash import Dash, html, dcc, Input, Output, dash_table
#import dash
import plotly.express as px
import pandas as pd
#import dash_bootstrap_components as dbc
#import dash_table
#from dash_table.Format import Format, Group, Scheme, Symbol
import plotly.graph_objects as go
#import plotly.offline as pyo

dash.register_page(__name__,  meta_tags=[{'name': 'viewport', 'content': 'width-device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}])

df = px.data.tips()
df2 = pd.read_excel("Vendas.xlsx")

color1 = '#d3d3d3'
color2 = 'white'


fig9 = go.Figure(data=[go.Table(
    header=dict(values=list(df2.columns), fill_color=[[color1]]), # dados do cabeçalho
    cells=dict(values=[df2['Valor Final'], df2['Valor Unitário'], df2['Quantidade'], df2['Produto'], df2['ID Loja'], df2['Data'], df2['Código Venda']], fill_color=[[color2]], line_color=[['pink']])), # dados do corpo da tabela

]
)
#pyo.offline.plot(fig9, filename = "tabela-01.html")

layout = html.Div(
    [
        dcc.RadioItems([x for x in df.day.unique()], id='day-choice'),
        dcc.Graph(id='bar-fig',
                  figure=px.bar(df, x='smoker', y='total_bill')),
        html.Div(
        [dash_table.DataTable(
        id='table',
        data=df2.to_dict('records'),
        style_cell=dict(textAlign='center'),
        style_header=dict(backgroundColor="#001d38"),
        style_data=dict(backgroundColor="#27293d"),
        style_table={'height': '390px', 'overflowY': 'auto'}, #auto
        fixed_rows={'headers': True},
        style_as_list_view=True,
    )], style={'display': 'inline-block', 'width': '50%', 'height': '400px', 'background-color': '#1e1e2f', 'margin-left': '25%', 'color': 'pink'}),
    ],
)
