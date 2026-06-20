## 🧠 Advanced System Monitor — Full Code Breakdown + Clean Technical Documentation

---

# 📄 Advanced System Monitor — Technical Documentation (Code-Backed)

# 📄 مانیتور پیشرفته سیستم — مستندات فنی (تحلیل کد)

---

# 1. Project Overview | نمای کلی پروژه

This system is a **real-time OS telemetry pipeline** built in Python using `psutil`.

It continuously:

- Samples CPU / RAM / process data
- Stores metrics in memory
- Displays live system status
- Generates post-run analytics
- Exports CSV logs and graphs

📌 Core idea:

> Turn OS metrics into a time-series analytics pipeline

---

این سیستم یک **خط لوله مانیتورینگ لحظه‌ای سیستم‌عامل** است که با پایتون و `psutil` ساخته شده است.

این سیستم به‌صورت مداوم:

- داده‌های CPU / RAM / پردازش‌ها را نمونه‌برداری می‌کند
- آن‌ها را در حافظه ذخیره می‌کند
- وضعیت زنده سیستم را نمایش می‌دهد
- بعد از اجرا تحلیل آماری تولید می‌کند
- خروجی CSV و نمودار تولید می‌کند

📌 ایده اصلی:

> تبدیل متریک‌های سیستم به یک پایپ‌لاین سری زمانی

---

# 2. System Architecture | معماری سیستم

### 🔁 Data Pipeline

```
psutil (OS layer)
   ↓
collector.py
   ↓
history.py (time-series buffer)
   ↓
main.py (execution loop)
   ↓
analyzer.py (statistics engine)
   ↓
logger.py + visualizer.py (output layer)
```

---

### 🧱 Design Principles

- Stateless data collection (collector)
- In-memory time-series buffer (history)
- Single-thread polling loop
- Post-execution batch analytics
- Minimal dependencies

---

# 3. Module Breakdown

---

## 3.1 main.py — Execution Engine 🧠

Controls full monitoring lifecycle.

### Loop
```python
while True:
```

Runs continuous system polling until interrupted.

### Data collection
```python
cpu = get_cpu()
ram = get_ram()
processes = get_processes()
```

### Storage
```python
add_snapshot(time.time() - start, cpu, ram, len(processes))
```

Stores time-series data using relative timestamps.

### Output
```python
print(f"CPU: {cpu}% | RAM: {ram}% | Processes: {len(processes)}")
```

### Shutdown
Triggered by Ctrl+C → runs:

- analyzer
- CSV export
- visualization

---

## 3.2 collector.py — OS Data Layer ⚙️

Built on `psutil`.

- CPU: `psutil.cpu_percent()`
- RAM: `psutil.virtual_memory().percent`
- Processes: `psutil.process_iter()`

Handles access errors safely.

---

## 3.3 history.py — Time-Series Buffer 🧾

Stores:

```python
history = {
  "time": [],
  "cpu": [],
  "ram": [],
  "process_count": []
}
```

All data is kept in RAM during execution.

---

## 3.4 analyzer.py — Statistics Engine 📊

Post-run analytics:

- CPU avg / max
- RAM avg / max
- Top CPU processes
- Top memory processes

Pure batch computation (no streaming).

---

## 3.5 visualizer.py — Graph Engine 📈

Uses matplotlib:

- CPU usage over time
- RAM usage over time

Simple index-based plots.

---

## 3.6 logger.py — CSV Export 💾

Exports:

```
time, cpu, ram, process_count
```

Saved as `log.csv`.

---

## 3.7 config.py — Settings ⚙️

```python
INTERVAL = 1
```

Controls sampling rate.

---

# 4. Runtime Flow 🔁

```
START
  ↓
collector
  ↓
history buffer
  ↓
live print
  ↓
sleep
  ↓
repeat loop
  ↓
CTRL+C
  ↓
analyzer
  ↓
logger + visualizer
  ↓
END
```

---

# 5. Engineering Evaluation

### Strengths
- Modular architecture
- Clean separation of concerns
- Lightweight dependencies
- Deterministic execution

### Weaknesses
- No async processing
- No persistence layer (DB)
- No UI/dashboard
- No anomaly detection

---

# 6. Upgrade Roadmap 🚀

### Level 1
- JSON export
- SQLite storage
- Better logging

### Level 2
- Flask dashboard
- Multi-threaded collector
- Filtering processes

### Level 3
- Anomaly detection
- Memory leak detection
- Alerting system (Telegram/webhook)

---

# 7. Summary 🧩

A lightweight **OS observability pipeline**:

- psutil-based telemetry
- in-memory time-series buffer
- batch analytics engine
- visualization + export layer

---

End of document.