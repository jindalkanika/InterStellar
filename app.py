import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly
import plotly.plotly as py

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

plotly.tools.set_credentials_file(username='samridhivaid', api_key='Vx7UzWPiInLQmDiwv3Q9')

df=pd.read_json('stellar_output_file')


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'text': ''
}

app.layout = html.Div(children=[
    html.H1(children='InterStellar: The Next Move (LUMENS FORECAST)',
        style={            
           'font-size':'40px',
            'height' : 'auto',
        'textAlign': 'center',
            'font-family': '"Times New Roman", Times, serif',
           ' font-weight': 'bolder',
        'padding': '40px',
            'border' : '5px solid #000',
            'color' : 'white',
            'background-color':'black'
    }),     
    html.H3(
    generate_table(df),
     style={
        'color': '#666',
        'margin': '50px',
         'float':'center',
         'padding': '10px 10px 10px 10px',
         'margin': '10px 10px 10px 700px',
      'font-family': 'Times New Roman'}),

    
    
     html.Iframe( style={'width':'100%',
                          'height':'800',
                         'float':'100%',
                           'frameborder':'0', 'scrolling':'no'},

        src="//plot.ly/~samridhivaid/23.embed")
     
    

   
]) 




if __name__ == '__main__':
    app.run_server(debug=True)