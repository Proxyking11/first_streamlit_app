import streamlit
import pandas
import requests
streamlit.title ('My parent need healthy food')
streamlit.header ('Breakfast Menu')
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
fruit_request= requests.get('https://fruityvice.com/api/fruit/'+'kiwi')


fruit_nicer=pandas.json_normalize(fruit_request.json())
streamlit.dataframe(fruit_nicer)

fruit_choice=streamlit.text_input('What fruit do you like ?' ,'kiwi')
streamlit.write('the user entered: ', fruit_choice)
                                
 
                                       

