# ECG Arrhythmia Assistant

ECG preprocessing (filtering, R-peaks, HR/HRV), segmenting, and later classification + GPT explanations.

## Setup
```bash
python -m venv venv
# Windows
venv\Scripts\activate
pip install -r requirements.txt

Project Title & Description
Clear and concise — what the project does.

Key Features

ECG processing (filtering, segmentation)

Deep learning model (1D CNN detecting NSR vs PVC)

Class imbalance handling via class weights

Model evaluation metrics

Usage Instructions
How to set up the environment, run the notebooks, train, and test.

Results Summary
Model performance:

NSR: 0.99 precision / 0.90 recall / 0.95 F1
PVC: 0.10 precision / 1.00 recall / 0.17 F1
