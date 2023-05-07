import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import json
import os
import pandas as pd
import psycopg2
import plotly.express as px

def create_agg_trans():
    path_country = r'C:\Users\gurur\Desktop\pulse\data\aggregated\transaction\country\india\state'
    rows=[]
    for state in os.listdir(path_country):
        state = state
        path_state = path_country+'\\'+state
        
        for year in os.listdir(path_state):
            year = year
            path_year = path_state+'\\'+year
            
            for quarter in os.listdir(path_year):
                q = quarter.split('.')[0]
                path_file = path_year+'\\'+quarter
                file = open(path_file, 'r')
                file_data = file.read()
                file_json = json.loads(file_data)
                for i in range(len(file_json['data']['transactionData'])):
                    row = []
                    row.append(state)
                    row.append(year)
                    row.append(q)
                    transcation_type = file_json['data']['transactionData'][i]['name']
                    row.append(transcation_type)
                    transcation_count = file_json['data']['transactionData'][i]['paymentInstruments'][0]['count']
                    row.append(transcation_count)
                    transaction_amount = file_json['data']['transactionData'][i]['paymentInstruments'][0]['amount']
                    row.append(transaction_amount)
                    rows.append(row)    
    df_agg_trans = pd.DataFrame(rows)
    df_agg_trans.columns=['state','year','quarter','transaction_type','transaction_count','transaction_amount']
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df_agg_trans.to_sql('agg_trans', engine, if_exists='replace', index=False)

def create_agg_users():
    path_country = r'C:\Users\gurur\Desktop\pulse\data\aggregated\user\country\india\state'
    rows = []
    for state in os.listdir(path_country):
        state = state
        path_state = path_country+'\\'+state
        for year in os.listdir(path_state):
            year = year
            path_year = path_state+'\\'+year
            for quarter in os.listdir(path_year):
                q = quarter.split('.')[0]
                #print(q)
                path_file = path_year+'\\'+quarter
                #print(path_file)
                file = open(path_file, 'r')
                file_data = file.read()
                file_json = json.loads(file_data)
                for i in range(len(file_json['data']['usersByDevice'])):
                    row = []
                    row.append(state)
                    row.append(year)
                    row.append(q)
                    reg_users = file_json['data']['aggregated']['registeredUsers']
                    row.append(reg_users)
                    appOpens = file_json['data']['aggregated']['appOpens']
                    row.append(appOpens)
                    brand = file_json['data']['usersByDevice'][i]['brand']
                    row.append(brand)
                    count = file_json['data']['usersByDevice'][i]['count']
                    row.append(count)
                    percentage = file_json['data']['usersByDevice'][i]['percentage']
                    row.append(percentage)
                    rows.append(row)
    df_agg_users = pd.DataFrame(rows)
    df_agg_users = df_agg_users.rename(columns = {0:'state',1:'year',2:'quarter',3:'registered_users',4:'app_opens',5:'phone_brand',6:'count',7:'percentage'})
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df_agg_users.to_sql('agg_users', engine, if_exists='replace', index=False)   

def create_top_transaction_district():
    path_country = r'C:\Users\gurur\Desktop\pulse\data\top\transaction\country\india\state'
    rows=[]
    for state in os.listdir(path_country):
        state = state
        path_state = path_country+'\\'+state
        for year in os.listdir(path_state):
            year = year
            path_year = path_state+'\\'+year
            for quarter in os.listdir(path_year):
                q = quarter.split('.')[0]
                path_file = path_year+'\\'+quarter
                file = open(path_file, 'r')
                file_data = file.read()
                file_json = json.loads(file_data)
                for i in range(len(file_json['data']['districts'])):
                    row = []
                    row.append(state)
                    row.append(year)
                    row.append(q)
                    district = file_json['data']['districts'][i]['entityName']
                    row.append(district)
                    count = file_json['data']['districts'][i]['metric']['count']
                    row.append(count)
                    amount = file_json['data']['districts'][i]['metric']['amount']
                    row.append(amount)
                    rows.append(row)
    df_top_transaction_district = pd.DataFrame(rows)
    df_top_transaction_district = df_top_transaction_district.rename(columns={0:'state',1:'year',2:'quarter',3:'district',4:'count',5:'amount'})
    from sqlalchemy import create_engine
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df_top_transaction_district.to_sql('top_trans_dist', engine, if_exists='append', index=False)

def create_top_transaction_pincode():
    path_country = r'C:\Users\gurur\Desktop\pulse\data\top\transaction\country\india\state'
    rows=[]
    for state in os.listdir(path_country):
        state = state
        path_state = path_country+'\\'+state
        for year in os.listdir(path_state):
            year = year
            path_year = path_state+'\\'+year
            for quarter in os.listdir(path_year):
                q = quarter.split('.')[0]
                path_file = path_year+'\\'+quarter
                file = open(path_file, 'r')
                file_data = file.read()
                file_json = json.loads(file_data)
                for i in range(len(file_json['data']['pincodes'])):
                    row = []
                    row.append(state)
                    row.append(year)
                    row.append(q)
                    pincode = file_json['data']['pincodes'][i]['entityName']
                    row.append(pincode)
                    count = file_json['data']['pincodes'][i]['metric']['count']
                    row.append(count)
                    amount = file_json['data']['pincodes'][i]['metric']['amount']
                    row.append(amount)
                    rows.append(row)
    df_top_transaction_pincode = pd.DataFrame(rows)
    df_top_transaction_pincode = df_top_transaction_pincode.rename(columns={0:'state',1:'year',2:'quarter',3:'pincode',4:'count',5:'amount'})
    from sqlalchemy import create_engine
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df_top_transaction_pincode.to_sql('top_trans_pincode', engine, if_exists='replace', index=False)
    
