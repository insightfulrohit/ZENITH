<div align="center">

# ✦ ZENITH
### Habit & Life Goals Tracker

**A beautiful, fully offline Python desktop app to track your daily habits,
manage tasks, set life goals, journal your thoughts, and grow every single day.**

![Python](https://img.shields.io/badge/Python-3.8%2B-gold?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/UI-Tkinter-teal?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen?style=for-the-badge)

---

*"We are what we repeatedly do. Excellence is not an act, but a habit."*
**— Aristotle**

</div>

---

## 📌 What is ZENITH?

**ZENITH** means *the highest point* — and that's exactly what this tool helps you reach.

ZENITH is a **free, open-source, completely offline** desktop application built with Python. It helps you:

- ✅ Track your **daily habits** and build powerful streaks
- 📋 Manage your **tasks** with deadlines, priorities, and status tracking
- 🎯 Set and track **life goals** with progress bars
- 📓 Write a **daily journal** and log your mood
- 📊 See beautiful **analytics and charts** of your progress
- 💬 Get motivated with **50 rotating daily quotes**
- 🔥 Stay consistent with a **live streak counter**

No internet needed. No account needed. No subscription. **Just you and your goals.**

---

## ✨ Why ZENITH?

| Feature | ZENITH |
|---|---|
| 💰 Cost | **100% Free** |
| 🌐 Internet Required | **No — fully offline** |
| 📦 Installation | **Zero dependencies** |
| 💾 Your Data | **Stays on your computer** |
| 🖥️ Platform | **Windows, Mac, Linux** |
| 🎨 Design | **Premium dark theme (Obsidian Gold)** |

Most habit tracking apps require an account, charge a subscription, or send your data to the cloud. ZENITH does none of that. Everything is saved locally in a single JSON file on your own machine.

---

## 🖥️ Screenshots & Features

### 🏠 Dashboard
Your daily command centre. The moment you open ZENITH, you see:
- Today's motivational quote (changes every day automatically)
- 5 live KPI cards — habits done, streak, open tasks, active goals, completion %
- An animated circular progress ring filling up as you tick habits
- A 7-day colour heatmap showing your weekly consistency
- All today's habits with one-click toggle
- Upcoming tasks at a glance

### ✅ Daily Habits
- Tick any habit by clicking its row — it turns green instantly
- See your streak per habit (e.g. 🔥 12 days) and best-ever streak
- View habits grouped by category (Fitness, Health, Learning, etc.)
- Add unlimited custom habits with a category and weekly target
- Archive habits you no longer need (data is preserved, not deleted)
- Export your habit data to CSV

### 📋 Task Manager
- Add tasks with name, due date, due time, category, priority and notes
- Priority levels: 🔴 High, 🟡 Medium, 🟢 Low
- Status tracking: Pending → In Progress → Done → Cancelled
- **Overdue detection** — tasks past their due date turn red with ⚠ badge
- Quick status buttons directly on each task row (no need to open edit dialog)
- Filter by: All / Pending / In Progress / Done / Cancelled / Overdue
- Sort by: Priority / Due Date / Status / Name
- Export tasks to CSV

### 🎯 Life Goals
- Set big-picture goals with a target date and category
- Track progress from 0% to 100% with a visual progress bar
- Use +10% / -10% quick buttons to update progress instantly
- Status labels: Active / In Progress / Completed / On Hold
- Add key milestones and notes to each goal
- See a live snapshot: how many goals are active, completed, on hold

### 📊 Analytics
- **30-day calendar heatmap** — every day colour-coded by completion %
- **Per-habit bar chart** — see which habits you're most consistent with
- **Detailed stats table** — 7-day count, 30-day count, %, streak, best streak, weekly target
- **Mood trend line chart** — see how your mood has changed over time (after logging mood)
- Hover over any heatmap cell for a tooltip showing exact numbers

### 📓 Daily Journal
- Write daily entries using 4 guided prompts:
  - 🌟 Top wins today
  - 💡 What can I improve
  - ❤️ I'm grateful for
  - 📋 Tomorrow's top priority
- Rate your mood from 1 😞 to 10 ✨ using emoji buttons
- All past entries shown below (last 10 days) with mood icon

### 💬 Quotes Library
- 50 unique motivational quotes from great thinkers and leaders
- One quote is featured every day (rotates automatically based on date)
- 🎲 Random Quote button for instant inspiration anytime
- Full library listed so you can read them all

### ⚙️ Settings
- Export all your data as a JSON backup file
- Import a backup to restore your data
- Export habits and tasks as separate CSV files
- Reset all data (with double-confirm safety)
- Live data summary — see how many habits, tasks, goals, and journal entries you have

---

## 🚀 How to Install & Run

### Step 1 — Check if Python is installed

Open your terminal or command prompt and type:

```bash
python --version
```

You should see something like `Python 3.10.0`. If you see an error, download Python from the official website:

👉 **https://www.python.org/downloads/**

> ⚠️ **Important for Windows users:** During installation, check the box that says **"Add Python to PATH"** before clicking Install.

---

### Step 2 — Download ZENITH

**Option A — Download directly:**
1. Go to this GitHub repository
2. Click the green **`<> Code`** button
3. Click **`Download ZIP`**
4. Extract the ZIP file anywhere on your computer (e.g. `Desktop/ZENITH/`)

**Option B — Using Git:**
```bash
git clone https://github.com/yourusername/zenith-tracker.git
cd zenith-tracker
```

---

### Step 3 — Run the app

Navigate to the folder where you saved `zenith_tracker.py`:

```bash
cd Desktop/ZENITH
```

Then run:

```bash
# Windows
python zenith_tracker.py

# Mac / Linux
python3 zenith_tracker.py
```

**That's it. The app opens immediately. No pip install. No setup. Nothing else needed.**

---

### 🖱️ Windows shortcut (optional)

On Windows you can simply **double-click** `zenith_tracker.py` to launch it, as long as Python is installed and associated with `.py` files.

---

## 📋 System Requirements

| Requirement | Minimum |
|---|---|
| Python | 3.8 or higher |
| tkinter | Comes built into standard Python |
| RAM | ~50 MB |
| Disk Space | < 1 MB |
| Internet | ❌ Not required |

> **tkinter** is included with the official Python installer on Windows and Mac. On Linux it may need to be installed separately (see Troubleshooting below).

---

## 🔧 Troubleshooting

### ❓ "ModuleNotFoundError: No module named 'tkinter'"

This only happens on Linux. Fix it with one command:

```bash
# Ubuntu / Debian / Linux Mint
sudo apt-get install python3-tk

# Fedora / RHEL
sudo dnf install python3-tkinter

# Arch Linux
sudo pacman -S tk
```

---

### ❓ "python is not recognized as a command" (Windows)

Python is not added to your PATH. Two options:

**Option 1 — Reinstall Python:**
Download Python again from python.org and this time tick **"Add Python to PATH"** during setup.

**Option 2 — Try `py` instead:**
```bash
py zenith_tracker.py
```

---

### ❓ App opens but fonts look different

ZENITH uses `Palatino Linotype` and `Segoe UI` which are standard on Windows. On Mac/Linux, Python automatically falls back to a similar system font. The app will still work perfectly — only the font style may look slightly different.

---

### ❓ Double-clicking doesn't open the app (Windows)

Right-click `zenith_tracker.py` → **Open with** → **Python**. If Python isn't listed, browse to `C:\Users\YourName\AppData\Local\Programs\Python\PythonXXX\python.exe`.

---

## 💾 Your Data

All your data is saved automatically in a file called **`zenith_data.json`** in the same folder as `zenith_tracker.py`.

- Data saves on **every action** (ticking a habit, adding a task, etc.) and when you close the app
- To **back up** your data: go to ⚙️ Settings → Export All Data (JSON)
- To **move to another computer**: copy both `zenith_tracker.py` and `zenith_data.json`
- To **start fresh**: delete `zenith_data.json` or use Settings → Reset All Data

---

## 📁 Project Structure

```
zenith-tracker/
│
├── zenith_tracker.py    ← The entire app (single file)
├── zenith_data.json     ← Your data (auto-created on first run)
└── README.md            ← This file
```

---

## 🎨 Design & Theme

ZENITH uses a custom **"Obsidian Gold"** dark theme:

| Element | Color |
|---|---|
| Background | Deep black `#080C0E` |
| Cards | Dark teal-black `#0F1E24` |
| Primary Accent | Molten gold `#D4A843` |
| Highlights | Bright gold `#FFD700` |
| Success | Emerald green `#10B981` |
| Danger / Overdue | Ruby red `#F43F5E` |
| Text | Soft white `#E8F4F8` |

The sidebar features a **live animated starfield** with particles that shift between teal and gold colours.

---

## 🗺️ Roadmap — Coming Soon

- [ ] 📱 Reminder / notification system
- [ ] 📆 Weekly review report (auto-generated PDF)
- [ ] 🌙 Light theme option
- [ ] 🔒 Password / PIN lock for privacy
- [ ] 📤 Google Sheets sync (optional)
- [ ] 🏆 Achievement badges for milestones
- [ ] 📅 Habit scheduling (specific days of week)

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** this repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Commit: `git commit -m "Add: your feature description"`
5. Push: `git push origin feature/your-feature-name`
6. Open a **Pull Request**

Please keep code clean, well-commented, and test on Windows before submitting.

---

## 📄 License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute it.

```
MIT License — Copyright (c) 2026 ZENITH Contributors
Permission is granted to use, copy, modify, and distribute this software
for any purpose, with or without fee.
```

---

## 🙏 Acknowledgements

- Built with ❤️ using **Python** and **Tkinter**
- Quotes sourced from Aristotle, James Clear, Robin Sharma, Nelson Mandela, and many more great thinkers
- Inspired by the belief that **small daily actions create extraordinary lives**

---

<div align="center">

**✦ Start today. Track daily. Reach your ZENITH. ✦**

*"Success is the sum of small efforts repeated day in and day out."*
**— Robert Collier**

---

⭐ **If ZENITH helps you build better habits, please give it a star on GitHub!** ⭐

</div>
