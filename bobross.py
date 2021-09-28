import streamlit as st
import numpy as np
import pandas as pd
import requests
import plotly.express as px

# Page config
st.set_page_config(
  page_title='Bob Ross Analyse',
  page_icon="https://i.pinimg.com/originals/82/30/a7/8230a7a2189e8af0111eb0b5010e3175.png",
  menu_items={
    'Get Help': None,
    'Report a bug': None
  }
)

# Page logic
@st.cache
def createDataFrame():
  # Fetch csv files
  df_elements = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/bob-ross/elements-by-episode.csv')
  df_paintings = pd.read_csv('https://raw.githubusercontent.com/jwilber/Bob_Ross_Paintings/master/data/bob_ross_paintings.csv', index_col=0)

  # Drop columns
  df_paintings.drop(['img_src', 'colors', 'color_hex'], 1, inplace=True)

  # Return clean dataframe
  return df_paintings.join(df_elements[['APPLE_FRAME', 'AURORA_BOREALIS', 'BARN', 'BEACH', 'BOAT', 'BRIDGE', 'BUILDING', 'BUSHES', 'CABIN', 'CACTUS', 'CIRCLE_FRAME', 'CIRRUS', 'CLIFF', 'CLOUDS', 'CONIFER', 'CUMULUS', 'DECIDUOUS', 'DIANE_ANDRE', 'DOCK', 'DOUBLE_OVAL_FRAME', 'FARM', 'FENCE', 'FIRE', 'FLORIDA_FRAME', 'FLOWERS', 'FOG', 'FRAMED', 'GRASS', 'GUEST', 'HALF_CIRCLE_FRAME', 'HALF_OVAL_FRAME', 'HILLS', 'LAKE', 'LAKES', 'LIGHTHOUSE', 'MILL', 'MOON', 'MOUNTAIN', 'MOUNTAINS', 'NIGHT', 'OCEAN', 'OVAL_FRAME', 'PALM_TREES', 'PATH', 'PERSON', 'PORTRAIT', 'RECTANGLE_3D_FRAME', 'RECTANGULAR_FRAME', 'RIVER', 'ROCKS', 'SEASHELL_FRAME', 'SNOW', 'SNOWY_MOUNTAIN', 'SPLIT_FRAME', 'STEVE_ROSS', 'STRUCTURE', 'SUN', 'TOMB_FRAME', 'TREE', 'TREES', 'TRIPLE_FRAME', 'WATERFALL', 'WAVES', 'WINDMILL', 'WINDOW_FRAME', 'WINTER', 'WOOD_FRAMED'] ])

def getQuote():
  r = requests.get('https://api.bobross.dev/api').json()
  return r['response'][0]['quote']

df = createDataFrame()

# Page content

st.markdown("# Bob Ross' schilderijen analyse")

st.caption("Geschreven door Boaz Geelhoed (500825279), Karlijn Huissen (500889478), Michael Westland (500889605) en Tessa Troostheiede (500799202)")
st.caption("Datum: 1 oktober 2021")

# st.markdown('> ' + getQuote() + '\n\r > *- Bob Ross*')

st.markdown("""
  ## Hoofdstuknaam 1

""")

st.dataframe(df)

st.markdown("---")

st.markdown("### Filters")

col1, col2 = st.columns(2)

with col1:
  minColor = st.slider('Minimaal aantal kleuren', 0, 15, 0, 1)

if minColor != 15:
  with col2:
    maxColor = st.slider('Maximaal aantal kleuren', minColor, 15, 15, 1)

st.markdown('Selecteer de kleuren die het schilderij moet bevatten')

col1, col2, col3 = st.columns(3)

with col1:
  blackGesso = st.checkbox('Black Gesso')
  brightRed = st.checkbox('Bright Red')
  burntUmber = st.checkbox('Burnt Umber')
  cardmiumYellow = st.checkbox('Cardmium Yellow')
  darkSienna = st.checkbox('Dark Sienna')
  indianRed = st.checkbox('Indian Red')

with col2:
  indianYellow = st.checkbox('Indian Yellow')
  liquidBlack = st.checkbox('Liquid Black')
  liquidClear = st.checkbox('Liquid Clear')
  midnightBlack = st.checkbox('Midnight Black')
  phthaloBlue = st.checkbox('Phthalo Blue')
  phthaloGreen = st.checkbox('Phthalo Green')

