# 🍴 Zomato Data Analysis Dashboard

A beautiful and interactive data analysis dashboard built with Streamlit to explore restaurant trends, ratings, customer preferences, and pricing strategies from Zomato data.

<img width="1919" height="859" alt="1" src="https://github.com/user-attachments/assets/c29fef73-a74e-4bb3-8415-f8a5a7f78519" />

<img width="1915" height="656" alt="2" src="https://github.com/user-attachments/assets/92e37501-b97f-442f-beed-a56205f5293c" />

<img width="1918" height="857" alt="3" src="https://github.com/user-attachments/assets/5cc9f6a3-836d-40f1-a82e-ac27519d2cfe" />


## 📋 Table of Contents

- [Overview](#Overview)
- [Features](#Features)
- [Installation](#Installation)
- [Usage](#Usage)
- [Dataset](#Dataset)
- [Analysis Steps](#analysis-steps)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)

## 🎯 Overview

This project provides a comprehensive analysis of Zomato restaurant data through an interactive web dashboard. It helps users understand:
- Restaurant distribution across different types
- Customer engagement patterns through votes
- Pricing strategies and cost distribution
- Impact of online ordering on ratings
- Overall service quality trends

## ✨ Features

- **Interactive Dashboard**: Beautiful UI with gradient cards and professional styling
- **Real-time Analysis**: Instant insights with interactive visualizations
- **9 Comprehensive Steps**: From data cleaning to final recommendations
- **Visual Insights**: Charts, graphs, heatmaps, and statistical summaries
- **Responsive Design**: Clean white containers with proper spacing
- **Key Metrics Display**: Important statistics highlighted in gradient cards
- **Detailed Explanations**: Each analysis step includes context and insights

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Step-by-step Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/zomato-analysis.git
cd zomato-analysis
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install required packages**
```bash
pip install -r requirements.txt
```

### Required Packages

Create a `requirements.txt` file with:
```
streamlit==1.28.0
pandas==2.0.3
numpy==1.24.3
matplotlib==3.7.2
seaborn==0.12.2
```

## 💻 Usage

1. **Place your dataset** in the project directory:
   - Ensure you have `Zomato-data-.csv` in the same folder as the app

2. **Run the Streamlit app**:
```bash
streamlit run app.py
```

3. **Open your browser**:
   - The app will automatically open at `http://localhost:8501`
   - If not, navigate to the URL shown in your terminal

## 📊 Dataset

The analysis uses the Zomato restaurant dataset containing:

### Key Columns:
- `name`: Restaurant name
- `online_order`: Whether online ordering is available (Yes/No)
- `rate`: Restaurant rating (format: "4.1/5")
- `votes`: Number of customer votes
- `approx_cost(for two people)`: Approximate cost for two people
- `listed_in(type)`: Type of restaurant (Dining, Cafe, Delivery, etc.)
- `location`: Restaurant location
- `Country Code`: Country identifier

### Data Source:
Download the dataset from [Kaggle - Zomato Bangalore Restaurants](https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants)

## 📈 Analysis Steps

The dashboard includes 9 comprehensive analysis steps:

### 1️⃣ **Dataset Overview**
- Total restaurants, columns, and countries covered
- Preview of data structure

### 2️⃣ **Data Cleaning**
- Converting rating format from "4.1/5" to 4.1
- Handling missing values

### 3️⃣ **Restaurant Types Analysis**
- Distribution of restaurant categories
- Customer engagement by type

### 4️⃣ **Most Popular Restaurant**
- Identifying the restaurant with maximum votes
- Display rating and location

### 5️⃣ **Online Order Availability**
- Pie chart showing digital adoption
- Percentage of restaurants with online ordering

### 6️⃣ **Ratings Distribution**
- Histogram with color gradient
- Average, median, min, and max ratings

### 7️⃣ **Cost Analysis**
- Price point distribution
- Statistics on dining costs

### 8️⃣ **Online vs Offline Ratings**
- Boxplot comparison
- Statistical analysis of rating differences

### 9️⃣ **Heatmap Analysis**
- Restaurant type vs online order availability
- Digital adoption rates by category

### 🎓 **Summary & Recommendations**
- Business insights
- Actionable recommendations

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical data visualization



## 📁 Project Structure

```
zomato-analysis/
│
├── app.py                      # Main Streamlit application
├── Zomato-data-.csv           # Dataset file
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
└── .gitignore                 # Git ignore file
```


**⭐ If you find this project helpful, please consider giving it a star!**

Made with ❤️ using Streamlit
