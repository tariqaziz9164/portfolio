import streamlit as st
import webbrowser


# Set page configuration
st.set_page_config(
    page_title="Projects",
    page_icon=":memo:",
    layout="wide"
)
container = st.container()
col1, col2 = st.columns([2, 1])
placeholder = st.empty()


image_school = open("C:/Users/tariq computers/Desktop/portfolio/pages/school.png", "rb").read()
image_chart = open("C:/Users/tariq computers/Desktop/portfolio/pages/chart.png", "rb").read()
image_tailor = open("C:/Users/tariq computers/Desktop/portfolio/pages/tailor.png", "rb").read()


container.header("My Projects")

container.markdown("### Welcome to my project showcase! Here, I present three remarkable projects that highlight my expertise. ")
    
container.write("---")

col1.text("\n ")
col1.text("\n ")
col1.text("\n ")
col1.text("\n ")

col1.subheader("School management system")
if col1.button("Visit Project", key = "btn_school"):
    webbrowser.open_new_tab("https://tariqaziz9164-schooldatabase-app-rhwbfo.streamlit.app/")
col2.image(image_school, width=200 )    

col1.text("\n ")
col1.text("\n ")
col1.text("\n ")
col1.text("\n ")
col1.text("\n ")
col1.text("\n ")


col1.subheader("Tailor Shope Management system")
if col1.button("Visit Project",key = "btn_tailor"):
    webbrowser.open_new_tab("https://tariqaziz9164-ali-app-wf3q69.streamlit.app/")
col2.image(image_tailor, width=200 )


col2.text(" \n")
col1.text("\n ")
col1.text("\n ")
col1.text("\n ")
col1.text("\n ")
col1.text("\n ")
col1.text("\n ")
col1.text("\n ")
col1.text("\n ")
col1.subheader("Data Analysis and Visualization")
if col1.button("Visit Project",key = "btn_analysis"):
    webbrowser.open_new_tab("https://tariqaziz9164-streamlit-app-fzs00a.streamlit.app/")
col2.image(image_chart, width=200 )
st.write("---")
    
st.markdown("""I am proud of the impact these projects have had on my clients' businesses.
 If you would like to learn more about these projects or discuss how I can assist you in leveraging the power of data for your business success,
  feel free to reach out to me. """)
st.markdown("**contact: 00923339139164**")
st.markdown("WhatsApp: https://wa.me/3339139164")
st.markdown("**Email: aionlinebez@gmail.com**")
