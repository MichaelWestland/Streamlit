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
  df_paintings = pd.read_csv('https://raw.githubusercontent.com/jwilber/Bob_Ross_Paintings/master/data/bob_ross_paintings.csv')

  # Drop columns
  df_paintings.drop(['painting_index', 'img_src', 'youtube_src' , 'colors', 'color_hex', 'Unnamed: 0'], 1, inplace=True)

  # Return dataframe with joined columns
  return df_paintings.join(df_elements[['APPLE_FRAME', 'AURORA_BOREALIS', 'BARN', 'BEACH', 'BOAT', 'BRIDGE', 'BUILDING', 'BUSHES', 'CABIN', 'CACTUS', 'CIRCLE_FRAME', 'CIRRUS', 'CLIFF', 'CLOUDS', 'CONIFER', 'CUMULUS', 'DECIDUOUS', 'DIANE_ANDRE', 'DOCK', 'DOUBLE_OVAL_FRAME', 'FARM', 'FENCE', 'FIRE', 'FLORIDA_FRAME', 'FLOWERS', 'FOG', 'FRAMED', 'GRASS', 'GUEST', 'HALF_CIRCLE_FRAME', 'HALF_OVAL_FRAME', 'HILLS', 'LAKE', 'LAKES', 'LIGHTHOUSE', 'MILL', 'MOON', 'MOUNTAIN', 'MOUNTAINS', 'NIGHT', 'OCEAN', 'OVAL_FRAME', 'PALM_TREES', 'PATH', 'PERSON', 'PORTRAIT', 'RECTANGLE_3D_FRAME', 'RECTANGULAR_FRAME', 'RIVER', 'ROCKS', 'SEASHELL_FRAME', 'SNOW', 'SNOWY_MOUNTAIN', 'SPLIT_FRAME', 'STEVE_ROSS', 'STRUCTURE', 'SUN', 'TOMB_FRAME', 'TREE', 'TREES', 'TRIPLE_FRAME', 'WATERFALL', 'WAVES', 'WINDMILL', 'WINDOW_FRAME', 'WINTER', 'WOOD_FRAMED']])

def getQuote():
  r = requests.get('https://api.bobross.dev/api').json()
  return r['response'][0]['quote']

df = createDataFrame()

# Page content

st.markdown("# Bob Ross' schilderijen analyse")

st.caption("Geschreven door Boaz Geelhoed (500825279), Karlijn Huissen (500889478), Michael Westland (500889605) en Tessa Troostheide (500799202)")
st.caption("Datum: 1 oktober 2021")

st.image("https://images0.persgroep.net/rcs/QwWUYB6t8dQG7cpgeJiA5R-WCLU/diocontent/70177042/_fitwidth/694/?appId=21791a8992982cd8da851550a453bd7f&quality=0.8")

# st.markdown('> ' + getQuote() + '\n\r > *- Bob Ross*')

st.markdown("""
  ## Inleiding
  Bob Ross (1942 - 1995) was een Amerikaanse landschapschilder die in zijn televisieserie *The Joy of Painting* veel verschillende schilderijen heeft geschilderd. Deze schilderijen zullen in dit rapport geanalyseert worden op basis van de geschilderde objecten en gebruikte kleuren.

  ## API
  Om de schilderijen van Bob Ross te analyseren, zal er gebruik gemaakt worden van twee verschillende csv datasets.
  - FiveThirtyEight heeft een [dataset](https://raw.githubusercontent.com/fivethirtyeight/data/master/bob-ross/elements-by-episode.csv) gepubliceert waarin per schilderij de objecten staan die zijn geschilderd. De nauwkeurigheid van deze dataset kan ter discussie staan. Er zijn meer dan 400 schilderijen die bekeken moesten worden voor de inhoud. Hier kunnen fouten zijn gemaakt en kan subjectief zijn beoordeeld. In dit rapport zal deze data letterlijk over genomen worden zonder verbeteringen.
  - GitHub gebruiker *jwilber* heeft een [dataset](https://raw.githubusercontent.com/jwilber/Bob_Ross_Paintings/master/data/bob_ross_paintings.csv) gepubliceerd waarin per schilderij onder andere de afbeelding, youtube-link en alle gebruikte kleuren staan. De kwaliteit van deze data zal hoog liggen, aangezien de kleuren afkomstig zijn van *TwoInchBrush*, een organisatie die per schilderij de kleuren beschikbaar stelt.

  De datasets bevatten de volgende kolommen:
""")

col1, col2 = st.columns(2)

