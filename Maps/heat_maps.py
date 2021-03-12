import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import plotly.offline as pyo
import folium
from folium.plugins import HeatMap

def create_location_map(path_name):
    map_data = pd.read_csv(map_data_path)
    print(map_data['latitude'].min(), map_data['latitude'].max(), map_data['longitude'].min(), map_data['longitude'].max())
    return map_data

def view_entire_location(map_data):
    # define the world map
    world_map = folium.Map()

    # San Diego Latitude and Longitude
    latitude = 32.72
    longitude = -117.16

    limit = 10000
    data = map_data.iloc[0:limit, :]

    san_map = folium.Map(location=[latitude, longitude], zoom_start=10)
    HeatMap(data[['latitude','longitude']].dropna(),radius=8,gradient={0.2:'blue',0.4:'purple',0.6:'orange',1.0:'red'}).add_to(san_map)
    san_map

    
    # Same figure above with markers    
    token = 'pk.eyJ1IjoiNzM2ODkxNDEwIiwiYSI6ImNrbDY4MnlvZzBibGMyd283OGprYWFuM3UifQ.MqFaTEXVYsnkkwFhxwEkmQ'
    fig = go.Figure(go.Scattermapbox(mode='markers',
                                    lon = data.longitude,
                                    lat = data.latitude,
                                    hovertext = data.id))
    fig.update_layout(mapbox={'accesstoken' : token, 'center' : {'lon' : -117.063, 'lat': 32.765}, 'zoom':10.0},
                    margin = {'l' : 0, 'r' : 0, 't' : 0, 'b' : 0})

    return data,token

def cheap_location_price(data, token):
    price_data = data[data.price < 300]
    fig = px.scatter_mapbox(price_data,
                        lon = 'longitude',
                        lat = 'latitude',
                        color = 'price',
                            title = 'price map',
                            hover_name = 'id',
                            color_continuous_scale = px.colors.carto.Temps
                        )
    fig.update_layout(mapbox={'accesstoken' : token, 'center' : {'lon' : -117.063, 'lat': 32.765}, 'zoom':10.0},
                    margin = {'l' : 0, 'r' : 0, 't' : 0, 'b' : 0})

def median_location_price(data,token):
    price_data = data[data.price > 300]
    price_data = price_data[price_data.price < 1000]
    fig = px.scatter_mapbox(price_data,
                        lon = 'longitude',
                        lat = 'latitude',
                        color = 'price',
                            title = 'price map',
                            hover_name = 'id',
                            color_continuous_scale = px.colors.carto.Temps
                        )
    fig.update_layout(mapbox={'accesstoken' : token, 'center' : {'lon' : -117.063, 'lat': 32.765}, 'zoom':10.0},
                    margin = {'l' : 0, 'r' : 0, 't' : 0, 'b' : 0})

def luxury_location_price(data,token):
    price_data = data[data.price > 1000]
    fig = px.scatter_mapbox(price_data,
                        lon = 'longitude',
                        lat = 'latitude',
                        color = 'price',
                            title = 'price map',
                            hover_name = 'id',
                            color_continuous_scale = px.colors.carto.Temps
                        )
    fig.update_layout(mapbox={'accesstoken' : token, 'center' : {'lon' : -117.063, 'lat': 32.765}, 'zoom':10.0},
                    margin = {'l' : 0, 'r' : 0, 't' : 0, 'b' : 0})


def view_avail_location(data,token):
    available_data = data
    fig = px.scatter_mapbox(available_data,
                        lon = 'longitude',
                        lat = 'latitude',
                        color = 'availability_365',
                            title = 'availability_365 map',
                            hover_name = 'id',
                            color_continuous_scale = px.colors.carto.Temps
                        )
    fig.update_layout(mapbox={'accesstoken' : token, 'center' : {'lon' : -117.063, 'lat': 32.765}, 'zoom':10.0},
                    margin = {'l' : 0, 'r' : 0, 't' : 0, 'b' : 0})

def min_nights5(data,token):
    minimum_nights_data = data[data.minimum_nights < 5]
    fig = px.scatter_mapbox(minimum_nights_data,
                        lon = 'longitude',
                        lat = 'latitude',
                        color = 'minimum_nights',
                            title = 'availability_365 map',
                            hover_name = 'id',
                            color_continuous_scale = px.colors.carto.Temps
                        )
    fig.update_layout(mapbox={'accesstoken' : token, 'center' : {'lon' : -117.063, 'lat': 32.765}, 'zoom':10.0},
                    margin = {'l' : 0, 'r' : 0, 't' : 0, 'b' : 0})
def over_night5(data,token):
    minimum_nights_data = data[data.minimum_nights > 5]
    minimum_nights_data = minimum_nights_data[minimum_nights_data.minimum_nights < 35]
    fig = px.scatter_mapbox(minimum_nights_data,
                        lon = 'longitude',
                        lat = 'latitude',
                        color = 'minimum_nights',
                            title = 'availability_365 map',
                            hover_name = 'id',
                            color_continuous_scale = px.colors.carto.Temps
                        )
    fig.update_layout(mapbox={'accesstoken' : token, 'center' : {'lon' : -117.063, 'lat': 32.765}, 'zoom':10.0},
                    margin = {'l' : 0, 'r' : 0, 't' : 0, 'b' : 0})
