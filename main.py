import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
from streamlit_option_menu import option_menu

st.set_page_config(layout='wide')
st.title('**Store sales forecasting**')


selected = option_menu(menu_title=None,options= ["Prediction using CSV file", 'Prediction on a single data'],orientation='horizontal',
                       icons=['forecasting.png', 'predictive-chart.png'], default_index=0,
                       styles={
        "container": {"padding": "0!important", "background-color": "grey"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "grey"},
        "nav-link-selected": {"background-color": "#35383d"},
    }
)
try:
    if selected == "Prediction using CSV file":
        file_upload=st.file_uploader('Upload excel file',type=['.csv'])
        if file_upload:
            dataframe = pd.read_csv(file_upload.name)
            st.subheader("Uploaded dataframe")
            st.dataframe(dataframe)
            dataframe['family']=encoder.fit_transform(dataframe['family'])
            dataframe['date']=pd.to_datetime(dataframe['date'])
            dataframe['year'] = dataframe['date'].dt.year
            dataframe['month'] = dataframe['date'].dt.month
            dataframe['day'] = dataframe['date'].dt.day
            dataframe['day_of_week'] = dataframe['date'].dt.dayofweek
            dataframe['weekend'] = dataframe['day_of_week'].isin([5, 6]).astype(int)
            dataframe=dataframe.drop("date", axis=1)
            if st.checkbox('Click Here to check the prediction of sales')==True:
                    st.subheader("Predicted Sales")
                    loadModel = joblib.load('xgb_model.joblib')
                    preds=loadModel.predict(dataframe)
                    pred_dataframe = pd.DataFrame({"ID":dataframe['id'],"Sales_Forcaste":list(preds)})
                    st.dataframe(pred_dataframe)
        else:
            st.warning("Please upload a CSV file.")
except Exception as e:
       st.error('**Upload a valid file**')

if selected=="Prediction on a single data":
    date = st.date_input('Enter the date for which you want to forecast')
    store_id = st.number_input('Enter Id',step=1)
    product_list=['AUTOMOTIVE', 'BABY CARE', 'BEAUTY', 'BEVERAGES', 'BOOKS',
        'BREAD/BAKERY', 'CELEBRATION', 'CLEANING', 'DAIRY', 'DELI', 'EGGS',
        'FROZEN FOODS', 'GROCERY I', 'GROCERY II', 'HARDWARE',
        'HOME AND KITCHEN I', 'HOME AND KITCHEN II', 'HOME APPLIANCES',
        'HOME CARE', 'LADIESWEAR', 'LAWN AND GARDEN', 'LINGERIE',
        'LIQUOR,WINE,BEER', 'MAGAZINES', 'MEATS', 'PERSONAL CARE',
        'PET SUPPLIES', 'PLAYERS AND ELECTRONICS', 'POULTRY',
        'PREPARED FOODS', 'PRODUCE', 'SCHOOL AND OFFICE SUPPLIES',
        'SEAFOOD']
    store_product=st.selectbox('Enter the Product Name',product_list)
    if store_product== product_list[0]:
            store_product=0
    elif store_product== product_list[1]:
            store_product=1
    elif store_product== product_list[2]:
            store_product=2
    elif store_product== product_list[3]:
            store_product=3
    elif store_product== product_list[4]:
            store_product=4
    elif store_product== product_list[5]:
            store_product=5
    elif store_product== product_list[7]:
            store_product=6
    elif store_product== product_list[8]:
            store_product=8
    elif store_product== product_list[9]:
            store_product=9
    elif store_product== product_list[10]:
            store_product=10
    elif store_product== product_list[11]:
            store_product=11
    elif store_product== product_list[12]:
            store_product=12
    elif store_product== product_list[13]:
            store_product=13
    elif store_product== product_list[14]:
            store_product=14
    elif store_product== product_list[15]:
            store_product=15
    elif store_product== product_list[16]:
            store_product=16
    elif store_product== product_list[17]:
            store_product=17
    elif store_product== product_list[18]:
            store_product=18
    elif store_product== product_list[19]:
            store_product=19
    elif store_product== product_list[20]:
            store_product=20
    elif store_product== product_list[21]:
            store_product=21
    elif store_product== product_list[22]:
            store_product=22
    elif store_product== product_list[23]:
            store_product=23
    elif store_product== product_list[24]:
            store_product=24
    elif store_product== product_list[25]:
            store_product=25
    elif store_product== product_list[26]:
            store_product=26
    elif store_product== product_list[27]:
            store_product=27
    elif store_product== product_list[28]:
            store_product=28
    elif store_product== product_list[29]:
            store_product=29
    elif store_product== product_list[30]:
            store_product=30
    elif store_product== product_list[31]:
            store_product=31
    elif store_product== product_list[32]:
            store_product=32
    else: 
        store_product=33

    store_promtion = st.number_input('How many time you have done advertisement',step=1)
    store_number = st.number_input('Enter you store unique number',step=1)


    if store_id and date and store_number and product_list and store_promtion:
            dataframe = pd.DataFrame({"id":[store_id],"date":[date],"store_nbr":[store_number],
                                    "family":[store_product],"onpromotion":[store_promtion]})
            dataframe['date']=pd.to_datetime(dataframe['date'])
            dataframe['year'] = dataframe['date'].dt.year
            dataframe['month'] = dataframe['date'].dt.month
            dataframe['day'] = dataframe['date'].dt.day
            dataframe['day_of_week'] = dataframe['date'].dt.dayofweek
            dataframe['weekend'] = dataframe['day_of_week'].isin([5, 6]).astype(int)
            dataframe=dataframe.drop("date", axis=1)
            if st.checkbox('Click Here to check the prediction of sales')==True:
                loadModel = joblib.load('xgb_model.joblib')
                preds=loadModel.predict(dataframe)
                if preds:
                        st.write(f'Your Sales will be {preds[0]} on {date}')