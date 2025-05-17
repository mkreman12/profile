import streamlit as st
from PIL import Image


st.set_page_config(page_title="Mayank Nagar", page_icon=":wave:", layout="wide")

st.title("👋 Hi, I'm Mayank Nagar")
st.subheader('Welcome to my personal portfolio!')
st.subheader("Aspiring Data Scientist | AI & Machine Learning Enthusiast | Passionate about AI-driven solutions")

st.write("""
I graduated from CMI with a Master's in Data Science, building on a strong foundation in mathematics and data science and I hold a master's degree in Mathematics from IIT Gandhinagar. 
To know about my education and experience visit the [Education](Education) page.
I am passionate about building fair and efficient machine learning models and exploring the intersection of AI and data science.
""")

# **Education:**  
# I hold an M.Sc. in Data Science (2025) from CMI and an M.Sc. in Mathematics from IIT Gandhinagar.  

# **Experience:**  
# I have worked as an AI Intern at HP and conducted research at IIT Bhilai.  

# Skills
st.header("🧠 Skills")
st.markdown("""
- **Languages:** Python, SQL, R  
- **Libraries:** Pandas, NumPy, Scikit-learn, PyTorch, OpenCV  
- **Tools:** Git, Docker, Streamlit  
- **Other:** Machine Learning, Deep Learning, Data Visualization
""")

# Add social links
st.header("🌐 Connect with me")
st.markdown("""
- [Email](mailto:nmayank1998@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/mayank-nagar-b7448a1b3/)
- [GitHub](https://github.com/mkreman)  
""")