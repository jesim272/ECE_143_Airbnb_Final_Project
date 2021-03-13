import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt

def price_plot(x_pos,y_pos,date_array, price_array):
    '''
    Plot the line plot for price changing:
    '''
    assert isinstance(x_pos,int), "x_pos not an int"
    assert isinstance(y_pos, int), "y_pos not an int"
    assert isinstance(date_array,np.ndarray), "date array not np array"
    assert isinstance(price_array,np.ndarray), "price array not np array"

    fig, ax = plt.subplots(1, figsize=(18, 15))# 18,10
    plt.title('Annual Trend of Room Pricing', fontsize=30)
    plt.xlabel('2015                        2016                        2017                        2018                        2019                        2020                        2021', fontsize=15)  
    plt.ylabel('Price ($) per Night', fontsize = 20)  
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    plt.text(x_pos, y_pos, "Year",fontsize = 20)
    plt.rc('ytick', labelsize=15)
    ax.plot(date_array, price_array[:,0], c='red', marker='',label='Shared Room')
    ax.plot(date_array, price_array[:,1], c='g', marker='',label='Hotel Room')
    ax.plot(date_array, price_array[:,2], c='b', marker='',label='Entire Home')
    ax.plot(date_array, price_array[:,3], c='y', marker='',label='Private Room')
    ax.spines['left'].set_visible(True)
    plt.xlim(date_array[0], date_array[-1])
    plt.subplots_adjust(bottom=0.5)
    plt.axis('on')
    plt.grid(False)
    plt.legend(bbox_to_anchor=(1.02, 1), prop={'size': 15})
    plt.show()

def avg_avail_plot(x_pos,y_pos,date_array,avail_array):
    '''
    Plot the line plot for price changing:
    '''
    assert isinstance(x_pos,int), "x_pos not an int"
    assert isinstance(y_pos, int), "y_pos not an int"
    assert isinstance(date_array,np.ndarray), "date array not np array"
    assert isinstance(avail_array,np.ndarray), "price array not np array"

    plt.figure(figsize=(18,15))
    plt.title('Annual Trend of Room Availability', fontsize=30)
    plt.xlabel('2015                        2016                        2017                        2018                        2019                        2020                        2021', fontsize = 15)  

    plt.ylabel('Number of Days Per 365', fontsize = 20)  
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    plt.rc('ytick', labelsize=15)
    plt.text(x_pos, y_pos, "Year",fontsize = 20)
    plt.plot(date_array, avail_array[:,0], c='red', marker='',label='Shared Room')
    plt.plot(date_array, avail_array[:,1], c='g', marker='',label='Hotel Room')
    plt.plot(date_array, avail_array[:,2], c='b', marker='',label='Entire Home')
    plt.plot(date_array, avail_array[:,3], c='y', marker='',label='Private Room')
    plt.xlim(date_array[0], date_array[-1])
    plt.subplots_adjust(bottom=0.5)
    plt.legend(bbox_to_anchor=(1.2, 1), prop={'size': 15})
    plt.show()

def min_night(x_pos,y_pos,date_array, minimum_night_array):
    '''
    Plot the line plot for price changing:
    '''
    assert isinstance(x_pos,int), "x_pos not an int"
    assert isinstance(y_pos, int), "y_pos not an int"
    assert isinstance(date_array,np.ndarray), "date array not np array"
    assert isinstance(minimum_night_array,np.ndarray), "price array not np array"

    plt.figure(figsize=(18,15))
    plt.title('Annual Trend of Minimum Nights', fontsize=30)
    plt.xlabel('2015                        2016                        2017                        2018                        2019                        2020                        2021', fontsize = 15)  
    plt.ylabel('Number of Nights', fontsize = 20)
    plt.rc('ytick', labelsize=15)
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    plt.text(x_pos, -1, "Year",fontsize = 20)
    plt.plot(date_array, minimum_night_array[:,0], c='red', marker='',label='Shared Room')
    plt.plot(date_array, minimum_night_array[:,1], c='g', marker='',label='Hotel Room')
    plt.plot(date_array, minimum_night_array[:,2], c='b', marker='',label='Entire Home')
    plt.plot(date_array, minimum_night_array[:,3], c='y', marker='',label='Private Room')
    plt.xlim(date_array[0], date_array[-1])
    plt.grid(False)
    plt.subplots_adjust(bottom=0.5)
    plt.legend(bbox_to_anchor=(1.02, 1), prop={'size': 15})
    plt.axis(True)
    plt.show()