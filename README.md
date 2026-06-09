# Advanced System Monitor / مانیتور پیشرفته سیستم

A lightweight Python-based system monitoring tool that tracks CPU, RAM, and process usage in real time, collects historical data, and provides graphs for analysis.

یک ابزار مانیتورینگ سبک پایتونی برای بررسی لحظه‌ای مصرف CPU، RAM و پردازش‌ها، جمع‌آوری داده‌های تاریخی و ارائه نمودار برای تحلیل.

---

## 🚀 Overview / معرفی

This project collects system performance data using `psutil` and provides live stats for analysis or debugging.  
It also stores historical snapshots, generates statistics, and visualizes CPU/RAM usage.

این پروژه با استفاده از کتابخانه `psutil` اطلاعات سیستم را جمع‌آوری کرده و برای تحلیل یا دیباگ، آمار زنده ارائه می‌دهد.  
همچنین داده‌های تاریخی را ذخیره می‌کند، آمار نهایی محاسبه می‌کند و مصرف CPU و RAM را بصری‌سازی می‌کند.

---

## ✨ Features / ویژگی‌ها

- Real-time CPU usage tracking / بررسی مصرف CPU به صورت لحظه‌ای
- Real-time RAM usage tracking / بررسی مصرف RAM به صورت لحظه‌ای
- Process monitoring (PID, name, CPU %, RAM %) / مانیتورینگ پردازش‌ها
- Time-series data collection / جمع‌آوری داده‌های زمانی
- Statistical analysis (average, max, top processes) / تحلیل آماری
- Data visualization using graphs / نمایش نمودار
- CSV export of collected data / خروجی CSV

---
    
## 📁 Project Structure / ساختار پروژه
main.py → entry point
collector.py → system data collection
history.py → time-series storage
analyzer.py → statistics engine
visualizer.py → graphs
logger.py → CSV export
config.py → configuration

## 🧱 Architecture / معماری
Collector → gathers system data
History → stores snapshots over time
Analyzer → computes statistics
Visualizer → generates graphs
Logger → exports CSV

## 📈 Output / خروجی
Real-time monitoring
CPU/RAM graphs
CSV log file
Final statistical report
🖥️ Concept / مفهوم

## 📦 Requirements / نیازمندی‌ها

- Python 3.8+
- psutil
- matplotlib

[pip install psutil matplotlib tk]

## ⚙️ How to Run / نحوه اجرا
python main.py

---

## 📌This project simulates OS-level resource monitoring, including CPU scheduling behavior and memory usage over time.

این پروژه رفتار سیستم‌عامل در مدیریت منابع مانند CPU و حافظه را شبیه‌سازی می‌کند.

- Built with pain, debugging, and too much CPU watching 😐