with col1:
  st.markdown("""  
    **FiveThirtyEights dataset**
    - `EPISODE`
    - `TITLE`
    - `APPLE_FRAME`
    - `AURORA_BOREALIS`
    - `BARN`
    - `BEACH`
    - `BOAT`
    - `BRIDGE`
    - `BUILDING`
    - `BUSHES`
    - `CABIN`
    - `CACTUS`
    - `CIRCLE_FRAME`
    - `CIRRUS`
    - `CLIFF`
    - `CLOUDS`
    - `CONIFER`
    - `CUMULUS`
    - `DECIDUOUS`
    - `DIANE_ANDRE`
    - `DOCK`
    - `DOUBLE_OVAL_FRAME`
    - `FARM`
    - `FENCE`
    - `FIRE`
    - `FLORIDA_FRAME`
    - `FLOWERS`
    - `FOG`
    - `FRAMED`
    - `GRASS`
    - `GUEST`
    - `HALF_CIRCLE_FRAME`
    - `HALF_OVAL_FRAME`
    - `HILLS`
    - `LAKE`
    - `LAKES`
    - `LIGHTHOUSE`
    - `MILL`
    - `MOON`
    - `MOUNTAIN`
    - `MOUNTAINS`
    - `NIGHT`
    - `OCEAN`
    - `OVAL_FRAME`
    - `PALM_TREES`
    - `PATH`
    - `PERSON`
    - `PORTRAIT`
    - `RECTANGLE_3D_FRAME`
    - `RECTANGULAR_FRAME`
    - `RIVER`
    - `ROCKS`
    - `SEASHELL_FRAME`
    - `SNOW`
    - `SNOWY_MOUNTAIN`
    - `SPLIT_FRAME`
    - `STEVE_ROSS`
    - `STRUCTURE`
    - `SUN`
    - `TOMB_FRAME`
    - `TREE`
    - `TREES`
    - `TRIPLE_FRAME`
    - `WATERFALL`
    - `WAVES`
    - `WINDMILL`
    - `WINDOW_FRAME`
    - `WINTER`
    - `WOOD_FRAMED`

    Uit deze datset zullen de kolommen `EPISODE` en `TITLE` niet gebruikt worden. De episode staat in de datset van jwilber in een beter formaat (seizoen en aflevering in een aparte kolom). Ook staat in zijn dataset de titel van de aflevering niet in hoofdletters.
  """)

with col2:
  st.markdown("""  
    **Jwilbers dataset**

    | Column | Description | 
    |---|---|
    | `painting_index` | Painting number as enumerated in collection. | 
    | `img_src` | Url path to image. | 
    | `painting_title` |  Title of the painting. | 
    | `season` | Season of 'The Joy of Painting' in which the painting was featured. | 
    | `episode` | Episode of 'The Joy of Painting' in which the painting was featured. | 
    | `num_colors` | Number of unique colors used in the painting. | 
    | `youtube_src` | Youtube video of episode featuring the painting. |
    | `colors` | List of colors used in the painting. | 
    | `colors_hex` | List of colors (hexadecimal code) used in the painting. | 
  """)

  st.markdown('')

  st.markdown("""
      Naast bovenstaande kolommen is er onderscheid gemaakt in de volgende kleuren:

      - `Black_Gesso`
      - `Bright_Red`
      - `Burnt_Umber`
      - `Cadmium_Yellow`
      - `Dark_Sienna`
      - `Indian_Red`
      - `Indian_Yellow`
      - `Liquid_Black`
      - `Liquid_Clear`
      - `Midnight_Black`
      - `Phthalo_Blue`
      - `Phthalo_Green`
      - `Prussian_Blue`
      - `Sap_Green`
      - `Titanium_White`
      - `Van_Dyke_Brown`
      - `Yellow_Ochre`
      - `Alizarin_Crimson`

      Uit deze datset zullen de kolommen `painting_index`, `img_src`, `youtube_src`, `colors` en `color_hex` niet gebruikt worden voor de analyse. De foto en video is lastig te analyseren en de (hex)kleuren zijn in de tabel al in aparte kolommen gegeven.
  """)

st.markdown("Bovenstaande datasets zijn samengevoegd (met uitzondering van de genoemde kolommen) tot de volgende dataframe:")

st.dataframe(df)

