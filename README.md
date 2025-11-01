# 🧰 DevOps Python Projects

This repository contains a collection of **DevOps-focused Python projects**, each exploring automation, scripting, and cloud concepts.  
All projects are organized into separate folders within this single repository.

---
## 📁 Repository Structure

```text
.
├── PythonProject3-Ec2StatusCheck/
├── PythonProject3-httpRequestGitLab/
├── PythonProject3-introToBotoAwsSdk/
├── PythonProject3-objectsAndClasses/
└── PythonProject-spreadsheets/


Each folder represents an independent project with its own purpose and source code.

---

## 🚀 Project Overviews

### 1. 🖥️ PythonProject3-Ec2StatusCheck
A Python script that checks the status of **AWS EC2 instances** using **Boto3**.

**Key Features**
- Monitors EC2 instance health and running state.  
- Uses AWS credentials from environment variables or config files.  
- Can be automated with the `schedule` library.  

**Tech Stack:** Python, Boto3, AWS SDK, Schedule

---

### 2. 🌐 PythonProject3-httpRequestGitLab
Demonstrates how to make **HTTP requests** and interact with the **GitLab API**.

**Key Features**
- Uses the `requests` library to call GitLab REST APIs.  
- Supports authentication with Personal Access Tokens.  
- Retrieves or manages GitLab resources such as projects, users, and issues.  

**Tech Stack:** Python, Requests, GitLab API

---

### 3. ☁️ PythonProject3-introToBotoAwsSdk
An introductory project using **Boto3** to interact with AWS services.

**Key Features**
- Lists EC2 instances, S3 buckets, and IAM users.  
- Explains how to set up and authenticate AWS SDK credentials.  
- Demonstrates reusable AWS automation patterns.  

**Tech Stack:** Python, Boto3, AWS SDK

---

### 4. 🧩 PythonProject3-objectsAndClasses
Covers **Object-Oriented Programming (OOP)** fundamentals in Python.

**Key Features**
- Demonstrates defining and using classes and objects.  
- Introduces inheritance and encapsulation concepts.  
- Applies OOP principles to DevOps scripting examples.  

**Tech Stack:** Core Python (OOP)

---

### 5. 📊 PythonProject-spreadsheets
Automates reading, writing, and editing **Excel spreadsheets**.

**Key Features**
- Reads and updates Excel/CSV files programmatically.  
- Uses `openpyxl` or `pandas` for spreadsheet manipulation.  
- Useful for automation of reporting or data tracking tasks.  

**Tech Stack:** Python, openpyxl, pandas

---

## ⚙️ How to Use

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>

Navigate to a specific project

cd PythonProject3-Ec2StatusCheck


Install dependencies

pip install -r requirements.txt


Run the project

python main.py


💡 Each project folder may have its own entry script or README for details.
🧠 Learning Focus

These projects help strengthen your skills in:

Python scripting for DevOps
AWS automation with Boto3
REST API integration (GitLab, HTTP requests)
Data manipulation with spreadsheets
Object-Oriented Programming principles
