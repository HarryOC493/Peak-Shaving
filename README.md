# Peak-Shaving
By Harry O'Connor @ ResourceKraft 14/Jun/22

A Peak Shaving Algorithm, Built to scale with as many batteries you have. Includes simulated power draw.
<br>https://fullstackenergy.com/peak-shaving-through-the-use-of-battery-technology/


The goal of this project was to create a simple algorithm, that could apply 'Peak Shaving' to Ireland's grid, through the use of a battery bank, which would recharge during periods of low demand, and discharge during periods of high power demand, to help alleviate some of the pressure on our grid

<h1>Index</h1><br>

- [Usage](#Usage)
  * [Running the main Peak Shaving Algorithm:](#--running-the-main-peak-shaving-algorithm)
    + [Configuring The Algorithm](#--configuring-mainpy)
    + [Custom Data](#custom-data)



<h2>Usage:</h2>
  <h3>- Running the main Peak Shaving Algorithm:</h3>
  &nbsp;&nbsp;&nbsp;To use the Peak Shaving Algorithm run:
  <h5>&nbsp;&nbsp;&nbsp;N.B There is already some test data inside the data folder for this script.<br>&nbsp;&nbsp;&nbsp;To add your own data please see the relevant section below</h5> &nbsp;&nbsp;&nbsp;&nbsp;
    
    pip3 install -r requirements.txt
    python3 Main/main.py
    
&nbsp;&nbsp;&nbsp;&nbsp;<h4>- Configuring **Main.py**:</h4>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _Your Data:_<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -Interval: This variable is the time interval of your data, in hours. The test data was taken every 15 minutes, so it's set at 0.25
<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _Configuring your battery:_<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Capacity:  This is the capacity of your battery in MW, a standard size is around 2MW<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CutIn:     This is the Frequency at which the battery will begin to assist the grid<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CutOut:    This is the Frequency at which the battery will begin to charge, if it needs it<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - MinCharge: This is the minimum level of charge for your battery, once it reaches the level it will stop discharging until it's recharged again<br>

<h2>Custom Data</h2><br>
Web Scraping<br>If you would like to try the script out on some recent data, there is a builtin WebScraper, which will scrape all of the available frequency and power demand data in the last 24h, from Irelands smart dashboard automatically. http://smartgriddashboard.com <br><br>
      
- **Scraping Data**:<br>
    To use the WebScraper run the following command:<br>
    `python3 Web_Scraping/Demand_WebScraping.py`<br>
    `python3 Web_Scraping/Frequency_WebScraping.py`<br>
    `python3 Web_Scraping/Merge.py`<br><br>

- **Adding Your Own Data**:<br>
    There is also the option to add your own data from scratch<br>
    When adding your own data, you need separate files for the **Grid Frequency** and the **Power Demand** data <br>
    Both need to be added as _.csv_ files in their respective folders within the /Data directory<br><br>
      **_Data Format:_**<br>
        For **_Grid Frequency Data:_** <br>
          Format: _| 12 June 2022 00:01:13 | 49.94 |_ <br><br>
        For **_Power Demand Data:_** <br>
          Format: _| "2022-06-12 03:30:00" | 3067 |_ <br>




