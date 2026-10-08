import streamlit as st


def home_page():
    st.title("⚡ CATS Online Time Series Anomaly Detection")
    st.markdown("##### Real-time Anomaly Detection & Model Evaluation Dashboard")
    st.markdown("---")

    # Overview metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Trained Models", value="16 Experiments")
    with col2:
        st.metric(label="Architectures", value="2 Autoencoders")
    with col3:
        st.metric(label="Sensor Channels", value="17 Features")
    with col4:
        st.metric(label="Streaming Engine", value="Apache Kafka")

    st.markdown("---")

    col_left, col_right = st.columns([3, 2])

    with col_left:
        st.subheader("🎯 Project Overview")
        st.write(
            """
            This application enables interactive exploration and real-time evaluation of sensor telemetry data 
            using **Deep Autoencoder Neural Networks**.
            
            - **Unsupervised Learning**: Learns baseline normal behavior across 17 telemetry features without manual labels.
            - **Real-Time Streaming**: Simulates online data ingestion via **Apache Kafka** streaming pipelines.
            - **Flexible Thresholding**: Analyzes reconstruction loss using configurable error percentiles (90th vs 95th).
            - **Comprehensive Benchmarking**: Compares architectures across optimizers (**Adam** vs **RMSprop**) and training duration (**30** vs **60** epochs).
            """
        )

        st.subheader("🚀 Getting Started")
        st.markdown(
            """
            1. 📖 **About Project**: Learn about the Controlled Anomalies Time Series (CATS) dataset and network architectures.
            2. 💻 **Code**: Review the complete Google Colab notebook for data preprocessing, Kafka setup, and model training.
            3. 📊 **Evaluation**: Interactively compare model performances, loss curves, confusion matrices, and ROC curves.
            4. 📈 **Execution**: Upload custom sensor CSV files, set analysis timeframes, and detect anomalies live.
            """
        )

    with col_right:
        st.subheader("🛠️ System Architecture")
        st.info(
            """
            **Pipeline Workflow**:
            ```text
            [ Sensor Telemetry Data ]
                        │
                        ▼
            [ Apache Kafka Stream ]
                        │
                        ▼
            [ TensorFlow Autoencoder ]
                        │
                        ▼
            [ Reconstruction MSE Loss ]
                        │
                        ▼
            [ Thresholding & Anomaly Alert ]
            ```
            """
        )