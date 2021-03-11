# San Diego Airbnb (Team 13)

## Team Members 
* [Ahnaf Ahmed](https://github.com/AhnafAhmed97) (ahnafahmed97@gmail.com)
* [Kevin Hau](https://github.com/pandadrago1) (kevin.hau19@gmail.com) 
* [Jesi Miranda-Santos](https://github.com/jesim272) (jesim272@gmail.com)
* Xibo Zhang
* [Zhizuo Zhang](https://github.com/MachineryZ "Zhizuo Zhang") (zhizuozhang@gmail.com)

## Problem 

Looking for the ideal Airbnb may be daunting for travellers, especially not knowing what factors come into play and if the airbnb is relatively close to where they want to visit. By understanding the host data for listing, one can make a decision whether or not it would be wise to become a host in a particular area. If one would like to become a host, which regions in San Diego are ideal for making an extra income? 

## Summary 
By analyzing the correlation between price and various external factors (ie reviews, room type, region, time of season, host rating, occupancy rate) and the profitability for hosts (through review metrics, price, number of listings per host, estimated occupancy, etc.), a better understanding of host-customer relationship was drawn. Additionally, the external factors helped identify which regions it would be wise to be a host in.

## Methodology
1. Visualized the price of a shared room, hotel room, entire home/apt, private room and average price of them all during a 5 year time span to understand the price trend.

2. Plotted the availability of a shared room, hotel room, entire home/apt, private room and average availiablity of them all to have an understanding of the most favorable type of room chosen by customers.

3. Graphed the number of minimum nights from mid 2015 to early 2020 of a shared room, hotel room, entire home/apt, private room, and average number of days to have a better sense of how many days hosts are willing to provide their space to traveling customers. 

4. Analyzed the relationship between the price ranges and the locations of the available spot. The top ten neignbourhoods were chosen for analysis and their repective price ranges were visualized.

5. Created a map of San Diego area and plotted points for the number of available places and 
for the minumum number of nights. This allowed for a visual cluster of hot spots for the most 
available Airbnb hostings.

6. Summarized findings of which regions are worthwhile to become a host.

## Dataset 
The data obtained can be found in the following links (look for San Diego):

* [Airbnb Data Pool](http://insideairbnb.com/get-the-data.html "Airbnb Data Pool")


Airbnb Datasets are created by Airbnb, an online marketplace company that connects people who want to rent out their homes with people who are looking for accommodation in that locale. Airbnb Datasets contain a lot of different csv files during different time periods. They record the price, room type, occupancy rate, host rating, location of room, etc. By analyzing Airbnb Datasets, we can find some relationship between those factors. 

Looking at San Deigo Airbnb data, the site includes listing data for various months over the past years, which is all placed under the ```./listing_data``` for easier viewing and analsis.

## Applications
Cross-correlate to ultimately determine if becoming a host is wise, and if so, how to improve their listings to attract travellers. Addionally, if one is deciding to become a host, how wise is to invest and become a host given prior years' data and the changes in density in certain regions to-date.

## File Structure
```
Group13_Project_2.ipynb
    main.py
    README.md
    Group13_Project_2.ipynb
    listing_data/
        .DS_Store
        listings_Apr_14_2018.csv
        listings_Apr_15_2019.csv
        listings_Apr_22_2020.csv
        ...
        
    presentation_photos/
        2020_coast_heatmap.PNG
        2020_downtown_heatmap.PNG
        2015_San_Diego_heatmap.PNG
        ...
    
    Cleaning_data/
        clean_data.py
       
    Get_file_structure/
        structure.py
   
    Maps/
        heat_maps.py
        charts.py
        
    Plots/
        line_plots.py
       
```
## The Code
* Python version: Python 3.6.8 64-bit and above
### Required Packages

For installing these packages, you can use either ```pip3``` to install packages. For example,

``` pip3 install numpy ```

or you can uses the Anaconda Command Prompt and use the following: 

``` conda install -c conda-forge [name of package] ```

1. numpy
2. pandas
3. matplotlib
4. seaborn
5. plotly
6. folium
 
```NOTE: If using VS Code and both methods above yield errors such as "module not found", open the terminal on VS Code and pip install the packages one the terminal```
### Running The Code

Download this github repository and open the Group13_Project_2 in Juptyer Notebook or in VS code.
Make sure you have all the packages downloaded.
If running the Jupyter Notebook code, you may run each line.

If one wants to use Jupyter Notebook within VS Code, please follow this link to create an environment:

[https://code.visualstudio.com/docs/python/jupyter-support](https://code.visualstudio.com/docs/python/jupyter-support)



If you are using the main.py file, you can just run the code itself by doing the following:
```
python main.py
```
The main.py will execute and display all the plots we generated. There is no difference in terms of output for the two files.

 
