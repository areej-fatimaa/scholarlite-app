import streamlit as st
import requests

st.title("🔍 Research Paper Finder")
st.write("Enter a topic to find relevant academic papers.")

# Input box
query = st.text_input("Enter a research topic:")

if st.button("Search") and query:
    # Call Semantic Scholar API
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,abstract,authors,url"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        papers = data.get("data", [])
        
        st.subheader("📄 Top 5 Papers")
        for i, paper in enumerate(papers):
            st.markdown(f"### {i+1}. [{paper['title']}]({paper['url']})")
            st.markdown(f"*Authors:* {', '.join([a['name'] for a in paper['authors']])}")
            st.markdown(f"**Abstract:** {paper['abstract'] if paper['abstract'] else 'No abstract available.'}")
            st.markdown("---")
    else:
        st.error("Failed to fetch papers from Semantic Scholar.")
