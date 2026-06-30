# 📊 Retail Sales Analysis with Python

This project is part of my Data Analytics learning journey. Using a retail sales dataset, I solved business case studies similar to real-world analyst tasks, focusing on data cleaning, exploratory data analysis (EDA), KPI generation, and dashboard creation using Python.

## 📁 Dataset

The dataset contains retail transaction data with the following columns:

| Column           | Description                                |
| ---------------- | ------------------------------------------ |
| `invoice_no`     | Unique invoice number for each transaction |
| `customer_id`    | Unique customer identifier                 |
| `gender`         | Customer gender                            |
| `age`            | Customer age                               |
| `category`       | Product category purchased                 |
| `quantity`       | Number of items purchased                  |
| `price`          | Price per unit                             |
| `payment_method` | Payment method used                        |
| `invoice_date`   | Date of purchase                           |
| `shopping_mall`  | Shopping mall where the purchase was made  |

A new column, **`revenue`**, was created using:

```python
revenue = quantity * price
```

---

# 🛠️ Tools & Libraries

* Python
* Pandas
* NumPy
* Matplotlib
* Google colab

---

# 📌 Case Study 1 – Sales Performance Dashboard

### Business Problem

The management wants an overview of the company's sales performance.

### KPIs

* Total Revenue
* Total Orders
* Total Customers
* Average Order Value (AOV)

### Analysis Performed

* Revenue by Product Category
* Revenue by Shopping Mall
* Monthly Revenue Trend
* Revenue by Payment Method

### Dashboard

A dashboard was created using **Matplotlib Subplots**, combining multiple visualizations into a single report.

---

# 📌 Case Study 2 – Customer Segmentation

### Business Problem

Understand how different age groups contribute to business performance.

### Feature Engineering

Created customer age groups:

* 0–18
* 19–25
* 26–35
* 36–45
* 46–60
* 60+

### Analysis Performed

For each age group:

* Number of Unique Customers
* Total Spending
* Average Spending
* Most Purchased Category
* Preferred Payment Method

The analysis helps identify customer purchasing behavior across different age segments.

---

# 📚 Concepts Practiced

* Data Cleaning
* Feature Engineering
* GroupBy Operations
* Aggregation (`sum`, `mean`, `count`, `nunique`)
* Sorting and Ranking
* Data Visualization
* Dashboard Creation
* Business KPI Analysis

---

# 🚀 Learning Outcome

Through this project I learned how to:

* Transform raw transactional data into meaningful business insights.
* Build KPIs used in retail analytics.
* Perform customer segmentation.
* Create professional charts and dashboards using Matplotlib.
* Solve business-oriented case studies using Python and Pandas.

---

## 📌 Future Improvements

* Interactive dashboard using Streamlit
* Advanced customer segmentation (RFM Analysis)
* Time series forecasting
* Sales prediction using Machine Learning
* SQL version of the same case studies