st.markdown("""
  Deze dataframe is door middel van de volgende code tot stand gekomen:

  ```python
  def createDataFrame():
    # Fetch csv files
    df_elements = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/bob-ross/elements-by-episode.csv')
    df_paintings = pd.read_csv('https://raw.githubusercontent.com/jwilber/Bob_Ross_Paintings/master/data/bob_ross_paintings.csv')

    # Drop columns
    df_paintings.drop(['painting_index', 'img_src', 'youtube_src' , 'colors', 'color_hex', 'Unnamed: 0'], 1, inplace=True)

    # Return dataframe with joined columns
    return df_paintings.join(df_elements[['APPLE_FRAME', 'AURORA_BOREALIS', 'BARN', 'BEACH', 'BOAT', 'BRIDGE', 'BUILDING', 'BUSHES', 'CABIN', 'CACTUS', 'CIRCLE_FRAME', 'CIRRUS', 'CLIFF', 'CLOUDS', 'CONIFER', 'CUMULUS', 'DECIDUOUS', 'DIANE_ANDRE', 'DOCK', 'DOUBLE_OVAL_FRAME', 'FARM', 'FENCE', 'FIRE', 'FLORIDA_FRAME', 'FLOWERS', 'FOG', 'FRAMED', 'GRASS', 'GUEST', 'HALF_CIRCLE_FRAME', 'HALF_OVAL_FRAME', 'HILLS', 'LAKE', 'LAKES', 'LIGHTHOUSE', 'MILL', 'MOON', 'MOUNTAIN', 'MOUNTAINS', 'NIGHT', 'OCEAN', 'OVAL_FRAME', 'PALM_TREES', 'PATH', 'PERSON', 'PORTRAIT', 'RECTANGLE_3D_FRAME', 'RECTANGULAR_FRAME', 'RIVER', 'ROCKS', 'SEASHELL_FRAME', 'SNOW', 'SNOWY_MOUNTAIN', 'SPLIT_FRAME', 'STEVE_ROSS', 'STRUCTURE', 'SUN', 'TOMB_FRAME', 'TREE', 'TREES', 'TRIPLE_FRAME', 'WATERFALL', 'WAVES', 'WINDMILL', 'WINDOW_FRAME', 'WINTER', 'WOOD_FRAMED']])

  df = createDataFrame()
  ```

""")

# De schilderijen van Bob Ross bevatten heel veel verschillende variabelen. Er zitten bijvoorbeeld veel verschillende kleuren in maar ook een hoop verschillende objecten zoals huizen en bomen. De data set laat veel informatie ook zien over in welke volgorde hij zijn schilderijen heeft gemaakt en in welk seizoen van zijn serie. Met de slider, de checkboxen en het dropdownmenu kan er gefilterd gaan worden op veel verschillende aspecten.

st.markdown("---")

st.markdown("## Filter door de dataset")

st.markdown("Hieronder zijn sliders weergegeven. Doormiddel van de sliders kan je de schilderijen filteren op kleur. Hierdoor kan je de sliders zo instellen dat je uiteindelijk de namen krijgt van de schilderijen met de kleuren die jij graag wilt. Bijvoorbeeld om het goed te laten matchen met je interieur.")

st.markdown("Vervolgens zijn in de tabel alle seizoenen met schilderijen te zien. Ook is hierin af te lezen welke kleuren het schilderij bevat en hoeveel.")

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
  cadmiumYellow = st.checkbox('Cadmium Yellow')
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

if blackGesso:
  df_filtered = df_filtered[df_filtered['Black_Gesso'] == blackGesso]

if brightRed:
  df_filtered = df_filtered[df_filtered['Bright_Red'] == brightRed]

if burntUmber:
  df_filtered = df_filtered[df_filtered['Burnt_Umber'] == burntUmber]

if cadmiumYellow:
  df_filtered = df_filtered[df_filtered['Cadmium_Yellow'] == cadmiumYellow]

if darkSienna:
  df_filtered = df_filtered[df_filtered['Dark_Sienna'] == darkSienna]

if indianRed:
  df_filtered = df_filtered[df_filtered['Indian_Red'] == indianRed]

if indianYellow:
  df_filtered = df_filtered[df_filtered['Indian_Yellow'] == indianYellow]

if liquidBlack:
  df_filtered = df_filtered[df_filtered['Liquid_Black'] == liquidBlack]

if liquidClear:
  df_filtered = df_filtered[df_filtered['Liquid_Clear'] == liquidClear]

if midnightBlack:
  df_filtered = df_filtered[df_filtered['Midnight_Black'] == midnightBlack]

if phthaloBlue:
  df_filtered = df_filtered[df_filtered['Phthalo_Blue'] == phthaloBlue]

if phthaloGreen:
  df_filtered = df_filtered[df_filtered['Phthalo_Green'] == phthaloGreen]

if prussianBlue:
  df_filtered = df_filtered[df_filtered['Prussian_Blue'] == prussianBlue]

if sapGreen:
  df_filtered = df_filtered[df_filtered['Sap_Green'] == sapGreen]

if titaniumWhite:
  df_filtered = df_filtered[df_filtered['Titanium_White'] == titaniumWhite]

