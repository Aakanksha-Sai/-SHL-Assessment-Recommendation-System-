import streamlit as st
from recommend import recommend  # This is your recommend function

st.title("SHL Assessment Recommendation System")

query = st.text_area("Enter job description or query:")

if st.button("Recommend"):
    results = recommend(query)
    if not results.empty:
        st.write("### Top Recommendations")
        st.dataframe(results[['Assessment Name', 'URL', 'Remote Testing Support', 'Adaptive/IRT Support', 'Duration', 'Test Type']])
    else:
        st.write("No recommendations found.")