def create_top_user_district():
    path_country = r'C:\Users\gurur\Desktop\pulse\data\top\user\country\india\state'
    rows=[]
    for state in os.listdir(path_country):
        state = state
        path_state = path_country+'\\'+state
        for year in os.listdir(path_state):
            year = year
            path_year = path_state+'\\'+year
            for quarter in os.listdir(path_year):
                q = quarter.split('.')[0]
                path_file = path_year+'\\'+quarter
                file = open(path_file, 'r')
                file_data = file.read()
                file_json = json.loads(file_data)
                for i in range(len(file_json['data']['districts'])):
                    row = []
                    row.append(state)
                    row.append(year)
                    row.append(q)
                    name = file_json['data']['districts'][i]['name']
                    row.append(name)
                    reg_users = file_json['data']['districts'][i]['registeredUsers']
                    row.append(reg_users)
                    rows.append(row)
    df_top_user_district = pd.DataFrame(rows)
    df_top_user_district = df_top_user_district.rename(columns = {0:'state',1:'year',2:'quarter',3:'district',4:'registered_users'})
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df_top_user_district.to_sql('top_user_district', engine, if_exists='replace', index=False)

def create_top_user_pincode():
    path_country = r'C:\Users\gurur\Desktop\pulse\data\top\user\country\india\state'
    rows=[]
    for state in os.listdir(path_country):
        state = state
        path_state = path_country+'\\'+state
        for year in os.listdir(path_state):
            year = year
            path_year = path_state+'\\'+year
            for quarter in os.listdir(path_year):
                q = quarter.split('.')[0]
                path_file = path_year+'\\'+quarter
                file = open(path_file, 'r')
                file_data = file.read()
                file_json = json.loads(file_data)
                for i in range(len(file_json['data']['pincodes'])):
                    row = []
                    row.append(state)
                    row.append(year)
                    row.append(q)
                    pincode = file_json['data']['pincodes'][i]['name']
                    row.append(pincode)
                    reg_users = file_json['data']['pincodes'][i]['registeredUsers']
                    row.append(reg_users)
                    rows.append(row)
    df_top_user_pincode = pd.DataFrame(rows)
    df_top_user_pincode = df_top_user_pincode.rename(columns={0:'state',1:'year',2:'quarter',3:'pincode',4:'registered_users'})
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df_top_user_pincode.to_sql('top_user_pincode', engine, if_exists='append', index=False)

def create_map_trans():
    path_country = r'C:\Users\gurur\Desktop\pulse\data\map\transaction\hover\country\india\state'
    rows = []
    for state in os.listdir(path_country):
        state = state
        path_state = path_country+'\\'+state
        for year in os.listdir(path_state):
            year = year
            path_year = path_state+'\\'+year
            for quarter in os.listdir(path_year):
                q = quarter.split('.')[0]
                path_file = path_year+'\\'+quarter
                file = open(path_file, 'r')
                file_data = file.read()
                file_json = json.loads(file_data)
                for i in range(len(file_json['data']['hoverDataList'])):
                    row = []
                    row.append(state)
                    row.append(year)
                    row.append(q)
                    name = file_json['data']['hoverDataList'][i]['name']
                    row.append(name)
                    count = file_json['data']['hoverDataList'][i]['metric'][0]['count']
                    row.append(count)
                    amount = file_json['data']['hoverDataList'][i]['metric'][0]['amount']
                    row.append(amount)
                    rows.append(row)
    df_map_transaction = pd.DataFrame(rows)
    df_map_transaction = df_map_transaction.rename(columns = {0:'state', 1:'year', 2:'quarter',3:'district',4:'count',5:'amount'})
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df_map_transaction.to_sql('map_trans', engine, if_exists='replace', index=False)