if vanDykeBrown:
  df_filtered = df_filtered[df_filtered['Van_Dyke_Brown'] == vanDykeBrown]

if yellowOchre:
  df_filtered = df_filtered[df_filtered['Yellow_Ochre'] == yellowOchre]

if alizarinCrimson:
  df_filtered = df_filtered[df_filtered['Alizarin_Crimson'] == alizarinCrimson]

st.markdown('')
st.markdown('Gefilterde dataframe')

df_filtered

st.markdown('Het is ook mogelijk om van een specifiek schilderij de details in te zien. Gebruik hiervoor de dropdown hieronder.')

col1, col2 = st.columns(2)

with col1:
  season = st.selectbox('Selecteer seizoen', range(1, 32))

with col2:
  episode = st.selectbox('Selecteer schilderij', df[df['season'] == season]['painting_title'])

st.dataframe(df[df['painting_title'] == episode].head())

# st.subheader(episode)
# st.caption(df[df['painting_title'] == episode]['season'])

st.markdown("---")

st.markdown("## Analyse")

st.dataframe(df.describe())

fig = px.histogram(df['num_colors'], title = 'Kleuren en schilderijen in verhouding',color_discrete_map = {'num_colors':'rgb(83, 167, 219)'},
labels = {'value':'Aantal kleuren'})

fig.update_layout(showlegend=False)

st.write(fig)

st.markdown("Het histogram dat te zien is, geeft weer hoeveel schilderijen een bepaald aantal kleur bevat. Uit het histogram is te concluderen dat de meeste schilderijen , namelijk 100 schilderijen, in totaal 12 kleuren bevatten.")

st.markdown("Hieronder is een staafdiagram te zien. Een staafdiagram is een grafiek met allerlei staven. De lengte van deze staven geeft de frequentie weer. In onderstaande staafdiagram valt te zien hoe vaak elke kleur voorkomt in de schilderijen. Dit is uitgedrukt in percentages. Zo is te zien dat Titanium White het meeste gebruikt is, deze kleur komt namelijk in 99,3% van de schilderijen voor.")

fig = px.bar(df[['Black_Gesso','Bright_Red', 'Burnt_Umber', 'Cadmium_Yellow', 'Dark_Sienna', 'Indian_Red', 'Indian_Yellow', 'Liquid_Black', 'Liquid_Clear', 'Midnight_Black', 'Phthalo_Blue', 'Phthalo_Green', 'Prussian_Blue', 'Sap_Green', 'Titanium_White', 'Van_Dyke_Brown', 'Yellow_Ochre', 'Alizarin_Crimson']].mean(), orientation='h', height=500)
st.write(fig)

st.markdown("Naast de verschillende kleuren is het ook interessant om te zien hoe vaak elk element in alle schilderijen voorkomt. Dit is weergegeven in de staafdiagram hieronder. Hier is te zien dat in ongeveer 90% van de schilderijen Bob Ross zijn iconische ‘happy little trees’ te zien zijn.")

fig = px.bar(df[['APPLE_FRAME', 'AURORA_BOREALIS', 'BARN', 'BEACH', 'BOAT', 'BRIDGE', 'BUILDING', 'BUSHES', 'CABIN', 'CACTUS', 'CIRCLE_FRAME', 'CIRRUS', 'CLIFF', 'CLOUDS', 'CONIFER', 'CUMULUS', 'DECIDUOUS', 'DIANE_ANDRE', 'DOCK', 'DOUBLE_OVAL_FRAME', 'FARM', 'FENCE', 'FIRE', 'FLORIDA_FRAME', 'FLOWERS', 'FOG', 'FRAMED', 'GRASS', 'GUEST', 'HALF_CIRCLE_FRAME', 'HALF_OVAL_FRAME', 'HILLS', 'LAKE', 'LAKES', 'LIGHTHOUSE', 'MILL', 'MOON', 'MOUNTAIN', 'MOUNTAINS', 'NIGHT', 'OCEAN', 'OVAL_FRAME', 'PALM_TREES', 'PATH', 'PERSON', 'PORTRAIT', 'RECTANGLE_3D_FRAME', 'RECTANGULAR_FRAME', 'RIVER', 'ROCKS', 'SEASHELL_FRAME', 'SNOW', 'SNOWY_MOUNTAIN', 'SPLIT_FRAME', 'STEVE_ROSS', 'STRUCTURE', 'SUN', 'TOMB_FRAME', 'TREE', 'TREES', 'TRIPLE_FRAME', 'WATERFALL', 'WAVES', 'WINDMILL', 'WINDOW_FRAME', 'WINTER', 'WOOD_FRAMED']].mean(), orientation='h', height=1500)
st.write(fig)