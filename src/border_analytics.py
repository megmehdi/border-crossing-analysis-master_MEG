from datetime import datetime
import csv
import operator

   

        # creat  a lists a to separate Canada data 
aCAD=[]
bCAD=[]
cCAD=[]
dCAD=[]
eCAD=[]
fCAD=[]
gCAD=[]
hCAD=[]
ICAD=[]
JCAD=[]
kCAD=[]
lCAD=[]
       # creat  a lists a to separate Canada data
a=[]  
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
I=[]
J=[]
k=[]
l=[]



with open('Border_Crossing_Entry_Data.csv') as data:
        csv = csv.reader(data)
        next (csv)



        for row in csv:
                if (row[3],row[5])== ("US-Canada Border","Bus Passengers"): 
                        aCAD.append(row)
                elif (row[3],row[5])== ("US-Mexico Border","Bus Passengers"): 
                        a.append(row) 

                elif (row[3], row[5])== ("US-Canada Border", "Buses"):
                        bCAD.append(row)
                elif (row[3], row[5])== ("US-Mexico Border", "Buses"):
                        b.append(row)

                elif (row[3], row[5])== ("US-Canada Border", "Pedestrians"):
                        cCAD.append(row)
                elif (row[3], row[5])== ("US-Mexico Border", "Pedestrians"):
                        c.append(row)
                        
                elif (row[3], row[5])== ("US-Canada Border", "Personal Vehicle Passengers"):
                        dCAD.append(row)
                elif (row[3], row[5])== ("US-Mexico Border", "Personal Vehicle Passengers"):
                        d.append(row)
                        
                elif (row[3], row[5])== ("US-Canada Border", "Personal Vehicles"):
                        eCAD.append(row)                        
                elif (row[3], row[5])== ("US-Mexico Border", "Personal Vehicles"):
                        e.append(row)
                        
                elif (row[3], row[5])== ("US-Canada Border", "Rail Containers Empty"):
                        fCAD.append(row)
                elif (row[3], row[5])== ("US-Mexico Border", "Rail Containers Empty"):
                        f.append(row)

                elif (row[3], row[5])== ("US-Canada Border", "Rail Containers Full"):
                        gCAD.append(row)
                elif (row[3], row[5])== ("US-Mexico Border", "Rail Containers Full"):
                        g.append(row)
                        
                elif (row[3], row[5])== ("US-Canada Border", "Train Passengers"):
                        hCAD.append(row)
                elif (row[3], row[5])== ("US-Mexico Border", "Train Passengers"):
                        h.append(row)

                elif (row[3], row[5])== ("US-Canada Border", "Trains"):
                        ICAD.append(row)                        
                elif (row[3], row[5])== ("US-Mexico Border", "Trains"):
                        I.append(row)

                elif (row[3], row[5])== ("US-Canada Border", "Truck Containers Empty"):
                        JCAD.append(row)                        
                elif (row[3], row[5])== ("US-Mexico Border", "Truck Containers Empty"):
                        J.append(row)

                elif (row[3], row[5])== ("US-Canada Border", "Truck Containers Full"):
                        kCAD.append(row)                        
                elif (row[3], row[5])== ("US-Mexico Border", "Truck Containers Full"):
                        k.append(row)

                elif (row[3], row[5])== ("US-Canada Border", "Trucks"):
                        lCAD.append(row)                        
                elif (row[3], row[5])== ("US-Mexico Border", "Trucks"):
                        l.append(row)


