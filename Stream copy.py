import streamlit as st
import pandas as pd
import polars as pl
import numpy as np
import plotly.express as px
import os
from jupyter_dash import JupyterDash
from dash import Dash, dcc, html, Input, Output, State
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.offline as plot
import requests
from dateutil.relativedelta import relativedelta
from datetime import datetime,timedelta
import plotly.io as pio
pio.templates.default = "plotly"
import folium
from folium import FeatureGroup, Map, Marker
import pandas as pd
import numpy as np


df = pd.read_feather(r"D:\Work for MWG\Dash folium\Data/Data.feather")
df = df[df['Date'] >= datetime(2023, 7, 1).date()]
df = pd.pivot_table(df,index="Mã siêu thị",values="Số lượng xuất nguyên giá",aggfunc=np.sum).reset_index()
df_store = pd.read_feather(r"D:\Work for MWG\Dash folium\Data\GetStoreDistance.feather")

dataset = pd.merge(left=df,right=df_store,on=['Mã siêu thị'],how='left')
dataset = dataset.dropna(axis=0)


app = JupyterDash(__name__)

product_list = np.random.choice([1, 2, 3, 4], size=10)
sub_group_list = np.random.choice([1, 2, 3, 4], size=10)
store_list = np.random.choice([1, 2, 3, 4], size=10)
rsm_list = np.random.choice([1, 2, 3, 4], size=10)
am_list = np.random.choice([1, 2, 3, 4], size=10)

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
            sub_group_list,
            sub_group_list[0],
            id='sub_group_selected'
            )],style={'flex': '1.4', 'margin-right': '10px'}),
        html.Div([
            dcc.Dropdown(
            options=product_list,
            value=product_list[0],
            id='product_selected'
            )],style={'flex': '2.4', 'margin-right': '10px'}),
        html.Div([
            dcc.Dropdown(
            options=rsm_list,
            value = rsm_list[0],
            id='rsm_selected'
        )],style={'flex': '2','margin-right': '10px'}),
        html.Div([
            dcc.Dropdown(
            options=am_list,
            value = am_list[0],
            id='am_selected'
        )],style={'flex': '2','margin-right': '10px'}),
        html.Div([
            dcc.Dropdown(
            options=store_list,
            value = store_list[0],
            id='store_selected'
        )],style={'flex': '0.7','margin-right': '10px'}),
        html.Div([
            dcc.Dropdown(
            options=[1,2,3,4,5,6,7,8,9,10,11,12],
            value = datetime.now().month,
            id='month_selected'
        )],style={'flex': '0.7','margin-right': '10px'}),
        html.Div([
            dcc.RangeSlider(
                id = 'days_selected',
                min = 1,
                max = 31,
                step = 1,
                dots = False,
                marks=None,
                tooltip={"placement": "bottom", "always_visible": True},
                value = [1,31],
                allowCross=False,
                )],style={'flex': '1.8'}),
    ], style={'display': 'flex', 'justify-content': 'flex-start', 'align-items': 'center'}),

    dcc.Graph(id='graph-with-slider'),

])

@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('sub_group_selected', 'value'),
    Input('product_selected', 'value'),
    Input('rsm_selected', 'value'),
    Input('am_selected', 'value'),
    Input('store_selected', 'value'),
    Input('month_selected', 'value'),
    Input('days_selected', 'value'),
    State('sub_group_selected', 'value'),
    State('product_selected', 'value'),
    State('rsm_selected', 'value'),
    State('am_selected', 'value'),
    State('store_selected', 'value'),
    State('month_selected', 'value'),
    State('days_selected', 'value'),
    )
def update_figure(sub_group_selected,product_selected,rsm_selected,am_selected,store_selected,month_selected,days_selected,sub_group_state,product_state,rsm_state,am_state,store_state,month_state,day_state):

    lat = 10.8231
    long = 106.6297
    zoom = 12
    gmap2 = folium.Map(location=(lat, long), zoom_start=zoom)

    def _addMarker(gmap):
        for i, row in dataset.iterrows():
            # Tính bán kính dựa trên số lượng bán
            radius = row['Số lượng xuất nguyên giá'] / 500
            # Tạo đánh dấu với bán kính và màu sắc tương ứng
            marker = folium.CircleMarker(location=(row['Kinh độ'], row['Vĩ độ']), radius=radius, color='red', fill=True, fill_color='red', fill_opacity=0.5, popup=row['Kho đến'])
            marker.add_to(gmap)

    _addMarker(gmap2)
    fig = gmap2
    return fig

if __name__ == "__main__":
    app.run(debug=False)
