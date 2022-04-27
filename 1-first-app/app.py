# SETUP

import streamlit as st
import pandas as pd
import datetime


#-------------------
# CREATE DATA

# Simple dataframe
df = pd.DataFrame({
    'A': [1, 4, 3, 2],
    'B': [10, 20, 30, 40]
    })

# Erzeuge Tabelle mit zwei Spalten A und B mit diesen vier Werten jeweils

#-------------------
# START OF APP

#-------------------
# HEADER

# Title of our app
st.title('Meine erste App')
# Add header
st.header('Mein Header')
# Add a gif from https://giphy.com/
st.markdown("![Katze](https://media.giphy.com/media/JmBXdjfIblJDi/giphy.gif)")

#st.image('hdm-logo.jpg')

#-------------------
# BODY

#-------------------
# Show static DataFrame
st.dataframe(df)

#-------------------
# Bar chart
st.bar_chart(df)


# Sidebar
st.sidebar.write("Das ist meine Sidebar")
st.sidebar.button("Hier klicken!")


add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)


# Spalten
col1, col2 = st.columns(2)
col1.write("Das ist Zeile 1")
col2.write("Das ist Zeile 2")

# Slider
age = st.slider("Wähle dein Alter", 0, 100)
st.write("Ich bin", age, 'Jahre alt')

# Datum
d = st.date_input(
    "Wann hast du Geburtstag?",
    (datetime.date(2019,7,6))
)
st.write('Dein Geburtstag ist:',d)