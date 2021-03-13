########################################
#            Libraries 
########################################
import os
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import plotly.offline as pyo
import folium
from folium.plugins import HeatMap
from Cleaning_data.clean_data import clean_data
from Plots.line_plots import *
from Maps.heat_maps import *
from Maps.charts import *
#from Get_file_structure.structure import list_files


def string_to_date(file_name):
    '''
    Turns strings to date

    param: file with dates
    input param: file
    return: data time object
    '''
    assert isinstance(file_name,str), "input is not a string"
    month_str_to_int = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 
                        'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 
                        'Sep':9, 'Oct':10,'Nov':11,'Dec':12}
    month = month_str_to_int[file_name[15+9:15+12]]
    day = int(file_name[15+13:15+15])
    year = int(file_name[15+16:15+20])
    return datetime.date(year, month, day)

def find_index(array, dt):
    '''
    Find index from array and datetime object
    param array: array of dates
    input array: array
    param dt: datetime object 
    input dt: datetime object
    return: index
    '''
    assert isinstance(array, list), "array is not an array"
    assert isinstance(dt, datetime.date), "dt is not datetime"

    for i in range(len(array)):
        if dt.__eq__(array[i]):
            return i

def get_listing_data_name():
    '''
    Iterating through the listing data and storing the 
    files into a list
    '''
    listing_data_path = './listing_data'
    listing_data_name = []

    # Loading all the listing data name
    for file in os.listdir(listing_data_path):
        name = listing_data_path + '/' + file
        if len(name) == 39:
            listing_data_name.append(listing_data_path + '/' +  file)
    return listing_data_name

def get_listing_data(listing_data_name):
    '''
    Clean the data and save in a new list
    '''
    assert isinstance(listing_data_name,list), "listinng_data_name not a list"
    listing_data = [] # the list contains the pandas variable
    for file_name in listing_data_name:
        #data = pd.read_csv(file_name)
        data = clean_data(file_name)
        listing_data.append(data)
    return listing_data

def get_time_line(listing_data_name):
    '''
    Creates a time line for all the data
    This is will be used for plotting
    '''
    assert isinstance(listing_data_name,list), "listinng_data_name not a list"

    num_data = 0 # total number of files
    date = [] # the datetime variable which restore the date
    date_array = None # The date_array, numpy array, restores the differnece of two dates
    # Create the time line array for date
    for file_name in listing_data_name:
        dt = string_to_date(file_name)
        date.append(dt)
    num_data = len(date)
    # Bubble Sort
    for i in range(num_data):
        for j in reversed(range(i, num_data)):
            if date[i].__ge__(date[j]):
                date[i], date[j] = date[j], date[i]
    date_array = np.zeros((len(date)))

    # Calculate the difference days between two dates:
    for i in range(num_data):
        if i == 0:
            continue
        date_array[i] = (date[i].__sub__(date[i-1])).days + date_array[i-1]
    price_array = np.zeros((num_data, 5))
    cnt_array = np.zeros((num_data, 5))
    return price_array, cnt_array, date, date_array,num_data

def get_variable():
    '''
    Returning a price array and count array
    This will be used for plotting
    '''
    room = {'Shared room':0, 'Hotel room':1, 'Entire home/apt':2, 'Private room':3} # room type dict  
    # Loop for all data
    for fname in listing_data_name:
        data = pd.read_csv(fname)
        dt = string_to_date(fname)
        index = find_index(date, dt)
        num = len(data)
        for i in range(num):
            price_array[index][room[data['room_type'][i]]] += data['price'][i]
            cnt_array[index][room[data['room_type'][i]]] += 1
            price_array[index][4] += data['price'][i]
            cnt_array[index][4] += 1
        for i in range(5):
            if cnt_array[index][i] == 0:
                continue
            price_array[index][i] /= cnt_array[index][i]
    
    return price_array,cnt_array
    
