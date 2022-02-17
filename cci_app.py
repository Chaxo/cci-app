import streamlit as st
import py_avataaars as pa
from PIL import Image
import base64
import random

# Introduction
st.header ('Welcome to this avatar customization application')
st.markdown ("""
Preview of the avatar and download option (PNG file) can be found below. Customization options can be found on the left side.""")
st.markdown("If you encounter any errors, try selecting another option to resolve it. Otherwise, refresh the page.")

# Change Avatar List Names
# Background
pa.AvatarStyle.Circle = pa.AvatarStyle.CIRCLE
pa.AvatarStyle.Transparent = pa.AvatarStyle.TRANSPARENT
# Skin Color
pa.SkinColor.Black = pa.SkinColor.BLACK
pa.SkinColor.Tanned = pa.SkinColor.TANNED
pa.SkinColor.Yellow = pa.SkinColor.YELLOW
pa.SkinColor.Pale = pa.SkinColor.PALE
pa.SkinColor.Light = pa.SkinColor.LIGHT
pa.SkinColor.Brown = pa.SkinColor.BROWN
pa.SkinColor.Dark_Brown = pa.SkinColor.DARK_BROWN
# Hair Color
pa.HairColor.Black = pa.HairColor.BLACK
pa.HairColor.Auburn = pa.HairColor.AUBURN
pa.HairColor.Blonde = pa.HairColor.BLONDE
pa.HairColor.Blonde_Golden = pa.HairColor.BLONDE_GOLDEN
pa.HairColor.Brown = pa.HairColor.BROWN
pa.HairColor.Brown_Dark = pa.HairColor.BROWN_DARK
pa.HairColor.Pastel_Pink = pa.HairColor.PASTEL_PINK
pa.HairColor.Platinum = pa.HairColor.PLATINUM
pa.HairColor.Red = pa.HairColor.RED
pa.HairColor.Silver_Gray = pa.HairColor.SILVER_GRAY
# Facial Hair
pa.FacialHairType.Default = pa.FacialHairType.DEFAULT
pa.FacialHairType.Medium = pa.FacialHairType.BEARD_MEDIUM
pa.FacialHairType.Light = pa.FacialHairType.BEARD_LIGHT
pa.FacialHairType.Majestic = pa.FacialHairType.BEARD_MAJESTIC
pa.FacialHairType.Moustache_Fancy = pa.FacialHairType.MOUSTACHE_FANCY
pa.FacialHairType.Moustache_Magnum = pa.FacialHairType.MOUSTACHE_MAGNUM
# Facial Hair + Hat + Clothe Color
pa.ClotheColor.Black = pa.ClotheColor.BLACK
pa.ClotheColor.Blue_Light = pa.ClotheColor.BLUE_01
pa.ClotheColor.Blue_Medium = pa.ClotheColor.BLUE_02
pa.ClotheColor.Blue_Dark = pa.ClotheColor.BLUE_03
pa.ClotheColor.Gray_Light = pa.ClotheColor.GRAY_01
pa.ClotheColor.Gray_Dark = pa.ClotheColor.GRAY_02
pa.ClotheColor.Heather = pa.ClotheColor.HEATHER
pa.ClotheColor.Pastel_Blue = pa.ClotheColor.PASTEL_BLUE
pa.ClotheColor.Pastel_Green = pa.ClotheColor.PASTEL_GREEN
pa.ClotheColor.Pastel_Orange = pa.ClotheColor.PASTEL_ORANGE
pa.ClotheColor.Pastel_Red = pa.ClotheColor.PASTEL_RED
pa.ClotheColor.Pastel_Yellow = pa.ClotheColor.PASTEL_YELLOW
pa.ClotheColor.Pink = pa.ClotheColor.PINK
pa.ClotheColor.Red = pa.ClotheColor.RED
pa.ClotheColor.White = pa.ClotheColor.WHITE
# Top/Hairstyle
pa.TopType.Bald_1 = pa.TopType.NO_HAIR
pa.TopType.Bald_2 = pa.TopType.SHORT_HAIR_SIDES
pa.TopType.Hat = pa.TopType.HAT
pa.TopType.Hijab = pa.TopType.HIJAB
pa.TopType.Turban = pa.TopType.TURBAN
pa.TopType.Winter_Hat_1 = pa.TopType.WINTER_HAT1
pa.TopType.Winter_Hat_2 = pa.TopType.WINTER_HAT2
pa.TopType.Winter_Hat_3 = pa.TopType.WINTER_HAT3
pa.TopType.Winter_Hat_4 = pa.TopType.WINTER_HAT4
pa.TopType.Long_Big = pa.TopType.LONG_HAIR_BIG_HAIR
pa.TopType.Long_Bob = pa.TopType.LONG_HAIR_BOB
pa.TopType.Long_Curly = pa.TopType.LONG_HAIR_CURLY
pa.TopType.Long_Curvy = pa.TopType.LONG_HAIR_CURVY
pa.TopType.Long_Dreads = pa.TopType.LONG_HAIR_DREADS
pa.TopType.Long_Fro = pa.TopType.LONG_HAIR_FRO
pa.TopType.Long_Fro_Band = pa.TopType.LONG_HAIR_FRO_BAND
pa.TopType.Long_Straight = pa.TopType.LONG_HAIR_STRAIGHT
pa.TopType.Long_Straight_Wavy = pa.TopType.LONG_HAIR_STRAIGHT2
pa.TopType.Long_Straight_Strand = pa.TopType.LONG_HAIR_STRAIGHT_STRAND
pa.TopType.Medium = pa.TopType.LONG_HAIR_NOT_TOO_LONG
pa.TopType.Medium_Dreads = pa.TopType.SHORT_HAIR_DREADS_02
pa.TopType.Bun = pa.TopType.LONG_HAIR_BUN
pa.TopType.Mia_Wallace = pa.TopType.LONG_HAIR_MIA_WALLACE
pa.TopType.Short_Dreads = pa.TopType.SHORT_HAIR_DREADS_01
pa.TopType.Short_Frizzle = pa.TopType.SHORT_HAIR_FRIZZLE
pa.TopType.Short_Mullet = pa.TopType.SHORT_HAIR_SHAGGY_MULLET
pa.TopType.Short_Curly = pa.TopType.SHORT_HAIR_SHORT_CURLY
pa.TopType.Short_Flat = pa.TopType.SHORT_HAIR_SHORT_FLAT
pa.TopType.Short_Round = pa.TopType.SHORT_HAIR_SHORT_ROUND
pa.TopType.Short_Waved = pa.TopType.SHORT_HAIR_SHORT_WAVED
pa.TopType.Short_Caesar_1 = pa.TopType.SHORT_HAIR_THE_CAESAR
pa.TopType.Short_Caesar_2 = pa.TopType.SHORT_HAIR_THE_CAESAR_SIDE_PART
# Mouth
pa.MouthType.Happy = pa.FacialHairType.DEFAULT
pa.MouthType.Concerned = pa.MouthType.CONCERNED
pa.MouthType.Disbelief = pa.MouthType.DISBELIEF
pa.MouthType.Eating = pa.MouthType.EATING
pa.MouthType.Grimace = pa.MouthType.GRIMACE
pa.MouthType.Sad = pa.MouthType.SAD
pa.MouthType.Shocked = pa.MouthType.SCREAM_OPEN
pa.MouthType.Serious = pa.MouthType.SERIOUS
pa.MouthType.Smile = pa.MouthType.SMILE
pa.MouthType.Tongue = pa.MouthType.TONGUE
pa.MouthType.Twinkle = pa.MouthType.TWINKLE
pa.MouthType.Vomit = pa.MouthType.VOMIT
# Eye
pa.EyesType.Open = pa.EyesType.DEFAULT
pa.EyesType.Close = pa.EyesType.CLOSE
pa.EyesType.Cry = pa.EyesType.CRY
pa.EyesType.Dizzy = pa.EyesType.DIZZY
pa.EyesType.Eye_Roll = pa.EyesType.EYE_ROLL
pa.EyesType.Happy = pa.EyesType.HAPPY
pa.EyesType.Hearts = pa.EyesType.HEARTS
pa.EyesType.Side = pa.EyesType.SIDE
pa.EyesType.Squint = pa.EyesType.SQUINT
pa.EyesType.Surprised = pa.EyesType.SURPRISED
pa.EyesType.Wink_1 = pa.EyesType.WINK
pa.EyesType.Wink_2 = pa.EyesType.WINK_WACKY
# Eyebrows
pa.EyebrowType.Happy_1 = pa.EyebrowType.DEFAULT
pa.EyebrowType.Happy_2 = pa.EyebrowType.DEFAULT_NATURAL
pa.EyebrowType.Angry_1 = pa.EyebrowType.ANGRY
pa.EyebrowType.Angry_2 = pa.EyebrowType.ANGRY_NATURAL
pa.EyebrowType.Flat = pa.EyebrowType.FLAT_NATURAL
pa.EyebrowType.Excited_1 = pa.EyebrowType.RAISED_EXCITED
pa.EyebrowType.Excited_2 = pa.EyebrowType.RAISED_EXCITED_NATURAL
pa.EyebrowType.Sad_1 = pa.EyebrowType.SAD_CONCERNED
pa.EyebrowType.Sad_2 = pa.EyebrowType.SAD_CONCERNED_NATURAL
pa.EyebrowType.Sad_3 = pa.EyebrowType.FROWN_NATURAL
pa.EyebrowType.Unibrow = pa.EyebrowType.UNI_BROW_NATURAL
pa.EyebrowType.Confused_1 = pa.EyebrowType.UP_DOWN
pa.EyebrowType.Confused_2 = pa.EyebrowType.UP_DOWN_NATURAL
# Glasses
pa.AccessoriesType.Default = pa.AccessoriesType.DEFAULT
pa.AccessoriesType.Kurt = pa.AccessoriesType.KURT
pa.AccessoriesType.Square_White = pa.AccessoriesType.PRESCRIPTION_01
pa.AccessoriesType.Square_Black = pa.AccessoriesType.PRESCRIPTION_02
pa.AccessoriesType.Round = pa.AccessoriesType.ROUND
pa.AccessoriesType.Sunglasses = pa.AccessoriesType.SUNGLASSES
pa.AccessoriesType.Wayfarers = pa.AccessoriesType.WAYFARERS
# Clothe
pa.ClotheType.Collar_Sweater = pa.ClotheType.COLLAR_SWEATER
pa.ClotheType.Graphic_Shirt = pa.ClotheType.GRAPHIC_SHIRT
pa.ClotheType.Hoodie = pa.ClotheType.HOODIE
pa.ClotheType.Shirt_Crew = pa.ClotheType.SHIRT_CREW_NECK
pa.ClotheType.Shirt_Scoop = pa.ClotheType.SHIRT_SCOOP_NECK
pa.ClotheType.Shirt_V_Neck = pa.ClotheType.SHIRT_V_NECK
# Clothe Graphic
pa.ClotheGraphicType.Bat = pa.ClotheGraphicType.BAT
pa.ClotheGraphicType.Deer = pa.ClotheGraphicType.DEER
pa.ClotheGraphicType.Diamond = pa.ClotheGraphicType.DIAMOND
pa.ClotheGraphicType.Hola = pa.ClotheGraphicType.HOLA
pa.ClotheGraphicType.Pizza = pa.ClotheGraphicType.PIZZA
pa.ClotheGraphicType.Bear = pa.ClotheGraphicType.BEAR
pa.ClotheGraphicType.Skull_1 = pa.ClotheGraphicType.SKULL
pa.ClotheGraphicType.Skull_2 = pa.ClotheGraphicType.SKULL_OUTLINE


