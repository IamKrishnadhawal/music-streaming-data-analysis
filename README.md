# 🎧 Music Streaming Data Pipeline & Analytics

**Tech Stack:** Python, SQLite (SQL), Power BI, DAX

---

## 📌 Project Overview

This project demonstrates an end-to-end data analytics pipeline built to analyze over **4 years of personal music streaming history**.

The objective was to:

* Understand how listening behavior correlates with audio features like **energy and danceability**
* Segment artists into meaningful categories such as **Workout vs Chill**
* Simulate a real-world data workflow from **raw ingestion to business insights**

---

## 🏗️ Architecture & Pipeline Flow

CSV Files → Python (Pandas) → SQLite → SQL Analysis → CSV Export → Power BI Dashboard

---

## ⚙️ Implementation Details

### 🔹 1. Data Ingestion (Python)

* Built an automated ingestion pipeline using **Pandas + SQLite**
* Dynamically loaded multiple CSV files into structured database tables
* Applied column standardization for SQL compatibility

---

### 🔹 2. Data Modeling & Analysis (SQL)

* Performed **INNER JOINs** to combine streaming history with track-level audio features
* Aggregated metrics like **Top Artists by Play Count**
* Calculated **Average Energy Scores per Artist**

---

### 🔹 3. Business Logic (DAX)

* Created a calculated column to segment music:

  * `Energy > 0.7 → Workout / High Energy`
  * `Energy ≤ 0.7 → Chill / Study`
* Enabled user-driven filtering for dynamic analysis

---

### 🔹 4. Visualization (Power BI)

* Built an interactive dashboard with:

  * Scatter Plot → Energy vs Popularity
  * Bar Chart → Top Artists
* Added page-level filters for category-based exploration

---

## 📊 Key Insights

* **Listening Behavior Insight:**
  My most-played artist, *Pink Floyd*, has a relatively low average energy score (~0.32), indicating a strong preference for **chill music during frequent listening sessions**.

* **Energy vs Popularity Trend:**
  Higher-energy tracks tend to appear more frequently in **high-play segments**, suggesting a link between **tempo and engagement**.

---

## 💡 Business Interpretation

This type of analysis can be used by streaming platforms to:

* Improve **playlist recommendations**
* Segment users based on **listening intent (Workout vs Relaxation)**
* Optimize **content discovery algorithms**

---

## 📂 Project Structure

```
/data           → Raw CSV files  
/database       → SQLite database  
/scripts        → Python ingestion + SQL queries  
/dashboard      → Power BI (.pbix file)  
```

---

## ▶️ How to Run

1. Run the ingestion script:

   ```
   python /scripts/ingest_data.py
   ```
2. Execute SQL queries from:

   ```
   /scripts/Music Streaming Project.session.sql
   ```
3. Open the Power BI file to explore insights

---

## 🚀 Key Skills Demonstrated

* Data Pipeline Development (Python + SQL)
* Data Cleaning & Transformation
* Relational Data Modeling
* Business Logic Implementation (DAX)
* Data Visualization & Storytelling
* End-to-End Project Structuring with Git

---
