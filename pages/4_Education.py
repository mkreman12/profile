import streamlit as st

st.header("🎓 Education")

with st.container(border=True):
    st.subheader("Master of Science - M.Sc. (Data Science)")
    st.write("##### Chennai Mathematical Institute, Chennai, India")
    st.caption("2023 - 2025")
    st.markdown(
        """
        - Grade: 9.50/10.00
        - Relevant Coursework: Machine Learning, Computer Vision, Text Analytics, Data Structures and Algorithms, SQL.
        - Projects: [Computer Vision Project](https://github.com/mkreman/MCNet-review), [Text Analytics Project](https://github.com/ialok00001/ABSA-Research-Project/tree/main), [Applied Machine Learning Project](https://github.com/mkreman/DL-Audio-Denoising-_AML-Project?tab=readme-ov-file)
        - **Internship at IIT Bhilai:**
            - *ML Fairness on Medical Images*: Created a novel MSGM CNN architecture to reduce fairness (ethnic) issues in ML models. Proposed a new EOM precision Fairness Metric for comprehensive model evaluation.
            - *Action Recognition-based Industrial Safety Violation Detection*: Trained FastRCNN, RetinaNet, and VOLOv9 models on a custom dataset to detect safety equipment and violations. Annotated data with AVA-style annotations for activity detection models.
        """
    )

with st.container(border=True):
    st.subheader("Masters of Mathematics")
    st.write("##### Indian Institute of Technology, Gandhinagar, India")
    st.caption("2019 - 2021")
    st.markdown(
        """
        - Grade: 8.55/10.00
        - Relevant Coursework: Linear Algebra, Real Analysis, Topology, Functional Analysis, Partial Differential Equations, Machine Learning.
        - Projects:
            - *Forensic Detection of Median Filtering Using Traditional Model*: Implemented a classification method from Gang Cao et al. to detect median filtering on image documents. Tools: Python, Jupyter Notebook, OpenCV.
            - *Median Filtering Forensics Based on CNN*: Implemented a CNN from Jiansheng Chen et al. to detect median filtering. Compared conventional and deep learning approaches. Tools: Python, Jupyter Notebook, Tensorflow, Keras, OpenCV, Google Colab.
        """
    )

with st.container(border=True):
    st.subheader("Bachelor of Science")
    st.write("##### Government College of Kota, Rajasthan")
    st.caption("2016 - 2019")
    st.markdown(
        """
        - Grade: 68.85/100.0
        - Relevant Coursework: Linear Algebra, Calculus, Linear Programming, Number Theory, Differential Equations, Real Analysis, Complex Analysis.
        """
    )
