import csv

#----------------- Begin User Configuration -----------------------------------------------
Interval = 0.25 #As a fraction of an hour, Note, your data interval needs to match this

MinCharge = 20 #Minium Charge level
Capacity = 65 #Battery Capacity in MWh

CutIn = 49.945 #Frequency For Battery To Cut In
CutOut = 50.01 #Frequency for battery to charge

#----------------- End User Configuration -----------------------------------------------

Charge = 100 #Battery Charge Level
IntervalCap = (Capacity * Interval)

FreqFile = open('../Data/Frequency/Data.csv')
FreqRows = list(csv.reader(FreqFile, delimiter=','))

DemandFile = open('../Data/Demand/chart.csv')
DemandRows = list(csv.reader(DemandFile, delimiter=','))

with open('Log.csv', 'a') as Log_file:
    Log_file.truncate(0) #Clear the file, of previous Logs
    Log_Writer = csv.writer(Log_file)
    PrevDemand = 0
    PrevActualDemand = 0

    for row in FreqRows:
        #Format timestamp, and get frequency data
        timestamp = row[0]
        data = row[1]

        for Demand_Row in DemandRows:
            if str(timestamp) in Demand_Row[0]:
                #Row Is Active, get power demand
                Demand = Demand_Row[1]
                if PrevActualDemand == 0:
                    PrevActualDemand = float(Demand)
                    PrevDemand = float(Demand)


                #Get the change in demand from the real world data, apply it to the simulated data (Diff)
                #Simulating data, to show the scripts impact if it was applied in the field

                #Calculating the change in deamnd:
                #Checks the actual demand from previous time stamp, then compare with the difference with the current
                #Then add or subtract the change in demand to the simulated demand data


                diff = (float(Demand) - PrevActualDemand) 
                CurDemand = PrevDemand + diff
                

                if float(data) >= CutOut:
                    #Charge Battery if it needs it

                    if Charge < Capacity:
                        #Battery Needs Charging
                        Charge += IntervalCap
                        if Charge > Capacity:
                            #Capping the charge at 100
                            Charge == Capacity
                        
                        PrevActualDemand = float(Demand)
                        PrevDemand = (float(CurDemand) + Capacity)
                        LogInput = [row[0].replace(':', ''), Charge, 'Charged', row[1], Demand, str((float(CurDemand) + Capacity))]
                        Log_Writer.writerow(LogInput)
                        break
                    
                    else:
                        #Battery Does not need charging
                        PrevDemand = float(CurDemand)
                        PrevActualDemand = float(Demand)
                        LogInput = [row[0].replace(':', ''), Charge, 'No Need To Charge', row[1], Demand, CurDemand]
                        Log_Writer.writerow(LogInput)
                        break
                
                elif float(data) <= CutIn:
                    #Grid Needs Battery To Cut In
                    if Charge > MinCharge:
                        #Battery Has Sufficent Capacity to discharge
                        Charge -= IntervalCap
                        PrevDemand = (float(CurDemand) - Capacity)
                        PrevActualDemand = float(Demand)
                        LogInput = [row[0].replace(':', ''), Charge, 'Discharged', row[1], Demand, str((float(CurDemand) - Capacity))]
                        Log_Writer.writerow(LogInput)
                        break
                    else:
                        #Battery Cirically low, cannot discharge
                        PrevDemand = float(CurDemand)
                        PrevActualDemand = float(Demand)
                        LogInput = [row[0].replace(':', ''), Charge, 'Critically Low', row[1], Demand, CurDemand]
                        Log_Writer.writerow(LogInput)
                        break
                else:
                    #No Action Required
                    PrevDemand = float(CurDemand)
                    PrevActualDemand = float(Demand)
                    LogInput = [row[0].replace(':', ''), Charge, 'Did Nothing', row[1], Demand, CurDemand]
                    Log_Writer.writerow(LogInput)
                    break