def create_map_users():
    path_country = r'C:\Users\gurur\Desktop\pulse\data\map\user\hover\country\india\state'
    rows = []
    for state in os.listdir(path_country):
        state = state
        path_state = path_country+'\\'+state
        for year in os.listdir(path_state):
            year = year
            path_year = path_state+'\\'+year
            for quarter in os.listdir(path_year):
                q = quarter.split('.')[0]
                #print(q)
                path_file = path_year+'\\'+quarter
                #print(path_file)
                file = open(path_file, 'r')
                file_data = file.read()
                file_json = json.loads(file_data)
                for i in file_json['data']['hoverData'].keys():
                    row = []
                    row.append(state)
                    row.append(year)
                    row.append(q)
                    dist = i
                    row.append(dist)
                    reg_users = file_json['data']['hoverData'][i]['registeredUsers']
                    row.append(reg_users)
                    app_opens = file_json['data']['hoverData'][i]['appOpens']
                    row.append(app_opens)
                    rows.append(row)
    df_map_users = pd.DataFrame(rows)
    df_map_users = df_map_users.rename(columns={0:'state',1:'year',2:'quarter',3:'district',4:'users',5:'app_opens'})
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df_map_users.to_sql('map_users', engine, if_exists='replace', index=False)

      
def agg_trans_count(state_query):
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df = pd.read_sql_query(f'SELECT * from agg_trans where agg_trans.state=\'{state_query}\'', engine)
    pd.options.display.float_format = '{:.2f}'.format
    df_trans_count = df.groupby(['state','transaction_type'])['transaction_count'].sum()
    display_df = pd.DataFrame(df_trans_count)
    display_df.reset_index(inplace=True)
    display_df = display_df.sort_values(by='transaction_count', ascending=False)
    display_df = display_df.reset_index(drop=True)
    new_df = display_df[['transaction_type','transaction_count']]
    return new_df

def agg_trans_amount(state_query):
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df = pd.read_sql_query(f'SELECT * from agg_trans where agg_trans.state=\'{state_query}\'', engine)
    pd.options.display.float_format = '{:.2f}'.format
    df_trans_amount = df.groupby(['state','transaction_type'])['transaction_amount'].sum()
    display_df = pd.DataFrame(df_trans_amount)
    display_df.reset_index(inplace=True)
    display_df = display_df.sort_values(by='transaction_amount', ascending=False)
    display_df = display_df.reset_index(drop=True)
    new_df =  display_df[['transaction_type','transaction_amount']]
    return new_df

def agg_trans_state_year_quarter(state_query,year_query,quarter_query,trans_query):
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df = pd.read_sql_query(f'select * from agg_trans where agg_trans.state=\'{state_query}\' and agg_trans.year = {year_query} and agg_trans.quarter= {quarter_query} and transaction_type=\'{trans_query}\'',engine);
    new_df = df[['transaction_count','transaction_amount']]
    return new_df

def agg_trans_state_year_count(state_query,year_query):
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    display_df = pd.read_sql_query(f'select * from agg_trans where agg_trans.state=\'{state_query}\' and agg_trans.year = {year_query}',engine);
    pd.options.display.float_format = '{:.2f}'.format
    display_df = display_df.groupby(['state','year','transaction_type'])['transaction_count'].sum()
    display_df = pd.DataFrame(display_df)
    display_df = display_df.sort_values(by='transaction_count', ascending=False)
    display_df.reset_index(inplace=True)
    new_df = display_df[['transaction_type','transaction_count']]
    return new_df

def agg_trans_state_year_amount(state_query,year_query):
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    display_df = pd.read_sql_query(f'select * from agg_trans where agg_trans.state=\'{state_query}\' and agg_trans.year = {year_query}',engine);
    pd.options.display.float_format = '{:.2f}'.format
    display_df = display_df.groupby(['state','year','transaction_type'])['transaction_amount'].sum()
    display_df = pd.DataFrame(display_df)
    display_df = display_df.sort_values(by='transaction_amount', ascending=False)
    display_df.reset_index(inplace=True)
    new_df = display_df[['transaction_type','transaction_amount']]
    return new_df

def agg_trans_state_quarter_count(state_query,quarter_query):
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    display_df = pd.read_sql_query(f'select * from agg_trans where agg_trans.state=\'{state_query}\' and agg_trans.quarter = {quarter_query}',engine);
    pd.options.display.float_format = '{:.2f}'.format
    display_df = display_df.groupby(['state','quarter','transaction_type'])['transaction_count'].sum()
    display_df = pd.DataFrame(display_df)
    display_df = display_df.sort_values(by='transaction_count', ascending=False)
    display_df.reset_index(inplace=True)
    new_df = display_df[['transaction_type','transaction_count']]
    return new_df

def agg_trans_state_quarter_amount(state_query,quarter_query):
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    display_df = pd.read_sql_query(f'select * from agg_trans where agg_trans.state=\'{state_query}\' and agg_trans.quarter = {quarter_query}',engine);
    pd.options.display.float_format = '{:.2f}'.format
    display_df = display_df.groupby(['state','quarter','transaction_type'])['transaction_amount'].sum()
    display_df = pd.DataFrame(display_df)
    display_df = display_df.sort_values(by='transaction_amount', ascending=False)
    display_df.reset_index(inplace=True)
    new_df= display_df[['transaction_type','transaction_amount']]
    return new_df

def get_top_10_state_count():
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df = pd.read_sql_query(f'SELECT * from top_trans_dist', engine)
    pd.options.display.float_format = '{:.2f}'.format
    temp = df.groupby(['state'])['count'].sum().sort_values(ascending=False).head(10)
    new_df = pd.DataFrame(temp)
    df_2 = new_df.reset_index()
    return df_2

