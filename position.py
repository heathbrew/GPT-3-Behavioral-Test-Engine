import openai
import os

api_key = os.environ["OPENAI_API_KEY"] = "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"
if api_key is None:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

import openai
import streamlit as st

# Create a function that generates a response to a user's query
def generate_response(prompt,length):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        # engine="davinci", 	
        prompt= "<|endoftext|>"+ prompt +"\n--\nLabel:",
        # max_tokens=687,
        max_tokens= int(length * 4.737),
        temperature=0.7,
        top_p=0.9
        #0.22,0.83 , 63 stop
        # 0.22,0.91, 70 - stop
    )
    return response["choices"][0]["text"]
    # return response




# Create a Streamlit app
st.set_page_config(page_title="GPT-3 Search Engine", page_icon=":mag_right:", layout="wide")

# # Create a text input for the user's query
# query = st.text_input("Enter your query:")

# Create a text box input for the user's query
position = st.text_input("Enter your Job role:")
tests = st.text_area("Enter your tests:", "", key='query', height=200)
sum = st.text_input("Enter sum of percentages")
part1 = f"Give consideration as per Job relevancece Sort the behavioral tests given below by assigning them percentages which sum up to 100 in descending order for a person working as a {position}.\n Only answer to sum percentages assigned to behavioral tests reaches {sum}, then stop assigning any more percentages or behavioral tests."
part2 = f"Note: These percentages are based on my understanding of the skills that are typically important for a {position} role and may vary depending on the specific job requirements and the company culture. \nAdditionally, some of the behavioral tests given may overlap with others and thus could be  grouped together but try to weigh them indivisually while sorting also give sum of percentages at the end"
# Generate a response to the user's query and display it
if st.button("Find") and position and tests:
    part3 = tests.split("\n")
    query = part1 + "\n" + str(part3) + "\n" + part2
    print(len(part3))

    response = generate_response(query,len(part3))
    st.write("Results:")
    st.write(response)