# Avatar Options Lists
list_background = ['Circle','Transparent']
list_skin_color = ['Pale','Tanned','Yellow','Black','Light','Brown','Dark_Brown']
list_hair_color = ['Blonde','Auburn','Black','Blonde_Golden','Brown','Brown_Dark','Pastel_Pink','Platinum','Red','Silver_Gray']
list_facial_hair_type = ['Default','Light','Medium','Majestic','Moustache_Fancy','Moustache_Magnum']
list_facial_hair_color = ['Black','Blue_Light','Blue_Medium','Blue_Dark','Gray_Light','Gray_Dark','Heather','Pastel_Blue','Pastel_Green','Pastel_Orange','Pastel_Red','Pastel_Yellow','Pink','Red','White']
list_hat_color = ['Black','Blue_Light','Blue_Medium','Blue_Dark','Gray_Light','Gray_Dark','Heather','Pastel_Blue','Pastel_Green','Pastel_Orange','Pastel_Red','Pastel_Yellow','Pink','Red','White']
list_clothe_color = ['Black','Blue_Light','Blue_Medium','Blue_Dark','Gray_Light','Gray_Dark','Heather','Pastel_Blue','Pastel_Green','Pastel_Orange','Pastel_Red','Pastel_Yellow','Pink','Red','White']
list_top_type = ['Bald_1','Bald_2','Hat','Hijab','Turban','Winter_Hat_1','Winter_Hat_2','Winter_Hat_3','Winter_Hat_4','Long_Big','Long_Bob','Long_Curly','Long_Curvy','Long_Dreads','Long_Fro','Long_Fro_Band','Long_Straight',
                    'Long_Straight_Wavy','Long_Straight_Strand','Medium','Medium_Dreads','Bun','Mia_Wallace','Short_Dreads','Short_Frizzle','Short_Mullet','Short_Curly','Short_Flat','Short_Round','Short_Waved',
                    'Short_Caesar_1','Short_Caesar_2']
                 #Removed 'EYE_PATCH' ''LONG_HAIR_SHAVED_SIDES' 'LONG_HAIR_FRIDA'
