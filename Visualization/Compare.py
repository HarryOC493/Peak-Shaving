import csv
from wsgiref.simple_server import demo_app
from numpy import size

import pandas as pd
import matplotlib.pyplot as plt

print("Welcome, This script will generate a Line Graph, which will show the impact, our peak shaving script had on the 'grid'")

DemandData = [] #Origianl Demand, Without Peak Shaving
NewDemandData = [] #Demand, With Peak Shaving
X_List = [] #Timestamps for chart

def GetData():
    #Read Scraped Data on Electricity Demand, and write it to the 'DemandData' variable for later use with Pandas
    with open('../Main/Log.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            X_List.append(float(row[0]))
            DemandData.append(float(row[4]))
            NewDemandData.append(float(row[5]))

def CreateGraph(NewDemandData, DemandData):
    #Define Graph Env
    fig, ax1 = plt.subplots(figsize=(20,5))
    color = 'tab:grey'
    plt.title("Examaning Our Peak Shaving Algorithm's Imapct", size=15)

    #Define The first data stream, and write its datapoints onto the graph
    ax1.set_xlabel('Time (Minutes)')
    ax1.set_ylabel('Power Demand (MW)', color=color)
    ax1.plot(X_List, DemandData, linewidth=1, color=color)
    ax1.plot(X_List, NewDemandData, linewidth=2, color='tab:green')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_facecolor((0.968, 0.949, 0.949))


    fig.legend(['Without Peak Shaving', 'With Peak Shaving']) #Create Coloured Legend, With Graph Keys
    
    #fig.tight_layout()  #Stops the right Y-Axis label clipping into the index
    plt.show()


GetData()

CreateGraph(NewDemandData, DemandData)