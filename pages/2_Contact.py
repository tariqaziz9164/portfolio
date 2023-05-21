import streamlit as st
import sqlite3


container = st.container()
col1, col2 = st.columns([2, 1])


# Function to insert contact information into the database
def insert_contact(name, email, contact, country, message):
    conn = sqlite3.connect('../portfolio/portfolio.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, email, contact, country, message) VALUES (?, ?, ?, ?, ?)",
              (name, email, contact, country, message))
    conn.commit()
    conn.close()
    st.success("Your message has been submitted!")    

def contact():
    
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
    
contact()        