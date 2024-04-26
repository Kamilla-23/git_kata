import pandas as pd
def load_and_filter_female_passengers:
data = pd.read_csv(C:\Users\Fuchs-Laptop\git\git_kata\data\titanic.csv) 
 female_passengers = data[data['sex'] == 'female']
    return female_passengers                                  