def get_top_10_state_amount():
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df = pd.read_sql_query(f'SELECT * from top_trans_dist', engine)
    pd.options.display.float_format = '{:.2f}'.format
    temp = df.groupby(['state'])['amount'].sum().sort_values(ascending=False).head(10)
    new_df = pd.DataFrame(temp)
    df_2 = new_df.reset_index()
    return df_2

def get_top_10_district_count():
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df = pd.read_sql_query(f'SELECT * from top_trans_dist', engine)
    pd.options.display.float_format = '{:.2f}'.format
    temp = df.groupby(['district'])['count'].sum().sort_values(ascending=False).head(10)
    new_df = pd.DataFrame(temp)
    df_2 = new_df.reset_index()
    return df_2

def get_top_10_district_amount():
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df = pd.read_sql_query(f'SELECT * from top_trans_dist', engine)
    pd.options.display.float_format = '{:.2f}'.format
    temp = df.groupby(['district'])['amount'].sum().sort_values(ascending=False).head(10)
    new_df = pd.DataFrame(temp)
    df_2 = new_df.reset_index()
    return df_2

def get_top_10_pincode_count():
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df = pd.read_sql_query(f'SELECT * from top_trans_pincode', engine)
    df = df.dropna()
    df = df.astype({"pincode":'int'}) 
    new_df = df.groupby(['pincode'])['count'].sum().sort_values(ascending=False).head(10) 
    df_2 = new_df.reset_index()
    return df_2

def get_top_10_pincode_amount():
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df = pd.read_sql_query(f'SELECT * from top_trans_pincode', engine)
    df = df.dropna()
    df = df.astype({"pincode":'int'}) 
    new_df = df.groupby(['pincode'])['amount'].sum().sort_values(ascending=False).head(10) 
    df_2 = new_df.reset_index()
    return df_2

def get_top_10_district_user():
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df = pd.read_sql_query(f'SELECT * from top_user_district', engine)
    new_df = df.groupby(['district'])['registered_users'].sum().sort_values(ascending=False).head(10)
    df_2 = new_df.reset_index()
    return df_2

def get_top_10_pincode_user():
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df = pd.read_sql_query(f'SELECT * from top_user_pincode', engine)
    new_df = df.groupby(['pincode'])['registered_users'].sum().sort_values(ascending=False).head(10)
    df_2 = new_df.reset_index()
    return df_2

def agg_users_state_y_q(state_query,year_query,quarter_query):
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df = pd.read_sql_query(f'SELECT * from agg_users where agg_users.state=\'{state_query}\' and agg_users.year = {year_query} and agg_users.quarter={quarter_query}', engine)
    new_df = df[['phone_brand','count']]
    new_df.set_index('phone_brand', inplace=True)
    return new_df

def agg_users_reg_user(state_query,year_query,quarter_query):
    list1 = []
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df = pd.read_sql_query(f'SELECT * from agg_users where agg_users.state=\'{state_query}\' and agg_users.year = {year_query} and agg_users.quarter={quarter_query}', engine)
    list1.append(df['registered_users'].unique()[0])
    list1.append(df['app_opens'].unique()[0])
    return list1

