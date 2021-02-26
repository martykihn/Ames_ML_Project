# this was called demo.py
# to get rid of that structure - delete: create_layout, demo_callbacks
# add some css files too for formatting

import io
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

import pandas as pd
import plotly.graph_objs as go
import plotly.figure_factory as ff

# components in the layout code

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)

def Card(children, **kwargs):
	return html.Section(children, className="card_style")
	
def NamedSlider(name, short, min, max, step, val, marks=None):
	if marks:
		step = None
	else:
		marks = {i: i for i in range(min, max + 1, step)}
		
	return html.Div(
        style={"margin": "25px 5px 30px 0px"},
        children=[
            f"{name}:",
            html.Div(
                style={"margin-left": "5px"},
                children=[
                    dcc.Slider(
                        id=f"slider-{short}",
                        min=min,
                        max=max,
                        marks=marks,
                        step=step,
                        value=val,
                    )
                ],
            ),
        ],
    )

def NamedInlineRadioItems(name, short, options, val, **kwargs):
    return html.Div(
        id=f"div-{short}",
        style={"display": "inline-block"},
        children=[
            f"{name}:",
            dcc.RadioItems(
                id=f"radio-{short}",
                options=options,
                value=val,
                labelStyle={"display": "inline-block", "margin-right": "7px"},
                style={"display": "inline-block", "margin-left": "7px"},
            ),
        ],
    )

# layout of the app here

def create_layout(app):
	return html.Div(
		className="row",
        style={"max-width": "100%", "font-size": "1.5rem", "padding": "0px 0px"},
        children=[
            # Header
            html.Div(
                className="row header",
                id="app-header",
                style={"background-color": "#f9f9f9"},
                children=[
                    html.Div(
                        [
                            html.Img(
                                src=app.get_asset_url("image.png"),
                                className="logo",
                                id="plotly-image",
                            )
                        ],
                        className="three columns header_img",
                    ),
                    html.Div(
                        [
                            html.H3(
                                "House Price Predictor",
                                className="header_title",
                                id="app-title",
                            )
                        ],
                        className="nine columns header_title_container",
                    ),
                ],
            ),
            
            #Body
            html.Div(
            	className="row background",
            	style={"padding": "10px"},
            	children=[
            		html.Div(
            			className="three columns",
            			children=[
            				Card(
            					[
            						dcc.Input(
            							id="saleprice_avg",
            							placeholder='Enter Avg. House Price',
            							type="number",
            							value=200000
            						),
            						dcc.Dropdown(
            							id="dropdown-neighborhood",
            							searchable=False,
            							clearable=False,
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
            							value=1.0,
            						),
            						NamedSlider(
            							name="Above-Ground Sq. Ft.",
            							short="above-ground-sf",
            							min=0,
            							max=2500,
            							step=None,
            							val=1500,
            							marks={
            								i: str(i) for i in [500, 1500, 2000]
            							},
            						),
            						NamedSlider(
            							name="Overall Quality",
            							short="overall-quality",
            							min=1,
            							max=5,
            							step=None,
            							val=3,
            							marks={
            								i: str(i) for i in [2, 3, 4]
            							},
            						),
            						NamedInlineRadioItems(
            							name="Basement Quality",
            							short="basement-quality",
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
        								val=1,
    								),
    								NamedInlineRadioItems(
            							name="Kitchen Quality",
            							short="kitchen-quality",
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
            							val=1,
    								),
            						NamedInlineRadioItems(
            							name="Exterior Quality",
            							short="exterior-quality",
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
        								val=1,
    								),
            						NamedInlineRadioItems(
            							name="# of Baths",
            							short="baths",
    									options=[
            								{
            									"label": "1",
            									"value": 0.95,
            								},
    										{
            									"label": "2",
            									"value": 1,
            								},
        									{
    											"label": "3+",
            									"value": 1.05}
            	 						],
            							val=1,
            						),
        							NamedSlider(
    									name="Wood Deck SF",
        								short="wood-deck",
        								min=0,
        								max=300,
										step=None,
        								val=200,
        								marks={i: str(i) for i in [100, 200]},
        							),
            						NamedInlineRadioItems(
            							name="Garage (Y/N)?",
        								short="garage",
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
            							val=1,
            						),
            						NamedInlineRadioItems(
        								name="Central Air (Y/N)?",
            							short="central-air",
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
    									val=1,
            						),
            					],
        					),
    					]
            		)
            	],
        	),
            html.Div(
            	className="six columns",
            	children=[
            		dcc.Graph(id="graph-price-dist", style={"height": "98vh"})
            	],
            ),
            html.Div(
            	className="three columns",
            	id = "third-column",
            ),
        ],
    )

def demo_callbacks(app):
	def generate_figure(mu1, factors_, layout):
	
		sigma_factor = 0.44
		sigma1 = mu1 * sigma_factor
		mu2 = mu1 * (1 + factors_) #this is product of all the factors
		sigma2 = mu2 * sigma_factor
		
		x1 = np.random.normal(mu1, sigma1, 1000)
		x2 = np.random.normal(mu2, sigma2, 1000)
		
		data_ = [x1, x2]
		labels = ['Baseline', 'Improved']
		colors = ['#333F44', '#37AA9C']
		figure = ff.create_displot(data_, labels, show_hist = False, colors = colors)
		
		figure.update_layout(title_text="Distribution of Sale Prices")
		
#		figure = go.Figure(data=data_, layout=layout)
		
		return figure
		
	@app.callback(
		Output("graph-price-dist", "figure"),
		[
			Input("saleprice_avg", "value"),
			Input("dropdown-neighborhood", "value"),
			Input("slider-above-ground-sf", "value"),
			Input("slider-overall-quality", "value"),
			Input("radio-basement-quality", "value"),
			Input("radio-kitchen-quality", "value"),
			Input("radio-exterior-quality", "value"),
			Input("radio-baths", "value"),
			Input("slider-wood-deck", "value"),
			Input("radio-garage", "value"),
			Input("radio-central-air", "value"),
		],
	)
	def display_price_plot(
		saleprice_avg,
		neighborhood,
		abovegroundsf,
		overallqual,
		basementqual,
		kitchenqual,
		exteriorqual,
		baths,
		wood_deck,
		garage,
		central_air,
		):
		
		factors_ = (neighborhood - 1) + (abovegroundsf/1500) + \
		(overallqual/3) + (basementqual - 1) + (kitchenqual - 1) + \
		(exteriorqual - 1) + (baths - 1) + (wood_deck/100 - 1) + \
		(garage - 1) + (central_air - 1)
		
		#plot layout
		axes = dict(title="", showgrid=True, zeroline=False, showticklabels=False)
		
		layout = go.Layout(
			margin=dict(l=0, r=0, b=0, t=0),
			scene=dict(xaxis=axes, yaxis=axes),
		)
		
		figure = generate_figure(saleprice_avg, factors_, layout)
		
		return figure

# main code here
server = app.server
app.layout = create_layout(app)
demo_callbacks(app)

# Running server
if __name__ == "__main__":
    app.run_server(debug=True)