list_mouth_type = ['Happy','Concerned','Disbelief','Eating','Grimace','Sad','Shocked','Serious','Smile','Tongue','Twinkle','Vomit']
list_eye_type = ['Open','Close','Cry','Dizzy','Eye_Roll','Happy','Hearts','Side','Squint','Surprised','Wink_1','Wink_2']
list_eyebrow_type = ['Happy_1','Happy_2','Angry_1','Angry_2','Flat','Excited_1','Excited_2','Sad_1','Sad_2','Sad_3','Unibrow','Confused_1','Confused_2']
list_glasses_type = ['Default','Kurt','Square_White','Square_Black','Round','Sunglasses','Wayfarers']
list_clothe_type = ['Hoodie','Collar_Sweater','Graphic_Shirt','Shirt_Crew','Shirt_Scoop','Shirt_V_Neck']
                    #Rmoved 'BLAZER_SHIRT' 'BLAZER_SWEATER' 'Overall'
list_clothe_graphic_type = ['Bat','Deer','Diamond','Hola','Pizza','Bear','Skull_1','Skull_2']

# Avatar Options
# The order and title can be changed here
st.sidebar.subheader('Background & Skin')
option_background = st.sidebar.selectbox('Background',list_background)
option_skin_color = st.sidebar.selectbox('Skin Color',list_skin_color)

