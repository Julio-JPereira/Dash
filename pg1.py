import dash
from dash import Dash, html, dcc, Input, Output
#import dash
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import time

dash.register_page(__name__, path='/', external_stylesheets=[dbc.themes.MATERIA])

df = pd.read_excel("Vendas.xlsx")
df2 = pd.read_excel("Falhas.xlsx") #parse_dates=['Falhas'])
#print(df2['Falhas'])
df3 = pd.read_excel("MesxMes.xlsx")
df4 = pd.read_excel("Leitura.xlsx")

last_10_rows = df4.tail(10)

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
fig= px.line(last_10_rows, x="Hora", y="Corrente",title='Valores lidos pelo sensor de Corrente')
#fig.update_layout(plot_bgcolor="#282b38")
fig2 = px.line(last_10_rows, x="Hora", y="Temperatura",title='Valores lidos pelo sensor de temperatura')
#fig3 = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group", color_continuous_scale=px.colors.qualitative.Pastel2, template='ggplot2')
fig3 = px.line(last_10_rows, x="Hora", y="Umidade",title='Valores lidos pelo sensor de Umidade')
#fig4 = px.line(df, x="Produto", y="Quantidade", color="ID Loja", template="plotly_white")#, template="plotly_dark"
fig4 = px.line(last_10_rows, x="Hora", y="Vibração",title='Valores lidos pelo sensor de Vibração')
#fig6 = px.bar(df2, x="Sensores", y="Falhas", barmode="group", color_continuous_scale=px.colors.qualitative.Pastel2)
fig6 = px.pie(df2, values='Falhas', names='Sensores')
#fig5 = px.pie(df, values=random_x, names=names)

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    #line_radius='20px'
)

fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
    #marker_color="red"
)

fig3.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

fig4.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
#fig3.update()
fig5 = px.bar(df3, x='sensor', y='media', color='Mês', barmode="group")

fig5.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],

)

#fig5.update_traces(opacity=0.6, marker_color='linear-gradient(to right, #ab63fa, #00b0f6)')
fig5.update_traces(opacity=0.6, marker_color='#ab63fa')




fig6.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


opcoes = list(df['ID Loja'].unique())
opcoes.append("Todas as Lojas")
#app.title = 'Manutenção preditiva'
#app.config = colors.update(

#)

app_color = {"graph_bg": "#082255", "graph_line": "#007ACE", 'background-color': '#007ACE'}
plot_layout = {
    "paper_bgcolor": "#141414",
}



#df = px.data.gapminder()


layout = html.Div(
    [
html.H1(children='Teste Dashboard',
            style={
            'textAlign': 'center',
            'color': 'white',

            }),

    html.H2(children='Gráfico para monitoração de motores elétricos',
            style={
            'textAlign': 'left',
            'color': 'white',
            }),
    html.H3(children='''
        Obs: Usei um excel de vendas de roupas, hehehe.
    ''',
        style={
        'color': 'white',
        }),
    html.Div([
        html.H6('Na linha a seguir tem conteúdo bicho', style={
            'color': 'pink',
            'font-size': '70%',
        }),

        #html.Br(),

        #df2.update(df2.tail(1)),
        df2['Falhas'].tail(1).to_string(index=False),
        html.Br(),


    ], style={'display': 'inline-block', 'width': '23%', 'height': '100px', 'background-color': '#27293d', 'border-width': '2px', 'border-color': 'white', 'border-style': 'solid', 'border-radius': '20px', 'text-align': 'center', 'color': 'white','margin-left': '2%', 'font-size': '20px'}),
    html.Div([
       'Esta é uma DIV2',
        html.Br(),
        html.Br(),

    ], style={'display': 'inline-block', 'width': '23%', 'height': '100px', 'background-color': '#27293d', 'border-width': '2px', 'border-color': 'white', 'border-style': 'solid', 'border-radius': '20px', 'text-align': 'center', 'color': 'white', 'margin-left': '1.3%'}),
    html.Div([
       'Esta é uma DIV3',
        html.Br(),
        html.Br(),

    ], style={'display': 'inline-block', 'width': '23%', 'height': '100px', 'background-color': '#27293d', 'border-width': '2px', 'border-color': 'white', 'border-style': 'solid', 'border-radius': '20px', 'text-align': 'center', 'color': 'white', 'margin-left': '1.3%'}),
    html.Div([
       'Esta é uma DIV4',
        html.Br(),
        html.Br(),

    ], style={'display': 'inline-block', 'width': '23%', 'height': '100px', 'background-color': '#27293d', 'border-width': '2px', 'border-color': 'white', 'border-style': 'solid', 'border-radius': '20px', 'text-align': 'center', 'color': 'white', 'margin-left': '1.3%'}),
    html.Div([
       ''
    ], style={'width': '100%', 'height': '50px'}),
                                                #O id Nome do botão

    dcc.Dropdown(opcoes, value='Todas as Lojas', id='lista_lojas', style={
        'background-image': 'linear-gradient(to right, #ab63fa, #00b0f6)', #ddb0f6, ab63fa
    }),
    html.Div([
       ''
    ], style={'width': '100%', 'height': '50px'}),
    html.Div([
        dcc.Graph(
            id='grafico_quantidade_vendas',
            figure=fig
            ),

        ], style={'display': 'inline-block', 'width': '49%', 'border-width': '5px', 'border-color': '#27293d', 'border-style': 'solid', 'border-radius': '20px'}), #'display': 'inline-block'
    html.Div([
        dcc.Graph(
            id='grafico_quantidade',
            figure=fig2,

            )
    ], style={'display': 'inline-block', 'width': '49%', 'float': 'right'}),
    html.Div([

        dcc.Graph(
            id='grafico_quantidade_3',
            figure=fig3,
            )
    ], style={'display': 'inline-block', 'width': '49%', 'float': 'right'}),
    html.Div([

        dcc.Graph(
            id='grafico_quantidade_4',
            figure=fig4
            )
    ], style={'display': 'inline-block', 'width': '49%'}),
    html.Div([
        dcc.Graph(
            id='grafico_pizza',
            figure=fig5,

        )
    ], style={'display': 'inline-block', 'width': '49%'}),
    html.Div([
        dcc.Graph(
            id='grafico_sensor',
            figure=fig6,

        )
    ], style={'display': 'inline-block', 'width': '40%',  'margin-left': '1.3%'}), #'float': 'right',
    ], style={'background-color': '#1e1e2f', 'margin': '0', 'padding': '0', "content": "width=device-width, initial-scale=1"}


)



#@layout.callback(
#    Output('grafico_quantidade_vendas', 'children'),
#    Input('df4', 'value')
#)

#def update_output(value):
#    return f'You have selected {value}'

