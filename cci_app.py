import streamlit as st
import py_avataaars as pa
from PIL import Image
import base64
from random import randrange

# Introduction
st.header ('**Welcome to my avatar/character creation interface**')
st.markdown ("""
Preview of the avatar and download option (PNG file) can be found below. Customization options can be found on the left side.
""")

# Changing Avatar List Names
pa.FacialHairType.NONE = pa.FacialHairType.DEFAULT
pa.MouthType.HAPPY = pa.FacialHairType.DEFAULT
pa.EyesType.OPEN = pa.EyesType.DEFAULT
pa.AccessoriesType.NONE = pa.AccessoriesType.DEFAULT
pa.TopType.WINTER_HAT_USHANKA = pa.TopType.WINTER_HAT1
pa.TopType.WINTER_HAT_HOLIDAY = pa.TopType.WINTER_HAT2
pa.TopType.WINTER_HAT_BEANIE = pa.TopType.WINTER_HAT3
pa.TopType.WINTER_HAT_BEANIE_EARS = pa.TopType.WINTER_HAT4
pa.TopType.LONG_HAIR_STRAIGHT_WAVY = pa.TopType.LONG_HAIR_STRAIGHT2
pa.TopType.SHORT_HAIR_DREADS_SHORT = pa.TopType.SHORT_HAIR_DREADS_01
pa.TopType.SHORT_HAIR_DREADS_LONG = pa.TopType.SHORT_HAIR_DREADS_02
pa.ClotheColor.BLUE_LIGHT = pa.ClotheColor.BLUE_01
pa.ClotheColor.BLUE_MEDIUM = pa.ClotheColor.BLUE_02
pa.ClotheColor.BLUE_DARK = pa.ClotheColor.BLUE_03
pa.ClotheColor.GRAY_LIGHT = pa.ClotheColor.GRAY_01
pa.ClotheColor.GRAY_DARK = pa.ClotheColor.GRAY_02
pa.AccessoriesType.PRESCRIPTION_WHITE = pa.AccessoriesType.PRESCRIPTION_01
pa.AccessoriesType.PRESCRIPTION_BLACK = pa.AccessoriesType.PRESCRIPTION_02

# Avatar Options Lists
list_background = ['CIRCLE','TRANSPARENT']
list_skin_color = ['BLACK','TANNED','YELLOW','PALE','LIGHT','BROWN','DARK_BROWN']
list_hair_color = ['BLACK','AUBURN','BLONDE','BLONDE_GOLDEN','BROWN','BROWN_DARK','PASTEL_PINK','PLATINUM','RED','SILVER_GRAY']
list_facial_hair_type = ['NONE','BEARD_MEDIUM','BEARD_LIGHT','BEARD_MAJESTIC','MOUSTACHE_FANCY','MOUSTACHE_MAGNUM']
list_facial_hair_color = ['BLACK','BLUE_LIGHT','BLUE_MEDIUM','BLUE_DARK','GRAY_LIGHT','GRAY_DARK','HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE','PASTEL_RED','PASTEL_YELLOW','PINK','RED','WHITE']
list_top_type = ['NO_HAIR','HAT','HIJAB','TURBAN','WINTER_HAT_USHANKA','WINTER_HAT_HOLIDAY','WINTER_HAT_BEANIE','WINTER_HAT_BEANIE_EARS','LONG_HAIR_BIG_HAIR','LONG_HAIR_BOB','LONG_HAIR_BUN',
                 'LONG_HAIR_CURLY','LONG_HAIR_CURVY','LONG_HAIR_DREADS','LONG_HAIR_FRO','LONG_HAIR_FRO_BAND','LONG_HAIR_NOT_TOO_LONG','LONG_HAIR_MIA_WALLACE',
                 'LONG_HAIR_STRAIGHT','LONG_HAIR_STRAIGHT_WAVY','LONG_HAIR_STRAIGHT_STRAND','SHORT_HAIR_DREADS_SHORT','SHORT_HAIR_DREADS_LONG','SHORT_HAIR_FRIZZLE',
                 'SHORT_HAIR_SHAGGY_MULLET','SHORT_HAIR_SHORT_CURLY','SHORT_HAIR_SHORT_FLAT','SHORT_HAIR_SHORT_ROUND','SHORT_HAIR_SHORT_WAVED','SHORT_HAIR_SIDES','SHORT_HAIR_THE_CAESAR','SHORT_HAIR_THE_CAESAR_SIDE_PART']
                 #Removed 'EYE_PATCH' ''LONG_HAIR_SHAVED_SIDES' 'LONG_HAIR_FRIDA'
