<p align="center">
  <h1 align="center">🔥 Real-Time Fire Detection System</h1>
  <h3 align="center">AI-Based Computer Vision Project Using OpenCV</h3>
</p>

---

## 📌 Project Overview

The **Real-Time Fire Detection System** is an AI-powered computer vision application that detects fire from live webcam video streams.

The system uses image processing and machine learning techniques to:

- 🔴 Detect fire regions in real-time
- 📦 Draw bounding boxes around detected flames
- 🚨 Trigger alerts for safety monitoring
- ⚡ Provide instant visual feedback

This project demonstrates practical implementation of computer vision for industrial and surveillance safety systems.

---

## 🎯 Problem Statement

Fire hazards pose serious threats in:

- Industrial environments  
- Warehouses  
- Forest areas  
- Oil & gas plants  
- Smart cities  

Manual monitoring is inefficient and delayed.

👉 This system automates fire detection using real-time AI-based image processing.

---

# 🛠 Tech Stack

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/>
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
<img src="https://img.shields.io/badge/Computer%20Vision-00C853?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Real--Time%20Detection-1976D2?style=for-the-badge"/>
<img src="https://img.shields.io/badge/AI%20Surveillance-FF5722?style=for-the-badge"/>

</p>

---

## 🏗 System Architecture

```
Webcam Input
      ↓
Frame Capture (OpenCV)
      ↓
Image Preprocessing (HSV Conversion)
      ↓
Fire Detection Algorithm
      ↓
Bounding Box Generation
      ↓
Alert Mechanism (Optional Sound)
      ↓
Live Display Output
```

---

## 📁 Project Structure

```
Real-Time-Fire-Detection/
│
├── models/                  # Detection models (if any)
│
├── notebooks/               # Model training / experimentation
│
├── sounds/                  # Alarm sound files
│
├── src/
│   └── fire_detection.py    # Main detection script
│
├── requirements.txt         # Project dependencies
└── README.md                # Documentation
```

---

## ⚙ How It Works

1️⃣ Captures video feed from webcam  
2️⃣ Converts frame to HSV color space  
3️⃣ Applies fire color threshold detection  
4️⃣ Identifies contours of potential fire regions  
5️⃣ Draws bounding box around detected fire  
6️⃣ Displays real-time detection window  

Press **'q'** to exit.

---

## 🚀 Installation & Setup Guide

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/Real-Time-Fire-Detection.git
cd Real-Time-Fire-Detection
```

---

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 3: Run the Application

```bash
python src/fire_detection.py
```

---

## 🔬 Applications

- 🔥 Industrial Fire Monitoring  
- 🌲 Forest Fire Detection  
- 🏭 Factory Safety Systems  
- 🏢 Smart Building Surveillance  
- 🛢 Oil & Gas Safety Monitoring  

---

## 📊 Key Features

✔ Real-Time Detection  
✔ Lightweight & Fast  
✔ Easy Deployment  
✔ Webcam-Based Monitoring  
✔ Expandable to Deep Learning Models  

---

## 🚀 Future Enhancements

- YOLO-based deep learning fire detection  
- SMS / Email alert integration  
- Cloud-based monitoring dashboard  
- Raspberry Pi edge deployment  
- Multi-camera support  
- Accuracy optimization with CNN  

---

## 👩‍💻 Developed By

**Dipali Mali**  
Computer Science & Engineering  
R C Patel Institute of Technology  

---

## 📄 License

This project is developed for academic and research purposes.

---

<p align="center">
⭐ If you found this project useful, please consider giving it a star!
</p>
