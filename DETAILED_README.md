## 🧠 Advanced System Monitor — Unified Line-by-Line Code Breakdown + Technical Documentation

## 🧠 مانیتور پیشرفته سیستم — تحلیل خط‌به‌خط + مستندات فنی

---

# 1. Project Overview | نمای کلی پروژه

### EN

This system is a **real-time OS telemetry pipeline** built in Python using `psutil`.

It continuously:

* Samples CPU / RAM / process data
* Stores metrics in an in-memory time-series buffer
* Displays live system status
* Performs post-run statistical analysis
* Exports CSV logs and visual graphs

📌 Core idea:

> Transform raw OS metrics into a structured time-series analytics system

---

### FA

این سیستم یک **خط لوله پایش لحظه‌ای سیستم‌عامل** است که با پایتون و `psutil` ساخته شده است.

به‌صورت مداوم:

* داده‌های CPU / RAM / پردازش‌ها را نمونه‌برداری می‌کند
* آن‌ها را در یک بافر سری زمانی در حافظه ذخیره می‌کند
* وضعیت زنده سیستم را نمایش می‌دهد
* بعد از اجرا تحلیل آماری انجام می‌دهد
* خروجی CSV و نمودار تولید می‌کند

📌 ایده اصلی:

> تبدیل داده‌های خام سیستم به یک سیستم تحلیل سری زمانی ساختاریافته

---

# 2. System Architecture | معماری سیستم

### 🔁 Data Pipeline Flow | جریان داده

```
psutil (OS layer)
   ↓
collector.py (data acquisition)
   ↓
history.py (time-series buffer)
   ↓
main.py (execution engine)
   ↓
analyzer.py (statistics engine)
   ↓
logger.py + visualizer.py (output layer)
```

---

### 🧱 Design Principles | اصول طراحی

**EN**

* Modular separation of concerns
* Stateless OS data extraction
* In-memory time-series storage
* Single-thread polling loop
* Batch post-execution analytics
* Lightweight dependency footprint

**FA**

* طراحی ماژولار و تفکیک مسئولیت‌ها
* استخراج بدون state از سیستم‌عامل
* ذخیره‌سازی سری زمانی در حافظه
* حلقه polling تک‌ریسمانی
* تحلیل پس از اجرا به‌صورت batch
* وابستگی‌های سبک

---

# 3. Module Breakdown (Line-by-Line Logic)

# 3. تحلیل ماژول‌ها (منطق خط‌به‌خط)

---
# 3.1 main.py — موتور اجرا

---

### Imports | ایمپورت‌ها

```python
import time
```

**EN:** Time control + timestamps
**FA:** کنترل زمان و ثبت timestamp

---

```python
from collector import get_cpu, get_ram, get_processes
```

**EN:** OS metrics interface
**FA:** رابط دریافت داده‌های سیستم (CPU/RAM/Processes)

---

```python
from history import history, add_snapshot
```

**EN:** time-series storage
**FA:** ذخیره‌سازی سری زمانی

---

```python
from analyzer import analyze
```

**EN:** post-run statistics engine
**FA:** موتور تحلیل آماری بعد از اجرا

---

```python
from visualizer import plot
```

**EN:** graph rendering
**FA:** رسم نمودارها

---

```python
from logger import save_csv
```

**EN:** CSV export layer
**FA:** خروجی گرفتن به CSV

---

```python
from config import INTERVAL
```

**EN:** sampling interval config
**FA:** تنظیم فاصله نمونه‌برداری

---

### Entry Point | نقطه شروع

```python
def main():
```

**EN:** runtime controller
**FA:** کنترل‌کننده اجرای برنامه

---

```python
start = time.time()
```

**EN:** baseline timestamp
**FA:** زمان شروع اجرای برنامه

---

```python
processes = []
```

**EN:** process snapshot placeholder
**FA:** نگهدارنده موقت لیست پردازش‌ها

---

### Monitoring Loop | حلقه مانیتورینگ

```python
while True:
```

**EN:** infinite polling loop
**FA:** حلقه بی‌نهایت جمع‌آوری داده

---

### Data Collection | جمع‌آوری داده

```python
cpu = get_cpu()
ram = get_ram()
processes = get_processes()
```

**EN:**

* CPU usage %
* RAM usage %
* Process snapshot list

**FA:**

* درصد استفاده CPU
* درصد استفاده RAM
* لیست پردازش‌ها

---

### Time-Series Storage | ذخیره سری زمانی

```python
add_snapshot(time.time() - start, cpu, ram, len(processes))
```

**EN:** stores synchronized telemetry frame
**FA:** ذخیره یک فریم همگام از داده‌ها

---

### Live Output | خروجی زنده

```python
print(f"CPU: {cpu}% | RAM: {ram}% | Processes: {len(processes)}")
```

**EN:** real-time terminal monitoring
**FA:** نمایش لحظه‌ای در ترمینال

---

### Sampling Control | کنترل نمونه‌برداری

```python
time.sleep(INTERVAL)
```

**EN:** prevents CPU overload
**FA:** جلوگیری از فشار بیش از حد به CPU

---

### Shutdown Handling | مدیریت توقف

```python
except KeyboardInterrupt:
```

**EN:** graceful stop (Ctrl + C)
**FA:** توقف امن برنامه

---

### Post-run Pipeline | پردازش نهایی

```python
result = analyze(history, processes)
```

**EN:** statistical analysis execution
**FA:** اجرای تحلیل آماری

---

```python
save_csv(history)
plot(history)
```

**EN:** export + visualization
**FA:** خروجی CSV + رسم نمودار

---
# 3.2 collector.py — لایه جمع‌آوری داده