list_hat_color = ['BLACK','BLUE_LIGHT','BLUE_MEDIUM','BLUE_DARK','GRAY_LIGHT','GRAY_DARK','HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE','PASTEL_RED','PASTEL_YELLOW','PINK','RED','WHITE']
list_mouth_type = ['HAPPY','CONCERNED','DISBELIEF','EATING','GRIMACE','SAD','SCREAM_OPEN','SERIOUS','SMILE','TONGUE','TWINKLE','VOMIT']
list_eye_type = ['OPEN','CLOSE','CRY','DIZZY','EYE_ROLL','HAPPY','HEARTS','SIDE','SQUINT','SURPRISED','WINK','WINK_WACKY']
list_eyebrow_type = ['DEFAULT','DEFAULT_NATURAL','ANGRY','ANGRY_NATURAL','FLAT_NATURAL','RAISED_EXCITED','RAISED_EXCITED_NATURAL','SAD_CONCERNED','SAD_CONCERNED_NATURAL','UNI_BROW_NATURAL','UP_DOWN','UP_DOWN_NATURAL','FROWN_NATURAL']
list_glasses_type = ['NONE','KURT','PRESCRIPTION_WHITE','PRESCRIPTION_BLACK','ROUND','SUNGLASSES','WAYFARERS']
list_clothe_type = ['COLLAR_SWEATER','GRAPHIC_SHIRT','HOODIE','OVERALL','SHIRT_CREW_NECK','SHIRT_SCOOP_NECK','SHIRT_V_NECK']
                    #Rmoved 'BLAZER_SHIRT' 'BLAZER_SWEATER'
list_clothe_color = ['BLACK','BLUE_LIGHT','BLUE_MEDIUM','BLUE_DARK','GRAY_LIGHT','GRAY_DARK','HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE','PASTEL_RED','PASTEL_YELLOW','PINK','RED','WHITE']
list_clothe_graphic_type = ['BAT','CUMBIA','DEER','DIAMOND','HOLA','PIZZA','RESIST','SELENA','BEAR','SKULL_OUTLINE','SKULL']

# Avatar Options
st.sidebar.subheader('Background & Skin')
option_background = st.sidebar.selectbox('Background',list_background)
option_skin_color = st.sidebar.selectbox('Skin Color',list_skin_color)

st.sidebar.subheader('Hairstyle/Hat')
option_top_type = st.sidebar.selectbox('Hairstyle',list_top_type)
option_hair_color = st.sidebar.selectbox('Hair Color (applicable if a hairstyle is selected)',list_hair_color)
option_hat_color = st.sidebar.selectbox('Hat Color (applicable if a hat is selected)',list_hat_color)

st.sidebar.subheader('Face')
option_eyebrow_type = st.sidebar.selectbox('Eyebrow Type',list_eyebrow_type)
option_eye_type = st.sidebar.selectbox('Eye Type',list_eye_type)
option_glasses_type = st.sidebar.selectbox('Glasses',list_glasses_type)
option_mouth_type = st.sidebar.selectbox('Mouth',list_mouth_type)
option_facial_hair_type = st.sidebar.selectbox('Facial Hair Type',list_facial_hair_type)
option_facial_hair_color = st.sidebar.selectbox('Facial Hair Color (applicable if a facial hair is selected)',list_facial_hair_color)

st.sidebar.subheader('Clothe')
option_clothe_type = st.sidebar.selectbox('Clothe',list_clothe_type)
option_clothe_color = st.sidebar.selectbox('Clothe Color',list_clothe_color)
option_clothe_graphic_type = st.sidebar.selectbox('Clothe Graphic (applicable if GRAPHIC_SHIRT is selected)',list_clothe_graphic_type)

st.sidebar.subheader('Sex')
st.sidebar.selectbox('',('Male','Female'))

# Customize Avatar
avatar = pa.PyAvataaar(
    style=eval('pa.AvatarStyle.%s' % option_background),
    skin_color=eval('pa.SkinColor.%s' % option_skin_color),
    hair_color=eval('pa.HairColor.%s' % option_hair_color),
    facial_hair_type=eval('pa.FacialHairType.%s' % option_facial_hair_type),
    facial_hair_color=eval('pa.ClotheColor.%s' % option_facial_hair_color),
    top_type=eval('pa.TopType.%s' % option_top_type),
    hat_color=eval('pa.ClotheColor.%s' % option_hat_color),
    mouth_type=eval('pa.MouthType.%s' % option_mouth_type),
    eye_type=eval('pa.EyesType.%s' % option_eye_type),
    eyebrow_type=eval('pa.EyebrowType.%s' % option_eyebrow_type),
    nose_type=pa.NoseType.DEFAULT,
    accessories_type=eval('pa.AccessoriesType.%s' % option_glasses_type),
    clothe_type=eval('pa.ClotheType.%s' % option_clothe_type),
    clothe_color=eval('pa.ClotheColor.%s' % option_clothe_color),
    clothe_graphic_type=eval('pa.ClotheGraphicType.%s' % option_clothe_graphic_type),
)

# Custom function by dataprofessor for encoding an donwloading avatar image
def imagedownload(filename):
    image_file = open(filename, 'rb')
    b64 = base64.b64encode(image_file.read()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:image/png;base64,{b64}" download={filename}>Download {filename}</a>'
    return href 

st.write('---')
st.subheader('**Avatar Preview**')

# Display Avatar
rendered_avatar = avatar.render_png_file('avatar.png')
image = Image.open('avatar.png')
st.image(image)
st.markdown(imagedownload('avatar.png'), unsafe_allow_html=True)

#st.write('---')

#st.markdown("""
#Credits:
#+ [py-avataars library](https://github.com/kebu/py-avataaars)
#+ Adapted from [Data Professor](https://www.youtube.com/watch?v=4UCfxvURjgI&t) streamlit tutorial series
#""")
