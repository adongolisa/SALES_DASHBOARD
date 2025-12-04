#  Sales Analytics Dashboard (Streamlit)

This interactive dashboard analyzes sales performance across products, regions, and daily activity.  
It highlights top insights such as:

-  **Top Performing Product**
-  **Highest Revenue Day**
-  **Region With Lowest Conversion Rate**
-  **Revenue Trends & Conversion Metrics**

Built with **Streamlit**, **Plotly**, and **Pandas**, this dashboard is fully responsive and deployable for free.

---

##  Live Demo  
🔗 *[https://salesdashboardgit-e7rjjktjbznfrkhukk5agq.streamlit.app/]*  

---

##  Tech Stack  
- **Python**
- **Streamlit**
- **Pandas**
- **Plotly Express**

---

##  Dataset  
`sales_data.csv` contains:

- `date`  
- `product`  
- `region`  
- `users`  
- `conversions`  
- `revenue`  
- Automatically calculated: `conversion_rate`

---

##  How to Run Locally

1. Clone the repository:
   ```bash
   git clone <https://github.com/adongolisa/SALES_DASHBOARD.git>
   cd SALES_DASHBOARD

2. Install requirements:
  ```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
   ```bash
streamlit run dashboard.py

