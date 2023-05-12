

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/DELL/Music/m/start up sucess rate/startup.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Start up sucess rate prediction using ml',
                          
                          [ 'Home',
                            'start up success prediction',
                           'graph comparsion',
                           'model prediction result',
                            'contact details'
                            ],
                          default_index=0)

# Diabetes Prediction Page
if (selected == 'Home'):
    
    # page title
    st.title('start up sucesss prediction')

    st.image("main-qimg-8098b883409cd8e342ad12.jpg")

    st.subheader(' Startups play a major role in economic growth. They bring new ideas, spur innovation, create employment thereby moving the economy. There has been an exponential growth in startups over the past few years. Predicting the success of a startup allows investors to find companies that have the potential for rapid growth, thereby allowing them to be one step ahead of the competition.')
    
  
    
# Diabetes Prediction Page
if (selected == 'start up success prediction'):
    
    # page title
    st.title('start up success prediction ml')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        nor_age_first_funding_year= st.text_input('nor_age_first_funding_year')
        
    with col2:
        nor_age_last_funding_year = st.text_input('nor_age_last_funding_year ')
    
    with col3:
        nor_age_first_milestone_year = st.text_input('nor_age_first_milestone_year')
    
    with col1:
        nor_age_last_milestone_year	 = st.text_input('nor_age_last_milestone_year')
    
    with col2:
        nor_funding_rounds = st.text_input('nor_funding_rounds')
    
    with col3:
        nor_funding_total_usd = st.text_input('nor_funding_total_usd ')
    
    with col1:
        nor_milestones	 = st.text_input('nor_milestones')
    
    with col2:
        is_CA = st.text_input('is_CA')

    with col3:
        is_NY = st.text_input('is_NY')
    
    with col1:
        is_othercategory= st.text_input('is_othercategory')
    
    with col2:
        has_VC	 = st.text_input('has_VC')

    with col3:
        has_angel = st.text_input(' has_angel ')
    
    with col1:
        has_roundA		 = st.text_input(' has_roundA	')

    with col2:
        has_roundB  = st.text_input(' has_roundB  ')
    
    with col3:
        has_roundC = st.text_input('has_roundC')

    with col1:
        has_roundD = st.text_input('has_roundD')
    
    with col2:
        nor_avg_participants	= st.text_input('nor_avg_participants')
    
    with col3:
        is_top500 = st.text_input('is_top500')

    with col1:
        nor_age = st.text_input(' nor_age')
    
    
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('start up Result'):
        diab_prediction = diabetes_model.predict([[nor_age_first_funding_year, nor_age_last_funding_year, 
            nor_age_first_milestone_year, nor_age_last_milestone_year, nor_relationships,
            nor_funding_rounds, nor_funding_total_usd, nor_milestone, is_CA,is_NY,
            is_othercategory, has_VC, has_angel, has_roundA, has_roundB, 
            has_roundC, has_roundD, nor_avg_participants, is_top500, nor_age]])

        st.success('The output is {}'.format(diab_prediction ))
        
        
        
    

# Parkinson's Prediction Page
if (selected == "graph comparsion"):
    
    # page title
    st.title("graph comparsion")

    st.image("Capture1.png")


    st.image("Capture2.png")


    st.image("Capture3.png")
    
    
# describtion
if (selected == 'model prediction result'):
    
    # page title
    st.title('model prediction result')

    st.title('XG BOOST') 
    st.image("Capture4.png")


    st.title('DECESION TREE')
    st.image("Capture5.png")

    
    st.title('KNN')
    st.image("Capture6.png")

# describtion
if (selected == 'contact details'):
    
    # page title
    st.title('contact details')

    st.subheader('T  Athira    -196C1A0592  ')
    st.subheader('N Krishna    -196C1A0561 ')
    st.subheader('S Swathi     -196C1A0585')
    st.subheader('P Vishnusree -196C1A0569')

    
   

if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")