############################## US-Canada Border #################################################
############################## US-Canada Border #################################################
############################## US-Canada Border #################################################
                        

        ############## CAD Bus Passengers ##################     missing data for 11/1/2019 and 12/1/2018

        for row in range (len(aCAD)):          
                aCAD[row][6]=int(aCAD[row][6])
        
        M_BusPassengers=[]
        y=0
        while y <(len(aCAD)-2):
                x = y + 1
                if (aCAD[y][4]!= aCAD[x][4]):
                        M_BusPassengers.append(aCAD[y])
                else:
                        while (aCAD[y][4]==aCAD[x][4]):
                                aCAD[y][6] =(aCAD[y][6]) +(aCAD[x][6])
                                x +=1
                                M_BusPassengers.append(aCAD[y])
                                if x== (len(aCAD)-2):
                                        aCAD[x][6]= aCAD[x][6] + aCAD[x+1][6]
                                        M_BusPassengers.append(aCAD[x])
                                        break
                                
                y=x



        M_BP_RunAvrg=[]
        row=0
        while row < (len(M_BusPassengers)-11):
                
                mm= datetime.strptime(M_BusPassengers[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(M_BusPassengers[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_BP_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(M_BusPassengers)):
                         M_BusPassengers[row][4]=datetime.strptime(M_BusPassengers[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         M_BusPassengers[row][4]=datetime.strftime(M_BusPassengers[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_BP_RunAvrg[row]
                         y=M_BusPassengers[row]
                         y.append(z)
                         M_BusPassengers[row]=y
                         print(M_BusPassengers[row][3:8])



                       
############################## US-Mexico Border #################################################

        ############## Bus Passengers ##################

        for row in range (len(a)):          
                a[row][6]=int(a[row][6])
        
        M_BusPassengers=[]
        y=0
        while y <(len(a)-2):
                x = y + 1
                if (a[y][4]!= a[x][4]):
                        M_BusPassengers.append(a[y])
                else:
                        while (a[y][4]==a[x][4]):
                                a[y][6] =(a[y][6]) +(a[x][6])
                                x +=1
                                M_BusPassengers.append(a[y])
                                if x== (len(a)-2):
                                        a[x][6]= a[x][6] + a[x+1][6]
                                        M_BusPassengers.append(a[x])
                                        break
                                
                y=x



        M_BP_RunAvrg=[]
        row=0
        while row < (len(M_BusPassengers)-11):
                j=0
                Sum=[]
                while j <12:
                        
                        avrg=0
                        for i in range(11-j):
                                avrg =avrg + int(M_BusPassengers[row+11-i][6])
                        j += 1 
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
               
                M_BP_RunAvrg.extend(Sum)
                row += 12


        for row in range(len(M_BusPassengers)):
                         M_BusPassengers[row][4]=datetime.strptime(M_BusPassengers[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         M_BusPassengers[row][4]=datetime.strftime(M_BusPassengers[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_BP_RunAvrg[row]
                         y=M_BusPassengers[row]
                         y.append(z)
                         M_BusPassengers[row]=y
                         print(M_BusPassengers[row][3:8])


       ##############  CAD Buses ##################

        for row in range (len(bCAD)):          
                bCAD[row][6]=int(bCAD[row][6])
        
        M_Buses=[]
        y=0
        while y <(len(bCAD)-2):
                x = y + 1
                if (bCAD[y][4]!= bCAD[x][4]):
                        M_Buses.append(bCAD[y])
                else:
                        while (bCAD[y][4]==bCAD[x][4]):
                                bCAD[y][6] =(bCAD[y][6]) +(bCAD[x][6])
                                x +=1
                                M_Buses.append(bCAD[y])
                                if x== (len(bCAD)-2):
                                        bCAD[x][6]= bCAD[x][6] + bCAD[x+1][6]
                                        M_Buses.append(bCAD[x])
                                        break
                                
                y=x




        M_B_RunAvrg=[]
        row=0
        while row < (len(M_Buses)-11):
                
                mm= datetime.strptime(M_Buses[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(M_Buses[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_B_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(M_Buses)):
                         M_Buses[row][4]=datetime.strptime(M_Buses[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         M_Buses[row][4]=datetime.strftime(M_Buses[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_B_RunAvrg[row]
                         y=M_Buses[row]
                         y.append(z)
                         M_Buses[row]=y
                         print(M_Buses[row][3:8])





     ####################### MEX Buses ##################

                         
        for row in range (len(b)):
                b[row][6]=int(b[row][6])
        
        M_Buses=[]
        y=0
        while y <(len(b)-2):
                x = y + 1
                if (b[y][4]!= b[x][4]):
                        M_Buses.append(b[y])
                else:
                        while (b[y][4]==b[x][4]):
                                b[y][6] =(b[y][6]) +(b[x][6])
                                x +=1
                                M_Buses.append(b[y])
                                if x== (len(b)-2):
                                        b[x][6]= b[x][6] + b[x+1][6]
                                        M_Buses.append(b[x])
                                        break
                                
                y=x
 
        M_B_RunAvrg=[]
        row=0
        while row < (len(M_Buses)-11):
                
                mm= datetime.strptime(M_Buses[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(M_Buses[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_B_RunAvrg.extend(Sum)
                row += mm

                
        for row in range(len(M_Buses)):
                         M_Buses[row][4]=datetime.strptime(M_Buses[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         M_Buses[row][4]=datetime.strftime(M_Buses[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z= M_B_RunAvrg[row]
                         y= M_Buses[row]
                         y.append(z)
                         M_Buses[row]=y
                         print(M_Buses[row][3:8])


   ###################### CAD Pedestrians ##################


        for row in range (len(cCAD)):          
                cCAD[row][6]=int(cCAD[row][6])
        
        Pedestrians=[]
        y=0
        while y <(len(cCAD)-2):
                x = y + 1
                if (cCAD[y][4]!= cCAD[x][4]):
                        Pedestrians.append(cCAD[y])
                else:
                        while (cCAD[y][4]==cCAD[x][4]):
                                cCAD[y][6] =(cCAD[y][6]) +(cCAD[x][6])
                                x +=1
                                Pedestrians.append(cCAD[y])
                                if x== (len(cCAD)-2):
                                        cCAD[x][6]= cCAD[x][6] + cCAD[x+1][6]
                                        Pedestrians.append(cCAD[x])
                                        break
                                
                y=x



        M_P_RunAvrg=[]
        row=0
        while row < (len(Pedestrians)-11):
                
                mm= datetime.strptime(Pedestrians[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(Pedestrians[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_P_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Pedestrians)):
                         Pedestrians[row][4]=datetime.strptime(Pedestrians[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Pedestrians[row][4]=datetime.strftime(Pedestrians[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_P_RunAvrg[row]
                         y=Pedestrians[row]
                         y.append(z)
                         Pedestrians[row]=y
                         print(Pedestrians[row][3:8])


                         

   ###################### MEX Pedestrians ##################


        for row in range (len(c)):          
                c[row][6]=int(c[row][6])
        
        Pedestrians=[]
        y=0
        while y <(len(c)-2):
                x = y + 1
                if (c[y][4]!= c[x][4]):
                        Pedestrians.append(c[y])
                else:
                        while (c[y][4]==c[x][4]):
                                c[y][6] =(c[y][6]) +(c[x][6])
                                x +=1
                                Pedestrians.append(c[y])
                                if x== (len(c)-2):
                                        c[x][6]= c[x][6] + c[x+1][6]
                                        Pedestrians.append(c[x])
                                        break
                                
                y=x



        M_P_RunAvrg=[]
        row=0
        while row < (len(Pedestrians)-11):
                
                mm= datetime.strptime(Pedestrians[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(Pedestrians[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_P_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Pedestrians)):
                         Pedestrians[row][4]=datetime.strptime(Pedestrians[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Pedestrians[row][4]=datetime.strftime(Pedestrians[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z= M_P_RunAvrg[row]
                         y= Pedestrians[row]
                         y.append(z)
                         Pedestrians[row]=y
                         print(Pedestrians[row][3:8])


    ############## CAD Personal Vehicle Passengers ##################


        for row in range (len(dCAD)):          
                dCAD[row][6]=int(dCAD[row][6])
        
        Personal_Vehicle_Passengers=[]
        y=0
        while y <(len(dCAD)-2):
                x = y + 1
                if (dCAD[y][4]!= dCAD[x][4]):
                        Personal_Vehicle_Passengers.append(dCAD[y])
                else:
                        while (dCAD[y][4]==dCAD[x][4]):
                                dCAD[y][6] =(dCAD[y][6]) +(dCAD[x][6])
                                x +=1
                                Personal_Vehicle_Passengers.append(dCAD[y])
                                if x== (len(dCAD)-2):
                                        dCAD[x][6]= dCAD[x][6] + dCAD[x+1][6]
                                        Personal_Vehicle_Passengers.append(dCAD[x])
                                        break
                                
                y=x



        M_PVP_RunAvrg=[]
        row=0
        while row < (len(Personal_Vehicle_Passengers)-11):
                
                mm= datetime.strptime(Personal_Vehicle_Passengers[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(Personal_Vehicle_Passengers[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_PVP_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Personal_Vehicle_Passengers)):
                         Personal_Vehicle_Passengers[row][4]=datetime.strptime(Personal_Vehicle_Passengers[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Personal_Vehicle_Passengers[row][4]=datetime.strftime(Personal_Vehicle_Passengers[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_PVP_RunAvrg[row]
                         y=Personal_Vehicle_Passengers[row]
                         y.append(z)
                         Personal_Vehicle_Passengers[row]=y
                         print(Personal_Vehicle_Passengers[row][3:8])





                         
    ############## MEX Personal Vehicle Passengers ##################

        for row in range (len(d)):          
                d[row][6]=int(d[row][6])
        
        Personal_Vehicle_Passengers=[]
        y=0
        while y <(len(d)-2):
                x = y + 1
                if (d[y][4]!= d[x][4]):
                        Personal_Vehicle_Passengers.append(d[y])
                else:
                        while (d[y][4]==d[x][4]):
                                d[y][6] =(d[y][6]) +(d[x][6])
                                x +=1
                                Personal_Vehicle_Passengers.append(d[y])
                                if x== (len(d)-2):
                                        d[x][6]= d[x][6] + d[x+1][6]
                                        Personal_Vehicle_Passengers.append(d[x])
                                        break
                                
                y=x



        M_PVP_RunAvrg=[]
        row=0
        while row < (len(Personal_Vehicle_Passengers)-11):
                
                mm= datetime.strptime(Personal_Vehicle_Passengers[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(Personal_Vehicle_Passengers[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_PVP_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Personal_Vehicle_Passengers)):
                         Personal_Vehicle_Passengers[row][4]=datetime.strptime(Personal_Vehicle_Passengers[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Personal_Vehicle_Passengers[row][4]=datetime.strftime(Personal_Vehicle_Passengers[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_PVP_RunAvrg[row]
                         y=Personal_Vehicle_Passengers[row]
                         y.append(z)
                         Personal_Vehicle_Passengers[row]=y
                         print(Personal_Vehicle_Passengers[row][3:8])

##       ############## CAD Personal Vehicles ############################


        for row in range (len(eCAD)):          
                eCAD[row][6]=int(eCAD[row][6])
        
        Personal_Vehicles=[]
        y=0
        while y <(len(eCAD)-2):
                x = y + 1
                if (eCAD[y][4]!= eCAD[x][4]):
                        Personal_Vehicles.append(eCAD[y])
                else:
                        while (eCAD[y][4]==eCAD[x][4]):
                                eCAD[y][6] =(eCAD[y][6]) +(eCAD[x][6])
                                x +=1
                                Personal_Vehicles.append(eCAD[y])
                                if x== (len(eCAD)-2):
                                        eCAD[x][6]= eCAD[x][6] + eCAD[x+1][6]
                                        Personal_Vehicles.append(eCAD[x])
                                        break
                                
                y=x



        M_PV_RunAvrg=[]
        row=0
        while row < (len(Personal_Vehicles)-11):
                
                mm= datetime.strptime(Personal_Vehicles[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(Personal_Vehicles[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_PV_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Personal_Vehicles)):
                         Personal_Vehicles[row][4]=datetime.strptime(Personal_Vehicles[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Personal_Vehicles[row][4]=datetime.strftime(Personal_Vehicles[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_PV_RunAvrg[row]
                         y=Personal_Vehicles[row]
                         y.append(z)
                         Personal_Vehicles[row]=y
                         print(Personal_Vehicles[row][3:8])


                       
       ############## MEX Personal Vehicles ############################


        for row in range (len(e)):          
                e[row][6]=int(e[row][6])
        
        Personal_Vehicles=[]
        y=0
        while y <(len(e)-2):
                x = y + 1
                if (e[y][4]!= e[x][4]):
                        Personal_Vehicles.append(e[y])
                else:
                        while (e[y][4]==e[x][4]):
                                e[y][6] =(e[y][6]) +(e[x][6])
                                x +=1
                                Personal_Vehicles.append(e[y])
                                if x== (len(e)-2):
                                        e[x][6]= e[x][6] + e[x+1][6]
                                        Personal_Vehicles.append(e[x])
                                        break
                                
                y=x



        M_PV_RunAvrg=[]
        row=0
        while row < (len(Personal_Vehicles)-11):
                
                mm= datetime.strptime(Personal_Vehicles[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(Personal_Vehicles[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_PV_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Personal_Vehicles)):
                         Personal_Vehicles[row][4]=datetime.strptime(Personal_Vehicles[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Personal_Vehicles[row][4]=datetime.strftime(Personal_Vehicles[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_PV_RunAvrg[row]
                         y=Personal_Vehicles[row]
                         y.append(z)
                         Personal_Vehicles[row]=y
                         print(Personal_Vehicles[row][3:8])




       ############## CAD Rail Containers Empty ########################
        for row in range (len(fCAD)):          
                fCAD[row][6]=int(fCAD[row][6])
        
        Rail_Containers_Empty=[]
        y=0
        while y <(len(fCAD)-2):
                x = y + 1
                if (fCAD[y][4]!= fCAD[x][4]):
                        Rail_Containers_Empty.append(fCAD[y])
                else:
                        while (fCAD[y][4]==fCAD[x][4]):
                                fCAD[y][6] =(fCAD[y][6]) +(fCAD[x][6])
                                x +=1
                                Rail_Containers_Empty.append(fCAD[y])
                                if x== (len(fCAD)-2):
                                        fCAD[x][6]= fCAD[x][6] + fCAD[x+1][6]
                                        Rail_Containers_Empty.append(fCAD[x])
                                        break
                                
                y=x



        M_RCE_RunAvrg=[]
        row=0
        while row < (len(Rail_Containers_Empty)-11):
                
                mm= datetime.strptime(Rail_Containers_Empty[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(Rail_Containers_Empty[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_RCE_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Rail_Containers_Empty)):
                         Rail_Containers_Empty[row][4]=datetime.strptime(Rail_Containers_Empty[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Rail_Containers_Empty[row][4]=datetime.strftime(Rail_Containers_Empty[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_RCE_RunAvrg[row]
                         y=Rail_Containers_Empty[row]
                         y.append(z)
                         Rail_Containers_Empty[row]=y
                         print(Rail_Containers_Empty[row][3:8])



                         
       ############## MEX Rail Containers Empty ########################


        for row in range (len(f)):          
                f[row][6]=int(f[row][6])
        
        Rail_Containers_Empty=[]
        y=0
        while y <(len(f)-2):
                x = y + 1
                if (f[y][4]!= f[x][4]):
                        Rail_Containers_Empty.append(f[y])
                else:
                        while (f[y][4]==f[x][4]):
                                f[y][6] =(f[y][6]) +(f[x][6])
                                x +=1
                                Rail_Containers_Empty.append(f[y])
                                if x== (len(f)-2):
                                        f[x][6]= f[x][6] + f[x+1][6]
                                        Rail_Containers_Empty.append(f[x])
                                        break
                                
                y=x



        M_RCE_RunAvrg=[]
        row=0
        while row < (len(Rail_Containers_Empty)-11):
                
                mm= datetime.strptime(Rail_Containers_Empty[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(Rail_Containers_Empty[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_RCE_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Rail_Containers_Empty)):
                         Rail_Containers_Empty[row][4]=datetime.strptime(Rail_Containers_Empty[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Rail_Containers_Empty[row][4]=datetime.strftime(Rail_Containers_Empty[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_RCE_RunAvrg[row]
                         y=Rail_Containers_Empty[row]
                         y.append(z)
                         Rail_Containers_Empty[row]=y
                         print(Rail_Containers_Empty[row][3:8])

       ############## CAD Rail Containers Full #########################

                         
        for row in range (len(gCAD)):          
                gCAD[row][6]=int(gCAD[row][6])
        
        Rail_Containers_Full=[]
        y=0
        while y <(len(gCAD)-2):
                x = y + 1
                if (gCAD[y][4]!= gCAD[x][4]):
                        Rail_Containers_Full.append(gCAD[y])
                else:
                        while (gCAD[y][4]==gCAD[x][4]):
                                gCAD[y][6] =(gCAD[y][6]) +(gCAD[x][6])
                                x +=1
                                Rail_Containers_Full.append(gCAD[y])
                                if x== (len(gCAD)-2):
                                        gCAD[x][6]= gCAD[x][6] + gCAD[x+1][6]
                                        Rail_Containers_Full.append(gCAD[x])
                                        break
                                
                y=x



        M_RCF_RunAvrg=[]
        row=0
        while row < (len(Rail_Containers_Full)-11):
                
                mm= datetime.strptime(Rail_Containers_Full[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(Rail_Containers_Full[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_RCF_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Rail_Containers_Full)):
                         Rail_Containers_Full[row][4]=datetime.strptime(Rail_Containers_Full[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Rail_Containers_Full[row][4]=datetime.strftime(Rail_Containers_Full[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_RCF_RunAvrg[row]
                         y=Rail_Containers_Full[row]
                         y.append(z)
                         Rail_Containers_Full[row]=y
                         print(Rail_Containers_Full[row][3:8])
                         
       ############## MEX Rail Containers Full #########################


        for row in range (len(g)):          
                g[row][6]=int(g[row][6])
        
        Rail_Containers_Full=[]
        y=0
        while y <(len(g)-2):
                x = y + 1
                if (g[y][4]!= g[x][4]):
                        Rail_Containers_Full.append(g[y])
                else:
                        while (g[y][4]==g[x][4]):
                                g[y][6] =(g[y][6]) +(g[x][6])
                                x +=1
                                Rail_Containers_Full.append(g[y])
                                if x== (len(g)-2):
                                        g[x][6]= g[x][6] + g[x+1][6]
                                        Rail_Containers_Full.append(g[x])
                                        break
                                
                y=x



        M_RCF_RunAvrg=[]
        row=0
        while row < (len(Rail_Containers_Full)-11):
                
                mm= datetime.strptime(Rail_Containers_Full[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(Rail_Containers_Full[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_RCF_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Rail_Containers_Full)):
                         Rail_Containers_Full[row][4]=datetime.strptime(Rail_Containers_Full[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Rail_Containers_Full[row][4]=datetime.strftime(Rail_Containers_Full[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_RCF_RunAvrg[row]
                         y=Rail_Containers_Full[row]
                         y.append(z)
                         Rail_Containers_Full[row]=y
                         print(Rail_Containers_Full[row][3:8])


       ############## Train Passengers #############################
        for row in range (len(hCAD)):          
                hCAD[row][6]=int(hCAD[row][6])
        
        Train_Passengers=[]
        y=0
        while y <(len(hCAD)-2):
                x = y + 1
                if (hCAD[y][4]!= hCAD[x][4]):
                        Train_Passengers.append(hCAD[y])
                else:
                        while (hCAD[y][4]==hCAD[x][4]):
                                hCAD[y][6] =(hCAD[y][6]) +(hCAD[x][6])
                                x +=1
                                Train_Passengers.append(hCAD[y])
                                if x== (len(hCAD)-2):
                                        hCAD[x][6]= hCAD[x][6] + hCAD[x+1][6]
                                        Train_Passengers.append(hCAD[x])
                                        break
                                
                y=x



        M_TP_RunAvrg=[]
        row=0
        while row < (len(Train_Passengers)-11):
                
                mm= datetime.strptime(Train_Passengers[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(Train_Passengers[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_TP_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Train_Passengers)):
                         Train_Passengers[row][4]=datetime.strptime(Train_Passengers[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Train_Passengers[row][4]=datetime.strftime(Train_Passengers[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_TP_RunAvrg[row]
                         y=Train_Passengers[row]
                         y.append(z)
                         Train_Passengers[row]=y
                         print(Train_Passengers[row][3:8])


                         
                         
       ############## Train Passengers #############################

        for row in range (len(h)):          
                h[row][6]=int(h[row][6])
        
        Train_Passengers=[]
        y=0
        while y <(len(h)-2):
                x = y + 1
                if (h[y][4]!= h[x][4]):
                        Train_Passengers.append(h[y])
                else:
                        while (h[y][4]==h[x][4]):
                                h[y][6] =(h[y][6]) +(h[x][6])
                                x +=1
                                Train_Passengers.append(h[y])
                                if x== (len(h)-2):
                                        h[x][6]= h[x][6] + h[x+1][6]
                                        Train_Passengers.append(h[x])
                                        break
                                
                y=x



        M_TP_RunAvrg=[]
        row=0
        while row <(len(Train_Passengers)-11):
                mm= datetime.strptime(Train_Passengers[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg +(Train_Passengers[row+mm-1-i][6])

                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                        j += 1
                
                M_TP_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Train_Passengers)):
                         Train_Passengers[row][4]=datetime.strptime(Train_Passengers[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Train_Passengers[row][4]=datetime.strftime(Train_Passengers[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_TP_RunAvrg[row]
                         y=Train_Passengers[row]
                         y.append(z)
                         Train_Passengers[row]=y
                         print(Train_Passengers[row][3:8])
                                        


       ############## CAD Train ########################################
        for row in range (len(ICAD)):          
                ICAD[row][6]=int(ICAD[row][6])
        
        Train=[]
        y=0
        while y <(len(ICAD)-2):
                x = y + 1
                if (ICAD[y][4]!= ICAD[x][4]):
                        Train.append(ICAD[y])
                else:
                        while (ICAD[y][4]==ICAD[x][4]):
                                ICAD[y][6] =(ICAD[y][6]) +(ICAD[x][6])
                                x +=1
                                Train.append(ICAD[y])
                                if x== (len(ICAD)-2):
                                        ICAD[x][6]= ICAD[x][6] + ICAD[x+1][6]
                                        Train.append(ICAD[x])
                                        break
                                
                y=x



        M_T_RunAvrg=[]
        row=0
        while row < (len(Train)-11):
                
                mm= datetime.strptime(Train[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(Train[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_T_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Train)):
                         Train[row][4]=datetime.strptime(Train[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Train[row][4]=datetime.strftime(Train[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_T_RunAvrg[row]
                         y=Train[row]
                         y.append(z)
                         Train[row]=y
                         print(Train[row][3:8])



                         
       ############## MEX Train ########################################



        for row in range(len(I)):          
                I[row][6]=int(I[row][6])
        
        Train=[]
        y=0
        while y <(len(I)-2):
                x = y + 1
                if (I[y][4]!= I[x][4]):
                        Train.append(I[y])
                else:
                        while (I[y][4]==I[x][4]):
                                I[y][6] =(I[y][6]) +(I[x][6])
                                x +=1
                                Train.append(I[y])
                                if x== (len(I)-2):
                                        I[x][6]= I[x][6] + I[x+1][6]
                                        Train.append(I[x])
                                        break
                                
                y=x


        M_T_RunAvrg=[]
        row=0
        while row < (len(Train)-11):
                
                mm= datetime.strptime(Train[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(Train[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_T_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Train)):
                         Train[row][4]=datetime.strptime(Train[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Train[row][4]=datetime.strftime(Train[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_T_RunAvrg[row]
                         y=Train[row]
                         y.append(z)
                         Train[row]=y
                         print(Train[row][3:8])


       ############## CAD Truck Containers Empty #######################

        for row in range (len(JCAD)):          
                JCAD[row][6]=int(JCAD[row][6])
        
        Truck_Containers_Empty=[]
        y=0
        while y <(len(JCAD)-2):
                x = y + 1
                if (JCAD[y][4]!= JCAD[x][4]):
                        Truck_Containers_Empty.append(JCAD[y])
                else:
                        while (JCAD[y][4]==JCAD[x][4]):
                                JCAD[y][6] =(JCAD[y][6]) +(JCAD[x][6])
                                x +=1
                                Truck_Containers_Empty.append(JCAD[y])
                                if x== (len(JCAD)-2):
                                        JCAD[x][6]= JCAD[x][6] + JCAD[x+1][6]
                                        Truck_Containers_Empty.append(JCAD[x])
                                        break
                                
                y=x



        M_TCE_RunAvrg=[]
        row=0
        while row < (len(Truck_Containers_Empty)-11):
                
                mm= datetime.strptime(Truck_Containers_Empty[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(Truck_Containers_Empty[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_TCE_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Truck_Containers_Empty)):
                         Truck_Containers_Empty[row][4]=datetime.strptime(Truck_Containers_Empty[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Truck_Containers_Empty[row][4]=datetime.strftime(Truck_Containers_Empty[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_TCE_RunAvrg[row]
                         y=Truck_Containers_Empty[row]
                         y.append(z)
                         Truck_Containers_Empty[row]=y
                         print(Truck_Containers_Empty[row][3:8])


                         
                         
       ############## MEX Truck Containers Empty #######################


        for row in range (len(J)):          
                J[row][6]=int(J[row][6])
        
        Truck_Containers_Empty=[]
        y=0
        while y <(len(J)-2):
                x = y + 1
                if (J[y][4]!= J[x][4]):
                        Truck_Containers_Empty.append(J[y])
                else:
                        while (J[y][4]==J[x][4]):
                                J[y][6] =(J[y][6]) +(J[x][6])
                                x +=1
                                Truck_Containers_Empty.append(J[y])
                                if x== (len(J)-2):
                                        J[x][6]= J[x][6] + J[x+1][6]
                                        Truck_Containers_Empty.append(J[x])
                                        break
                                
                y=x



        M_TCE_RunAvrg=[]
        row=0
        while row < (len(Truck_Containers_Empty)-11):
                
                mm= datetime.strptime(Truck_Containers_Empty[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(Truck_Containers_Empty[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_TCE_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Truck_Containers_Empty)):
                         Truck_Containers_Empty[row][4]=datetime.strptime(Truck_Containers_Empty[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Truck_Containers_Empty[row][4]=datetime.strftime(Truck_Containers_Empty[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_TCE_RunAvrg[row]
                         y=Truck_Containers_Empty[row]
                         y.append(z)
                         Truck_Containers_Empty[row]=y
                         print(Truck_Containers_Empty[row][3:8])
                         


       ############## CAD Truck Containers Full ########################

        for row in range (len(kCAD)):          
                kCAD[row][6]=int(kCAD[row][6])
        
        Truck_Containers_FULL=[]
        y=0
        while y <(len(kCAD)-2):
                x = y + 1
                if (kCAD[y][4]!= kCAD[x][4]):
                        Truck_Containers_FULL.append(kCAD[y])
                else:
                        while (kCAD[y][4]==kCAD[x][4]):
                                kCAD[y][6] =(kCAD[y][6]) +(kCAD[x][6])
                                x +=1
                                Truck_Containers_FULL.append(kCAD[y])
                                if x== (len(kCAD)-2):
                                        kCAD[x][6]= kCAD[x][6] + kCAD[x+1][6]
                                        Truck_Containers_FULL.append(kCAD[x])
                                        break
                                
                y=x



        M_TCF_RunAvrg=[]
        row=0
        while row < (len(Truck_Containers_FULL)-11):
                
                mm= datetime.strptime(Truck_Containers_FULL[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(Truck_Containers_FULL[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_TCF_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Truck_Containers_FULL)):
                         Truck_Containers_FULL[row][4]=datetime.strptime(Truck_Containers_FULL[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Truck_Containers_FULL[row][4]=datetime.strftime(Truck_Containers_FULL[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_TCF_RunAvrg[row]
                         y=Truck_Containers_FULL[row]
                         y.append(z)
                         Truck_Containers_FULL[row]=y
                         print(Truck_Containers_FULL[row][3:8])



                         
       ############## MEX Truck Containers Full ########################

        for row in range (len(k)):          
                k[row][6]=int(k[row][6])
        
        Truck_Containers_FULL=[]
        y=0
        while y <(len(k)-2):
                x = y + 1
                if (k[y][4]!= k[x][4]):
                        Truck_Containers_FULL.append(k[y])
                else:
                        while (k[y][4]==k[x][4]):
                                k[y][6] =(k[y][6]) +(k[x][6])
                                x +=1
                                Truck_Containers_FULL.append(k[y])
                                if x== (len(k)-2):
                                        k[x][6]= k[x][6] + k[x+1][6]
                                        Truck_Containers_FULL.append(k[x])
                                        break
                                
                y=x



        M_TCF_RunAvrg=[]
        row=0
        while row < (len(Truck_Containers_FULL)-11):
                
                mm= datetime.strptime(Truck_Containers_FULL[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(Truck_Containers_FULL[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_TCF_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Truck_Containers_FULL)):
                         Truck_Containers_FULL[row][4]=datetime.strptime(Truck_Containers_FULL[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Truck_Containers_FULL[row][4]=datetime.strftime(Truck_Containers_FULL[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_TCF_RunAvrg[row]
                         y=Truck_Containers_FULL[row]
                         y.append(z)
                         Truck_Containers_FULL[row]=y
                         print(Truck_Containers_FULL[row][3:8])


       ############## CAD Truck  #######################################

                         
        for row in range (len(lCAD)):          
                lCAD[row][6]=int(lCAD[row][6])
        
        Truck=[]
        y=0
        while y <(len(lCAD)-2):
                x = y + 1
                if (lCAD[y][4]!= lCAD[x][4]):
                        Truck.append(lCAD[y])
                else:
                        while (lCAD[y][4]==lCAD[x][4]):
                                lCAD[y][6] =(lCAD[y][6]) +(lCAD[x][6])
                                x +=1
                                Truck.append(lCAD[y])
                                if x== (len(lCAD)-2):
                                        lCAD[x][6]= lCAD[x][6] + lCAD[x+1][6]
                                        Truck.append(lCAD[x])
                                        break
                                
                y=x



        M_Tk_RunAvrg=[]
        row=0
        while row < (len(Truck)-11):
                
                mm= datetime.strptime(Truck[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(Truck[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_Tk_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Truck)):
                         Truck[row][4]=datetime.strptime(Truck[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Truck[row][4]=datetime.strftime(Truck[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_Tk_RunAvrg[row]
                         y=Truck[row]
                         y.append(z)
                         Truck[row]=y
                         print(Truck[row][3:8])


                         
       ############## MEX Truck  #######################################

        for row in range (len(l)):          
                l[row][6]=int(l[row][6])
        
        Truck=[]
        y=0
        while y <(len(l)-2):
                x = y + 1
                if (l[y][4]!= l[x][4]):
                        Truck.append(l[y])
                else:
                        while (l[y][4]==l[x][4]):
                                l[y][6] =(l[y][6]) +(l[x][6])
                                x +=1
                                Truck.append(l[y])
                                if x== (len(l)-2):
                                        l[x][6]= l[x][6] + l[x+1][6]
                                        Truck.append(l[x])
                                        break
                                
                y=x



        M_Tk_RunAvrg=[]
        row=0
        while row < (len(Truck)-11):
                
                mm= datetime.strptime(Truck[row][4],'%m/%d/%Y %H:%M')
                mm=mm.month
                Sum=[]
                j=0
                while j <12:
                        
                        avrg=0
                        for i in range(mm-j-1):
                                avrg =avrg + int(Truck[row+mm-1-i][6])
                        j += 1
                        avrg=round (avrg/(i+1))
                        Sum.append(avrg)
                
                M_Tk_RunAvrg.extend(Sum)
                row += mm


        for row in range(len(Truck)):
                         Truck[row][4]=datetime.strptime(Truck[row][4],'%m/%d/%Y %H:%M') # string to datetime object
                         Truck[row][4]=datetime.strftime(Truck[row][4],'%m/%d/%Y %I:%M:%S %p')# Save the year of each row
                         z=M_T_RunAvrg[row]
                         y=Truck[row]
                         y.append(z)
                         Truck[row]=y
                         print(Truck[row][3:8])
 



                       
                        