with col3:
  prussianBlue = st.checkbox('Prussian Blue')
  sapGreen = st.checkbox('Sap Green')
  titaniumWhite = st.checkbox('Titanium White')
  vanDykeBrown = st.checkbox('Van Dyke Brown')
  yellowOchre = st.checkbox('Yellow Ochre')
  alizarinCrimson = st.checkbox('Alizarin Crimson')

if minColor != 15:
  df_filtered = df[(df['num_colors'] >= minColor) & (df['num_colors'] <= maxColor)]
else:
  df_filtered = df[df['num_colors'] >= minColor]

df_filtered = df_filtered[
  (df_filtered['Black_Gesso'] == blackGesso) &
  (df_filtered['Bright_Red'] == brightRed) &
  (df_filtered['Burnt_Umber'] == burntUmber) &
  (df_filtered['Cadmium_Yellow'] == cardmiumYellow) &
  (df_filtered['Dark_Sienna'] == darkSienna) &
  (df_filtered['Indian_Red'] == indianRed) &
  (df_filtered['Indian_Yellow'] == indianYellow) &
  (df_filtered['Liquid_Black'] == liquidBlack) &
  (df_filtered['Liquid_Clear'] == liquidClear) &
  (df_filtered['Midnight_Black'] == midnightBlack) &
  (df_filtered['Phthalo_Blue'] == phthaloBlue) &
  (df_filtered['Phthalo_Green'] == phthaloGreen) &
  (df_filtered['Prussian_Blue'] == prussianBlue) &
  (df_filtered['Sap_Green'] == sapGreen) &
  (df_filtered['Titanium_White'] == titaniumWhite) &
  (df_filtered['Van_Dyke_Brown'] == vanDykeBrown) &
  (df_filtered['Yellow_Ochre'] == yellowOchre) &
  (df_filtered['Alizarin_Crimson'] == alizarinCrimson)
]

st.markdown('')
st.markdown('Gefilterde dataframe')
df_filtered

options = st.multiselect(
  'What are your favorite colors',
  ['Green', 'Yellow', 'Red', 'Blue'],
  ['Yellow', 'Red'])

option = st.selectbox(
  'How would you like to be contacted?',
  ('Email', 'Home phone', 'Mobile phone'))

st.markdown("---")

st.dataframe(df.describe())

fig = px.histogram(df['num_colors'])
st.write(fig)

fig = px.bar(df[['Black_Gesso','Bright_Red', 'Burnt_Umber', 'Cadmium_Yellow', 'Dark_Sienna', 'Indian_Red', 'Indian_Yellow', 'Liquid_Black', 'Liquid_Clear', 'Midnight_Black', 'Phthalo_Blue', 'Phthalo_Green', 'Prussian_Blue', 'Sap_Green', 'Titanium_White', 'Van_Dyke_Brown', 'Yellow_Ochre', 'Alizarin_Crimson']].mean(), orientation='h', height=500)
st.write(fig)

fig = px.bar(df[['APPLE_FRAME', 'AURORA_BOREALIS', 'BARN', 'BEACH', 'BOAT', 'BRIDGE', 'BUILDING', 'BUSHES', 'CABIN', 'CACTUS', 'CIRCLE_FRAME', 'CIRRUS', 'CLIFF', 'CLOUDS', 'CONIFER', 'CUMULUS', 'DECIDUOUS', 'DIANE_ANDRE', 'DOCK', 'DOUBLE_OVAL_FRAME', 'FARM', 'FENCE', 'FIRE', 'FLORIDA_FRAME', 'FLOWERS', 'FOG', 'FRAMED', 'GRASS', 'GUEST', 'HALF_CIRCLE_FRAME', 'HALF_OVAL_FRAME', 'HILLS', 'LAKE', 'LAKES', 'LIGHTHOUSE', 'MILL', 'MOON', 'MOUNTAIN', 'MOUNTAINS', 'NIGHT', 'OCEAN', 'OVAL_FRAME', 'PALM_TREES', 'PATH', 'PERSON', 'PORTRAIT', 'RECTANGLE_3D_FRAME', 'RECTANGULAR_FRAME', 'RIVER', 'ROCKS', 'SEASHELL_FRAME', 'SNOW', 'SNOWY_MOUNTAIN', 'SPLIT_FRAME', 'STEVE_ROSS', 'STRUCTURE', 'SUN', 'TOMB_FRAME', 'TREE', 'TREES', 'TRIPLE_FRAME', 'WATERFALL', 'WAVES', 'WINDMILL', 'WINDOW_FRAME', 'WINTER', 'WOOD_FRAMED']].mean(), orientation='h', height=1500)
st.write(fig)