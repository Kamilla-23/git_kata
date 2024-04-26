import pandas as pd
def load_and_filter_female_passengers(filepath):
    data = pd.read_csv(filepath) 
    female_passengers = data[data['sex'] == 'male']
    return female_passengers