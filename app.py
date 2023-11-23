'''
 # @ Create Time: 2023-11-23 13:08:57.136857
'''

from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Convert the NumPy array to a pandas DataFrame
# Set a random seed for reproducibility
np.random.seed(42)

# Define the dimensions of the array
rows, columns = 50, 50

# Generate a random 2D array of nitrogen levels between 50 and 200
nitrogen_levels = np.random.uniform(120, 200, size=(rows, columns))

# Convert the NumPy array to a pandas DataFrame
df = pd.DataFrame(nitrogen_levels)

# Generate random numbers between 195 and 200
random_numbers0_20 = np.random.uniform(195, 200, size=(20, 20))
random_numbers20_35 = np.random.uniform(175, 195, size=(15, 20))
random_numbers35_50 = np.random.uniform(155, 175, size=(15, 20))

irandom_numbers0_20 = np.random.uniform(195, 200, size=(20, 15))
irandom_numbers20_35 = np.random.uniform(175, 195, size=(15, 15))
irandom_numbers35_50 = np.random.uniform(155, 175, size=(15, 15))

# Update the specified range in the DataFrame with the random numbers
df.iloc[0:20, 0:20] = random_numbers0_20
df.iloc[20:35, 0:20] = random_numbers20_35
df.iloc[35:50, 0:20] = random_numbers35_50

df.iloc[0:20, 20:35] = irandom_numbers0_20
df.iloc[20:35, 20:35] = irandom_numbers20_35
df.iloc[35:50, 20:35] = irandom_numbers35_50

df = pd.DataFrame(nitrogen_levels)
# Create a meshgrid for the surface plot
x, y = np.meshgrid(np.arange(0, columns), np.arange(0, rows))

# Create a 3D topographical map plot
fig = go.Figure(data=[go.Surface(z=df.values, x=x, y=y)])

# Update the layout
fig.update_layout(title='3D Topographical Map of Nitrogen Level Distribution Pound per Acre',
                  scene=dict(
                      xaxis=dict(title='Farm Dimension (X)'),
                      yaxis=dict(title='Farm Dimension (Y)'),
                      zaxis=dict(title='Nitrogen Level'),
                  ),
                  autosize=True,
                  width=800, height=600,
                  margin=dict(l=65, r=50, b=65, t=90)
)

# Notes
notes = html.Div([
    html.P("Sample Tests for Nitrogen Level in 2500 Acres Farm. Shows Nitrogen Concentration in terms of Pound per Acre.", style={'margin': '10px'}),
    html.P("Yellow Area: Very High Concentration between 195 and 200 lbs/acre.", style={'margin': '10px', 'color': 'yellow'}),
    html.P("Orange Area: High Concentration between 175 and 194 lbs/acre.", style={'margin': '10px', 'color': 'orange'}),
    html.P("Red Area: Average Concentration between 150 and 174 lbs/acre.", style={'margin': '10px', 'color': 'red'}),
    html.P("Purple Area: Low Concentration below 150 lbs/acre.", style={'margin': '10px', 'color': 'purple'}),
    html.P("Blue Area: very Low Concentration.", style={'margin': '10px', 'color': 'blue'}),
    # Note with a clickable link

])
note_with_link = html.P([
    "Note: This is a demo Map for 30daymapchallenge, if you are looking for the best way to interpret your soil sample test, refer to this amazing Paper ",
    html.A("Link to Paper", href="https://www.agry.purdue.edu/ext/corn/news/timeless/assessavailablen.html", target="_blank"),
], style={'margin': '10px', 'color': 'blue'})


app = Dash(__name__)

# Declare server for Heroku deployment. Needed for Procfile.
server = app.server

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
app.layout = html.Div([
    dcc.Graph(figure=fig),
    notes,
    note_with_link
])


if __name__ == '__main__':
    app.run_server(debug=True)
