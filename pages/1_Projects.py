import streamlit as st
import requests

st.header("🚀 Projects")
# Add static projects
st.markdown("""
### Other Projects
**🔬 Fairness in Disease Classification**  
Developed ML models with fairness constraints to ensure equitable outcomes across ethnic groups.  
*Tools:* PyTorch, FairLearn

**🦺 PPE Detection in Industrial Settings**  
Built a real-time computer vision system to detect PPE and improve worker safety.  
*Tools:* YOLOv5, OpenCV
""")

# Fetch public repositories from GitHub
response = requests.get(f"https://api.github.com/users/mkreman/repos")
if response.status_code == 200:
    repos = response.json()
    if repos:
        repos = sorted(repos, key=lambda repo: repo['updated_at'], reverse=True)
        st.markdown("### Projects on GitHub")
        for repo in repos:
            with st.container(border=True):
                st.markdown(f"""
                #### [{repo['name']}]({repo['html_url']})  
                {repo['description'] if repo['description'] else 'No description provided.'}  
                *Language:* {repo['language'] if repo['language'] else 'Not specified'}  
                *Topics:* {', '.join(repo['topics']) if repo['topics'] else 'No topics specified'}
                """)
    else:
        st.write("No public repositories found.")
else:
    st.error("Failed to fetch repositories from GitHub. Please check your username or try again later.")