def get_map_users():
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df_2 = pd.read_sql_query(f'SELECT * from map_users', engine)
    df_3 = df_2.groupby(['state'])['users'].sum()
    new_df = df_3.reset_index()
    new_df['new_state'] = 0
    for i in range(len(new_df)):
        if new_df['state'][i] == 'andaman-&-nicobar-islands':
            new_df['new_state'][i] = 'Andaman & Nicobar'
        elif new_df['state'][i] == 'andhra-pradesh':
            new_df['new_state'][i] = 'Andhra Pradesh'
        elif new_df['state'][i] == 'arunachal-pradesh':
            new_df['new_state'][i] = 'Arunachal Pradesh'
        elif new_df['state'][i] == 'assam':
            new_df['new_state'][i] = 'Assam'
        elif new_df['state'][i] == 'bihar':
            new_df['new_state'][i] = 'Bihar'
        elif new_df['state'][i] == 'chandigarh':
            new_df['new_state'][i] = 'Chandigarh'
        elif new_df['state'][i] == 'chhattisgarh':
            new_df['new_state'][i] = 'Chhattisgarh'
        elif new_df['state'][i] == 'dadra-&-nagar-haveli-&-daman-&-diu':
            new_df['new_state'][i] = 'Dadra and Nagar Haveli and Daman and Diu'
        elif new_df['state'][i] == 'delhi':
            new_df['new_state'][i] = 'Delhi'
        elif new_df['state'][i] == 'goa':
            new_df['new_state'][i] = 'Goa'
        elif new_df['state'][i] == 'gujarat':
            new_df['new_state'][i] = 'Gujarat'
        elif new_df['state'][i] == 'haryana':
            new_df['new_state'][i] = 'Haryana'
        elif new_df['state'][i] == 'himachal-pradesh':
            new_df['new_state'][i] = 'Himachal Pradesh'
        elif new_df['state'][i] == 'jammu-&-kashmir':
            new_df['new_state'][i] = 'Jammu & Kashmir'
        elif new_df['state'][i] == 'jharkhand':
            new_df['new_state'][i] = 'Jharkhand'
        elif new_df['state'][i] == 'karnataka':
            new_df['new_state'][i] = 'Karnataka'
        elif new_df['state'][i] == 'kerala':
            new_df['new_state'][i] = 'Kerala'
        elif new_df['state'][i] == 'ladakh':
            new_df['new_state'][i] = 'Ladakh'
        elif new_df['state'][i] == 'lakshadweep':
            new_df['new_state'][i] = 'Lakshadweep'
        elif new_df['state'][i] == 'madhya-pradesh':
            new_df['new_state'][i] = 'Madhya Pradesh'
        elif new_df['state'][i] == 'maharashtra':
            new_df['new_state'][i] = 'Maharashtra'
        elif new_df['state'][i] == 'manipur':
            new_df['new_state'][i] = 'Manipur'
        elif new_df['state'][i] == 'meghalaya':
            new_df['new_state'][i] = 'Meghalaya'
        elif new_df['state'][i] == 'mizoram':
            new_df['new_state'][i] = 'Mizoram'
        elif new_df['state'][i] == 'nagaland':
            new_df['new_state'][i] = 'Nagaland'
        elif new_df['state'][i] == 'odisha':
            new_df['new_state'][i] = 'Odisha'
        elif new_df['state'][i] == 'puducherry':
            new_df['new_state'][i] = 'Puducherry'
        elif new_df['state'][i] == 'punjab':
            new_df['new_state'][i] = 'Punjab'
        elif new_df['state'][i] == 'rajasthan':
            new_df['new_state'][i] = 'Rajasthan'
        elif new_df['state'][i] == 'sikkim':
            new_df['new_state'][i] = 'Sikkim'
        elif new_df['state'][i] == 'tamil-nadu':
            new_df['new_state'][i] = 'Tamil Nadu'
        elif new_df['state'][i] == 'telangana':
            new_df['new_state'][i] = 'Telangana'
        elif new_df['state'][i] == 'tripura':
            new_df['new_state'][i] = 'Tripura'
        elif new_df['state'][i] == 'uttar-pradesh':
            new_df['new_state'][i] = 'Uttar Pradesh'
        elif new_df['state'][i] == 'uttarakhand':
            new_df['new_state'][i] = 'Uttarakhand'
        elif new_df['state'][i] == 'west-bengal':
            new_df['new_state'][i] = 'West Bengal'
    dummy = new_df.groupby(['new_state'])['users'].sum()
    final_df = dummy.reset_index()
    return final_df


def get_map_trans():
    engine = create_engine('postgresql+psycopg2://postgres:Postgres123$@localhost/phonepe_db')
    df_2 = pd.read_sql_query(f'SELECT * from map_trans', engine)
    df_3 = df_2.groupby(['state'])['amount'].sum()
    new_df = df_3.reset_index()
    new_df['new_state'] = 0
    for i in range(len(new_df)):
        if new_df['state'][i] == 'andaman-&-nicobar-islands':
            new_df['new_state'][i] = 'Andaman & Nicobar'
        elif new_df['state'][i] == 'andhra-pradesh':
            new_df['new_state'][i] = 'Andhra Pradesh'
        elif new_df['state'][i] == 'arunachal-pradesh':
            new_df['new_state'][i] = 'Arunachal Pradesh'
        elif new_df['state'][i] == 'assam':
            new_df['new_state'][i] = 'Assam'
        elif new_df['state'][i] == 'bihar':
            new_df['new_state'][i] = 'Bihar'
        elif new_df['state'][i] == 'chandigarh':
            new_df['new_state'][i] = 'Chandigarh'
        elif new_df['state'][i] == 'chhattisgarh':
            new_df['new_state'][i] = 'Chhattisgarh'
        elif new_df['state'][i] == 'dadra-&-nagar-haveli-&-daman-&-diu':
            new_df['new_state'][i] = 'Dadra and Nagar Haveli and Daman and Diu'
        elif new_df['state'][i] == 'delhi':
            new_df['new_state'][i] = 'Delhi'
        elif new_df['state'][i] == 'goa':
            new_df['new_state'][i] = 'Goa'
        elif new_df['state'][i] == 'gujarat':
            new_df['new_state'][i] = 'Gujarat'
        elif new_df['state'][i] == 'haryana':
            new_df['new_state'][i] = 'Haryana'
        elif new_df['state'][i] == 'himachal-pradesh':
            new_df['new_state'][i] = 'Himachal Pradesh'
        elif new_df['state'][i] == 'jammu-&-kashmir':
            new_df['new_state'][i] = 'Jammu & Kashmir'
        elif new_df['state'][i] == 'jharkhand':
            new_df['new_state'][i] = 'Jharkhand'
        elif new_df['state'][i] == 'karnataka':
            new_df['new_state'][i] = 'Karnataka'
        elif new_df['state'][i] == 'kerala':
            new_df['new_state'][i] = 'Kerala'
        elif new_df['state'][i] == 'ladakh':
            new_df['new_state'][i] = 'Ladakh'
        elif new_df['state'][i] == 'lakshadweep':
            new_df['new_state'][i] = 'Lakshadweep'
        elif new_df['state'][i] == 'madhya-pradesh':
            new_df['new_state'][i] = 'Madhya Pradesh'
        elif new_df['state'][i] == 'maharashtra':
            new_df['new_state'][i] = 'Maharashtra'
        elif new_df['state'][i] == 'manipur':
            new_df['new_state'][i] = 'Manipur'
        elif new_df['state'][i] == 'meghalaya':
            new_df['new_state'][i] = 'Meghalaya'
        elif new_df['state'][i] == 'mizoram':
            new_df['new_state'][i] = 'Mizoram'
        elif new_df['state'][i] == 'nagaland':
            new_df['new_state'][i] = 'Nagaland'
        elif new_df['state'][i] == 'odisha':
            new_df['new_state'][i] = 'Odisha'
        elif new_df['state'][i] == 'puducherry':
            new_df['new_state'][i] = 'Puducherry'
        elif new_df['state'][i] == 'punjab':
            new_df['new_state'][i] = 'Punjab'
        elif new_df['state'][i] == 'rajasthan':
            new_df['new_state'][i] = 'Rajasthan'
        elif new_df['state'][i] == 'sikkim':
            new_df['new_state'][i] = 'Sikkim'
        elif new_df['state'][i] == 'tamil-nadu':
            new_df['new_state'][i] = 'Tamil Nadu'
        elif new_df['state'][i] == 'telangana':
            new_df['new_state'][i] = 'Telangana'
        elif new_df['state'][i] == 'tripura':
            new_df['new_state'][i] = 'Tripura'
        elif new_df['state'][i] == 'uttar-pradesh':
            new_df['new_state'][i] = 'Uttar Pradesh'
        elif new_df['state'][i] == 'uttarakhand':
            new_df['new_state'][i] = 'Uttarakhand'
        elif new_df['state'][i] == 'west-bengal':
            new_df['new_state'][i] = 'West Bengal'
    dummy = new_df.groupby(['new_state'])['amount'].sum()
    final_df = dummy.reset_index()
    return final_df


