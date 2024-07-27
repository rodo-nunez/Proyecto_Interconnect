import pandas as pd
from sklearn.preprocessing import StandardScaler, OrdinalEncoder


""" Funcion para leer archivos csv """
def read_csv(path):
    data = pd.read_csv(path)
    return data


""" Funcion para leer archivos parquet """
def read_parquet(path):
    data = pd.read_parquet(path)
    return data


""" Funcion para cambiar a formato fecha """
def to_date_time(data):
    data = pd.to_datetime(data, format='%Y-%m-%d')
    return data


""" Funcion para codificar caracteristicas categoricas """
def encoder(data):
    encoder = OrdinalEncoder()
    data_encoded = pd.DataFrame(encoder.fit_transform(data), columns=data.columns)
    return data_encoded
    
    
""" Funcion para escalar caracteristicas numericas """
def scaler(data):
    scaler = StandardScaler()
    data_scaled = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
    return data_scaled


""" Funcion para guardar archivos parquet """
def parquet(data, path):
    engine='pyarrow'
    index=False
    return data.to_parquet(path, engine=engine, index=index)
    
 
""" Funcion para agrupar por servicio derivado de internet y contar las cancelaciones   """   

def group_service(full_data, column):
    values = full_data.groupby(column)['Churn'].value_counts()
    values = values.reset_index(name='count')
    #conservar solo la clase negativa 
    data = values[values['Churn'] == 0].drop(['Churn'], axis=1).reset_index(drop=True)
    data = data.sort_values(by='count', ascending=False)
    return data