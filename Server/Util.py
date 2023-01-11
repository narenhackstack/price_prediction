import json,pickle
import numpy as np

#variables for storing artifacts
__locations=None
__data_columns=None
__model=None

def loadsavedartifacts():
    print("Loading required files")
    global __data_columns
    global __locations
    global __model
    with open('I://Workspace//Python//multilocationds2project//Server//artifacts//columns.json','r') as f:
        __data_columns=json.load(f)['Data_columns']
        __locations=__data_columns[1:]

    with open('I://Workspace//Python//multilocationds2project//Server//artifacts//multilocationmodelds2','rb') as f:
        __model=pickle.load(f)

def get_location_names():
    return __locations
def predictprice(location,sqft):
    #step1: #need to create a numpy array with 0, for X length x=[0,0,0,0,0]
    x=np.zeros(len(__data_columns))
    #step2:#x[0]=sqft --> x=[sqft,0,0,0,0]
    x[0]=sqft
    #step 3: #we have to find out the index of that particular location in the
    # X value iin the variable locindex
    try:
        locindex=__data_columns.index(location.lower())
    except:
        locindex=-1

    #step 4: allocate value 1 in the found index
    if locindex>=0:
        x[locindex]=1 #--> x=[sqft,0,0,1,0]
    print(x)
    return round(__model.predict([x])[0],2) #rounding of to 2 decimal places


if __name__=='__main__':
    loadsavedartifacts()
    print(get_location_names())
    print(predictprice("saibaba colony", 1750))