---

### CPU

```python
def get_cpu():
    return psutil.cpu_percent(interval=None)
```

**EN:** instant CPU usage
**FA:** استفاده لحظه‌ای CPU

---

### RAM

```python
def get_ram():
    mem = psutil.virtual_memory()
    return mem.percent
```

**EN:** memory usage percentage
**FA:** درصد مصرف RAM

---

### Process Snapshot

```python
def get_processes():
    processes = []
```

**EN:** process container init
**FA:** ایجاد لیست پردازش‌ها

---

```python
for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
```

**EN:** iterates system processes
**FA:** پیمایش پردازش‌های سیستم

---

```python
p.cpu_percent(None)
```

**EN:** initializes CPU tracking
**FA:** فعال‌سازی شمارش CPU برای process

---

```python
processes.append(p.info)
```

**EN:** stores process metadata
**FA:** ذخیره اطلاعات پردازش

---

```python
except (psutil.NoSuchProcess, psutil.AccessDenied):
    continue
```

**EN:** safe error handling
**FA:** مدیریت خطای امن

---

# 3.3 history.py — Time-Series Buffer 🧾

# 3.3 history.py — بافر سری زمانی

---

```python
history = {
    "time": [],
    "cpu": [],
    "ram": [],
    "process_count": []
}
```

**EN:** aligned telemetry dataset
**FA:** دیتاست همگام‌سازی‌شده

---

```python
def add_snapshot(t, cpu, ram, process_count):
```

**EN:** inserts telemetry frame
**FA:** افزودن یک فریم داده

---
# 3.4 analyzer.py — موتور تحلیل

---

### Guard Clause

```python
if not history["cpu"]:
```

**EN:** prevents empty dataset crash
**FA:** جلوگیری از خطا در دیتای خالی

---

### CPU Stats

```python
cpu_avg = sum(history["cpu"]) / len(history["cpu"])
cpu_max = max(history["cpu"])
```

**EN:** average + peak CPU
**FA:** میانگین و بیشینه CPU

---

### RAM Stats

```python
ram_avg = sum(history["ram"]) / len(history["ram"])
ram_max = max(history["ram"])
```

**EN/FA:** memory usage analysis / تحلیل مصرف RAM

---

### Top Processes

```python
top_cpu = sorted(processes, key=lambda x: x.get("cpu_percent", 0), reverse=True)[:5]
```

**EN:** top CPU consumers
**FA:** پردازش‌های پرمصرف CPU

---

```python
top_mem = sorted(processes, key=lambda x: x.get("memory_percent", 0), reverse=True)[:5]
```

**EN/FA:** top RAM consumers / پردازش‌های پرمصرف RAM

---
# 3.5 visualizer.py — موتور نمودار

---

```python
plt.plot(history["cpu"])
plt.title("CPU Usage Over Time")
plt.xlabel("Time")
plt.ylabel("CPU %")
plt.show()
```

**EN:** CPU trend graph
**FA:** نمودار تغییرات CPU

---

```python
plt.plot(history["ram"])
```

**EN:** RAM trend visualization
**FA:** نمودار مصرف RAM

---
# 3.6 logger.py — خروجی CSV

---

```python
import csv
```

**EN/FA:** CSV engine / موتور خروجی CSV

---

```python
writer.writerow(["time", "cpu", "ram", "process_count"])
```

**EN:** header row
**FA:** ردیف عنوان‌ها

---

```python
for i in range(len(history["time"])):
```

**EN/FA:** iterate dataset / پیمایش داده‌ها

---

```python
writer.writerow([...])
```

**EN:** writes telemetry row
**FA:** نوشتن داده‌ها در فایل

---
# 3.7 config.py — تنظیمات

```python
INTERVAL = 1
```

**EN:** sampling rate (1s)
**FA:** نرخ نمونه‌برداری (هر ۱ ثانیه)

---

# 4. Runtime Flow 🔁 | جریان اجرا

```
START
  ↓
collector (psutil)
  ↓
history buffer
  ↓
main loop
  ↓
live output
  ↓
sleep
  ↓
repeat
  ↓
CTRL + C
  ↓
analyzer
  ↓
logger
  ↓
visualizer
  ↓
END
```

---

# 5. Engineering Evaluation | ارزیابی فنی

### ✅ Strengths | نقاط قوت

* Modular architecture / معماری ماژولار
* Clean separation / تفکیک واضح
* Lightweight system / سبک بودن
* Deterministic flow / جریان قابل پیش‌بینی

---

### ⚠️ Weaknesses | ضعف‌ها

* No async / بدون async
* No database / بدون دیتابیس
* No UI dashboard / بدون داشبورد
* No anomaly detection / بدون تشخیص خطا

---

# 6. Upgrade Roadmap 🚀 | نقشه توسعه

### Level 1

* JSON export / خروجی JSON
* SQLite storage / دیتابیس سبک
* logging system / سیستم لاگ

### Level 2

* Web dashboard / داشبورد تحت وب
* multi-threading / چندریسمانی
* filtering engine / فیلتر پردازش‌ها

### Level 3

* anomaly detection / تشخیص ناهنجاری
* alert system / سیستم هشدار
* predictive analytics / پیش‌بینی بار سیستم

---

# 7. Final Summary 🧩 | جمع‌بندی

### EN

Lightweight observability + analytics pipeline:

* OS metrics → structured data → analytics → visualization → export

### FA

سیستم سبک پایش و تحلیل:

* داده سیستم → ساختاردهی → تحلیل → نمایش → خروجی

---

If needed: can convert this into a **professor-ready Word (.docx) report with cover page, diagrams, and formal academic formatting**.
