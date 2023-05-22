import streamlit as st
import sqlite3
from PIL import Image
import webbrowser
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

# Function to insert contact information into the database
def insert_contact(name, email, contact, country, message):
    conn = sqlite3.connect('../portfolio/portfolio.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, email, contact, country, message) VALUES (?, ?, ?, ?, ?)",
              (name, email, contact, country, message))
    conn.commit()
    conn.close()
    st.success("Your message has been submitted!")    


    
def main(): 

    st.set_page_config(
    page_title="Welcome to my Portfolio",
    page_icon= "🏠" ,
    layout="wide")

    creat_table()
    container = st.container()
    col1, col2 = st.columns([2, 1])
    placeholder = st.empty() 

    image_my =Image.open("images/myphoto-removebg-preview.png")
    image_scatter = Image.open("images/scatter.png")
    image_bar = Image.open("images/bar.png")
    image_category = Image.open("images/category.png")
    image_pai = Image.open("images/pai.png")
    image_alipass = Image.open("images/alipass.png")
    image_aliui2 = Image.open("images/aliui2.png")
    image_aliadd = Image.open("images/aliadd.png")
    image_alisearch = Image.open("images/alisearch.png")
    image_datahome = Image.open("images/datahome.png")
    image_schoolstudent = Image.open("images/schoolstudent.png")
    image_schooladdstudent = Image.open("images/schoolstudent.png")
    image_dataanalysis = Image.open("images/dataanalysis.png")
    image_datafile = Image.open("images/datafile.png")
    image_poster = Image.open("images/poster.png")   


    image_school = Image.open("images/school.png")
    image_chart = Image.open("images/chart.png")
    image_tailor = Image.open("images/tailor.png")
    
    menu = ["Home","Projects","Contact"]
    options = st.sidebar.radio("Pages",menu)
    
    if options == "Home":
        


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
        col2.write("\n")
        col2.write("\n")
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
        
        
        col2.image(image_schoolstudent, width=200 )
    

        col1.image(image_aliadd, width=500 )
        col2.write("\n")
        col2.write("\n")
        col2.write("\n")
        col2.image(image_aliui2, width=200 )
    
        col1.subheader("Data Analysis")
        col1.markdown("Beyond dashboard creation, I bring forth a comprehensive skill set encompassing **data cleaning**, **transformation**, and **modeling**. Ensuring the accuracy and integrity of data is my utmost priority, as it forms the *bedrock upon which strategic insights are built*. By meticulously curating and refining data, I guarantee that organizations can confidently rely on the outputs of my analyses for critical decision-making.")
    
        col1.image(image_dataanalysis,width=500)
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
      
        
        col1.subheader("Data is the Future")
        
        col1.markdown("The future of businesses hinges upon *data mastery*, and with my expertise as a database creator and data analyst, I am here to guide you on this transformative journey. Together, we will unlock the full potential of your organization, navigating the digital landscape with *confidence* and *foresight*.")
        col2.write("\n")
        col2.write("\n")
        col1.image(image_pai,width=300)
    
        col1.subheader("Data Partner")
        col1.markdown("Whether you seek to optimize operations, understand customer behavior, or stay ahead of the competition, I am your partner in harnessing the true power of data. Let us embark on a *collaborative endeavor* to propel your business into the realm of data-driven success.")
        col1.image(image_poster,width=300)
    
    
        st.markdown("Contact me today to experience the unparalleled expertise and insights that will propel your organization towards a *prosperous* and *informed future*.")
    
        st.write("---")
    
    
        st.write("WhatsApp: https://wa.me/3339139164")
        st.write("Email: aionlinebez@gmail.com")


    elif options == "Projects":






        container.header("My Projects")

        container.markdown("### Welcome to my project showcase! Here, I present three remarkable projects that highlight my expertise. ")
    
        container.write("---")

        col1.text("\n ")
        col1.text("\n ")
        col1.text("\n ")
        col1.text("\n ")

        col1.subheader("School management system")
        if col1.button("Visit Project", key = "btn_school"):
            webbrowser.open_new_tab("https://school.streamlit.app/")
        col2.image(image_school, width=200 )    

        col1.text("\n ")
        col1.text("\n ")
        col1.text("\n ")
        col1.text("\n ")
        col1.text("\n ")
        col1.text("\n ")


        col1.subheader("Tailor Shope Management system")
        if col1.button("Visit Project",key = "btn_tailor"):
            webbrowser.open_new_tab("https://alishop.streamlit.app/")
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
            webbrowser.open_new_tab("https://datavisualizatio.streamlit.app/")
        col2.image(image_chart, width=200 )
        st.write("---")
    
        st.markdown("""I am proud of the impact these projects have had on my clients' businesses.
        If you would like to learn more about these projects or discuss how I can assist you in leveraging the power of data for your business success,
        feel free to reach out to me. """)
        st.markdown("**contact: 00923339139164**")
        st.markdown("WhatsApp: https://wa.me/3339139164")
        st.markdown("**Email: aionlinebez@gmail.com**")

    elif options == "Contact":
        container.title("Contact Me")
    
        col1.write("Fill out the form below to get in touch:")
        col2.write("WhatsApp: 00923339139164")
        col2.write("Email: aionlinebez@gmail.com")

        # Form for collecting user information
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        contact = st.text_input("Mobile Number")
        country = st.text_input("Country")
        message = st.text_input("Your Message")

        if st.button("Submit"):
            if not name or not contact :
                 st.warning("Please fill in Name and Contact fields.")
        
            elif len (contact) < 10:
                st.warning("Please enter a valid contact")    
                     
            else:         
                insert_contact(name, email, contact, country, message)       

if __name__ == main():
   main()   

