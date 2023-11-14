import pandas as pd
import numpy as np
import streamlit as st
from fuzzywuzzy import fuzz



st.write("""
         # School and Scholarship Recommender System
        
         Find schools and sholarships in your field of study in 5 secs
        """ )

st.sidebar.header("User input details") 


#st.write(field)



def input_parameters():
    field = st.sidebar.text_input("What field are you looking for a scholarship in?")
    user_specialization = field.lower()
    country = st.sidebar.text_input("What country are you looking for a scholarship in?")
    data = {'Field' : field,
            "country" : country}
    scholarship_df = pd.read_csv('scholarship_df.csv')
    #st.dataframe(scholarship_df)
    # # Convert the 'Area of Specialisation' column in the DataFrame to lowercase for case-insensitive matching
    scholarship_df['Area of specialisation'] = scholarship_df['Area of specialisation'].str.lower()
    # Create a list of specializations from your DataFrame
    specializations = scholarship_df['Area of specialisation'].unique().tolist()
     # Initialize a dictionary to store similarity scores
    similarity_scores = {}

    # Calculate similarity scores between the user's input and specializations
    for spec in specializations:
        similarity_score = fuzz.partial_ratio(user_specialization, spec.lower())
        similarity_scores[spec] = similarity_score

    # Sort specializations by similarity score in descending order
    sorted_specializations = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)

    # Extract matched specializations with a similarity score threshold (e.g., 80)
    threshold = 80  # Adjust as needed
    matched_specializations = [spec for spec, score in sorted_specializations if score >= threshold]

    # Filter scholarships based on matched specializations
    recommended_scholarships = scholarship_df[scholarship_df['Area of specialisation'].isin(matched_specializations)]

    # Remove duplicate scholarships based on their names
    recommended_scholarships = recommended_scholarships.drop_duplicates(subset=['Name'])
    # Check if there are any recommended scholarships
    if recommended_scholarships.empty:
        st.write("Unfortunately, there are no scholarships for your specialization. Try another closely related field or type *All disciplines* for your field on interest.")
    else:
        num_scholarships = len(recommended_scholarships)
        st.write("I have st.write (num_scholarships)suggestions for you in st.write(user_specialization).\n Here are the scholarships/universities to start your search:\n ")
        for index, scholarship in recommended_scholarships.iterrows():
            st.write( scholarship['Name'])
    return field, country,specializations,recommended_scholarships

# Ask the user to enter their area of specialization
#user_specialization = field.lower()

df = input_parameters()


st.write ("""  # What do you do next with this information? 
          """)

st.write ("""  
          - Copy the name of the university or scholarship, paste into Google, add the name of your area of field of interest and the link will pop up.
            - Example : Google "University of Toronto scholarship Planning" to obtain the link and requirements or 
            -  Google : University of Toronto Planning Graduate
        - Read the admission requirements, gather the documents, cold email, pay application fee if neccessary and apply
          """)

