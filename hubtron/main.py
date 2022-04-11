import streamlit as st
import mapa.Marvin as page_marvin
import mapa.About as page_about

st.set_page_config(
     page_title="Marvin",
     page_icon="https://cdn0.iconfinder.com/data/icons/monster-14/64/cyborg_halloween_machine_robot_teen_-256.png",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )

############################################################

def main():
    st.sidebar.image('https://ganda.com/wp-content/uploads/2017/05/robot-gif-3-1.gif')

    menu_dict = {
            "Marvin": page_marvin.chamaMarvin,
            "About": page_about.About
            }

    choice = st.sidebar.radio("Menu", menu_dict.keys())

    menu_dict[choice]()


if __name__ == '__main__':
    main()