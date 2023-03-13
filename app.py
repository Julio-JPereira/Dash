import dash
from dash import Dash, html, dcc, Input, Output
#import dash
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.MATERIA],  meta_tags=[{'name': 'viewport', 'content': 'width-device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}])
server = app.server

#-----------------------------------------------------------------------------------------------------------------
grid = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dcc.Graph(), md=4),
                dbc.Col(dcc.Graph(),md=8)
            ]
        )
    ]
)
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Pág 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Outros", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Dashboard de analise preditiva",
    brand_href="#",
    color="#27293d",
    dark=True,
)

navbar2 = dbc.NavbarSimple(
    #children=[
        #dbc.NavItem(dbc.NavLink("Pág 1", href="#")),
     #   dbc.DropdownMenu(
      #      children=[
                #dbc.DropdownMenuItem("Outros", header=True),
                #dbc.DropdownMenuItem("Page 2", href="#"),
                #dbc.DropdownMenuItem("Page 3", href="#"),
       #     ],
        #    nav=True,
        #    in_navbar=True,
            #label="More",
        #),
    #],
    brand="© 2023 Copyright: Centro Universitário FEI",
    brand_href="#",
    color="#27293d",
    dark=True,
)
#-----------------------------------------------------------------------------------------------
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Vendas.xlsx")
df2 = pd.read_excel("Falhas.xlsx") #parse_dates=['Falhas'])
#print(df2['Falhas'])
df3 = pd.read_excel("MesxMes.xlsx")
df4 = pd.read_excel("Leitura.xlsx")



random_x = [100, 2000, 550]
names = ['A', 'B', 'C']

colors = {
    'background': '#27293d',
    'text': 'pink'
}

colors2 = {
    'background-image': 'linear-gradient(to right, #ab63fa, #00b0f6)',

}

#color3='rgb({}, {}, {})'.format((i/100*255),(i/100*255),(i/100*255)),
#Criando o gráfico produto = sensores, quantidade = n° de falhas                      color = De acordo com o sensor
#fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group", color_continuous_scale=px.colors.qualitative.Pastel2)#template='plotly_dark'


opcoes = list(df['ID Loja'].unique())
opcoes.append("Todas as Lojas")
app.title = 'Manutenção preditiva'
#app.config = colors.update(

#)

app_color = {"graph_bg": "#082255", "graph_line": "#007ACE", 'background-color': '#007ACE'}
plot_layout = {
    "paper_bgcolor": "#141414",
}





#final = df2.tail(1),

#str = (final.to_string()),
#print('String:', str)
#destro = ','.join(df2.tail(1))
#print(destro)



#app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.MATERIA])

app.layout = html.Div(
    [
        navbar,
        # main app framework

        html.Div([
            dcc.Link(page['name']+"  |  ", href=page['path'])
            for page in dash.page_registry.values()
        ]),
        html.Hr(),

        # content of each page
        dash.page_container,
        navbar,
        navbar2,
    ], style={'background-color': '#1e1e2f', 'margin': '0', 'padding': '0', "content": "width=device-width, initial-scale=1"}
)




if __name__ == "__main__":
    app.run(debug=True)
