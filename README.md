# Advanced System Monitor / مانیتور پیشرفته سیستم

A lightweight Python-based system monitoring tool that tracks CPU, RAM, and process usage in real time.

یک ابزار مانیتورینگ سبک پایتونی برای بررسی لحظه‌ای مصرف CPU، RAM و پردازش‌ها.

---

## 🚀 Overview / معرفی

This project collects system performance data using `psutil` and provides live stats for analysis or debugging.

این پروژه با استفاده از کتابخانه `psutil` اطلاعات سیستم را جمع‌آوری کرده و برای تحلیل یا دیباگ، آمار زنده ارائه می‌دهد.

---

## ✨ Features / ویژگی‌ها

- CPU usage tracking / بررسی مصرف CPU
- RAM usage tracking / بررسی مصرف RAM
- Process monitoring / مانیتورینگ پردازش‌ها
- Lightweight and fast / سبک و سریع

---

## 📦 Requirements / نیازمندی‌ها

- Python 3.8+
- psutil

Install dependency:

```bash
pip install psutil
```

---

## ⚙️ How to Run / نحوه اجرا

Run the main script:

```bash
python main.py
```

If your entry file is different, run:

```bash
python <your_file>.py
```

---

## 📁 Project Structure / ساختار پروژه

```
collector.py   -> system data collection / جمع‌آوری داده‌ها
analyzer.py    -> data analysis / تحلیل داده‌ها
config.py      -> configuration / تنظیمات
```

---

## 🧠 Notes / نکات

This project is meant for learning, experimentation, and basic system monitoring.

این پروژه برای یادگیری، آزمایش و مانیتورینگ پایه سیستم طراحی شده است.

---

Built with pain, debugging, and way too much CPU watching 😐