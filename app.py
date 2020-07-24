import dash
from dash.dependencies import Output, Input, State
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(external_stylesheets=external_stylesheets)
server = app.server

colors = {'background': '#ffffff', 'text': '#33B5FF'}

app.layout = html.Div(style={'backgroundColor': colors['background'], 'color': colors['text'], 'height':'100vh', 'width':'100%', 'height':'100%', 'top':'0px', 'left':'0px'}, 
	children=[
		# Heading/Title
		html.H1(children='WSYB - The app that helps you decide what your next purchase should be.'),

		html.Div(style={'width':'100%'},
			children=[
				# Output
				html.Div(id='output_container', style={'display':'inline-block', 'float':'right', 'padding':50}),
				
				html.H4(children='Mandatory selections'),

				# Q1
				html.Div(children="What are you looking for?"),
				html.Div(style={'height': '5px'}),
				dcc.Dropdown(
					id='category_dropdown',
					style={'width': '35%'},
					options=[
			            {'label': 'Camera', 'value': 'Camera'},
			            {'label': 'Laptop', 'value': 'Laptop'},
			            {'label': 'Phone', 'value': 'Phone'}
			        ],
		        ),
		        html.Div(style={'height': '15px'}),

				# Q2
				html.Div(children="What's your budget?"),
				html.Div(style={'height': '5px'}),
				dcc.Dropdown(
					id='budget_dropdown',
					style={'width': '35%'},
					options=[
			            {'label': '< $1k', 'value': 'under_1k'},
			            {'label': '$1k to 2k', 'value': '1_2k'},
			            {'label': '> $2k', 'value': 'above_2k'}
			        ],
		        ),
		        html.Div(style={'height': '15px'}),

		        # Q3
		        html.Div(children="Are you ok with used products, or do you want only brand new?"),
		        html.Div(style={'height': '5px'}),
				dcc.Dropdown(
					id='used_or_new_dropdown',
					style={'width': '35%'},
					options=[
			            {'label': 'Used only', 'value': 'used_only'},
			            {'label': 'New only', 'value': 'new_only'},
			            {'label': 'Both used or new', 'value': 'both'}
			        ],
		        ),
		        html.Div(style={'height': '15px'}),

		        html.H4(children='Optional selections'),

		        # Q4
		        html.Div(children="What do you like to shoot?"),
		        html.Div(style={'height': '5px'}),
				dcc.Checklist(
					id='shooting_dropdown',
					options=[
			            {'label': 'Portrait', 'value': 'portrait'},
			            {'label': 'Landscape', 'value': 'landscape'},
			            {'label': 'Street', 'value': 'street'},
			            {'label': 'General/Daily stuff', 'value': 'general'},
			        ],
		        ),
		        html.Div(style={'height': '15px'}),

		        # Q5
		        html.Div(children="Are you looking for any specific sensor size?"),
				dcc.Checklist(
					id='sensor_dropdown',
					options=[
			            {'label': 'APSC', 'value': 'apsc'},
			            {'label': 'Full Frame', 'value': 'full_frame'},
			            {'label': 'Micro four-thirds', 'value': 'm43'},
			            {'label': 'Medium Format', 'value': 'medium_format'},
			        ],
		        ),
		        html.Div(style={'height': '10px'}),

		        # Q6
		        html.Div(children="Are you looking for any specific brand(s)?"),
		        html.Div(style={'height': '5px'}),
				dcc.Checklist(
					id='brand_dropdown',
					options=[
			            {'label': 'Nikon', 'value': 'nikon'},
			            {'label': 'Canon', 'value': 'canon'},
			            {'label': 'Sony', 'value': 'sony'},
			            {'label': 'Leica', 'value': 'leica'},
			            {'label': 'Fujifilm', 'value': 'fujifilm'},
			            {'label': 'Olympus', 'value': 'olympus'}
			        ],
		        ),

		        # Submit button
		        html.Button('Submit', id='submit_button'),
		    ]),
	])

@app.callback(
	Output('output_container', 'children'),
	[Input('submit_button', 'n_clicks')],
	[State('category_dropdown', 'value'),
	State('budget_dropdown', 'value'),
	State('used_or_new_dropdown', 'value'),
	])
def display_buy(n_clicks, category_dropdown, budget_dropdown, used_or_new_dropdown):
	if n_clicks:
		if category_dropdown=='Camera':
			if budget_dropdown=='under_1k':
				if used_or_new_dropdown=='both':
					return html.H3(children="You should buy: \n1. Fujifilm X-T2\n2. Nikon D5700\n3. Canon 80D"),
				elif used_or_new_dropdown=='new_only':
					return html.H3(children="You should buy: \n1. Nikon D5700\n2. Canon 80D"),
				else:
					return html.H3(children="You should buy: \n1. Fujifilm X-T2\n2. Nikon D750"),

			elif budget_dropdown=='1_2k':
				if used_or_new_dropdown=='both':
					return html.H3(children="You should buy: \n1. Fujifilm X-T3\n2. Nikon Z7\n3. Canon EOS R\n4. Fujifilm X-T4\n5. Sony A7 III"),
				elif used_or_new_dropdown=='new_only':
					return html.H3(children="You should buy: \n1. Nikon D760\n2. Canon R6"),
				else:
					return html.H3(children="You should buy: \n1. Fujifilm X-T3\n2. Sony A7 III\n3. Nikon Z7"),

			elif budget_dropdown=='above_2k':
				if used_or_new_dropdown=='both':
					return html.H3(children="You should buy: \n1. Sony A7R IV\n2. Fujifilm X-T4\n3. Nikon Z7\n4. Canon R5"),
				elif used_or_new_dropdown=='new_only':
					return html.H3(children="You should buy: \n1. Nikon Z7\n2. Canon R5"),
				else:
					return html.H3(children="You should buy: \n1. Leica Q\n2. Sony A7R IV"),
	else:
		return dash.no_update

if __name__ == '__main__':
	app.run_server(debug=True)