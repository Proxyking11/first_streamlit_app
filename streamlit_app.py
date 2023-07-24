import streamlit
import pandas
import requests

streamlit.title ("My Mom's New Healthy Dinner")
streamlit.header ('Breakfast Favourites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('🥑🍞Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.header ('🍌🥭Build your own Fruit Smoothie 🥝🍇')

my_fruit_list=pandas.read_csv ('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list= my_fruit_list.set_index('Fruit')
streamlit.dataframe (my_fruit_list)

fruit_selected= streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruit_to_show)

streamlit.header('Fruit Vice Advice')

fruit_choice=streamlit.text_input('What fruit do you like ?' ,'kiwi')
streamlit.write('the user entered: ', fruit_choice)
fruit_request= requests.get('https://fruityvice.com/api/fruit/'+'fruit_choice')
                                
import 'snowflake-connector-python'
                                       

