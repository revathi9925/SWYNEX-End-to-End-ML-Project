# 🚢 Titanic Survival Prediction – End-to-End Machine Learning Project

## 📌 Project Overview

This project focuses on building an end-to-end Machine Learning system to predict whether a passenger survived the Titanic disaster based on passenger information.

The project covers the complete Machine Learning workflow, including data preprocessing, exploratory data analysis, feature preparation, model training, evaluation, and prediction.

Two Machine Learning algorithms, Logistic Regression and Random Forest, are implemented and evaluated to understand their performance.

## 🎯 Project Objectives

- Understand and preprocess the Titanic dataset.
- Perform exploratory data analysis (EDA).
- Handle missing values and prepare features.
- Train multiple Machine Learning models.
- Evaluate model performance using classification metrics.
- Save trained models for future predictions.
- Develop a prediction application.

## 📊 Dataset Description

The project uses the Titanic passenger dataset.

The dataset contains passenger information such as:

- Passenger age
- Gender
- Passenger class
- Ticket fare
- Number of siblings and spouses
- Number of parents and children
- Embarkation port
- Survival status (target variable)

**Target Variable:**
- `0` – Did not survive
- `1` – Survived

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Exploratory data analysis |
| Scikit-learn | Machine Learning |
| Pickle | Saving trained models |
| Streamlit | Application interface |

## ⚙️ Project Workflow

### 1. Data Preprocessing
- Loaded and inspected the dataset.
- Identified and handled missing values.
- Prepared categorical and numerical features.
- Encoded categorical variables.
- Prepared training and testing datasets.

### 2. Exploratory Data Analysis
- Examined passenger survival patterns.
- Analyzed relationships between features.
- Studied numerical and categorical variables.
- Visualized important patterns in the dataset.

### 3. Model Training

Two classification algorithms were implemented:

**Logistic Regression**
- Used as a baseline classification model.
- Predicts survival using a logistic function.

**Random Forest Classifier**
- Uses multiple decision trees.
- Combines predictions to improve classification performance.

### 4. Model Evaluation

The models were evaluated using appropriate classification metrics:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

The evaluation results are saved in the project files for reference.

### 5. Model Saving and Prediction

The trained models were saved using Pickle.

The saved model files can be loaded to make predictions on passenger information without retraining the models.

## 📁 Project Structure

```text
SWYNEX-End-to-End-ML-Project/
│
├── app.py
├── README.md
├── requirements.txt
├── titanic_survival_model.pkl
├── model_evaluation_results.csv
│
└── outputs/
    ├── model_evaluation.txt
    ├── test_predictions.csv
    ├── titanic_model.pkl
    └── model_features.pkl
```

## 💻 Installation and Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/revathi9925/SWYNEX-End-to-End-ML-Project.git
```

### Step 2: Navigate to the project directory

```bash
cd SWYNEX-End-to-End-ML-Project
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access the application.

## 📈 Results

The project trains and evaluates Logistic Regression and Random Forest classification models.

**Evaluation results:**

Refer to:
- `model_evaluation_results.csv`
- `outputs/model_evaluation.txt`

These files contain the recorded model evaluation results.

## 🔮 Future Improvements

- Experiment with additional classification algorithms.
- Improve feature engineering.
- Perform hyperparameter tuning.
- Improve prediction performance.
- Enhance the application interface.

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- End-to-end Machine Learning development.
- Data preprocessing and exploratory data analysis.
- Training and evaluating classification models.
- Model persistence using Pickle.
- Building a Machine Learning prediction application.
- Organizing and documenting projects using GitHub.

## 👩‍💻 Author

**Revathi Maka**

B.Tech – Computer Science and Engineering (AI & ML)

Vignan Institute of Technology and Science, Hyderabad

## 🔗 Project Repository

GitHub: https://github.com/revathi9925/SWYNEX-End-to-End-ML-Project

---

**Task 4 – End-to-End Machine Learning Project**

Completed as part of the SWYNEX Internship Program.

#SWYNEX #MachineLearning #Python #DataScience
