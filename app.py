import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

d1 = pd.read_csv('locationwise_crimes.csv')
d2 = pd.read_csv('crimes_against_women.csv')
d3 = pd.read_csv('juvenile.csv')
#
d1 = preprocessor.preprocess(d1)

st.sidebar.title("Crimes in Pune Analysis")
# st.sidebar.image('https://e7.pngegg.com/pngimages/1020/402/png-clipart-2024-summer-olympics-brand-circle-area-olympic-rings-olympics-logo-text-sport.png')
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Overall Analysis','Location-wise Analysis','Crimes Against Females Analysis','Juvenile Crimes Analysis')
)

# st.dataframe(d1)
print(d1)
if user_menu == 'Location-wise Analysis':
    st.sidebar.header("Location Wise Analysis")
    location = helper.location_list(d1)

    selected_location = st.sidebar.selectbox("Select Location", location)
#
    locationwise = helper.fetch_locationwise(d1,selected_location)
    if selected_location == 'Overall':
        st.title("Overall Crimes in Various Locations")
    if selected_location != 'Overall':
        st.title("Crimes in " + str(selected_location))



    st.dataframe(locationwise)
    # ------------------------------------------------------------------------------
    # abcd = helper.abc(d1)
    # print(type(abcd))
    # print("Model Loaded")
    # dict = abcd.to_dict()
    # print(dict)
    # # fig = abcd.plot.line()
    # # fig.show()
    # st.plotly_chart(dict)
#--------------------------------------------------------------------------------------------

if user_menu == 'Overall Analysis':
    st.sidebar.header("Overall Analysis")


    localities = d1['Locality'].unique().shape[0]
    crimes = d3['Crime Head'].unique().shape[0]
    # events = df['Event'].unique().shape[0]
    # athletes = df['Name'].unique().shape[0]
    # nations = df['region'].unique().shape[0]

    # st.title("Top Statistics")
    col1, col2= st.columns(2)
    with col1:
        st.header("Localities")
        st.title(localities)
    with col2:
        st.header("Number of Crimes")
        st.title(crimes)



    st.title("Crimes across various Locations")
    st.dataframe(d1)

    st.title("Locality vs Total Crimes Occured")
    total=helper.total_crimes(d1)
    fig = px.line(d1, x="Locality", y="Total Crimes")
    st.plotly_chart(fig)


if user_menu == 'Crimes Against Females Analysis':
    st.sidebar.header("Crimes against Females")
    year,locality = helper.locality_year_list(d2)

    selected_year = st.sidebar.selectbox("Select Year",year)
    selected_locality = st.sidebar.selectbox("Select Location", locality)

    female = helper.fetch_female(d2,selected_year,selected_locality)
    if selected_year == 'Overall' and selected_locality == 'Overall':
        st.title("Overall Crimes against Women")
    if selected_year != 'Overall' and selected_locality == 'Overall':
        st.title("Crimes against women in " + str(selected_year))
    if selected_year == 'Overall' and selected_locality != 'Overall':
        st.title(selected_locality + "'s overall crime against women")
    if selected_year != 'Overall' and selected_locality != 'Overall':
        st.title("Crimes against Women in " + str(selected_year) + " in " + selected_locality)
    st.table(female)


if user_menu == 'Juvenile Crimes Analysis':
    st.title("Juvenile Crimes")
    st.table(d3)

    st.title("Cases Reported For Each Crime Against Juveniles")
    cases = helper.juvenile(d3)
    fig = px.line(d3, x='Cases Reported against Juveniles', y='Crimes')
    st.plotly_chart(fig)

    st.title("Cases against Juveniles below 12 years")
    total = helper.juvenile(d3)
    fig = px.line(d3, x="Crimes", y="Below 12 Years-Total")
    st.plotly_chart(fig)

    st.title("Cases against Juveniles above 12 years and below 16 years")
    total = helper.juvenile(d3)
    fig = px.line(d3, x="Crimes", y="12 Years & Above and below 16 Years-Total")
    st.plotly_chart(fig)

    st.title("Cases against Juveniles above 16 Years and below 18 Years")
    total = helper.juvenile(d3)
    fig = px.line(d3, x="Crimes", y="16 Years & Above and below 18 Years-Total")
    st.plotly_chart(fig)
