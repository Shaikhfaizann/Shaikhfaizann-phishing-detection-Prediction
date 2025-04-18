# 🛡️ Phishing Website Detection using Machine Learning

This project focuses on building a machine learning model to detect phishing websites using a dataset with URL-based features. The goal is to classify whether a given website is legitimate or a phishing attempt based on various engineered features.

---

## 📂 Dataset Description

The dataset contains a collection of websites labeled as either **phishing** or **legitimate**, along with **89 features** extracted from each website's URL and domain attributes.

### 🔑 Target Variable
- `status`: 
  - `phishing` – malicious websites used for phishing attacks.
  - `legitimate` – safe, trustworthy websites.

### 🧩 Feature Examples

Some key features include:

| Feature Name               | Description                                                |
|---------------------------|------------------------------------------------------------|
| `URL_Length`              | Length of the URL                                          |
| `Having_At_Symbol`        | Presence of '@' symbol in the URL                          |
| `Prefix_Suffix`           | Use of '-' in domain name                                  |
| `DNS_Record`              | Availability of DNS records                                |
| `Web_Traffic`             | Website traffic ranking info                               |
| `SSLfinal_State`          | Validity of SSL certificate                                |
| `Domain_Age`              | Age of the domain                                          |
| `Iframe`                  | Use of `<iframe>` tags in source code                      |
| `Statistical_Report`      | Match with known phishing URLs/IPs                         |

> Note: The dataset is pre-processed and may include encoded categorical features or normalized values.

---

## 📊 Dataset Shape
- **Rows:** ~11,000
- **Columns:** 90 (89 features + 1 target)

---

## 🗂️ Source
- Originally derived from phishing detection research datasets.
- Feature set based on a combination of URL-based heuristics, domain analysis, and statistical indicators.

---

## 💡 Usage
This dataset is suitable for:
- Supervised classification tasks
- Model interpretability using SHAP or LIME
- Feature importance and anomaly detection
- Building real-time phishing detection systems

---

## ⚠️ Disclaimer
This dataset is intended for educational and research purposes only. Always ensure proper handling of security-related models and outputs.

---

