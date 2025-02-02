# from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler
import pickle as pkl
import joblib
import numpy as np


def wrangle(new_data_df):  

    
    # Loading the saved encoders and scalers
    type_encoder = joblib.load('type_encoder.pkl')
    boy_encoder = joblib.load('boy_encoder.pkl')
    density_encoder = joblib.load('density_encoder.pkl')
    cond_encoder = joblib.load('cond_encoder.pkl')
    ceil_encoder = joblib.load('ceil_encoder.pkl')
    floor_encoder = joblib.load('floor_encoder.pkl')
    roof_encoder = joblib.load('roof_encoder.pkl')
    win_encoder = joblib.load('win_encoder.pkl')
    paint_encoder = joblib.load('paint_encoder.pkl')
    water_encoder = joblib.load('water_encoder.pkl')
    ele_encoder = joblib.load('ele_encoder.pkl')
    car_encoder = joblib.load('car_encoder.pkl')
    sec_encoder = joblib.load('sec_encoder.pkl')

    build_scaler = joblib.load('build_scaler.pkl')
    bed_scaler = joblib.load('bed_scaler.pkl')
    age_scaler = joblib.load('age_scaler.pkl')
    toil_scaler = joblib.load('toil_scaler.pkl')
    bath_scaler = joblib.load('bath_scaler.pkl')
    scaler_y = joblib.load('scaler_y.pkl')
    
    # Apply the encoders and scalers to new data
    new_data_df['type'] = type_encoder.transform([new_data_df['type']])
    new_data_df["Boy'squarter"] = boy_encoder.transform([new_data_df["Boy'squarter"]])
    new_data_df['loc_density'] = density_encoder.transform([new_data_df['loc_density']])
    new_data_df['condition'] = cond_encoder.transform([new_data_df['condition']])
    new_data_df['Ceiling '] = ceil_encoder.transform([new_data_df['Ceiling ']])
    new_data_df['Floor'] = floor_encoder.transform([new_data_df['Floor']])
    new_data_df['Roof'] = roof_encoder.transform([new_data_df['Roof']])
    new_data_df['Window '] = win_encoder.transform([new_data_df['Window ']])
    new_data_df['Painting'] = paint_encoder.transform([new_data_df['Painting']])
    new_data_df['water'] = water_encoder.transform([new_data_df['water']])
    new_data_df['Electricity'] = ele_encoder.transform([new_data_df['Electricity']])
    new_data_df['Car_park'] = car_encoder.transform([new_data_df['Car_park']])
    new_data_df['Security'] = sec_encoder.transform([new_data_df['Security']])

    new_data_df['building_size'] = build_scaler.transform(np.array(new_data_df['building_size']).reshape(-1, 1))
    new_data_df['bedroom'] = bed_scaler.transform(np.array(new_data_df['bedroom']).reshape(-1, 1))
    new_data_df['age'] = age_scaler.transform(np.array(new_data_df['age']).reshape(-1, 1))
    new_data_df['toilets'] = toil_scaler.transform(np.array(new_data_df['toilets']).reshape(-1, 1))
    new_data_df['bathrooms'] = bath_scaler.transform(np.array(new_data_df['bathrooms']).reshape(-1, 1))

    
    return new_data_df





def prediction(inputs):

        
    with open('model_3.pkl', 'rb') as f:
        model = pkl.load(f)
    with open('nn_model.pkl', 'rb') as f:
        nn_model = pkl.load(f)

    scaler_y = joblib.load('scaler_y.pkl')
        
        
    inputs = inputs.values.reshape(1, -1)
    
    predict = model.predict(inputs)
    nn_prediction = nn_model.predict(inputs)
    
    trasform = scaler_y.inverse_transform(predict.reshape(-1, 1))
    nn_trasform = scaler_y.inverse_transform(nn_prediction.reshape(-1, 1))
    
    return {'linear':trasform, 'nn':nn_trasform}