if __name__ == "__main__":
    global state_query, year, quarter
    create_agg_trans()
    create_agg_users()
    create_top_transaction_district()
    create_top_transaction_pincode()
    create_top_user_district()
    create_top_user_pincode()
    create_map_trans()
    create_map_users()
    st.header(':blue[Phonepe Pulse Data Visualization and Exploration]')
    st.divider()
    st.subheader(":orange[About the project]")
    st.markdown('<div style="text-align: justify"> Unified Payments Interface (UPI) is a system that powers multiple bank accounts into a single mobile application (of any participating bank), merging several banking features, seamless fund routing & merchant payments into one hood. It also caters to the “Peer to Peer” collect request which can be scheduled and paid as per requirement and convenience. UPI is unique in several ways like: Immediate money transfer through mobile device round the clock 24*7 and 365 days, Single mobile application for accessing different bank accounts, Single Click 2 Factor Authentication, QR Code, Best answer to Cash on Delivery hassle, running to an ATM or rendering exact amount, Merchant Payment with Single Application or In-App Payments. The best thing about UPI is that it is a 24/7 service and can be used even on bank holidays and weekends. The app can be downloaded on both Android and Apple phones.</div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> PhonePe Private Limited is a leading e-commerce payment platform in India. The digital wallet company was founded in December 2015. This platform offers services in over 11 Indian regional languages. As a user, you can use the app and book cabs, book hotel services, order food online, pay for your Redbus tickets, and also pay for your flight tickets. You can carry out transactions in the PhonPe app by following any of these methods: UPI Debit Card, UPI Credit Card, Via linked Bank account and using PhonePe Wallet. </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> This project explores the phonepe pulse data to help audience understand how ( Net banking/ Debit card payment/ Credit card payment ), where, when and who( using which device ) does the UPI transactions. </div>', unsafe_allow_html=True)
    st.divider()
    tab1, tab2, tab3, tab4 = st.tabs(['Aggregated_transaction','Aggreagted_users','Map','Top 10'])
    with tab1:
        st.subheader(':orange[**Explore the data**]')
        st.markdown(':orange[**Aggregated transcation count by state**]')
        state_query = st.selectbox(':green[Select the state]',
            ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
            'assam', 'bihar', 'chandigarh', 'chhattisgarh',
            'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
            'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
            'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
            'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
            'uttarakhand', 'west-bengal'))
        if st.button('Fetch the details',key=1):
                dataframe = agg_trans_count(state_query) 
                st.table(dataframe)
                new_df = dataframe.set_index("transaction_type")
                st.bar_chart(new_df)

                   
     
        st.markdown(':orange[**Aggregated transcation Amount by state**]')
        state_query = st.selectbox(':green[Select the state]',
            ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
            'assam', 'bihar', 'chandigarh', 'chhattisgarh',
            'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
            'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
            'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
            'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
            'uttarakhand', 'west-bengal'),key=3)
        if st.button('Fetch the details',key=2):
            dataframe = agg_trans_amount(state_query) 
            st.table(dataframe)
            new_df = dataframe.set_index("transaction_type")
            st.bar_chart(new_df)




        st.markdown('')
        st.markdown(':orange[**Aggregated transacation count and amount by state, year, quarter and transaction type**]')
        col1, col2, col3,col4 = st.columns(4)
        with col1:
            state_query = st.selectbox(':green[**Select the state**]',
            ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
            'assam', 'bihar', 'chandigarh', 'chhattisgarh',
            'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
            'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
            'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
            'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
            'uttarakhand', 'west-bengal'),key=4)
        with col2:
            year_query = st.selectbox(':green[**Select the year**]',
            ('2018', '2019', '2020', '2021', '2022'),key=5)
        
        with col3:
            quarter_query = st.selectbox(':green[**Select the quarter**]',
            ('1', '2', '3', '4'),key=6)
        with col4:
            trans_query = st.selectbox(':green[**Select the type of transaction**]',
            ('Recharge & bill payments', 'Peer-to-peer payments',
       'Merchant payments', 'Financial Services', 'Others'),key=8)
        if st.button('Fetch the details',key=7):
            dataframe = agg_trans_state_year_quarter(state_query,year_query,quarter_query,trans_query) 
            st.table(dataframe)
            

        st.markdown(':orange[**Aggregated transacation type,count by state and year**]')
        col5, col6 = st.columns(2)
        with col5:
            state_query = st.selectbox(':green[**Select the state**]',
            ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
            'assam', 'bihar', 'chandigarh', 'chhattisgarh',
            'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
            'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
            'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
            'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
            'uttarakhand', 'west-bengal'),key=9)
        with col6:
            year_query = st.selectbox(':green[**Select the year**]',
            ('2018', '2019', '2020', '2021', '2022'),key=10)
        if st.button('Fetch the details',key=11):
            dataframe = agg_trans_state_year_count(state_query,year_query) 
            st.table(dataframe)
            new_df = dataframe.set_index("transaction_type")
            st.bar_chart(new_df)

        st.markdown(':orange[**Aggregated transacation type,amount by state and year**]')
        col7, col8 = st.columns(2)
        with col7:
            state_query = st.selectbox(':green[**Select the state**]',
            ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
            'assam', 'bihar', 'chandigarh', 'chhattisgarh',
            'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
            'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
            'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
            'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
            'uttarakhand', 'west-bengal'),key=12)
        with col8:
            year_query = st.selectbox(':green[**Select the year**]',
            ('2018', '2019', '2020', '2021', '2022'),key=13)
        if st.button('Fetch the details',key=14):
            dataframe = agg_trans_state_year_amount(state_query,year_query) 
            st.table(dataframe)
            new_df = dataframe.set_index("transaction_type")
            st.bar_chart(new_df)

        st.markdown(':orange[**Aggregated transacation type,count by state and quarter**]')
        col9, col10 = st.columns(2)
        with col9:
            state_query = st.selectbox(':green[**Select the state**]',
            ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
            'assam', 'bihar', 'chandigarh', 'chhattisgarh',
            'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
            'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
            'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
            'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
            'uttarakhand', 'west-bengal'),key=15)
        with col10:
            quarter_query = st.selectbox(':green[**Select the quarter**]',
            ('1', '2', '3', '4'),key=18)
        if st.button('Fetch the details',key=17):
            dataframe = agg_trans_state_quarter_count(state_query,quarter_query) 
            st.table(dataframe)
            new_df = dataframe.set_index("transaction_type")
            st.bar_chart(new_df)
            

        st.markdown(':orange[**Aggregated transacation type,amount by state and quarter**]')
        col11, col12 = st.columns(2)
        with col11:
            state_query = st.selectbox(':green[**Select the state**]',
            ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
            'assam', 'bihar', 'chandigarh', 'chhattisgarh',
            'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
            'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
            'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
            'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
            'uttarakhand', 'west-bengal'),key=19)
        with col12:
            quarter_query = st.selectbox(':green[**Select the quarter**]',
            ('1', '2', '3', '4'),key=20)
        if st.button('Fetch the details',key=21):
            dataframe = agg_trans_state_quarter_amount(state_query,quarter_query) 
            st.table(dataframe)
            new_df = dataframe.set_index("transaction_type")
            st.bar_chart(new_df)

    with tab2:
        st.markdown(':orange[**Phone brands using the app by state, year and quarter**]')
        col13, col14, col15 = st.columns(3)
        with col13:
            state_query = st.selectbox(':green[**Select the state**]',
            ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
            'assam', 'bihar', 'chandigarh', 'chhattisgarh',
            'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
            'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
            'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
            'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
            'uttarakhand', 'west-bengal'),key=99)
        with col14:
            year_query = st.selectbox(':green[**Select the year**]',
            ('2018', '2019', '2020', '2021'),key=30)
        with col15:
            quarter_query = st.selectbox(':green[**Select the quarter**]',
            ('1', '2', '3', '4'),key=31)
        if st.button('Fetch the details',key=32):
            dataframe = agg_users_state_y_q(state_query,year_query,quarter_query) 
            st.table(dataframe)
            st.bar_chart(dataframe)

        st.markdown(':orange[**Registered users and app opens by state, year and quarter**]')
        col16, col17, col18 = st.columns(3)
        with col16:
            state_query = st.selectbox(':green[**Select the state**]',
            ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
            'assam', 'bihar', 'chandigarh', 'chhattisgarh',
            'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
            'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
            'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
            'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
            'uttarakhand', 'west-bengal'),key=33)
        with col17:
            year_query = st.selectbox(':green[**Select the year**]',
            ('2018', '2019', '2020', '2021'),key=34)
        with col18:
            quarter_query = st.selectbox(':green[**Select the quarter**]',
            ('1', '2', '3', '4'),key=35)
        col19, col20, col21 = st.columns(3)
        with col20:
            if st.button('Fetch the details',key=36):
                ans_list = agg_users_reg_user(state_query,year_query,quarter_query) 
                st.markdown(f':orange[Registered users :] :green[**{ans_list[0]}**]')
                st.markdown(f':orange[App opens :] :green[**{ans_list[1]}**]')


    with tab3:
        st.markdown(':orange[** Statewise users**]')
        dataframe = get_map_users()
        fig = px.choropleth(dataframe,
                   geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                   featureidkey='properties.ST_NM',
                   locations='new_state',
                   color='users',
                   hover_data=['new_state','users'])
        fig.update_geos(fitbounds = 'locations',visible = False )
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.write(fig)

        st.divider()
        st.markdown(':orange[** Statewise Transaction**]')
        dataframe = get_map_trans()
        fig = px.choropleth(dataframe,
                   geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                   featureidkey='properties.ST_NM',
                   locations='new_state',
                   color='amount',
                   hover_data=['new_state','amount'])
        fig.update_geos(fitbounds = 'locations',visible = False )
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.write(fig)

    with tab4:
        st.markdown(':orange[Top 10 states by transaction count]')
        if st.button('Fetch the details',key=22):
            dataframe = get_top_10_state_count()
            st.table(dataframe)
            fig = px.pie(values=dataframe['count'], names=dataframe['state'])
            st.write(fig)

        st.markdown(':orange[Top 10 states by transaction amount]')
        if st.button('Fetch the details',key=23):
            dataframe = get_top_10_state_amount()
            st.table(dataframe)
            fig = px.pie(values=dataframe['amount'], names=dataframe['state'])
            st.write(fig)

        st.markdown(':orange[Top 10 districts by transaction count]')
        if st.button('Fetch the details',key=24):
            dataframe = get_top_10_district_count()
            st.table(dataframe)
            fig = px.pie(values=dataframe['count'], names=dataframe['district'])
            st.write(fig)

        st.markdown(':orange[Top 10 districts by transaction amount]')
        if st.button('Fetch the details',key=25):
            dataframe = get_top_10_district_amount()
            st.table(dataframe)
            fig = px.pie(values=dataframe['amount'], names=dataframe['district'])
            st.write(fig)

        st.markdown(':orange[Top 10 pincode by transaction count]')
        if st.button('Fetch the details',key=26):
            dataframe = get_top_10_pincode_count()
            st.table(dataframe)
            fig = px.pie(values=dataframe['count'], names=dataframe['pincode'])
            st.write(fig)

        st.markdown(':orange[Top 10 pincode by transaction amount]')
        if st.button('Fetch the details',key=27):
            dataframe = get_top_10_pincode_amount()
            st.table(dataframe)
            fig = px.pie(values=dataframe['amount'], names=dataframe['pincode'])
            st.write(fig)
        

        
        st.markdown(':orange[Top 10 districts by users]')
        if st.button('Fetch the details',key=28):
            dataframe = get_top_10_district_user()
            st.table(dataframe)
            fig = px.pie(values=dataframe['registered_users'], names=dataframe['district'])
            st.write(fig)



        st.markdown(':orange[Top 10 pincodes by users]')
        if st.button('Fetch the details',key=29):
            dataframe = get_top_10_pincode_user()
            st.table(dataframe)
            fig = px.pie(values=dataframe['registered_users'], names=dataframe['pincode'])
            st.write(fig)

st.subheader(':orange[About the developer]')
st.write('')
st.markdown('<div style="text-align: justify">Gururaj H C is passionate about Machine Learning and fascinated by its myriad real world applications. Possesses work experience with both IT industry and academia. Currently pursuing “IIT-Madras Certified Advanced Programmer with Data Science Mastery Program” course as a part of his learning journey.  </div>', unsafe_allow_html=True)
st.divider()
st.markdown('_An effort by_ :blue[**MAVERICK_GR**]')
st.markdown(':green[**DEVELOPER CONTACT DETAILS**]')
st.markdown(":orange[email id:] gururaj008@gmail.com")
st.markdown(":orange[Personal webpage hosting other Datascience projects :] http://gururaj008.pythonanywhere.com/")
st.markdown(":orange[LinkedIn profile :] https://www.linkedin.com/in/gururaj-hc-machine-learning-enthusiast/")
st.markdown(":orange[Github link:] https://github.com/Gururaj008 ")