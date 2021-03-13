import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns

def func(pct, allvals):
    '''
    Function to label percentage and number of listings for the given neighbourhood
    input pct: percentage
    input allvals: neighborhood names
    return: pr
    '''
    assert isinstance(allvals,np.ndarray), "allvals not an np array"
    absolute = int(pct/100.*np.sum(allvals))
    return "{:1.1f}%\n({:d})".format(pct, absolute)

def view_neighbourhood_dist(data):
    '''
    Create a pie chart for the neighbourhood distribution
    '''
    assert isinstance(data,pd.DataFrame), "data not an dataframe"    
    labels = data.neighbourhood.value_counts().index[0:10]
    shape = data.neighbourhood.value_counts().values[0:10]
    plt.figure(figsize=(12,12))

    # Visualize the pie chart
    plt.pie(shape, explode = None, labels=labels, colors= None, autopct = lambda pct: func(pct, shape), startangle=90)
    plt.title('Neighborhood Occupancy in San Diego', fontsize= 30)
    plt.rcParams['font.size'] = 15
    plt.show()
    
def view_price_distribution(data):
    '''
    Plot Price Distribution on top 10 region area
    Only use the data whose price is less than $1000
    '''
    assert isinstance(data,pd.DataFrame), "data not an dataframe"
    price_data = data[data.price < 1000]
    labels = data.neighbourhood.value_counts().index[0:10]
    ten_top_neighbourhood = price_data.loc[data['neighbourhood'].isin(labels)]
    plt.style.use('fivethirtyeight')
    plt.figure(figsize=(16,14))
    sns.boxplot(y='price',x='neighbourhood',data = ten_top_neighbourhood)
    plt.xlabel('Cities', fontsize = 20)
    plt.ylabel('Price', fontsize = 20)
    plt.title('City Price Distribution', fontsize = 30)
    plt.show()

def get_mini_pies(data):
    '''
    Plot room type proportion on all region area
    '''
    assert isinstance(data,pd.DataFrame), "data not an dataframe"

    #set color
    colors = ['#16478E', '#0083BF', '#32C3EB', '#97D9EA']
    room_types=data.groupby(['neighbourhood', 'room_type']).size()
    # use below line to show rooms types in all cities
    # for region in data.neighbourhood.unique():
    plot_num = 0
    for region in ['Mission Bay', 'La Jolla', 'Pacific Beach']:
        neighbourhood_types = room_types[region]
        labels = neighbourhood_types.index
        sizes = neighbourhood_types.values
        
        neighbourhood_fig = go.Figure(data = [go.Pie(labels = labels, values = sizes, hole = 0.6)])
        neighbourhood_fig.update_traces(title = region, marker=dict(colors=colors))
        neighbourhood_fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=1.1
        )   )
        neighbourhood_fig.show()
        plot_num += 1