import streamlit as st


def contact_page():
    st.title("📬 Contact & Project Information")
    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("💡 About this Project")
        st.write(
            """
            This **Online Anomaly Detection System** was developed as part of the **DEPI Course** 
            to benchmark and simulate real-time anomaly detection on time-series telemetry data using 
            **Autoencoder Neural Networks** and **Apache Kafka**.
            """
        )

        st.subheader("👥 Project Maintainers & Contributors")
        st.markdown(
            """
            - **Repository**: [CATS Online Anomaly Detection](https://github.com/salahtarek404/CATS-online-anomaly-detection)
            - **Dataset**: Controlled Anomalies Time Series (CATS)
            - **Technologies**: Python, TensorFlow/Keras, Streamlit, Apache Kafka, Plotly, Pandas
            """
        )

        st.subheader("📩 Get in Touch / Feedback")
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message / Feedback")
            submitted = st.form_submit_button("Send Feedback")
            if submitted:
                if name and email and message:
                    st.success("Thank you for your feedback!")
                else:
                    st.warning("Please fill in all fields before submitting.")

    with col2:
        st.info(
            """
            ### 📌 Quick Links
            - [GitHub Repository](https://github.com/salahtarek404/CATS-online-anomaly-detection)
            - [Streamlit Visualization](https://github.com/salahtarek404/CATS-online-anomaly-detection/tree/main/Streamlit_result_visualization)
            - [Google Colab Notebook](https://github.com/salahtarek404/CATS-online-anomaly-detection/blob/main/AnomalyDetection.ipynb)
            """
        )
