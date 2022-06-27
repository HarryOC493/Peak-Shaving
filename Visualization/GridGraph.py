import csv
from wsgiref.simple_server import demo_app
from numpy import size

import pandas as pd
import matplotlib.pyplot as plt

print("Welcome, This script will generate a Line Graph to show the relationship between the power draw on Ireland's grid, and its frequency.")

Interval = 1    #Time Interval is a multiplier of 15, as demand data in 15m intervals, 
                #For example if you wanted an interval of 30m set this to '2'

Interval = int(input("Please enter an interval time: Format: 1 = 15 minutes, e.g for an interval of 30 minutes, enter '2'"))

FrequencyData = []
DemandData = []
X_List = []

def ReadDemand():
    #Read Scraped Data on Electricity Demand, and write it to the 'DemandData' variable for later use with Pandas
    with open('../Data/Demand/chart.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        LineCount = 1
        for row in csv_reader:
            if LineCount == 1:
                #Skipping first line as it contains the column headers
                pass
            elif LineCount % (Interval * 1) == 0:
                #This row is within current interval
                #Write data to Demand Data Variable
                data = float(row[1])
                DemandData.append(data)
            else:
                #This row i
                pass

            LineCount += 1

def ReadFrequency():
    #Read Scraped Data on Electricity Demand, and write it to the 'DemandData' variable for later use with Pandas
    with open('../Data/Frequency/Data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        LineCount = 1
        TimeCount = 1
        for row in csv_reader:
            if LineCount == 1:
                #Skipping first line as it contains the column headers
                pass
            elif LineCount % (Interval * 180) == 0:
                #This row is within current interval
                #Write data to Demand Data Variable
                data = float(row[1])
                X_List.append(TimeCount * 15)
                FrequencyData.append(data)
                TimeCount += 1
            else:
                #This row is not within the current time interval
                pass
            LineCount += 1

def CreateGraph(FrequencyData, DemandData):
    #Define Graph Env
    fig, ax1 = plt.subplots(figsize=(9,4))
    color = 'tab:red'
    plt.title('Grid Demand Vs Grid Frequency', size=15)

    #Define The first data stream, and write its datapoints onto the graph
    ax1.set_xlabel('Time (Minutes)')
    ax1.set_ylabel('Demand (MW)', color=color)
    ax1.plot(X_List, DemandData, color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_facecolor((0.968, 0.949, 0.949))
    ax1.set_ylim([1500, 6000])


    #Define The first data stream, and write its datapoints onto the graph
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Frequency (Hz)', color=color) 
    ax2.plot(X_List, FrequencyData, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim([49, 51])


    fig.legend(['Power Demand', 'Grid Frequency']) #Create Coloured Legend, With Graph Keys
    
    fig.tight_layout()  #Stops the right Y-Axis label clipping into the index
    plt.show()


ReadDemand()
ReadFrequency()
CreateGraph(FrequencyData, DemandData)