def avg_availablilty(listing_data_name,num_data):
    '''
    Get all the data under the "availability" column which
    will be used to plot the availability trend
    '''
    assert isinstance(listing_data_name,list), "listinng_data_name not a list"
    assert isinstance(num_data, int), "num_data not an int"
    # Loop for all data
    room = {'Shared room':0, 'Hotel room':1, 'Entire home/apt':2, 'Private room':3} # room type dict
    avail_array = np.zeros((num_data, 5))
    cnt_array = np.zeros((num_data, 5))

    for fname in listing_data_name:
        data = pd.read_csv(fname)
        dt = string_to_date(fname)
        index = find_index(date, dt)
        num = len(data)
        for i in range(num):
            avail_array[index][room[data['room_type'][i]]] += data['availability_365'][i]
            cnt_array[index][room[data['room_type'][i]]] += 1
            avail_array[index][4] += data['availability_365'][i]
            cnt_array[index][4] += 1
        for i in range(5):
            if cnt_array[index][i] == 0:
                continue
            avail_array[index][i] /= cnt_array[index][i]
    return date_array, avail_array

def min_nights(listing_date_name,num_data):
    '''
    Get all the data under the "minimum nights" column which
    will be used to plot the minimum nights trend
    '''
    assert isinstance(listing_data_name,list), "listinng_data_name not a list"
    assert isinstance(num_data,int), "num_data is not an int"
    room = {'Shared room':0, 'Hotel room':1, 'Entire home/apt':2, 'Private room':3} # room type dict
    # Loop for all data
    minimum_night_array = np.zeros((num_data, 5))
    cnt_array = np.zeros((num_data, 5))

    for fname in listing_data_name:
        data = pd.read_csv(fname)
        dt = string_to_date(fname)
        index = find_index(date, dt)
        num = len(data)
        for i in range(num):
            minimum_night_array[index][room[data['room_type'][i]]] += data['minimum_nights'][i]
            cnt_array[index][room[data['room_type'][i]]] += 1
            minimum_night_array[index][4] += data['minimum_nights'][i]
            cnt_array[index][4] += 1
        for i in range(5):
            if cnt_array[index][i] == 0:
                continue
            minimum_night_array[index][i] /= cnt_array[index][i]

    return date_array, minimum_night_array

#######################################################
#                    def MAIN ():
#######################################################

if __name__ == "__main__":   
    '''
    This main function will stores and clean all that data under the 
    listing data folder and will create the trend's plot and the heat maps
    necessary to make a investment decision for potential host
    '''   
    # Separate file information for plotting the charts and heat maps
    listing_data_name = get_listing_data_name()
    listing_data = get_listing_data(listing_data_name)
    
    price_array, cnt_array,date, date_array,num_data = get_time_line(listing_data_name)
    price_array, cnt_array = get_variable()
    # Additional text for x-axis
    x_pos = 950
    y_pos = -55
    price_plot(x_pos,y_pos,date_array,price_array)
    
    # Trend of the Average availability
    listing_data_name = get_listing_data_name()
    date_array, avail_array = avg_availablilty(listing_data_name,num_data)
    avg_avail_plot(x_pos,y_pos,date_array,avail_array)

    # Trend of Minimum Nights
    listing_data_name = get_listing_data_name()
    date_array, min_night_array = min_nights(listing_data_name, num_data)
    min_night(x_pos, y_pos,date_array, min_night_array)

    # Visualize all Location Maps
    path_name  = './listing_data/listings_Dec_23_2020.csv'  # use any listing
    map_data  = create_location_map(path_name)
    data, token = view_entire_location(map_data)
    #Visualize price < $300
    cheap_location_price(data,token)
    #Visualize prices between $300 and $1000
    median_location_price(data,token)
    #Visualize prices > $1000
    luxury_location_price(data,token)

    #View the locations with availability
    view_avail_location(data,token)

    # Visualize minimum nights plots
    min_nights5(data,token)
    over_night5(data,token)

    #Visualize neightbourhoods
    view_neighbourhood_dist(data)
    view_price_distribution(data)

    #View mini pie charts of the neighborhoods
    get_mini_pies(data)