import streamlit
streamlit.header(' My parents new healthy diner')
streamlit.title('Breakfast Favourites')
streamlit.text('🥣Omega-3 and blueberry oatmeal')
streamlit.text('🥬Kale,Spinach & Rocket smoothie')
streamlit.text('🐔Hard-boiled free range eggs')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🍐Build your own fruit smoothie🍑🥝')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
