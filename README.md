# 🚀 EET Contract Uploader System

A professional internal tool designed to automate the process of uploading hotel contracts via Excel files to the Juniper system. This application eliminates the need for manual input, reduces human error, and drastically improves speed and efficiency. Built using Python, Streamlit, and deployed on AWS EC2.

---

## 📌 Project Overview

The EET Contract Uploader System allows operations and contracting teams to upload multiple types of hotel contract data through a user-friendly web interface. Instead of relying on Juniper's manual web forms, this app simplifies the workflow by accepting standardized Excel templates that are automatically validated and submitted.

---

## ✨ Features

✅ Upload multiple contract modules:
- Rates
- Allotments
- Stop Sales
- Releases
- Restrictions
- Supplements

✅ Bulk upload support through Excel files  
✅ Built-in data validation for each module  
✅ Clear feedback and error messages  
✅ Simple and fast Streamlit UI  
✅ Deployed on AWS EC2 for multi-user access  
✅ Saves hours of manual work weekly

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python     | Core business logic and data processing |
| Streamlit  | Web interface and user input handling |
| Excel (pandas) | Input file structure and parsing |
| AWS EC2    | Hosting and deployment |
| Juniper API | Backend contract integration |

---

## 📁 Folder Structure

```
EET-Contract-Uploader/
├── eetglobal-contracting.py # Streamlit main app
├── requirements.txt         # Python package dependencies
├── README.md                # Project documentation
├── images/                  # UI screenshots
```

---

## 📸 Screenshots

> Add interface visuals to help users understand the flow

![Main Upload UI](images/upload_ui.png)

---

## 📄 Sample Excel Modules

| Module       | Description                             |
|--------------|-----------------------------------------|
| Rates        | Hotel pricing by season and room type   |
| Allotments   | Room availability and quotas            |
| Stop Sales   | Dates where availability is blocked     |
| Releases     | Required booking lead time              |
| Restrictions | Stay conditions (min/max nights, etc.)  |
| Supplements  | Extra charges by person/room/category   |


---

## ⚙️ How to Run Locally

### 🧪 Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### 🖥️ Step 2: Run the Application
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8506`

---

## 🔐 Deployment & Credentials
- This system is for internal use only.
- Deployment is done on AWS EC2.
- API credentials and environment variables should be handled using `.env` files or AWS Secrets Manager (not included in the repo).

---

## ✅ Benefits

- ⏱️ Reduces manual data entry time drastically
- ✅ Ensures cleaner data before sending to Juniper
- 📊 Helps operations teams focus more on analysis than uploading
- 🧠 Easy for non-technical users to operate

---

## 🧑‍💻 Author

**Amr Atef**  
Senior Data Analyst | Data Automation & APIs  
GitHub: [github.com/AmrAtefAmer](https://github.com/AmrAtefAmer)  
LinkedIn: [linkedin.com/in/amr-atef-665336151](https://linkedin.com/in/amr-atef-665336151)

---

## 📝 License

This project is intended for internal use within EET Global. Not licensed for public distribution.

