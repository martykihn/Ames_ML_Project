import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.figure_factory as ff
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

app = dash.Dash(__name__)
colors = {
	'background': '#EDF4F5',
	'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background'],
						'paddingLeft': 50, 'paddingRight': 50},
						children=[
	html.H2(children="Housing Price Predictor"),
#style={'backgroundColor': colors['background']}, children=[
#	html.H1(
#		children='House Price Predictor',
#		style={
#			'textAlign': 'center',
#			'color': colors['text']
#		}
#	),
#	html.Div(children='Is it worth it to remodel your home?', style={
#		'textAlign': 'center',
#		'color': colors['text']
#	},
		
	html.P("Enter Average House Price:"),

	dcc.Input(
		id="saleprice_avg",
		placeholder="Enter Avg House Price",
		type="number",
		value=200000
		),
		
	html.P("Select Your Neighborhood Type:"),

	dcc.Dropdown(
		id="neighborhood",
		options=[
			{
				"label": "Type 4 ($$$$)",
            	"value": 1.3,
            },
            {
            	"label": "Type 3 ($$$)",
            	"value": 1.0,
            },
            {
            	"label": "Type 2 ($$)",
            	"value": 0.7,
            },
            {
            	"label": "Type 1 ($)",
            	"value": 0.5,
            },
        	],
        	placeholder="Neighborhood Type",
        	value=1,
		),

	html.P(""),
	html.P("Above-Ground Square Feet:"),

	dcc.Slider(
#		name="Above-Ground Sq Ft",
		id="above-ground-sf",
		min= 0,
		max= 2500,
		step=None,
		value= 1500,
		marks= {i: str(i) for i in [0, 500, 1000, 1500, 2000, 2500]},
	),
				
	html.P(""),
	html.P("Overall Quality (1-5):"),

	dcc.Slider(
#		name="Overall Quality",
		id="overall-quality",
		min=1,
		max=5,
		step=None,
		value=3,
		marks = {i: str(i) for i in [1, 2, 3, 4, 5]},
	),		
		
	html.P(""),
	html.P("Basement Quality:"),

	dcc.RadioItems(
#		name="Basement Quality",
		id="basement-quality",
		options=[
			{
				"label": "Average",
            	"value": 1,
            },
            {
            	"label": "High",
            	"value": 1.06,
            },
        ],
        value=1,
    ),
		
	html.P(""),
	html.P("Kitchen Quality:"),

	dcc.RadioItems(
#		name="Kitchen Quality",
		id="kitchen-quality",
		options=[
			{
				"label": "Average",
            	"value": 1,
            },
            {
            	"label": "High",
            	"value": 1.1,
            },
        ],
        value=1,
    ),
		
	html.P(""),
	html.P("Exterior Quality:"),

	dcc.RadioItems(
#		name="Exterior Quality",
		id="exterior-quality",
		options=[
			{
				"label": "Average",
            	"value": 1,
            },
            {
            	"label": "High",
            	"value": 1.09,
            },
        ],
        value=1,
    ),
		
	html.P(""),
	html.P("Number of Baths:"),

	dcc.RadioItems(
#		name="# of Baths",
		id="baths",
		options=[
			{
				"label": "Average",
            	"value": 1,
            },
            {
            	"label": "High",
            	"value": 1.06,
            },
        ],
        value=1,
    ),
		
	html.P(""),
	html.P("Wood Deck Sq. Feet (0-300+):"),

	dcc.Slider(
#		name="Wood Deck SF",
		id="wood-deck",
		min=0,
		max=300,
		step=None,
		value=200,
		marks={i: str(i) for i in [0, 100, 200, 300]},
	),
		
	html.P(""),
	html.P("Have a Garage (Y/N)?"),

	dcc.RadioItems(
#		name="Garage (Y/N)?",
		id="garage",
		options=[
			{
				"label": "Average",
            	"value": 0.98,
            },
            {
            	"label": "High",
            	"value": 1,
            },
        ],
        value=1,
    ),
		
	html.P(""),
	html.P("Have Central Air (Y/N)?"),

	dcc.RadioItems(
#		name="Central Air (Y/N)?",
		id="central-air",
		options=[
			{
				"label": "None",
            	"value": 0.92,
            },
            {
            	"label": "Yes",
            	"value": 1,
            },
        ],
        value=1,
    ),
    		
	html.P(""),

	dcc.Graph(id="display-value")
	
])
#	html.Div(id="display-value")

#	dcc.Graph(
#		figure={
#			"data": [
#				{"x": [1, 2], "y": [100000, 200000], 'type': 'bar', 'name': 'Mean'},
#				{"x": [1, 2], "y": [150000, 250000], 'type': 'bar', 'name': 'Mean2'},
#			],
#			"layout": {
#				'plot_bgcolor': colors['background'],
#				'paper_bgcolor': colors['background'],
#				'font': {
#					'color': colors['text']
#				}
#			}
#		}
#	)
#])
	
#callbacks
@app.callback(
	Output("display-value", "figure"),
	[
		Input("saleprice_avg", "value"),
		Input("neighborhood", "value"),
		Input("above-ground-sf", "value"),
		Input("overall-quality", "value"),
		Input("basement-quality", "value"),
		Input("kitchen-quality", "value"),
		Input("exterior-quality", "value"),
		Input("baths", "value"),
		Input("wood-deck", "value"),
		Input("garage", "value"),
		Input("central-air", "value"),
	],
)
def display_price_plot(
	saleprice_avg,
	neighborhood,
	above_ground_sf,
	overall_quality,
	basement_quality,
	kitchen_quality,
	exterior_quality,
	baths,
	wood_deck,
	garage,
	central_air):
	
	data_ = np.random.normal(saleprice_avg, 0.44, 1000)
	data_2 = np.random.normal(saleprice_avg*neighborhood, 0.44, 1000)
	
	fig = px.histogram(data_)
	return fig



if __name__ == "__main__":
	app.run_server(debug=True)
	