st.sidebar.subheader('Hairstyle/Hat')
option_top_type = st.sidebar.selectbox('Hairstyle',list_top_type,index=27)
option_hair_color = st.sidebar.selectbox('Hair Color (applicable if a hairstyle is selected)',list_hair_color)
option_hat_color = st.sidebar.selectbox('Hat Color (applicable if a hat is selected)',list_hat_color)

st.sidebar.subheader('Face')
option_eyebrow_type = st.sidebar.selectbox('Eyebrow Type',list_eyebrow_type)
option_eye_type = st.sidebar.selectbox('Eye Type',list_eye_type)
option_glasses_type = st.sidebar.selectbox('Glasses',list_glasses_type)
option_mouth_type = st.sidebar.selectbox('Mouth',list_mouth_type,index=8)
option_facial_hair_type = st.sidebar.selectbox('Facial Hair Type',list_facial_hair_type)
option_facial_hair_color = st.sidebar.selectbox('Facial Hair Color (applicable if a facial hair is selected)',list_facial_hair_color)

st.sidebar.subheader('Clothing')
option_clothe_type = st.sidebar.selectbox('Clothing',list_clothe_type)
option_clothe_color = st.sidebar.selectbox('Clothing Color',list_clothe_color)
option_clothe_graphic_type = st.sidebar.selectbox('Clothing Graphic (applicable if GRAPHIC_SHIRT is selected)',list_clothe_graphic_type)

st.sidebar.subheader('Gender')
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

# Link can be changed
link = '[Click here to go back to survey](http://github.com)'
st.markdown(link, unsafe_allow_html=True)

#st.markdown("""
#Credits:
#+ [py-avataars library](https://github.com/kebu/py-avataaars)
#+ Adapted from [Data Professor](https://www.youtube.com/watch?v=4UCfxvURjgI&t) streamlit tutorial series
#""")
