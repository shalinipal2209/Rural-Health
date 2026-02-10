import streamlit as st
st.title("RuralHealth+")
menu= st.sidebar.selectbox(
    "Select Feature",
    ["AI Diagnostics", "Education Hub",
     "Clinic Locator", "Community Forum",
     "Health Tracker"]
    )
if menu == "AI Diagnostics":
    st.header("AI Diagnostics")
    img = st.file_uploader("Upload image")
    if img:
        st.image(img)
        st.success("Possible condition detected(Demo)")
    elif menu == "Education Hub":
        st.header("Education Hub")
        st.write(".Malaria Prevention")
        st.write(".Nutrition Tips")
        st.write(".Child Health")
    elif menu == "Clinic Locator":
        st.header("Clinic Locator")
        place = st.text_input("Enter your location")
        if place:
            st.success("Nearby clinics found (Demo)")
    elif menu == "Community Forum":
        st.header("Community Forum")
        question = st.text_input("Ask your question")
        if question:
            st.write("Community reply: Please consult a doctor.")
    elif menu == "Health Tracker":
        st.header("Health Tracker")
        symptom =
        st.text_input("Symptoms")
        if st.button("Save"):
            st.success("Saved successfully")

 
