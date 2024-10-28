# Consumer Complaints Project 🌍

**Demo Available**: [Watch the Project Walkthrough](https://vimeo.com/940595873?share=copy)

---

## Table of Contents 📑

- [Overview](#overview)
- [Core Objectives](#core-objectives)
- [Tech Stack](#tech-stack)
- [Quick Start Guide](#quick-start-guide)
  - [Requirements](#requirements)
  - [Installation](#installation)
- [Key Project Phases](#key-project-phases)
- [Files and Directory Structure](#files-and-directory-structure)

---

## Overview

This project dives into a comprehensive analysis of consumer complaints, leveraging a rich dataset from the Consumer Financial Protection Bureau (CFPB) that includes over 2.3 million records. By studying narratives and metadata across various categories, the project aims to extract insights on complaint trends, geographical patterns, and the effectiveness of complaint resolutions. Through this analysis, we aim to highlight improvement areas for enhanced customer satisfaction within the financial sector.

---

## Core Objectives 🎯

1. **Insights for Internal Optimization**  
   - Pinpoint sources of complaints and route insights to relevant teams to help reduce complaint volume.
   - Evaluate the sentiment tied to complaint types, which enables prioritization of high-impact issues.

2. **Identifying Common Themes**  
   - Apply topic modelling to detect and track recurring themes, with a focus on emerging consumer issues.

3. **Understanding Text Complexity and Outcomes**  
   - Analyze the readability of complaint narratives to explore its relationship with the likelihood of resolution.

4. **Geographical Patterns**  
   - Segment complaint data by region to uncover location-based trends and unique issues faced by consumers in different areas.

5. **Predictive Analysis**  
   - Build predictive models to forecast resolution outcomes based on complaint narratives and metadata.

6. **Benchmarking for Comparison**  
   - Compare complaint handling across companies and product types, identifying those associated with the highest dissatisfaction rates.

---

## Tech Stack 🧰

The project leverages Python's data analysis and machine learning ecosystem:

- **Pandas**: Data handling and manipulation.
- **NLTK & SpaCy**: Natural language processing for text analysis.
- **Scikit-Learn**: Machine learning algorithms and feature engineering.
- **Flask**: Framework for deploying the predictive model as a web app.

---

## Quick Start Guide

### Requirements

To set up this project, ensure you have Python installed. Install dependencies with:

```bash
pip install -r requirements.txt
```

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/consumer-complaints.git
   ```
2. **Navigate to the Directory:**
   ```bash
   cd consumer-complaints
   ```
3. **Run the Flask App:**
   ```bash
   python web_app.py
   ```

To work with the Jupyter notebooks for data exploration and model training:

```bash
jupyter notebook
```

---

## Key Project Phases 🧩

- **Data Preparation and Cleaning**
  - Merge datasets, handle missing values, and perform data balancing.
  - Generate relevant features to maximize the dataset's analytical potential.

- **Root Cause & Sentiment Analysis**
  - Investigate major complaint drivers and map them to sentiment scores for effective prioritization.

- **Topic Modelling and Readability Insights**
  - Apply NLP techniques to uncover common complaint themes and evaluate text complexity.

- **Geographic Insights**
  - Use regional segmentation to spotlight geographical trends and unique consumer challenges.

- **Predictive Modelling**
  - Build and train models to predict likely complaint outcomes or company response strategies.

- **Evaluation and Comparison**
  - Conduct comparative analyses on how companies and product types perform in terms of complaint handling and consumer satisfaction.

- **Deployment and Future Enhancements**
  - Deploy the model via Flask and plan future improvements, such as more advanced NLP techniques and multilingual capabilities.

---

## Files and Directory Structure 📂

Here’s an overview of the main files and directories in the project:

### Root Directory

- **Flask Web App/**: Contains files related to the Flask-based web application.
- **Images/**: Stores visual outputs like plots and word clouds.
- **Jupyter notebooks/**: Houses Jupyter notebooks for various stages of analysis and modeling.
- `Text Analytics Group Presentation.pdf`: PDF presentation summarising the project insights and findings.

### Flask Web App

- `filtered_data_new.csv`: Dataset used by the Flask app for predictions.
- `model.pkl`: Serialized machine learning model for predicting complaint responses.
- `tfidf.pkl`: Pre-trained TF-IDF vectorizer used for text input transformation.
- `web_app.py`: Main Flask application script for running the web app.
- **templates/**: Directory containing HTML templates for the web app interface.

### Images

- **Plots/**: Includes various data visualizations created during analysis.
- **Wordclouds/**: Contains word clouds representing common terms in consumer complaints.

### Jupyter Notebooks

- `Company public response prediction.ipynb`: Predicts if a company will respond to a complaint.
- `Company response consumer prediction.ipynb`: Analyzes consumer feedback and likelihood of company response.
- `eda_main_file.ipynb`: Main exploratory data analysis (EDA) notebook.
- `eda_satisfaction_scores.ipynb`: EDA on satisfaction scores and complaint factors.
- `Product prediction.ipynb`: Model targeting product-related feedback.
- `Satisfaction score.ipynb`: Detailed analysis of satisfaction scores.
- `Word cloud.ipynb`: Generates word clouds to visualize common themes in complaints.
- `filtered_dataset.csv`: Preprocessed dataset for EDA and modeling.
- `vecSmall.csv`, `wfFile.csv`: Supporting datasets for data processing or training.

---
