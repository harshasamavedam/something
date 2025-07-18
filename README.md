# Wrogn Products Extraction & Reporting Automation

## 📌 Project Overview

This project automates the extraction of product data from the Wrogn website, transforms the data into analyzable formats, generates Excel-based product reports, and sends them via email.

It integrates:
- **Web scraping** with Selenium
- **Data transformation** with pandas
- **Excel report generation**
- **Automated report delivery over email**

---

## ✅ Features

- Scrapes product names, prices, and discount info from the Wrogn "View All" page.
- Applies structured transformations to the extracted data (e.g., price ranges, color/type separation).
- Exports both raw and "gold" (processed) data to Excel.
- Sends the Excel report via email to a list of recipients.

---

## 📁 File Structure

| File              | Purpose                                                                 |
|-------------------|-------------------------------------------------------------------------|
| `Main.py`         | Orchestrates data extraction, processing, Excel writing, and emailing. |
| `wrogn_extract.py`| Web scraping logic and data transformation functions.                   |
| `email_trigger.py`| Contains logic to email the Excel report as an attachment.              |
| `requirement.txt` | Python dependencies (not shown, but recommended to include).            |

---

## 🧠 How It Works

1. **Scraping with Selenium** (`wrogn_extract_raw`):
   - Headless Chrome browser scrolls and collects product data.
   - Parses product names, prices, and offers.

2. **Data Enrichment** (`raw_to_gold`):
   - Splits product names into `type`, `color`, and style tags.
   - Converts prices to integers and classifies into price buckets.

3. **Excel Report Generation** (`Main.py`):
   - Creates an Excel file with two sheets:
     - `Raw Data`
     - `Wrogn Products` (cleaned and enriched data)

4. **Email Automation** (`send_email`):
   - Automatically sends the `.xlsx` file to a specified list via Gmail SMTP.

---

## ⚙️ Setup Instructions

### 1. Prerequisites

- Python 3.7 or newer
- Chrome and ChromeDriver installed (ensure your ChromeDriver matches your browser version)


This will:
- Extract and process data
- Save to an Excel file (`wrogn_products-YYYY-MM-DD.xlsx`)
- Email the file to recipients

The output will look like:
- `wrogn_products2024-06-16.xlsx`
  - Sheet 1: `Raw Data`
  - Sheet 2: `Wrogn Products`

---



## 📬 Notes

- Ensure ChromeDriver is available on your system PATH.
- Email sending uses port 587 with TLS.
- For maximum reliability, wrap email authentication details in environment variables or use a `.env` file (security best practice).

---

## 🔧 Potential Enhancements

- Add retry mechanisms and error logging.
- Integrate with Airflow or cron for scheduling.
- Store extracted data in a database (MySQL/PostgreSQL).
- Expand to other fashion or e-commerce websites.

---

## 📚 License

MIT License – free to use, adapt, and distribute with attribution.
