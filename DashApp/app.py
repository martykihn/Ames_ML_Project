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

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)
colors = {
	'background': '#EDF4F5',
	'text': '#333399'
}

app.layout = html.Div(style={'backgroundColor': colors['background'],
						'paddingLeft': 20, 'paddingRight': 20,
						'paddingTop': 20},
						children=[
	html.Div([
	html.H4(children="Tell Us About the House", style={'color': colors['text']}),
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
        labelStyle={'display': 'inline-block', 'margin-right': '7px'},
        style={'display': 'inline-block', 'margin-left': '7px'},
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
        labelStyle={'display': 'inline-block', 'margin-right': '7px'},
        style={'display': 'inline-block', 'margin-left': '7px'},
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
        labelStyle={'display': 'inline-block', 'margin-right': '7px'},
        style={'display': 'inline-block', 'margin-left': '7px'},
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
        labelStyle={'display': 'inline-block', 'margin-right': '7px'},
        style={'display': 'inline-block', 'margin-left': '7px'},
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
				"label": "None",
            	"value": 0.98,
            },
            {
            	"label": "Yes",
            	"value": 1,
            },
        ],
        value=1,
        labelStyle={'display': 'inline-block', 'margin-right': '7px'},
        style={'display': 'inline-block', 'margin-left': '7px'},
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
        labelStyle={'display': 'inline-block', 'margin-right': '7px'},
        style={'display': 'inline-block', 'margin-left': '7px'},
    ),
    ], className='six columns'),
    
    html.Div([
    	html.H4(children="Range of Potential Prices", style={'color': colors['text']}),

		dcc.Graph(id="display-value"),
		
		html.P(""),
		html.H6("Number above the arrow is the amount you could potentially gain in value by doing the improvements selected at right."),

		html.P(""),
		
		html.Img(
			src=app.get_asset_url("house.jpg"),
			className="house",
			id="house-image",
			)
		
		], className='six columns'),
		
	], className='row')
	
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
	
	above_ground_sf = above_ground_sf / 1500
	overall_quality = overall_quality / 3
	if wood_deck < 100:
		wood_deck = 1
	else:
		wood_deck = wood_deck / 100
	
	new_price = saleprice_avg * neighborhood * above_ground_sf * overall_quality
	new_price = new_price * basement_quality * kitchen_quality * exterior_quality
	new_price = new_price * baths * garage * central_air
#	new_price = new_price * wood_deck
	
#	 * basement_quality * kitchen_quality * \
#	exterior_quality * baths * wood_deck * garage * central_air
	sigma = new_price * 0.35
	data_ = np.random.normal(new_price, sigma, 1000)
	change = new_price - saleprice_avg
	change = int(change)
	new_change = f'{"Gain => $"}{change:,}'
#	data_2 = np.random.normal(saleprice_avg*neighborhood, 0.44, 1000)
	
#	factors_ = (neighborhood - 1) + (above_ground_sf / 1500) + \
#	(overall_quality / 3) + (basement_quality - 1) + \
#	(kitchen_quality - 1) + (exterior_quality - 1) + (baths - 1) + \
#	((wood_deck / 100) - 1) + (garage - 1) + (central_air - 1)
	
#	factors_ = factors_ + 1
#	new_saleprice = saleprice_avg * factors_
	
#	data_ = np.random.normal(new_saleprice, 0.44, 1000)

#	fig = ff.create_distplot(data_, [], show_hist=False)
	
	fig = px.histogram(data_, labels={'count': 'Dist.', 'value': 'Prices'})
	fig.update_layout({
		'plot_bgcolor': 'rgba(0, 0, 0, 0)',
		'paper_bgcolor': 'rgba(8,124,210,0.1)',
		})
	fig.update_yaxes(visible=False, showticklabels=False)
	fig.add_annotation(
		text=new_change, x=new_price, y=100, arrowhead=2, showarrow=True, 
		font=dict(family="Courier New, monospace", size=24)
	)
	fig.layout.update(showlegend=False)
	
	return fig



if __name__ == "__main__":
	app.run_server(debug=True)
	