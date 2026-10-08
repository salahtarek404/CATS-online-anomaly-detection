<h1 align="center">⚡ CATS Online Time Series Anomaly Detection</h1>

<p align="center">
  <a href="https://github.com/salahtarek404/CATS-online-anomaly-detection">
    <img src="https://img.shields.io/badge/Python-3.9%2B-blue.svg" alt="Python Version">
  </a>
  <a href="https://tensorflow.org">
    <img src="https://img.shields.io/badge/TensorFlow-2.10%2B-FF6F00.svg" alt="TensorFlow">
  </a>
  <a href="https://streamlit.io">
    <img src="https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg" alt="Streamlit">
  </a>
  <a href="https://kafka.apache.org">
    <img src="https://img.shields.io/badge/Apache%20Kafka-3.7-black.svg" alt="Apache Kafka">
  </a>
</p>

## 📜 Project Description

This repository presents an **Online Time Series Anomaly Detection System** utilizing **Autoencoder Neural Networks** and **Apache Kafka**. The primary goal is to evaluate deep learning autoencoders for real-time anomaly detection using the **Controlled Anomalies Time Series (CATS)** dataset.

A total of **16 different model configurations** were trained and evaluated across various hyperparameters:
- **Architectures**: Deep Autoencoder (Model 1 with 10 hidden layers & Batch Normalization) vs. Lightweight Autoencoder (Model 2 with 5 hidden layers)
- **Optimizers**: `Adam` vs. `RMSprop`
- **Training Epochs**: `30` vs. `60` epochs
- **Threshold Percentiles**: `90th` vs. `95th` percentile reconstruction error

---

## 🛠️ System Architecture & Workflow

```text
┌────────────────────────────────┐
│   Controlled Time Series Data  │ (17 Sensor Telemetry Features)
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│   Apache Kafka Streaming       │ (cats-train & cats-test Topics)
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│   TensorFlow Autoencoder Model │ (Reconstruction of Baseline Signals)
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│   MSE Reconstruction Loss      │ (Calculates Deviation per Timestep)
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│   Thresholding & Visualization │ (Streamlit Dashboard & Plotly Graphs)
└────────────────────────────────┘
```

---

## 🚀 Interactive Streamlit Dashboard

The repository includes a feature-packed Streamlit application to visualize evaluation metrics and perform real-time inference on custom telemetry files.

### Features
1. **Home**: High-level metrics, system architecture summary, and navigation guide.
2. **About Project**: In-depth explanations of the CATS dataset structure, autoencoder theory, and model code.
3. **Code**: Full Google Colab code walkthrough including Kafka cluster setup and stream processing.
4. **Evaluation**: Interactive side-by-side comparative plots (Loss curves, Confusion Matrices, ROC curves) across Architectures, Optimizers, and Percentiles.
5. **Execution**: Upload any sensor telemetry CSV, select time ranges via dynamic sliders, run model inference live, and plot sensor signals with anomaly highlights.
6. **Contact & Info**: Project links, team contact, and feedback form.

---

## 💻 Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/salahtarek404/CATS-online-anomaly-detection.git
cd CATS-online-anomaly-detection
```

### 2. Install Dependencies
```bash
pip install -r Streamlit_result_visualization/requirements.txt
```

### 3. Launch the Streamlit Dashboard
```bash
streamlit run Streamlit_result_visualization/app.py
```

---

## 📁 Repository Structure

```text
.
├── AnomalyDetection.ipynb              # Google Colab notebook for training & Kafka setup
├── ProjectSummary.pptx                 # Project presentation slides
├── README.md                           # Project documentation
├── extract.py                          # PPTX content extraction script
├── extracted_pptx.txt                  # Text contents extracted from slides
└── Streamlit_result_visualization/
    ├── app.py                          # Streamlit application entrypoint
    ├── requirements.txt                # Python dependencies
    ├── TestPrediction.csv              # Sample sensor test dataset
    ├── menu_pages/                     # Dashboard pages
    │   ├── colab_page.py               # Colab code walkthrough page
    │   ├── contact_page.py             # Contact & feedback page
    │   ├── evaluation_page.py          # Model comparative evaluation page
    │   ├── execution_page.py           # Real-time execution & detection page
    │   ├── home_page.py                # Dashboard home page
    │   └── model_page.py               # Model & dataset documentation page
    ├── models/                         # Trained Keras model weights (.h5)
    └── models_info/                    # Training metrics, confusion matrices, & ROC curves
```

---

## 📊 Dataset Information

The **CATS (Controlled Anomalies Time Series)** dataset consists of 17 telemetry sensor features:
`aimp`, `amud`, `arnd`, `asin1`, `asin2`, `adbr`, `adfl`, `bed1`, `bed2`, `bfo1`, `bfo2`, `bso1`, `bso2`, `bso3`, `ced1`, `cfo1`, `cso1`.

---

## 🤝 Contributing & License

Feel free to open issues or submit pull requests to enhance the models or dashboard features.
