import streamlit as st
import sqlite3
from PIL import Image
#comment
def creat_table():
    conn = sqlite3.connect('portfolio.db')
    c = conn.cursor()

    # Create a table to store contact information
    c.execute('''CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT,
                contact TEXT NOT NULL,
                country TEXT,
                message TEXT
            )''')
    conn.commit()
    conn.close()



    
def main(): 


    creat_table()
    st.set_page_config(
      page_title="Welcome to my Portfolio",
      page_icon= "🏠" ,
      layout="wide",
    #initial_sidebar_state="expanded",
    )
    col1, col2 = st.columns([2, 1])
    container = st.container()
    image_my =Image.open("images/myphoto-removebg-preview.png")
    image_scatter = Image.open("scatter.png")
    image_bar = open("C:/Users/tariq computers/Desktop/portfolio/bar.png", "rb").read()
    image_category = open("C:/Users/tariq computers/Desktop/portfolio/category.png", "rb").read()
    image_pai = open("C:/Users/tariq computers/Desktop/portfolio/pai.png", "rb").read()
    image_alipass = open("C:/Users/tariq computers/Desktop/portfolio/alipass.png", "rb").read()
    image_aliui2 = open("C:/Users/tariq computers/Desktop/portfolio/aliui2.png", "rb").read()
    image_aliadd = open("C:/Users/tariq computers/Desktop/portfolio/aliadd.png", "rb").read()
    image_alisearch = open("C:/Users/tariq computers/Desktop/portfolio/alisearch.png", "rb").read()
    image_datahome = open("C:/Users/tariq computers/Desktop/portfolio/datahome.png", "rb").read()
    image_schoolstudent = open("C:/Users/tariq computers/Desktop/portfolio/schoolstudent.png", "rb").read()
    image_schooladdstudent = open("C:/Users/tariq computers/Desktop/portfolio/schoolstudent.png", "rb").read()
    image_dataanalysis = open("C:/Users/tariq computers/Desktop/portfolio/dataanalysis.png", "rb").read()
    image_datafile = open("C:/Users/tariq computers/Desktop/portfolio/datafile.png", "rb").read()
    image_poster = open("C:/Users/tariq computers/Desktop/portfolio/poster.png", "rb").read()

    col2.image(image_my, width=100 )
    col2.write("\n")
    col2.write("\n")
    col2.write("\n")
    col2.write("\n")
    col2.write("\n")
    col2.write("\n")
    col1.title("Welcome to the World of Data Power!")
    col1.markdown("**Where the *possibilities are limitless*, and success awaits those who seize it.**")
    col1.markdown("**Unlock the Future of Business with Tariq Aziz**")
    col1.write("\n")
    
    st.write("---")
    
    col1.subheader("Data is every thing ")
    col1.markdown("Data is the *lifeblood* of the modern business landscape, and in this era of *limitless possibilities*, those who harness its potential hold the keys to success. I am **Tariq Aziz**, a visionary **database creator** and **data analyst**, dedicated to shaping the future of businesses through the art of data manipulation.")
    col1.write("\n")
    col1.write("\n")
    col2.image(image_scatter, width=200 )
    col2.write("\n")
   
    col1.subheader("Data for Prediction")
    col1.markdown("With an unwavering belief that **data is the true power** that drives organizations forward, I have honed my skills in the craft of **data analysis** and **visualization**. Through meticulous examination and interpretation, I transform raw data into *valuable insights* that unveil the hidden opportunities and predict the path to optimal business decisions.")
    col2.write("\n")
    col2.write("\n")
    col2.image(image_bar, width=200 )
    col2.write("\n")
    col1.subheader("Dashboards and UI")
    col1.markdown("One of my specialties lies in crafting captivating **dashboards** and **user-friendly interfaces** that revolutionize the way businesses interact with their data. *Seamlessly blending form and function*, these visually stunning and intuitive interfaces empower stakeholders to navigate complex datasets effortlessly. By distilling complex information into digestible visualizations, I empower decision-makers to grasp critical trends and patterns, leading to agile, data-driven strategies.")
    col1.write("\n")
    col2.write("\n")
    col2.write("\n")
    col2.write("\n")
    col2.write("\n")
    col2.write("\n")
    col2.write("\n")
    col2.write("\n")
    col2.write("\n")
    col2.image(image_schoolstudent, width=200 )
    

    col1.image(image_aliadd, width=500 )
    col2.write("\n")
    col2.image(image_aliui2, width=200 )
    
    col1.subheader("Data Analysis")
    col1.markdown("Beyond dashboard creation, I bring forth a comprehensive skill set encompassing **data cleaning**, **transformation**, and **modeling**. Ensuring the accuracy and integrity of data is my utmost priority, as it forms the *bedrock upon which strategic insights are built*. By meticulously curating and refining data, I guarantee that organizations can confidently rely on the outputs of my analyses for critical decision-making.")
    
    col1.image(image_dataanalysis,width=500)
    col2.write("\n")
    col2.write("\n")
    col2.write("\n")
    col2.write("\n")
    col2.write("\n")
    col2.write("\n")
    col2.write("\n") 
    col2.image(image_datafile)
    col1.write("\n")
    col1.write("\n")
    col1.write("\n")
    col1.write("\n")
    col1.write("\n")
    col1.write("\n")
    col1.write("\n")
    col1.write("\n")
    col1.write("\n")
    col1.write("\n")
    container.write("\n")
    col1.subheader("Data is the Future")
    container.markdown("The future of businesses hinges upon *data mastery*, and with my expertise as a database creator and data analyst, I am here to guide you on this transformative journey. Together, we will unlock the full potential of your organization, navigating the digital landscape with *confidence* and *foresight*.")
    container.image(image_pai,width=500)
    
    container.subheader("Data Partner")
    container.markdown("Whether you seek to optimize operations, understand customer behavior, or stay ahead of the competition, I am your partner in harnessing the true power of data. Let us embark on a *collaborative endeavor* to propel your business into the realm of data-driven success.")
    container.image(image_poster,width=500)
    
    
    st.markdown("Contact me today to experience the unparalleled expertise and insights that will propel your organization towards a *prosperous* and *informed future*.")
    
    st.write("---")
    
    
    st.write("WhatsApp: https://wa.me/3339139164")
    st.write("Email: aionlinebez@gmail.com")

if __name__ == main():
   main()   

