import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output
import pandas as pd
import plotly.express as px

df1=""

app=dash.Dash()

app.layout=html.Div(
    <html>
<head>
<title> page1 </title>
</head>
<body>
<h1>pie chart for 5308 </h1>
<body bgcolour="red" text="yellow">
# to create a pie chart
import plotly.express as px
df = px.data.gapminder().query("state of health= df[capacity of discharge]/df[capactiy of charge]*100)
fig = px.pie(df, values='pop', names='country', title='cell id: 5308')
fig.show()
</body>
</html>)
<head>
<title> pie chart for 5308 </h1>
</head>
<body>
<h1>pie chart for 5329</h1>
<body bgcolour="blue" text="white">
import plotly.express as px
df = px.data.gapminder().query("state of health= df[capacity of discharge]/df[capactiy of charge]*100)
fig = px.pie(df, values='pop', names='country', title='cell id: 5308')
fig.show()
</body>
</html>

<head>
<title>frameset</title>
</head>
<frameset cols="50%,50%">
<frameset src="page 1">
<frameset src="page 2">
</html>

#Run local Server

if __name__=='__main__':
    app.run_server(debug=True)
