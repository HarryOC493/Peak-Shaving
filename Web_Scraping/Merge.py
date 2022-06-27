import csv

from datetime import datetime, timedelta

toWrite = []
Yesterday = datetime.strftime(datetime.now() - timedelta(1), '%d')
Today = datetime.strftime(datetime.now(), '%d')
Month = datetime.strftime(datetime.now(), '%b')
Year = datetime.strftime(datetime.now(), '%Y')

def Merge():
    #This function merges all 24 csv files with the hourly frequency data into one, and cleans the data format

    #Define variables for dynamic filenames, allowing script to open all 24 files
    time1 = 0
    time2 = 1
    counter1 = 0

    for x in range(0, 24):
        #Looping 24 times, once for each file
        #Creating dynamic filename
        FileEnd = str(f"{time1:02}" + '.00_' + Yesterday + '.' + Month + '.' + Year + '.' + f"{time2:02}" + '.00.csv') 
        Filebase = '../Data/Frequency/Frequency_' + Yesterday + '.' + Month + '.' + Year + '.'
        Filename = str(Filebase + FileEnd)

        if counter1 == 23 or counter1 == 24:
            #Temp Lazy fix, for date in file changing at midnight
            FileEnd = str(f"{time1:02}" + '.00_' + Today + '.' + Month + '.' + Year + '.' + '00.00.csv') 
            Filebase = '../Data/Frequency/Frequency_' + Yesterday + '.' + Month +'.' + Year + '.'
            Filename = str(Filebase + FileEnd)

        with open(Filename) as csv_file:
            #Reading csv file
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                #Skipping first line as that contains column headers
                if line_count == 0:
                    pass
                else:
                    #Combining Column data into one list
                    timestamp = row[0]
                    data = row[1]
                    
                    #print(row)
                    thisrow = [str(timestamp[-8:]), str(data)]
                    #Adding row data, to overall list of row data, for writing to file later
                    toWrite.append(thisrow)

                line_count += 1
        counter1 += 1
        time1 += 1
        time2 += 1

    with open('../Data/Data.csv', 'w') as f:
        f.truncate(0)
        #Write Data to csv file
        writer = csv.writer(f)
        writer.writerows(toWrite)



            

