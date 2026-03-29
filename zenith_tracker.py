"""
╔══════════════════════════════════════════════════════════════════╗
║        ✦ ZENITH — Advanced Habit & Life Goals Tracker ✦          ║
║              Python Desktop App  |  Premium Edition              ║
╚══════════════════════════════════════════════════════════════════╝
Run: python zenith_tracker.py
Requires: Python 3.8+  (tkinter built-in)
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json, os, datetime, random, math, threading, time, csv

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zenith_data.json")

# ══════════════════════════════════════════════════════════════════
#  QUOTES  (50 unique)
# ══════════════════════════════════════════════════════════════════
QUOTES = [
    ("We are what we repeatedly do. Excellence is not an act, but a habit.", "Aristotle"),
    ("Success is the sum of small efforts repeated day in and day out.", "Robert Collier"),
    ("Motivation gets you started. Habit keeps you going.", "Jim Ryun"),
    ("You don't rise to your goals — you fall to your systems.", "James Clear"),
    ("The secret of getting ahead is getting started.", "Mark Twain"),
    ("Discipline is choosing what you want most over what you want now.", "Abraham Lincoln"),
    ("Small daily improvements over time lead to stunning results.", "Robin Sharma"),
    ("Either you run the day, or the day runs you.", "Jim Rohn"),
    ("The difference between who you are and who you want to be is what you do.", "Unknown"),
    ("Champions are built one habit at a time.", "Unknown"),
    ("Push yourself — no one else is going to do it for you.", "Unknown"),
    ("Wake up with determination. Go to bed with satisfaction.", "Unknown"),
    ("Little by little, a little becomes a lot.", "Tanzanian Proverb"),
    ("It always seems impossible until it is done.", "Nelson Mandela"),
    ("Your only limit is your mind.", "Unknown"),
    ("Don't watch the clock — do what it does. Keep going.", "Sam Levenson"),
    ("Dream big. Start small. Act now.", "Robin Sharma"),
    ("Great things never come from comfort zones.", "Unknown"),
    ("You are one decision away from a completely different life.", "Unknown"),
    ("The best time to plant a tree was 20 years ago. The second best time is now.", "Chinese Proverb"),
    ("Success comes from what you do consistently, not occasionally.", "Marie Forleo"),
    ("A year from now you may wish you had started today.", "Karen Lamb"),
    ("Progress, not perfection.", "Unknown"),
    ("The only bad workout is the one that didn't happen.", "Unknown"),
    ("Invest in yourself. It pays the best interest.", "Benjamin Franklin"),
    ("Your future self is watching you right now through your memories.", "Unknown"),
    ("Focus on being productive instead of busy.", "Tim Ferriss"),
    ("Hard work beats talent when talent doesn't work hard.", "Tim Notke"),
    ("Energy and persistence conquer all things.", "Benjamin Franklin"),
    ("Fall seven times, stand up eight.", "Japanese Proverb"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("The mind is everything. What you think, you become.", "Buddha"),
    ("An unexamined life is not worth living.", "Socrates"),
    ("Do not wait; the time will never be just right.", "Napoleon Hill"),
    ("Strive not to be a success, but rather to be of value.", "Albert Einstein"),
    ("The secret to getting ahead is getting started.", "Agatha Christie"),
    ("Life is 10% what happens and 90% how you react to it.", "Charles Swindoll"),
    ("Quality is not an act, it is a habit.", "Aristotle"),
    ("You miss 100% of the shots you don't take.", "Wayne Gretzky"),
    ("Act as if what you do makes a difference. It does.", "William James"),
    ("Courage is resistance to fear, mastery of fear — not absence of fear.", "Mark Twain"),
    ("I have not failed. I've just found 10,000 ways that won't work.", "Thomas Edison"),
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("If you want to lift yourself up, lift up someone else.", "Booker T. Washington"),
    ("No one can make you feel inferior without your consent.", "Eleanor Roosevelt"),
    ("In the middle of every difficulty lies opportunity.", "Albert Einstein"),
    ("It is never too late to be what you might have been.", "George Eliot"),
    ("What you get by achieving your goals is not as important as what you become.", "Henry David Thoreau"),
    ("The two most important days are the day you were born and the day you find out why.", "Mark Twain"),
    ("Happiness is not something ready-made. It comes from your own actions.", "Dalai Lama"),
]

# ══════════════════════════════════════════════════════════════════
#  THEME — "Obsidian Gold" — Deep black-green with molten gold
# ══════════════════════════════════════════════════════════════════
T = {
    # Backgrounds
    "bg":        "#080C0E",
    "bg2":       "#0D1518",
    "bg3":       "#111C20",
    "card":      "#0F1E24",
    "card2":     "#162830",
    "card3":     "#1C3340",
    "hover":     "#1F3A47",
    # Accents
    "gold":      "#D4A843",
    "gold2":     "#F0C060",
    "gold3":     "#FFD980",
    "teal":      "#2DD4BF",
    "teal2":     "#14B8A6",
    "teal3":     "#0D9488",
    "emerald":   "#10B981",
    "emerald2":  "#059669",
    "ruby":      "#F43F5E",
    "ruby2":     "#E11D48",
    "amber":     "#F59E0B",
    "violet":    "#8B5CF6",
    "sky":       "#38BDF8",
    # Text
    "text":      "#E8F4F8",
    "text2":     "#A8C5CE",
    "text3":     "#5A8A96",
    "text4":     "#2D5A66",
    # Borders / dividers
    "border":    "#1A3040",
    "border2":   "#0F2530",
    "glow":      "#2DD4BF",
    # Status backgrounds
    "done_bg":   "#0A2018",
    "done_fg":   "#6EE7B7",
    "pend_bg":   "#0C1A28",
    "pend_fg":   "#93C5FD",
    "prog_bg":   "#1A1408",
    "prog_fg":   "#FCD34D",
    # Fonts
    "F_TITLE":   ("Palatino Linotype", 24, "bold"),
    "F_HEAD":    ("Palatino Linotype", 15, "bold"),
    "F_SUB":     ("Palatino Linotype", 12, "bold"),
    "F_BODY":    ("Segoe UI", 10),
    "F_SMALL":   ("Segoe UI", 9),
    "F_QUOTE":   ("Palatino Linotype", 13, "italic"),
    "F_MONO":    ("Consolas", 10),
    "F_BIG":     ("Palatino Linotype", 32, "bold"),
    "F_NUM":     ("Palatino Linotype", 20, "bold"),
    "F_MICRO":   ("Segoe UI", 8),
}

CAT_COLORS = {
    "Fitness":   "#10B981",
    "Health":    "#38BDF8",
    "Learning":  "#8B5CF6",
    "Wellness":  "#F472B6",
    "Work":      "#F59E0B",
    "Finance":   "#2DD4BF",
    "Social":    "#FB923C",
    "Creativity":"#A78BFA",
    "Other":     "#64748B",
}

PRIORITY_META = {
    "🔴 High":   ("#F43F5E", "#1A0810"),
    "🟡 Medium": ("#F59E0B", "#1A1208"),
    "🟢 Low":    ("#10B981", "#081A10"),
}

STATUS_META = {
    "Pending":     ("#93C5FD", "#0C1A28"),
    "In Progress": ("#FCD34D", "#1A1408"),
    "Done":        ("#6EE7B7", "#0A2018"),
    "Cancelled":   ("#94A3B8", "#111820"),
}

DEFAULT_HABITS = [
    {"id":1,"name":"🏃 Morning Exercise",       "category":"Fitness",  "target":7, "active":True, "note":""},
    {"id":2,"name":"💧 Drink 8 Glasses Water",  "category":"Health",   "target":7, "active":True, "note":""},
    {"id":3,"name":"📖 Read 30 Minutes",         "category":"Learning", "target":7, "active":True, "note":""},
    {"id":4,"name":"🧘 Meditate / Mindfulness", "category":"Wellness", "target":7, "active":True, "note":""},
    {"id":5,"name":"🥗 Eat Healthy Meals",       "category":"Health",   "target":5, "active":True, "note":""},
    {"id":6,"name":"📝 Journal / Reflect",       "category":"Wellness", "target":7, "active":True, "note":""},
    {"id":7,"name":"💻 Skill Learning",          "category":"Learning", "target":5, "active":True, "note":""},
    {"id":8,"name":"😴 Sleep 7-8 Hours",         "category":"Health",   "target":7, "active":True, "note":""},
    {"id":9,"name":"🚶 10,000 Steps",            "category":"Fitness",  "target":5, "active":True, "note":""},
    {"id":10,"name":"💰 Track Expenses",         "category":"Finance",  "target":7, "active":True, "note":""},
]

# ══════════════════════════════════════════════════════════════════
#  DATA LAYER
# ══════════════════════════════════════════════════════════════════
def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE,"r") as f: return json.load(f)
        except: pass
    return {
        "habits": DEFAULT_HABITS[:],
        "tasks": [],
        "goals": [],
        "completions": {},
        "daily_notes": {},
        "mood_log": {},
        "next_habit_id": 11,
        "next_task_id":  1,
        "next_goal_id":  1,
        "settings": {"theme": "obsidian", "show_motivations": True, "daily_target": 80},
    }

def save_data(data):
    with open(DATA_FILE,"w") as f:
        json.dump(data, f, indent=2)

def today_str():
    return datetime.date.today().isoformat()

def get_today_quote():
    doy = datetime.date.today().timetuple().tm_yday
    return QUOTES[doy % len(QUOTES)]

# ══════════════════════════════════════════════════════════════════
#  ANIMATED CANVAS BACKGROUND
# ══════════════════════════════════════════════════════════════════
class StarField:
    """
    Animated star background drawn on a Canvas that is placed
    inside the sidebar using .place() only — never .pack()/.grid().
    This avoids the Windows Tkinter geometry-manager conflict.
    """
    def __init__(self, root_app, parent, x, y, w, h):
        self._app     = root_app
        self._w, self._h = w, h
        self._running = False
        self._after_id = None

        self.canvas = tk.Canvas(parent, width=w, height=h,
                                bg=T["bg2"], highlightthickness=0)
        self.canvas.place(x=x, y=y, width=w, height=h)

        self._stars = []
        for _ in range(50):
            self._stars.append({
                "x":     random.uniform(0, w),
                "y":     random.uniform(0, h),
                "r":     random.uniform(0.6, 2.0),
                "speed": random.uniform(0.1, 0.45),
            })

        # Bind destroy so we stop cleanly
        self.canvas.bind("<Destroy>", self._on_destroy)
        # Start animation after the window is fully drawn
        self._app.after(200, self._start)

    def _start(self):
        self._running = True
        self._animate()

    def _on_destroy(self, event=None):
        self._running = False
        if self._after_id:
            try:
                self._app.after_cancel(self._after_id)
            except Exception:
                pass
        self._after_id = None

    def _animate(self):
        if not self._running:
            return
        try:
            if not self.canvas.winfo_exists():
                self._running = False
                return
            self.canvas.delete("star")
            for s in self._stars:
                s["y"] = (s["y"] + s["speed"]) % self._h
                phase = s["y"] / self._h
                if phase < 0.5:
                    r = int(45  + 120 * phase * 2)
                    g = int(180 -  60 * phase * 2)
                    b = int(191 -  80 * phase * 2)
                else:
                    r = int(165 + 45 * (phase - 0.5) * 2)
                    g = int(150 + 58 * (phase - 0.5) * 2)
                    b = int(111 - 80 * (phase - 0.5) * 2)
                col = (f"#{max(0,min(255,r)):02x}"
                       f"{max(0,min(255,g)):02x}"
                       f"{max(0,min(255,b)):02x}")
                self.canvas.create_oval(
                    s["x"]-s["r"], s["y"]-s["r"],
                    s["x"]+s["r"], s["y"]+s["r"],
                    fill=col, outline="", tags="star")
            self._after_id = self._app.after(60, self._animate)
        except tk.TclError:
            self._running = False

    def stop(self):
        self._running = False


# ══════════════════════════════════════════════════════════════════
#  CUSTOM WIDGETS
# ══════════════════════════════════════════════════════════════════
class GlowButton(tk.Frame):
    """Button with animated hover glow effect."""
    def __init__(self, parent, text, command=None,
                 bg=None, fg=None, glow_color=None,
                 font=None, padx=18, pady=8, **kw):
        super().__init__(parent, bg=parent["bg"] if hasattr(parent,"cget") else T["bg"],
                         cursor="hand2", **kw)
        self._bg       = bg or T["teal3"]
        self._fg       = fg or T["text"]
        self._glow     = glow_color or T["teal"]
        self._font     = font or T["F_BODY"]
        self._command  = command
        self._hovered  = False

        self._lbl = tk.Label(self, text=text, font=self._font,
                             bg=self._bg, fg=self._fg,
                             padx=padx, pady=pady, cursor="hand2",
                             highlightbackground=self._bg,
                             highlightthickness=1)
        self._lbl.pack()
        self._lbl.bind("<Enter>", self._on_enter)
        self._lbl.bind("<Leave>", self._on_leave)
        self._lbl.bind("<Button-1>", self._on_click)
        self.bind("<Button-1>", self._on_click)

    def _on_enter(self, e=None):
        self._lbl.config(bg=self._glow,
                         highlightbackground=self._glow,
                         highlightthickness=2)

    def _on_leave(self, e=None):
        self._lbl.config(bg=self._bg,
                         highlightbackground=self._bg,
                         highlightthickness=1)

    def _on_click(self, e=None):
        if self._command: self._command()


class TooltipMixin:
    """Add tooltip to any widget."""
    def add_tooltip(self, widget, text):
        tip = None
        def show(e):
            nonlocal tip
            tip = tk.Toplevel(widget)
            tip.wm_overrideredirect(True)
            tip.wm_geometry(f"+{e.x_root+12}+{e.y_root+12}")
            tk.Label(tip, text=text, font=T["F_SMALL"],
                     bg=T["card3"], fg=T["gold2"],
                     relief="flat", padx=8, pady=4,
                     highlightbackground=T["gold"],
                     highlightthickness=1).pack()
        def hide(e):
            nonlocal tip
            if tip: tip.destroy(); tip = None
        widget.bind("<Enter>", show)
        widget.bind("<Leave>", hide)


class CircularProgress(tk.Canvas):
    """Animated circular progress ring."""
    def __init__(self, parent, size=90, thickness=8,
                 bg=T["card"], fg=T["teal"], track=T["card2"], **kw):
        super().__init__(parent, width=size, height=size,
                         bg=bg, highlightthickness=0, **kw)
        self._size = size
        self._thick = thickness
        self._fg = fg
        self._track = track
        self._pct = 0
        self._target = 0
        self._draw()
        self._animate_to(0)

    def set_value(self, pct):
        self._target = min(100, max(0, pct))
        self._animate_to(self._target)

    def _animate_to(self, target):
        if abs(self._pct - target) < 0.5:
            self._pct = target; self._draw(); return
        self._pct += (target - self._pct) * 0.12
        self._draw()
        self.after(16, lambda: self._animate_to(target))

    def _draw(self):
        self.delete("all")
        pad = self._thick
        s = self._size
        # Track ring
        self.create_arc(pad, pad, s-pad, s-pad,
                        start=90, extent=360,
                        style="arc", outline=self._track, width=self._thick)
        # Progress ring
        if self._pct > 0:
            ext = -3.6 * self._pct
            self.create_arc(pad, pad, s-pad, s-pad,
                            start=90, extent=ext,
                            style="arc", outline=self._fg, width=self._thick)
        # Center text
        self.create_text(s//2, s//2,
                         text=f"{int(self._pct)}%",
                         font=("Palatino Linotype", int(s*0.18), "bold"),
                         fill=T["gold2"])


class HeatCell(tk.Frame):
    """Single day cell for heatmap."""
    def __init__(self, parent, date_str, pct, tooltip_text="", **kw):
        if pct >= 0.9:    bg = T["teal"];    fg = T["bg"]
        elif pct >= 0.6:  bg = T["teal3"];   fg = T["text"]
        elif pct >= 0.3:  bg = T["gold"];    fg = T["bg"]
        elif pct > 0:     bg = T["amber"];   fg = T["bg"]
        else:             bg = T["card3"];   fg = T["text3"]

        super().__init__(parent, bg=bg, width=28, height=28,
                         highlightbackground=T["border"],
                         highlightthickness=1, cursor="hand2", **kw)
        self.pack_propagate(False)
        day = datetime.date.fromisoformat(date_str).day
        lbl = tk.Label(self, text=str(day), font=T["F_MICRO"],
                       bg=bg, fg=fg, cursor="hand2")
        lbl.place(relx=0.5, rely=0.5, anchor="center")

        tip = None
        def show(e):
            nonlocal tip
            tip = tk.Toplevel(self)
            tip.wm_overrideredirect(True)
            tip.wm_geometry(f"+{e.x_root+8}+{e.y_root+8}")
            tk.Label(tip, text=tooltip_text or date_str,
                     font=T["F_SMALL"], bg=T["card3"], fg=T["gold2"],
                     padx=8, pady=4,
                     highlightbackground=T["gold"],
                     highlightthickness=1).pack()
        def hide(e):
            nonlocal tip
            if tip: tip.destroy(); tip = None
        self.bind("<Enter>", show); lbl.bind("<Enter>", show)
        self.bind("<Leave>", hide); lbl.bind("<Leave>", hide)


# ══════════════════════════════════════════════════════════════════
#  MAIN APPLICATION
# ══════════════════════════════════════════════════════════════════
class ZenithApp(tk.Tk, TooltipMixin):
    def __init__(self):
        super().__init__()
        self.title("✦ ZENITH — Habit & Life Goals Tracker")
        self.geometry("1280x820")
        self.minsize(1100, 700)
        self.configure(bg=T["bg"])
        self.resizable(True, True)

        self.data = load_data()
        self._tab  = tk.StringVar(value="dashboard")
        self._notification_queue = []

        self._build_ui()
        self._start_clock()
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _on_close(self):
        save_data(self.data)
        self.destroy()

    # ── GLOBAL UI LAYOUT ───────────────────────────────────────────
    def _build_ui(self):
        # Left sidebar
        self.sidebar = tk.Frame(self, bg=T["bg2"], width=230)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)
        self._build_sidebar()

        # Right: top notification bar + content
        right = tk.Frame(self, bg=T["bg"])
        right.pack(side="left", fill="both", expand=True)

        # Notification bar (hidden by default)
        self._notif_bar = tk.Frame(right, bg=T["teal3"], height=0)
        self._notif_bar.pack(fill="x")
        self._notif_lbl = tk.Label(self._notif_bar, text="",
                                   font=T["F_BODY"], bg=T["teal3"],
                                   fg=T["bg"], pady=6)
        self._notif_lbl.pack()

        # Page container
        self.content = tk.Frame(right, bg=T["bg"])
        self.content.pack(fill="both", expand=True)

        self.pages = {}
        for name in ("dashboard","habits","tasks","goals","analytics","journal","quotes","settings"):
            f = tk.Frame(self.content, bg=T["bg"])
            self.pages[name] = f
            f.place(relx=0, rely=0, relwidth=1, relheight=1)

        self._build_dashboard()
        self._build_habits_page()
        self._build_tasks_page()
        self._build_goals_page()
        self._build_analytics_page()
        self._build_journal_page()
        self._build_quotes_page()
        self._build_settings_page()
        self._switch_tab("dashboard")

    # ── SIDEBAR ────────────────────────────────────────────────────
    def _build_sidebar(self):
        # Animated starfield — uses .place() only, no pack/grid conflict
        self._starfield = StarField(self, self.sidebar, x=0, y=0, w=230, h=820)

        # ══ LOGO BLOCK — solid dark panel so stars never bleed into text ══
        # Panel covers y=0..144, full width
        logo_panel = tk.Frame(self.sidebar, bg=T["bg2"])
        logo_panel.place(x=0, y=0, width=230, height=144)

        # ✦  gold diamond icon
        tk.Label(logo_panel, text="✦",
                 font=("Palatino Linotype", 28, "bold"),
                 bg=T["bg2"], fg=T["gold"],
                 anchor="center").place(x=0, y=8, width=230, height=34)

        # ZENITH — large, bright white, bold, centred — no underline possible
        tk.Label(logo_panel, text="ZENITH",
                 font=("Palatino Linotype", 24, "bold"),
                 bg=T["bg2"], fg="#FFFFFF",
                 anchor="center").place(x=0, y=42, width=230, height=30)

        # Subtitle
        tk.Label(logo_panel, text="Habit & Life Goals Tracker",
                 font=("Segoe UI", 8),
                 bg=T["bg2"], fg=T["text3"],
                 anchor="center").place(x=0, y=74, width=230, height=16)

        # Clock  (no emoji prefix — clean digits only)
        self._clock_lbl = tk.Label(logo_panel, text="",
                                   font=("Consolas", 14, "bold"),
                                   bg=T["bg2"], fg=T["gold2"],
                                   anchor="center")
        self._clock_lbl.place(x=0, y=94, width=230, height=22)

        # Date
        self._date_lbl = tk.Label(logo_panel, text="",
                                  font=("Segoe UI", 8),
                                  bg=T["bg2"], fg=T["text3"],
                                  anchor="center")
        self._date_lbl.place(x=0, y=118, width=230, height=16)

        # ── Thin gold line below logo panel → above nav
        tk.Frame(self.sidebar, bg=T["gold"], height=1).place(x=16, y=143, width=198)

        # ── Navigation  8 rows × 44 px = 352 px  →  y=146 … y=498
        nav_items = [
            ("dashboard","🏠","Dashboard"),
            ("habits",   "✅","Daily Habits"),
            ("tasks",    "📋","Task Manager"),
            ("goals",    "🎯","Life Goals"),
            ("analytics","📊","Analytics"),
            ("journal",  "📓","Daily Journal"),
            ("quotes",   "💬","Quotes Library"),
            ("settings", "⚙️","Settings"),
        ]
        self._nav_btns = {}
        nav_y = 146
        for tab, icon, label in nav_items:
            btn = self._make_nav_btn(tab, icon, label, nav_y)
            self._nav_btns[tab] = btn
            nav_y += 44   # ends at y = 146 + 8×44 = 498

        # ── Thin gold line below nav  — y=500
        tk.Frame(self.sidebar, bg=T["gold"], height=1).place(x=16, y=500, width=198)

        # ══ Current Streak card  — y=510 … y=630  (height=112) ══════════
        # Outer border frame (gold, 2 px)
        streak_border = tk.Frame(self.sidebar, bg=T["gold"])
        streak_border.place(x=12, y=510, width=206, height=112)

        # Inner card (inset 2 px on each side)
        streak_inner = tk.Frame(streak_border, bg=T["card2"])
        streak_inner.place(x=2, y=2, width=202, height=108)

        # "🔥  CURRENT STREAK" header band
        header = tk.Frame(streak_inner, bg=T["card3"], height=26)
        header.place(x=0, y=0, width=202, height=26)
        tk.Label(header, text="🔥  CURRENT STREAK",
                 font=("Segoe UI", 8, "bold"),
                 bg=T["card3"], fg=T["gold"]).place(relx=0.5, rely=0.5, anchor="center")

        # Big number
        self._sidebar_streak_val = tk.Label(streak_inner, text="",
                                            font=("Palatino Linotype", 30, "bold"),
                                            bg=T["card2"], fg=T["gold2"])
        self._sidebar_streak_val.place(x=0, y=28, width=202)

        # "days" sub-label
        tk.Label(streak_inner, text="days in a row",
                 font=("Segoe UI", 8), bg=T["card2"],
                 fg=T["text3"]).place(x=0, y=74, width=202)

        # compat ref (not displayed)
        self._sidebar_streak_lbl = tk.Label(streak_inner, text="",
                                            bg=T["card2"], fg=T["card2"])
        self._sidebar_streak_lbl.place(x=0, y=0)

        self._update_sidebar_streak()

        # ── Version tag  — y=632
        tk.Label(self.sidebar, text="ZENITH v2.0  ✦  Premium",
                 font=T["F_MICRO"], bg=T["bg2"], fg=T["text4"]).place(x=0, y=634, width=230)

    def _make_nav_btn(self, tab, icon, label, y):
        f = tk.Frame(self.sidebar, bg=T["bg2"], height=44, cursor="hand2")
        f.place(x=0, y=y, width=230, height=44)

        accent_bar = tk.Frame(f, bg=T["bg2"], width=3)
        accent_bar.place(x=0, y=0, height=40)
        icon_lbl = tk.Label(f, text=icon, font=("Segoe UI Emoji", 13),
                            bg=T["bg2"], fg=T["text2"], cursor="hand2")
        icon_lbl.place(x=16, y=8)
        text_lbl = tk.Label(f, text=label, font=("Segoe UI", 11),
                            bg=T["bg2"], fg=T["text2"], anchor="w", cursor="hand2")
        text_lbl.place(x=44, y=9)

        widgets = [f, icon_lbl, text_lbl]
        def on_enter(e, ws=widgets, ab=accent_bar):
            for w in ws: w.config(bg=T["hover"])
            ab.config(bg=T["teal"])
        def on_leave(e, ws=widgets, ab=accent_bar, t=tab):
            is_active = self._tab.get() == t
            bg = T["card2"] if is_active else T["bg2"]
            ab_col = T["gold"] if is_active else T["bg2"]
            for w in ws: w.config(bg=bg)
            ab.config(bg=ab_col)
        def on_click(e, t=tab): self._switch_tab(t)
        for w in widgets:
            w.bind("<Enter>", on_enter)
            w.bind("<Leave>", on_leave)
            w.bind("<Button-1>", on_click)
        return (f, accent_bar, icon_lbl, text_lbl)

    def _switch_tab(self, tab):
        prev = self._tab.get()
        self._tab.set(tab)
        # Reset old
        if prev in self._nav_btns:
            f, ab, il, tl = self._nav_btns[prev]
            for w in (f, il, tl): w.config(bg=T["bg2"])
            ab.config(bg=T["bg2"])
        # Activate new
        if tab in self._nav_btns:
            f, ab, il, tl = self._nav_btns[tab]
            for w in (f, il, tl): w.config(bg=T["card2"])
            ab.config(bg=T["gold"])
        # Refresh content
        refreshers = {
            "dashboard":self._refresh_dashboard,
            "habits":   self._refresh_habits,
            "tasks":    self._refresh_tasks,
            "goals":    self._refresh_goals,
            "analytics":self._refresh_analytics,
            "journal":  self._refresh_journal,
            "quotes":   self._refresh_quotes,
            "settings": self._refresh_settings,
        }
        if tab in refreshers: refreshers[tab]()
        self.pages[tab].lift()

    # ── CLOCK ──────────────────────────────────────────────────────
    def _start_clock(self):
        def tick():
            now = datetime.datetime.now()
            self._clock_lbl.config(text=now.strftime("%H : %M : %S"))
            self._date_lbl.config(text=now.strftime("%A, %d %B %Y"))
            self.after(1000, tick)
        tick()

    def _update_sidebar_streak(self):
        s = self._calc_streak()
        self._sidebar_streak_val.config(text=f"{s} days")

    # ── NOTIFICATION ───────────────────────────────────────────────
    def _show_notification(self, msg, color=None):
        color = color or T["teal3"]
        self._notif_bar.config(bg=color, height=36)
        self._notif_lbl.config(text=msg, bg=color)
        self.after(3000, lambda: self._notif_bar.config(height=0))

    # ── SCROLLABLE CONTAINER ───────────────────────────────────────
    def _get_scroll(self, cv):
        """Return current scroll fraction of a canvas (0.0 – 1.0)."""
        try:
            return cv.yview()[0]
        except Exception:
            return 0.0

    def _set_scroll(self, cv, pos):
        """Restore scroll position after a refresh."""
        try:
            cv.update_idletasks()
            cv.yview_moveto(pos)
        except Exception:
            pass

    def _scrollable(self, parent):
        outer = tk.Frame(parent, bg=T["bg"])
        outer.pack(fill="both", expand=True)
        cv = tk.Canvas(outer, bg=T["bg"], highlightthickness=0)
        sb = ttk.Scrollbar(outer, orient="vertical", command=cv.yview)
        cv.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        cv.pack(side="left", fill="both", expand=True)
        inner = tk.Frame(cv, bg=T["bg"])
        wid = cv.create_window((0, 0), window=inner, anchor="nw")

        def _cfg(e):
            cv.configure(scrollregion=cv.bbox("all"))
            cv.itemconfig(wid, width=cv.winfo_width())
        def _resize(e):
            cv.itemconfig(wid, width=e.width)
        inner.bind("<Configure>", _cfg)
        cv.bind("<Configure>", _resize)

        # Scroll only when mouse is over THIS canvas (fixes jump-to-top bug)
        def _scroll_win(e):  cv.yview_scroll(int(-1*(e.delta/120)), "units")
        def _scroll_up(e):   cv.yview_scroll(-1, "units")   # Linux/trackpad
        def _scroll_dn(e):   cv.yview_scroll( 1, "units")

        def _bind_wheel(e=None):
            cv.bind_all("<MouseWheel>", _scroll_win)
            cv.bind_all("<Button-4>",   _scroll_up)
            cv.bind_all("<Button-5>",   _scroll_dn)
        def _unbind_wheel(e=None):
            try:
                cv.unbind_all("<MouseWheel>")
                cv.unbind_all("<Button-4>")
                cv.unbind_all("<Button-5>")
            except Exception:
                pass

        cv.bind("<Enter>",    _bind_wheel)
        cv.bind("<Leave>",    _unbind_wheel)
        inner.bind("<Enter>", _bind_wheel)
        return outer, cv, inner

    # ══════════════════════════════════════════════════════════════
    #  DASHBOARD
    # ══════════════════════════════════════════════════════════════
    def _build_dashboard(self):
        page = self.pages["dashboard"]
        # Header
        hdr = tk.Frame(page, bg=T["bg2"], pady=0)
        hdr.pack(fill="x")
        # Gold top bar
        tk.Frame(hdr, bg=T["gold"], height=3).pack(fill="x")
        inner_hdr = tk.Frame(hdr, bg=T["bg2"], pady=14)
        inner_hdr.pack(fill="x")
        tk.Label(inner_hdr, text="✦  ZENITH DASHBOARD",
                 font=T["F_TITLE"], bg=T["bg2"], fg=T["gold"]).pack(side="left", padx=24)
        self._dash_greeting = tk.Label(inner_hdr, text="", font=("Palatino Linotype",12,"italic"),
                                       bg=T["bg2"], fg=T["text3"])
        self._dash_greeting.pack(side="right", padx=24)
        _, self._dash_cv, self._dash_inner = self._scrollable(page)

    def _refresh_dashboard(self):
        for w in self._dash_inner.winfo_children(): w.destroy()
        inner = self._dash_inner

        # Greeting
        hr = datetime.datetime.now().hour
        greet = "Good Morning ☀️" if hr < 12 else "Good Afternoon 🌤" if hr < 18 else "Good Evening 🌙"
        self._dash_greeting.config(text=greet)

        today = today_str()
        completions_today = self.data["completions"].get(today, [])
        active_habits = [h for h in self.data["habits"] if h["active"]]
        done_count = sum(1 for h in active_habits if h["id"] in completions_today)
        total = len(active_habits)
        pct = int(done_count/total*100) if total else 0
        streak = self._calc_streak()
        open_tasks = len([t for t in self.data["tasks"] if t.get("status") not in ("Done","Cancelled")])
        goals_active = len([g for g in self.data["goals"] if g.get("status")!="Completed"])

        # ── Quote ──────────────────────────────────────────────────
        q_text, q_author = get_today_quote()
        qf = tk.Frame(inner, bg=T["bg3"],
                      highlightbackground=T["gold"], highlightthickness=1)
        qf.pack(fill="x", padx=20, pady=(18,6))
        tk.Frame(qf, bg=T["gold"], height=2).pack(fill="x")
        q_inner = tk.Frame(qf, bg=T["bg3"], padx=24, pady=14)
        q_inner.pack(fill="x")
        tk.Label(q_inner, text="✦  QUOTE OF THE DAY",
                 font=("Segoe UI",9,"bold"), bg=T["bg3"], fg=T["gold"]).pack(anchor="w")
        tk.Label(q_inner, text=f'"{q_text}"',
                 font=T["F_QUOTE"], bg=T["bg3"], fg=T["text"],
                 wraplength=920, justify="left").pack(anchor="w", pady=(8,4))
        tk.Label(q_inner, text=f"— {q_author}",
                 font=("Segoe UI",10,"bold"), bg=T["bg3"], fg=T["gold2"]).pack(anchor="e")
        tk.Frame(qf, bg=T["gold"], height=2).pack(fill="x")

        # ── KPI Row ─────────────────────────────────────────────────
        kpi_row = tk.Frame(inner, bg=T["bg"])
        kpi_row.pack(fill="x", padx=20, pady=8)
        kpis = [
            ("✅ Done Today",   f"{done_count}/{total}",  T["emerald"],  T["done_bg"]),
            ("🔥 Streak",       f"{streak}d",             T["gold2"],    T["bg3"]),
            ("📋 Open Tasks",   str(open_tasks),          T["sky"],      T["pend_bg"]),
            ("🎯 Active Goals", str(goals_active),        T["violet"],   T["card"]),
            ("📊 Today %",      f"{pct}%",                T["teal"],     T["card2"]),
        ]
        for lbl, val, fg, bg in kpis:
            kf = tk.Frame(kpi_row, bg=bg, padx=10, pady=12,
                          highlightbackground=T["border"], highlightthickness=1)
            kf.pack(side="left", expand=True, fill="x", padx=4)
            tk.Label(kf, text=val, font=T["F_BIG"], bg=bg, fg=fg).pack()
            tk.Label(kf, text=lbl, font=T["F_SMALL"], bg=bg, fg=T["text3"]).pack()

        # ── Progress section ────────────────────────────────────────
        prog_section = tk.Frame(inner, bg=T["bg"])
        prog_section.pack(fill="x", padx=20, pady=4)

        # Circular progress
        cp_frame = tk.Frame(prog_section, bg=T["card"],
                            highlightbackground=T["border"], highlightthickness=1,
                            padx=16, pady=14)
        cp_frame.pack(side="left", fill="y", padx=(0,6))
        tk.Label(cp_frame, text="Today's Progress",
                 font=T["F_SUB"], bg=T["card"], fg=T["gold"]).pack()
        cp_color = T["emerald"] if pct>=80 else T["teal"] if pct>=50 else T["amber"]
        circ = CircularProgress(cp_frame, size=110, thickness=10,
                                bg=T["card"], fg=cp_color)
        circ.pack(pady=6)
        circ.set_value(pct)

        # Weekly heat strip
        heat_frame = tk.Frame(prog_section, bg=T["card"],
                              highlightbackground=T["border"], highlightthickness=1,
                              padx=16, pady=14)
        heat_frame.pack(side="left", fill="both", expand=True, padx=6)
        tk.Label(heat_frame, text="📆  This Week",
                 font=T["F_SUB"], bg=T["card"], fg=T["gold"]).pack(anchor="w")
        week_row = tk.Frame(heat_frame, bg=T["card"])
        week_row.pack(anchor="w", pady=8)
        for i in range(6, -1, -1):
            d = (datetime.date.today() - datetime.timedelta(days=i)).isoformat()
            cnt = len(self.data["completions"].get(d, []))
            p = cnt / max(total, 1)
            day_name = datetime.date.fromisoformat(d).strftime("%a")
            df = tk.Frame(week_row, bg=T["card"])
            df.pack(side="left", padx=3)
            hc = HeatCell(df, d, p, f"{day_name}: {cnt}/{total} habits")
            hc.pack()
            tk.Label(df, text=day_name[:2], font=T["F_MICRO"],
                     bg=T["card"], fg=T["text3"]).pack()

        # ── Today's Habits ──────────────────────────────────────────
        tk.Label(inner, text="✦  TODAY'S HABITS",
                 font=T["F_HEAD"], bg=T["bg"], fg=T["gold"]).pack(anchor="w", padx=22, pady=(16,4))

        if not active_habits:
            tk.Label(inner, text="No habits yet. Go to Daily Habits to add some! ✨",
                     font=T["F_BODY"], bg=T["bg"], fg=T["text3"]).pack(padx=24)

        for habit in active_habits:
            done = habit["id"] in completions_today
            self._dash_habit_row(inner, habit, done)

        # ── Overdue / Upcoming Tasks ────────────────────────────────
        tk.Label(inner, text="✦  UPCOMING TASKS",
                 font=T["F_HEAD"], bg=T["bg"], fg=T["gold"]).pack(anchor="w", padx=22, pady=(16,4))
        upcoming = sorted(
            [t for t in self.data["tasks"] if t.get("status") not in ("Done","Cancelled")],
            key=lambda t: t.get("due_date","9999")
        )[:6]
        if not upcoming:
            tk.Label(inner, text="All clear! No pending tasks 🎉",
                     font=T["F_BODY"], bg=T["bg"], fg=T["text3"]).pack(padx=24)
        for t in upcoming:
            self._mini_task_row(inner, t)

        tk.Frame(inner, bg=T["bg"], height=40).pack()

    def _dash_habit_row(self, parent, habit, done):
        row_bg = T["done_bg"] if done else T["card"]
        cat_col = CAT_COLORS.get(habit.get("category","Other"), T["teal"])
        row = tk.Frame(parent, bg=row_bg, padx=0, pady=0,
                       highlightbackground=T["border"], highlightthickness=1,
                       cursor="hand2")
        row.pack(fill="x", padx=20, pady=2)

        # Left category stripe
        tk.Frame(row, bg=cat_col, width=4).pack(side="left", fill="y")

        content = tk.Frame(row, bg=row_bg, padx=12, pady=10)
        content.pack(side="left", fill="x", expand=True)

        tick = tk.Label(content, text="✅" if done else "○",
                        font=("Segoe UI Emoji", 18), bg=row_bg,
                        fg=T["done_fg"] if done else T["text3"], cursor="hand2")
        tick.pack(side="left", padx=(0,12))

        name_fg = T["done_fg"] if done else T["text"]
        name_font = ("Segoe UI",11) if done else ("Segoe UI",11,"bold")
        name_lbl = tk.Label(content, text=habit["name"],
                            font=name_font, bg=row_bg, fg=name_fg, anchor="w")
        name_lbl.pack(side="left", fill="x", expand=True)

        h_streak = self._habit_streak(habit["id"])
        if h_streak > 0:
            tk.Label(content, text=f"🔥{h_streak}d",
                     font=("Segoe UI",9,"bold"), bg=row_bg, fg=T["gold2"]).pack(side="right", padx=6)

        cat_tag = tk.Label(content, text=habit.get("category","Other"),
                           font=("Segoe UI",8,"bold"),
                           bg=cat_col, fg=T["bg"], padx=8, pady=2)
        cat_tag.pack(side="right", padx=4)

        def toggle(hid=habit["id"]):
            _pos = self._get_scroll(self._dash_cv)
            self._toggle_habit(hid)
            self._refresh_dashboard()
            self._update_sidebar_streak()
            self.after(10, lambda: self._set_scroll(self._dash_cv, _pos))
            done_now = hid in self.data["completions"].get(today_str(), [])
            msg = f"✅ Habit marked done!" if done_now else "☐ Habit unmarked."
            self._show_notification(msg, T["emerald2"] if done_now else T["card3"])

        for w in (row, content, tick, name_lbl):
            w.bind("<Button-1>", lambda e, fn=toggle: fn())

    def _mini_task_row(self, parent, task):
        status = task.get("status","Pending")
        pri = task.get("priority","🟡 Medium")
        pri_col = PRIORITY_META.get(pri, (T["teal"], T["card"]))[0]
        st_fg, st_bg = STATUS_META.get(status, (T["text2"], T["card"]))

        row = tk.Frame(parent, bg=T["card"], padx=0,
                       highlightbackground=T["border"], highlightthickness=1)
        row.pack(fill="x", padx=20, pady=2)
        tk.Frame(row, bg=pri_col, width=4).pack(side="left", fill="y")
        inner = tk.Frame(row, bg=T["card"], padx=12, pady=8)
        inner.pack(side="left", fill="x", expand=True)
        tk.Label(inner, text=task["name"], font=("Segoe UI",10,"bold"),
                 bg=T["card"], fg=T["text"], anchor="w").pack(side="left")
        meta = []
        if task.get("due_date"): meta.append(f"📅 {task['due_date']}")
        if task.get("due_time"): meta.append(f"⏰ {task['due_time']}")
        if meta:
            tk.Label(inner, text="  ".join(meta), font=T["F_SMALL"],
                     bg=T["card"], fg=T["text3"]).pack(side="left", padx=8)
        tk.Label(inner, text=status, font=("Segoe UI",8,"bold"),
                 bg=st_bg, fg=st_fg, padx=6, pady=2).pack(side="right")

    # ══════════════════════════════════════════════════════════════
    #  HABITS PAGE
    # ══════════════════════════════════════════════════════════════
    def _build_habits_page(self):
        page = self.pages["habits"]
        hdr = tk.Frame(page, bg=T["bg2"])
        hdr.pack(fill="x")
        tk.Frame(hdr, bg=T["gold"], height=3).pack(fill="x")
        inner_hdr = tk.Frame(hdr, bg=T["bg2"], pady=14)
        inner_hdr.pack(fill="x")
        tk.Label(inner_hdr, text="✅  DAILY HABITS",
                 font=T["F_TITLE"], bg=T["bg2"], fg=T["gold"]).pack(side="left", padx=24)
        btn_row = tk.Frame(inner_hdr, bg=T["bg2"])
        btn_row.pack(side="right", padx=24)
        GlowButton(btn_row, "＋  Add Habit", command=self._add_habit_dialog,
                   bg=T["teal3"], glow_color=T["teal"],
                   font=("Segoe UI",10,"bold")).pack(side="left", padx=4)
        GlowButton(btn_row, "📤  Export CSV", command=self._export_habits_csv,
                   bg=T["card3"], glow_color=T["gold"],
                   font=("Segoe UI",10,"bold")).pack(side="left", padx=4)
        _, self._habits_cv, self._habits_inner = self._scrollable(page)

    def _refresh_habits(self, _scroll_pos=None):
        _pos = _scroll_pos if _scroll_pos is not None else self._get_scroll(self._habits_cv)
        for w in self._habits_inner.winfo_children(): w.destroy()
        inner = self._habits_inner
        today = today_str()
        completions_today = self.data["completions"].get(today, [])
        active = [h for h in self.data["habits"] if h["active"]]

        # ── 7-day heat strip ───────────────────────────────────────
        heat_card = tk.Frame(inner, bg=T["card"], padx=20, pady=14,
                             highlightbackground=T["border"], highlightthickness=1)
        heat_card.pack(fill="x", padx=20, pady=(16,6))
        tk.Label(heat_card, text="📆  7-DAY OVERVIEW",
                 font=T["F_SUB"], bg=T["card"], fg=T["gold"]).pack(anchor="w")
        strip = tk.Frame(heat_card, bg=T["card"])
        strip.pack(anchor="w", pady=8)
        total = max(len(active), 1)
        for i in range(6,-1,-1):
            d = (datetime.date.today()-datetime.timedelta(days=i)).isoformat()
            cnt = len(self.data["completions"].get(d,[]))
            p = cnt / total
            day_name = datetime.date.fromisoformat(d).strftime("%A")[:3]
            df = tk.Frame(strip, bg=T["card"])
            df.pack(side="left", padx=4)
            HeatCell(df, d, p, f"{day_name}: {cnt}/{total}").pack()
            tk.Label(df, text=day_name, font=T["F_MICRO"],
                     bg=T["card"], fg=T["text3"]).pack()

        # ── Per-category progress ──────────────────────────────────
        cats = {}
        for h in active:
            c = h.get("category","Other")
            done = h["id"] in completions_today
            cats.setdefault(c, [0,0])
            cats[c][1] += 1
            if done: cats[c][0] += 1

        if cats:
            tk.Label(inner, text="✦  BY CATEGORY",
                     font=T["F_HEAD"], bg=T["bg"], fg=T["gold"]).pack(anchor="w", padx=22, pady=(12,4))
            cat_row = tk.Frame(inner, bg=T["bg"])
            cat_row.pack(fill="x", padx=20, pady=2)
            for cat, (done_c, total_c) in cats.items():
                pct = int(done_c/total_c*100)
                col = CAT_COLORS.get(cat, T["teal"])
                cf = tk.Frame(cat_row, bg=T["card"], padx=10, pady=8,
                              highlightbackground=T["border"], highlightthickness=1)
                cf.pack(side="left", expand=True, fill="x", padx=3)
                tk.Label(cf, text=cat, font=("Segoe UI",9,"bold"),
                         bg=T["card"], fg=col).pack()
                tk.Label(cf, text=f"{done_c}/{total_c}",
                         font=("Palatino Linotype",14,"bold"),
                         bg=T["card"], fg=T["text"]).pack()
                # mini bar
                bar_bg = tk.Frame(cf, bg=T["bg3"], height=6)
                bar_bg.pack(fill="x", pady=2)
                bar_bg.update_idletasks()
                if pct > 0:
                    tk.Frame(bar_bg, bg=col, height=6,
                             width=max(4, int(bar_bg.winfo_reqwidth()*pct/100))).place(x=0,y=0)

        # ── Habits list ────────────────────────────────────────────
        tk.Label(inner, text="✦  ALL HABITS  —  click row to toggle",
                 font=T["F_HEAD"], bg=T["bg"], fg=T["gold"]).pack(anchor="w", padx=22, pady=(16,4))

        for habit in self.data["habits"]:
            if not habit["active"]: continue
            done = habit["id"] in completions_today
            cat_col = CAT_COLORS.get(habit.get("category","Other"), T["teal"])
            row_bg = T["done_bg"] if done else T["card"]

            row = tk.Frame(inner, bg=row_bg,
                           highlightbackground=T["border"], highlightthickness=1,
                           cursor="hand2")
            row.pack(fill="x", padx=20, pady=3)

            # Category stripe
            tk.Frame(row, bg=cat_col, width=5).pack(side="left", fill="y")

            content = tk.Frame(row, bg=row_bg, padx=12, pady=12)
            content.pack(side="left", fill="x", expand=True)

            tick_lbl = tk.Label(content, text="✅" if done else "○",
                                font=("Segoe UI Emoji",20), bg=row_bg,
                                fg=T["done_fg"] if done else T["text3"])
            tick_lbl.pack(side="left", padx=(0,14))

            info = tk.Frame(content, bg=row_bg)
            info.pack(side="left", fill="x", expand=True)
            name_col = T["done_fg"] if done else T["text"]
            tk.Label(info, text=habit["name"],
                     font=("Segoe UI",11,"bold" if not done else "normal"),
                     bg=row_bg, fg=name_col, anchor="w").pack(anchor="w")
            if habit.get("note"):
                tk.Label(info, text=habit["note"], font=T["F_SMALL"],
                         bg=row_bg, fg=T["text3"], anchor="w").pack(anchor="w")

            # Right side stats
            right_f = tk.Frame(content, bg=row_bg)
            right_f.pack(side="right")

            h_streak = self._habit_streak(habit["id"])
            best     = self._habit_best_streak(habit["id"])
            tk.Label(right_f, text=f"🔥 {h_streak}d  ⭐ best {best}d",
                     font=("Segoe UI",9,"bold"), bg=row_bg, fg=T["gold2"]).pack(side="top", anchor="e")

            btn_row = tk.Frame(right_f, bg=row_bg)
            btn_row.pack(side="top", anchor="e", pady=4)
            tk.Label(btn_row, text=habit.get("category","Other"),
                     font=("Segoe UI",8,"bold"),
                     bg=cat_col, fg=T["bg"], padx=8, pady=2).pack(side="left", padx=2)
            tk.Button(btn_row, text="✏", font=("Segoe UI",9),
                      bg=T["bg3"], fg=T["text2"], relief="flat", cursor="hand2",
                      command=lambda h=habit: self._edit_habit_dialog(h)).pack(side="left", padx=2)
            tk.Button(btn_row, text="✕", font=("Segoe UI",9),
                      bg=T["bg3"], fg=T["ruby"], relief="flat", cursor="hand2",
                      command=lambda hid=habit["id"]: self._delete_habit(hid)).pack(side="left", padx=2)

            def toggle(hid=habit["id"]):
                _pos = self._get_scroll(self._habits_cv)
                self._toggle_habit(hid)
                self._refresh_habits(_scroll_pos=_pos)
                self._update_sidebar_streak()

            for w in (row, content, tick_lbl, info):
                if not isinstance(w, tk.Button):
                    w.bind("<Button-1>", lambda e, fn=toggle: fn())

        # Inactive habits section
        inactive = [h for h in self.data["habits"] if not h["active"]]
        if inactive:
            tk.Label(inner, text="⬜  ARCHIVED HABITS",
                     font=T["F_SUB"], bg=T["bg"], fg=T["text3"]).pack(anchor="w", padx=22, pady=(16,4))
            for habit in inactive:
                row = tk.Frame(inner, bg=T["bg3"], padx=16, pady=8,
                               highlightbackground=T["border2"], highlightthickness=1)
                row.pack(fill="x", padx=20, pady=2)
                tk.Label(row, text=habit["name"], font=("Segoe UI",10),
                         bg=T["bg3"], fg=T["text3"]).pack(side="left")
                tk.Button(row, text="Restore", font=("Segoe UI",9),
                          bg=T["card3"], fg=T["teal"], relief="flat", cursor="hand2",
                          command=lambda hid=habit["id"]: self._restore_habit(hid)).pack(side="right")

        tk.Frame(inner, bg=T["bg"], height=40).pack()
        self.after(10, lambda: self._set_scroll(self._habits_cv, _pos))

    def _add_habit_dialog(self, habit=None):
        editing = habit is not None
        dlg = tk.Toplevel(self)
        dlg.title("Edit Habit" if editing else "Add New Habit")
        dlg.geometry("480x380")
        dlg.configure(bg=T["bg"])
        dlg.grab_set()
        tk.Frame(dlg, bg=T["gold"], height=3).pack(fill="x")
        tk.Label(dlg, text="✏️  Edit Habit" if editing else "✦  New Habit",
                 font=T["F_HEAD"], bg=T["bg"], fg=T["gold"]).pack(pady=(16,4))

        fields = {}
        for lbl, key, default, wtype, opts in [
            ("Habit Name",   "name",     habit["name"] if editing else "",            "entry", None),
            ("Category",     "category", habit.get("category","Fitness") if editing else "Fitness", "combo", list(CAT_COLORS.keys())),
            ("Weekly Target","target",   str(habit.get("target",7)) if editing else "7", "combo", ["1","2","3","4","5","6","7"]),
            ("Note/Reminder","note",     habit.get("note","") if editing else "",     "entry", None),
        ]:
            tk.Label(dlg, text=lbl, font=T["F_BODY"],
                     bg=T["bg"], fg=T["text2"]).pack(anchor="w", padx=30, pady=(6,0))
            if wtype == "entry":
                var = tk.StringVar(value=default)
                tk.Entry(dlg, textvariable=var, font=T["F_BODY"],
                         bg=T["card"], fg=T["text"], insertbackground=T["text"],
                         relief="flat", width=42, highlightbackground=T["border"],
                         highlightthickness=1).pack(padx=30, pady=2, ipady=6)
                fields[key] = var
            else:
                var = tk.StringVar(value=default)
                ttk.Combobox(dlg, textvariable=var, values=opts, width=40).pack(padx=30, pady=2)
                fields[key] = var

        def save():
            name = fields["name"].get().strip()
            if not name:
                messagebox.showwarning("Empty","Habit name cannot be empty.",parent=dlg); return
            if editing:
                habit["name"]     = name
                habit["category"] = fields["category"].get()
                habit["target"]   = int(fields["target"].get() or 7)
                habit["note"]     = fields["note"].get().strip()
            else:
                nid = self.data["next_habit_id"]
                self.data["habits"].append({
                    "id": nid, "name": name,
                    "category": fields["category"].get(),
                    "target":   int(fields["target"].get() or 7),
                    "active":   True,
                    "note":     fields["note"].get().strip(),
                })
                self.data["next_habit_id"] += 1
            save_data(self.data)
            dlg.destroy()
            self._refresh_habits()
            self._show_notification("✅ Habit saved!", T["emerald2"])

        GlowButton(dlg, "  Save Habit  ", command=save,
                   bg=T["teal3"], glow_color=T["teal"],
                   font=("Segoe UI",11,"bold")).pack(pady=16)

    def _edit_habit_dialog(self, habit): self._add_habit_dialog(habit=habit)

    def _delete_habit(self, hid):
        if messagebox.askyesno("Archive","Archive this habit? (Can be restored later)"):
            for h in self.data["habits"]:
                if h["id"] == hid: h["active"] = False; break
            save_data(self.data); self._refresh_habits()

    def _restore_habit(self, hid):
        for h in self.data["habits"]:
            if h["id"] == hid: h["active"] = True; break
        save_data(self.data); self._refresh_habits()

    def _toggle_habit(self, hid):
        today = today_str()
        if today not in self.data["completions"]:
            self.data["completions"][today] = []
        lst = self.data["completions"][today]
        if hid in lst: lst.remove(hid)
        else:          lst.append(hid)
        save_data(self.data)

    def _export_habits_csv(self):
        fp = filedialog.asksaveasfilename(defaultextension=".csv",
                                          filetypes=[("CSV","*.csv")],
                                          initialfile="habits_export.csv")
        if not fp: return
        rows = []
        days = [(datetime.date.today()-datetime.timedelta(days=i)).isoformat() for i in range(29,-1,-1)]
        for h in self.data["habits"]:
            if not h["active"]: continue
            count = sum(1 for d in days if h["id"] in self.data["completions"].get(d,[]))
            rows.append({"Name":h["name"],"Category":h.get("category",""),
                         "Streak":self._habit_streak(h["id"]),
                         "30-Day Count":count,
                         "30-Day %":f"{count/30*100:.1f}%"})
        with open(fp,"w",newline="") as f:
            w = csv.DictWriter(f, fieldnames=rows[0].keys())
            w.writeheader(); w.writerows(rows)
        self._show_notification(f"✅ Exported to {os.path.basename(fp)}", T["emerald2"])

    # ══════════════════════════════════════════════════════════════
    #  TASKS PAGE
    # ══════════════════════════════════════════════════════════════
    def _build_tasks_page(self):
        page = self.pages["tasks"]
        hdr = tk.Frame(page, bg=T["bg2"])
        hdr.pack(fill="x")
        tk.Frame(hdr, bg=T["gold"], height=3).pack(fill="x")
        inner_hdr = tk.Frame(hdr, bg=T["bg2"], pady=14)
        inner_hdr.pack(fill="x")
        tk.Label(inner_hdr, text="📋  TASK MANAGER",
                 font=T["F_TITLE"], bg=T["bg2"], fg=T["gold"]).pack(side="left", padx=24)
        btn_row = tk.Frame(inner_hdr, bg=T["bg2"])
        btn_row.pack(side="right", padx=24)
        GlowButton(btn_row, "＋  Add Task", command=self._add_task_dialog,
                   bg=T["teal3"], glow_color=T["teal"],
                   font=("Segoe UI",10,"bold")).pack(side="left", padx=4)
        GlowButton(btn_row, "📤  Export", command=self._export_tasks_csv,
                   bg=T["card3"], glow_color=T["gold"],
                   font=("Segoe UI",10,"bold")).pack(side="left", padx=4)

        # Filter bar
        fbar = tk.Frame(page, bg=T["bg3"], pady=8)
        fbar.pack(fill="x")
        tk.Label(fbar, text="  Filter:", font=T["F_BODY"],
                 bg=T["bg3"], fg=T["text3"]).pack(side="left", padx=12)
        self._task_filter = tk.StringVar(value="All")
        for fv in ("All","Pending","In Progress","Done","Cancelled","Overdue"):
            rb = tk.Radiobutton(fbar, text=fv, variable=self._task_filter,
                                value=fv, bg=T["bg3"], fg=T["text2"],
                                selectcolor=T["teal3"], activebackground=T["bg3"],
                                font=T["F_BODY"], cursor="hand2",
                                command=self._refresh_tasks)
            rb.pack(side="left", padx=8)

        self._task_sort = tk.StringVar(value="Priority")
        tk.Label(fbar, text="Sort:", font=T["F_BODY"],
                 bg=T["bg3"], fg=T["text3"]).pack(side="left", padx=(20,4))
        ttk.Combobox(fbar, textvariable=self._task_sort, width=12,
                     values=["Priority","Due Date","Status","Name"],
                     state="readonly").pack(side="left")
        tk.Button(fbar, text="Go", font=T["F_SMALL"],
                  bg=T["card3"], fg=T["teal"], relief="flat",
                  command=self._refresh_tasks).pack(side="left", padx=4)

        _, self._tasks_cv, self._tasks_inner = self._scrollable(page)

    def _refresh_tasks(self):
        for w in self._tasks_inner.winfo_children(): w.destroy()
        inner = self._tasks_inner
        filt  = self._task_filter.get()
        sort  = self._task_sort.get() if hasattr(self,"_task_sort") else "Priority"
        today = today_str()

        tasks = list(self.data["tasks"])
        if filt == "Overdue":
            tasks = [t for t in tasks if t.get("due_date","") < today
                     and t.get("status") not in ("Done","Cancelled")]
        elif filt != "All":
            tasks = [t for t in tasks if t.get("status","Pending") == filt]

        if sort == "Priority":
            order = {"🔴 High":0,"🟡 Medium":1,"🟢 Low":2}
            tasks.sort(key=lambda t: order.get(t.get("priority","🟡 Medium"),1))
        elif sort == "Due Date":
            tasks.sort(key=lambda t: t.get("due_date","9999"))
        elif sort == "Status":
            tasks.sort(key=lambda t: t.get("status","Pending"))
        elif sort == "Name":
            tasks.sort(key=lambda t: t.get("name",""))

        # Stats strip
        all_tasks = self.data["tasks"]
        counts = {s: sum(1 for t in all_tasks if t.get("status","Pending")==s)
                  for s in ("Pending","In Progress","Done","Cancelled")}
        overdue = sum(1 for t in all_tasks if t.get("due_date","") < today
                      and t.get("status") not in ("Done","Cancelled"))

        stats_f = tk.Frame(inner, bg=T["card"], padx=16, pady=12,
                           highlightbackground=T["border"], highlightthickness=1)
        stats_f.pack(fill="x", padx=20, pady=(16,4))
        stat_items = [
            ("Total",       len(all_tasks), T["text"]),
            ("Pending",     counts["Pending"],     T["sky"]),
            ("In Progress", counts["In Progress"], T["amber"]),
            ("Done",        counts["Done"],         T["emerald"]),
            ("Overdue",     overdue,               T["ruby"]),
        ]
        for lbl, val, col in stat_items:
            sf = tk.Frame(stats_f, bg=T["card"])
            sf.pack(side="left", expand=True)
            tk.Label(sf, text=str(val), font=T["F_NUM"], bg=T["card"], fg=col).pack()
            tk.Label(sf, text=lbl, font=T["F_SMALL"], bg=T["card"], fg=T["text3"]).pack()

        if not tasks:
            tk.Label(inner, text="No tasks match this filter 🎉",
                     font=T["F_BODY"], bg=T["bg"], fg=T["text3"]).pack(pady=30)
            return

        tk.Label(inner, text=f"✦  TASKS  ({len(tasks)} shown)",
                 font=T["F_HEAD"], bg=T["bg"], fg=T["gold"]).pack(anchor="w", padx=22, pady=(12,4))

        for task in tasks:
            self._full_task_row(inner, task, today)

        tk.Frame(inner, bg=T["bg"], height=40).pack()

    def _full_task_row(self, parent, task, today=""):
        status = task.get("status","Pending")
        pri    = task.get("priority","🟡 Medium")
        pri_col, pri_bg = PRIORITY_META.get(pri, (T["teal"], T["card"]))
        st_fg, st_bg    = STATUS_META.get(status, (T["text2"], T["card"]))
        overdue = (task.get("due_date","") < (today or today_str())
                   and status not in ("Done","Cancelled"))
        row_bg = T["done_bg"] if status == "Done" else (
                 "#1A0508" if overdue else T["card"])

        row = tk.Frame(parent, bg=row_bg,
                       highlightbackground=T["ruby"] if overdue else T["border"],
                       highlightthickness=1)
        row.pack(fill="x", padx=20, pady=3)
        tk.Frame(row, bg=pri_col, width=5).pack(side="left", fill="y")

        content = tk.Frame(row, bg=row_bg, padx=12, pady=10)
        content.pack(side="left", fill="x", expand=True)

        top_row = tk.Frame(content, bg=row_bg)
        top_row.pack(fill="x")

        name_col = T["done_fg"] if status=="Done" else (T["ruby"] if overdue else T["text"])
        tk.Label(top_row, text=task["name"],
                 font=("Segoe UI",11,"bold"), bg=row_bg, fg=name_col,
                 anchor="w").pack(side="left")
        if overdue:
            tk.Label(top_row, text="⚠ OVERDUE", font=("Segoe UI",9,"bold"),
                     bg="#3A0810", fg=T["ruby"], padx=6, pady=1).pack(side="left", padx=8)

        meta_row = tk.Frame(content, bg=row_bg)
        meta_row.pack(fill="x", pady=2)
        meta_parts = []
        if task.get("due_date"): meta_parts.append(f"📅 {task['due_date']}")
        if task.get("due_time"): meta_parts.append(f"⏰ {task['due_time']}")
        if task.get("category"): meta_parts.append(f"🏷 {task['category']}")
        if task.get("notes"):    meta_parts.append(f"📝 {task['notes'][:40]}…" if len(task.get('notes',''))>40 else f"📝 {task['notes']}")
        if meta_parts:
            tk.Label(meta_row, text="   ".join(meta_parts),
                     font=T["F_SMALL"], bg=row_bg, fg=T["text3"]).pack(side="left")

        # Right buttons
        right_f = tk.Frame(content, bg=row_bg)
        right_f.pack(side="right", anchor="center")

        tk.Label(right_f, text=status, font=("Segoe UI",8,"bold"),
                 bg=st_bg, fg=st_fg, padx=8, pady=3).pack(side="left", padx=4)
        tk.Label(right_f, text=pri, font=("Segoe UI",8,"bold"),
                 bg=pri_bg, fg=pri_col, padx=6, pady=3).pack(side="left", padx=2)

        # Quick status change
        if status not in ("Done","Cancelled"):
            next_s = "Done" if status == "In Progress" else "In Progress"
            btn_col = T["emerald"] if next_s == "Done" else T["amber"]
            tk.Button(right_f, text=f"→{next_s}", font=("Segoe UI",8),
                      bg=T["bg3"], fg=btn_col, relief="flat", cursor="hand2",
                      command=lambda tid=task["id"], ns=next_s: self._quick_status(tid,ns)
                      ).pack(side="left", padx=2)

        tk.Button(right_f, text="✏", font=("Segoe UI",10),
                  bg=T["bg3"], fg=T["text2"], relief="flat", cursor="hand2",
                  command=lambda t=task: self._add_task_dialog(task=t)).pack(side="left", padx=2)
        tk.Button(right_f, text="✕", font=("Segoe UI",10),
                  bg=T["bg3"], fg=T["ruby"], relief="flat", cursor="hand2",
                  command=lambda tid=task["id"]: self._delete_task(tid)).pack(side="left", padx=2)

    def _quick_status(self, tid, new_status):
        for t in self.data["tasks"]:
            if t["id"] == tid: t["status"] = new_status; break
        save_data(self.data)
        self._refresh_tasks()
        self._show_notification(f"✅ Task moved to: {new_status}", T["emerald2"])

    def _add_task_dialog(self, task=None):
        editing = task is not None
        dlg = tk.Toplevel(self)
        dlg.title("Edit Task" if editing else "Add New Task")
        dlg.geometry("520x560")
        dlg.configure(bg=T["bg"])
        dlg.grab_set()
        tk.Frame(dlg, bg=T["gold"], height=3).pack(fill="x")
        tk.Label(dlg, text="✏️  Edit Task" if editing else "✦  New Task",
                 font=T["F_HEAD"], bg=T["bg"], fg=T["gold"]).pack(pady=(16,4))

        fields = {}
        cfg = [
            ("Task Name",   "name",     task["name"] if editing else "",              "entry", None),
            ("Category",    "category", task.get("category","Work") if editing else "Work", "entry", None),
            ("Due Date",    "due_date", task.get("due_date", datetime.date.today().isoformat()) if editing else datetime.date.today().isoformat(), "entry", None),
            ("Due Time",    "due_time", task.get("due_time","09:00") if editing else "09:00", "entry", None),
            ("Priority",    "priority", task.get("priority","🟡 Medium") if editing else "🟡 Medium", "combo", ["🔴 High","🟡 Medium","🟢 Low"]),
            ("Status",      "status",   task.get("status","Pending") if editing else "Pending", "combo", ["Pending","In Progress","Done","Cancelled"]),
        ]
        for lbl, key, default, wtype, opts in cfg:
            row = tk.Frame(dlg, bg=T["bg"])
            row.pack(fill="x", padx=30, pady=3)
            tk.Label(row, text=lbl, font=T["F_BODY"], bg=T["bg"],
                     fg=T["text2"], width=12, anchor="w").pack(side="left")
            if wtype == "entry":
                var = tk.StringVar(value=default)
                tk.Entry(row, textvariable=var, font=T["F_BODY"],
                         bg=T["card"], fg=T["text"], insertbackground=T["text"],
                         relief="flat", highlightbackground=T["border"],
                         highlightthickness=1).pack(side="left", fill="x", expand=True, ipady=5)
                fields[key] = var
            else:
                var = tk.StringVar(value=default)
                ttk.Combobox(row, textvariable=var, values=opts).pack(side="left", fill="x", expand=True)
                fields[key] = var

        tk.Label(dlg, text="Notes:", font=T["F_BODY"],
                 bg=T["bg"], fg=T["text2"]).pack(anchor="w", padx=30, pady=(8,2))
        notes_w = tk.Text(dlg, font=T["F_BODY"], bg=T["card"], fg=T["text"],
                          insertbackground=T["text"], relief="flat", height=4,
                          highlightbackground=T["border"], highlightthickness=1)
        notes_w.pack(padx=30, fill="x", pady=2)
        if editing and task.get("notes"):
            notes_w.insert("1.0", task["notes"])

        def save():
            name = fields["name"].get().strip()
            if not name: messagebox.showwarning("Empty","Task name required.",parent=dlg); return
            notes_val = notes_w.get("1.0","end-1c").strip()
            if editing:
                task["name"]     = name
                task["category"] = fields["category"].get().strip()
                task["due_date"] = fields["due_date"].get().strip()
                task["due_time"] = fields["due_time"].get().strip()
                task["priority"] = fields["priority"].get()
                task["status"]   = fields["status"].get()
                task["notes"]    = notes_val
            else:
                nid = self.data["next_task_id"]
                self.data["tasks"].append({
                    "id": nid, "name": name,
                    "category": fields["category"].get().strip(),
                    "due_date": fields["due_date"].get().strip(),
                    "due_time": fields["due_time"].get().strip(),
                    "priority": fields["priority"].get(),
                    "status":   fields["status"].get(),
                    "notes":    notes_val,
                    "created":  today_str(),
                })
                self.data["next_task_id"] += 1
            save_data(self.data)
            dlg.destroy()
            self._refresh_tasks()
            self._show_notification("✅ Task saved!", T["emerald2"])

        GlowButton(dlg, "  Save Task  ", command=save,
                   bg=T["teal3"], glow_color=T["teal"],
                   font=("Segoe UI",11,"bold")).pack(pady=14)

    def _delete_task(self, tid):
        if messagebox.askyesno("Delete","Delete this task permanently?"):
            self.data["tasks"] = [t for t in self.data["tasks"] if t["id"]!=tid]
            save_data(self.data)
            self._refresh_tasks()

    def _export_tasks_csv(self):
        fp = filedialog.asksaveasfilename(defaultextension=".csv",
                                          filetypes=[("CSV","*.csv")],
                                          initialfile="tasks_export.csv")
        if not fp: return
        tasks = self.data["tasks"]
        if not tasks: self._show_notification("No tasks to export.", T["amber"]); return
        keys = ["name","category","due_date","due_time","priority","status","notes","created"]
        with open(fp,"w",newline="") as f:
            w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
            w.writeheader(); w.writerows(tasks)
        self._show_notification(f"✅ Tasks exported!", T["emerald2"])

    # ══════════════════════════════════════════════════════════════
    #  GOALS PAGE
    # ══════════════════════════════════════════════════════════════
    def _build_goals_page(self):
        page = self.pages["goals"]
        hdr = tk.Frame(page, bg=T["bg2"])
        hdr.pack(fill="x")
        tk.Frame(hdr, bg=T["gold"], height=3).pack(fill="x")
        ih = tk.Frame(hdr, bg=T["bg2"], pady=14)
        ih.pack(fill="x")
        tk.Label(ih, text="🎯  LIFE GOALS",
                 font=T["F_TITLE"], bg=T["bg2"], fg=T["gold"]).pack(side="left", padx=24)
        GlowButton(ih, "＋  Add Goal", command=self._add_goal_dialog,
                   bg=T["teal3"], glow_color=T["teal"],
                   font=("Segoe UI",10,"bold")).pack(side="right", padx=24)
        _, self._goals_cv, self._goals_inner = self._scrollable(page)

    def _refresh_goals(self):
        for w in self._goals_inner.winfo_children(): w.destroy()
        inner = self._goals_inner
        goals = self.data.get("goals", [])

        # Snapshot
        snap_f = tk.Frame(inner, bg=T["card"], padx=20, pady=14,
                          highlightbackground=T["border"], highlightthickness=1)
        snap_f.pack(fill="x", padx=20, pady=(16,6))
        tk.Label(snap_f, text="✦  GOALS SNAPSHOT",
                 font=T["F_SUB"], bg=T["card"], fg=T["gold"]).pack(anchor="w")
        snap_row = tk.Frame(snap_f, bg=T["card"])
        snap_row.pack(fill="x", pady=8)
        stati = ["Active","In Progress","Completed","On Hold"]
        cols  = [T["sky"],T["amber"],T["emerald"],T["text3"]]
        for s, col in zip(stati, cols):
            cnt = sum(1 for g in goals if g.get("status")==s)
            sf = tk.Frame(snap_row, bg=T["card2"], padx=14, pady=8,
                          highlightbackground=T["border"], highlightthickness=1)
            sf.pack(side="left", expand=True, fill="x", padx=4)
            tk.Label(sf, text=str(cnt), font=T["F_NUM"], bg=T["card2"], fg=col).pack()
            tk.Label(sf, text=s, font=T["F_SMALL"], bg=T["card2"], fg=T["text3"]).pack()

        if not goals:
            tk.Label(inner, text="Set your first life goal above! 🎯",
                     font=T["F_BODY"], bg=T["bg"], fg=T["text3"]).pack(pady=40)
            return

        tk.Label(inner, text="✦  YOUR GOALS",
                 font=T["F_HEAD"], bg=T["bg"], fg=T["gold"]).pack(anchor="w", padx=22, pady=(12,4))

        for goal in goals:
            pct = goal.get("progress", 0)
            status = goal.get("status","Active")
            st_col = {"Active":T["sky"],"In Progress":T["amber"],
                      "Completed":T["emerald"],"On Hold":T["text3"]}.get(status,T["text2"])
            cat_col = CAT_COLORS.get(goal.get("category","Other"), T["teal"])

            card = tk.Frame(inner, bg=T["card"],
                            highlightbackground=T["border"], highlightthickness=1)
            card.pack(fill="x", padx=20, pady=4)
            tk.Frame(card, bg=cat_col, width=5).pack(side="left", fill="y")

            content = tk.Frame(card, bg=T["card"], padx=14, pady=12)
            content.pack(side="left", fill="x", expand=True)

            top = tk.Frame(content, bg=T["card"])
            top.pack(fill="x")
            tk.Label(top, text=goal["name"], font=("Segoe UI",12,"bold"),
                     bg=T["card"], fg=T["text"], anchor="w").pack(side="left")
            tk.Label(top, text=status, font=("Segoe UI",9,"bold"),
                     bg=T["card2"], fg=st_col, padx=8, pady=2).pack(side="right")

            meta = tk.Frame(content, bg=T["card"])
            meta.pack(fill="x", pady=3)
            meta_parts = []
            if goal.get("category"):   meta_parts.append(f"🏷 {goal['category']}")
            if goal.get("target_date"):meta_parts.append(f"📅 Target: {goal['target_date']}")
            if goal.get("milestone"):  meta_parts.append(f"🏁 {goal['milestone']}")
            tk.Label(meta, text="   ".join(meta_parts), font=T["F_SMALL"],
                     bg=T["card"], fg=T["text3"]).pack(side="left")

            # Progress bar
            pb_outer = tk.Frame(content, bg=T["bg3"], height=10)
            pb_outer.pack(fill="x", pady=4)
            pb_outer.update_idletasks()
            if pct > 0:
                fill_col = T["emerald"] if pct>=100 else T["teal"] if pct>=50 else T["amber"]
                tk.Frame(pb_outer, bg=fill_col, height=10,
                         width=max(6,int(pb_outer.winfo_reqwidth()*pct/100))).place(x=0,y=0)
            tk.Label(content, text=f"{pct}% complete",
                     font=T["F_SMALL"], bg=T["card"], fg=T["text3"]).pack(anchor="w")

            if goal.get("notes"):
                tk.Label(content, text=goal["notes"],
                         font=T["F_SMALL"], bg=T["card"],
                         fg=T["text3"], wraplength=700, anchor="w").pack(anchor="w")

            # Buttons
            btn_f = tk.Frame(content, bg=T["card"])
            btn_f.pack(anchor="e", pady=4)
            tk.Button(btn_f, text="+10%", font=T["F_SMALL"],
                      bg=T["card3"], fg=T["emerald"], relief="flat", cursor="hand2",
                      command=lambda gid=goal["id"]: self._inc_goal(gid,10)).pack(side="left",padx=2)
            tk.Button(btn_f, text="-10%", font=T["F_SMALL"],
                      bg=T["card3"], fg=T["amber"], relief="flat", cursor="hand2",
                      command=lambda gid=goal["id"]: self._inc_goal(gid,-10)).pack(side="left",padx=2)
            tk.Button(btn_f, text="✏ Edit", font=T["F_SMALL"],
                      bg=T["card3"], fg=T["text2"], relief="flat", cursor="hand2",
                      command=lambda g=goal: self._add_goal_dialog(goal=g)).pack(side="left",padx=2)
            tk.Button(btn_f, text="✕", font=T["F_SMALL"],
                      bg=T["card3"], fg=T["ruby"], relief="flat", cursor="hand2",
                      command=lambda gid=goal["id"]: self._delete_goal(gid)).pack(side="left",padx=2)

        tk.Frame(inner, bg=T["bg"], height=40).pack()

    def _inc_goal(self, gid, delta):
        for g in self.data["goals"]:
            if g["id"]==gid:
                g["progress"] = max(0, min(100, g.get("progress",0)+delta))
                if g["progress"]==100: g["status"]="Completed"
                break
        save_data(self.data); self._refresh_goals()

    def _add_goal_dialog(self, goal=None):
        editing = goal is not None
        dlg = tk.Toplevel(self)
        dlg.title("Edit Goal" if editing else "Add Life Goal")
        dlg.geometry("500x520")
        dlg.configure(bg=T["bg"])
        dlg.grab_set()
        tk.Frame(dlg, bg=T["gold"], height=3).pack(fill="x")
        tk.Label(dlg, text="✏️  Edit Goal" if editing else "✦  New Life Goal",
                 font=T["F_HEAD"], bg=T["bg"], fg=T["gold"]).pack(pady=(16,4))

        fields = {}
        cfg = [
            ("Goal Name",    "name",        goal["name"] if editing else "",         "entry"),
            ("Category",     "category",    goal.get("category","Other") if editing else "Other", "combo_cat"),
            ("Target Date",  "target_date", goal.get("target_date","") if editing else "", "entry"),
            ("Status",       "status",      goal.get("status","Active") if editing else "Active", "combo_st"),
            ("Progress %",   "progress",    str(goal.get("progress",0)) if editing else "0", "combo_pct"),
            ("Key Milestone","milestone",   goal.get("milestone","") if editing else "", "entry"),
        ]
        for lbl, key, default, wtype in cfg:
            row = tk.Frame(dlg, bg=T["bg"])
            row.pack(fill="x", padx=30, pady=3)
            tk.Label(row, text=lbl, font=T["F_BODY"], bg=T["bg"],
                     fg=T["text2"], width=14, anchor="w").pack(side="left")
            if wtype == "entry":
                var = tk.StringVar(value=default)
                tk.Entry(row, textvariable=var, font=T["F_BODY"],
                         bg=T["card"], fg=T["text"], insertbackground=T["text"],
                         relief="flat", highlightbackground=T["border"],
                         highlightthickness=1).pack(side="left", fill="x", expand=True, ipady=5)
                fields[key] = var
            elif wtype == "combo_cat":
                var = tk.StringVar(value=default)
                ttk.Combobox(row, textvariable=var,
                             values=list(CAT_COLORS.keys())).pack(side="left", fill="x", expand=True)
                fields[key] = var
            elif wtype == "combo_st":
                var = tk.StringVar(value=default)
                ttk.Combobox(row, textvariable=var,
                             values=["Active","In Progress","Completed","On Hold"]
                             ).pack(side="left", fill="x", expand=True)
                fields[key] = var
            elif wtype == "combo_pct":
                var = tk.StringVar(value=default)
                ttk.Combobox(row, textvariable=var,
                             values=[str(i) for i in range(0,110,10)]
                             ).pack(side="left", fill="x", expand=True)
                fields[key] = var

        tk.Label(dlg, text="Notes:", font=T["F_BODY"],
                 bg=T["bg"], fg=T["text2"]).pack(anchor="w", padx=30, pady=(8,2))
        notes_w = tk.Text(dlg, font=T["F_BODY"], bg=T["card"], fg=T["text"],
                          insertbackground=T["text"], relief="flat", height=3,
                          highlightbackground=T["border"], highlightthickness=1)
        notes_w.pack(padx=30, fill="x")
        if editing and goal.get("notes"): notes_w.insert("1.0", goal["notes"])

        def save():
            name = fields["name"].get().strip()
            if not name: messagebox.showwarning("Empty","Goal name required.",parent=dlg); return
            notes_val = notes_w.get("1.0","end-1c").strip()
            pct = int(fields["progress"].get() or 0)
            if editing:
                goal["name"]        = name
                goal["category"]    = fields["category"].get()
                goal["target_date"] = fields["target_date"].get().strip()
                goal["status"]      = fields["status"].get()
                goal["progress"]    = pct
                goal["milestone"]   = fields["milestone"].get().strip()
                goal["notes"]       = notes_val
            else:
                nid = self.data["next_goal_id"]
                self.data["goals"].append({
                    "id":nid, "name":name,
                    "category":   fields["category"].get(),
                    "target_date":fields["target_date"].get().strip(),
                    "status":     fields["status"].get(),
                    "progress":   pct,
                    "milestone":  fields["milestone"].get().strip(),
                    "notes":      notes_val,
                    "created":    today_str(),
                })
                self.data["next_goal_id"] += 1
            save_data(self.data); dlg.destroy(); self._refresh_goals()
            self._show_notification("✅ Goal saved!", T["emerald2"])

        GlowButton(dlg, "  Save Goal  ", command=save,
                   bg=T["teal3"], glow_color=T["teal"],
                   font=("Segoe UI",11,"bold")).pack(pady=14)

    def _delete_goal(self, gid):
        if messagebox.askyesno("Delete","Delete this goal?"):
            self.data["goals"] = [g for g in self.data["goals"] if g["id"]!=gid]
            save_data(self.data); self._refresh_goals()

    # ══════════════════════════════════════════════════════════════
    #  ANALYTICS
    # ══════════════════════════════════════════════════════════════
    def _build_analytics_page(self):
        page = self.pages["analytics"]
        hdr = tk.Frame(page, bg=T["bg2"])
        hdr.pack(fill="x")
        tk.Frame(hdr, bg=T["gold"], height=3).pack(fill="x")
        ih = tk.Frame(hdr, bg=T["bg2"], pady=14)
        ih.pack(fill="x")
        tk.Label(ih, text="📊  ANALYTICS & INSIGHTS",
                 font=T["F_TITLE"], bg=T["bg2"], fg=T["gold"]).pack(side="left", padx=24)
        _, _, self._analytics_inner = self._scrollable(page)

    def _refresh_analytics(self):
        for w in self._analytics_inner.winfo_children(): w.destroy()
        inner = self._analytics_inner

        active = [h for h in self.data["habits"] if h["active"]]
        total  = max(len(active), 1)
        days30 = [(datetime.date.today()-datetime.timedelta(days=i)).isoformat() for i in range(29,-1,-1)]
        days14 = [(datetime.date.today()-datetime.timedelta(days=i)).isoformat() for i in range(13,-1,-1)]

        # ── 30-day heatmap calendar ────────────────────────────────
        tk.Label(inner, text="✦  30-DAY COMPLETION HEATMAP",
                 font=T["F_HEAD"], bg=T["bg"], fg=T["gold"]).pack(anchor="w", padx=22, pady=(16,6))

        hmap_card = tk.Frame(inner, bg=T["card"], padx=20, pady=14,
                             highlightbackground=T["border"], highlightthickness=1)
        hmap_card.pack(fill="x", padx=20, pady=4)

        # Week row headers
        week_hdr = tk.Frame(hmap_card, bg=T["card"])
        week_hdr.pack(anchor="w")
        for d in ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]:
            tk.Label(week_hdr, text=d, font=T["F_MICRO"], width=4,
                     bg=T["card"], fg=T["text3"]).pack(side="left", padx=1)

        # Build calendar grid
        today_d = datetime.date.today()
        start = today_d - datetime.timedelta(days=29)
        # Pad to Monday
        pad = start.weekday()
        grid_row = tk.Frame(hmap_card, bg=T["card"])
        grid_row.pack(anchor="w")
        for _ in range(pad):
            tk.Frame(grid_row, bg=T["card"], width=32, height=32).pack(side="left", padx=1, pady=1)
        cur = start
        while cur <= today_d:
            if cur.weekday() == 0 and cur > start:
                grid_row = tk.Frame(hmap_card, bg=T["card"])
                grid_row.pack(anchor="w")
            ds = cur.isoformat()
            cnt = len(self.data["completions"].get(ds,[]))
            p = cnt / total
            tt = f"{cur.strftime('%d %b')}: {cnt}/{total} ({int(p*100)}%)"
            HeatCell(grid_row, ds, p, tt).pack(side="left", padx=1, pady=1)
            cur += datetime.timedelta(days=1)

        # Legend
        leg = tk.Frame(hmap_card, bg=T["card"])
        leg.pack(anchor="w", pady=(6,0))
        for lbl, col in [("0%",T["card3"]),("1-29%",T["amber"]),("30-59%",T["teal3"]),
                          ("60-89%",T["teal"]),("≥90%",T["emerald"])]:
            tk.Frame(leg, bg=col, width=14, height=14,
                     highlightbackground=T["border"], highlightthickness=1).pack(side="left",padx=2)
            tk.Label(leg, text=lbl, font=T["F_MICRO"],
                     bg=T["card"], fg=T["text3"]).pack(side="left",padx=(0,10))

        # ── Per-habit bar chart ────────────────────────────────────
        tk.Label(inner, text="✦  HABIT COMPLETION — LAST 30 DAYS",
                 font=T["F_HEAD"], bg=T["bg"], fg=T["gold"]).pack(anchor="w", padx=22, pady=(16,4))

        chart_card = tk.Frame(inner, bg=T["card"], padx=20, pady=16,
                              highlightbackground=T["border"], highlightthickness=1)
        chart_card.pack(fill="x", padx=20, pady=4)

        chart_w, chart_h = 900, 280
        cv = tk.Canvas(chart_card, width=chart_w, height=chart_h,
                       bg=T["card"], highlightthickness=0)
        cv.pack()

        if active:
            n = len(active)
            bar_w = max(20, min(55, int((chart_w-80)/n) - 6))
            spacing = (chart_w - 80) // n

            # Grid lines
            for pv in [0,25,50,75,100]:
                y = chart_h - 40 - int(pv/100*(chart_h-60))
                cv.create_line(40, y, chart_w-10, y,
                               fill=T["border"], dash=(2,4), width=1)
                cv.create_text(32, y, text=str(int(pv*30/100)),
                               font=("Consolas",8), fill=T["text3"], anchor="e")

            for i, habit in enumerate(active):
                count = sum(1 for d in days30 if habit["id"] in self.data["completions"].get(d,[]))
                x = 50 + i * spacing + spacing // 2
                bar_h_px = int((count/30)*(chart_h-60))
                col = CAT_COLORS.get(habit.get("category","Other"), T["teal"])

                # Bar with rounded top simulation
                y1 = chart_h - 40 - bar_h_px
                y2 = chart_h - 40
                if bar_h_px > 0:
                    cv.create_rectangle(x-bar_w//2, y1+3, x+bar_w//2, y2,
                                        fill=col, outline="", width=0)
                    cv.create_oval(x-bar_w//2, y1, x+bar_w//2, y1+6,
                                   fill=col, outline="", width=0)
                # Count label
                cv.create_text(x, max(y1-12, 10), text=str(count),
                               font=("Consolas",9,"bold"), fill=T["text2"])
                # Name label
                name_short = habit["name"].split(" ")[-1][:7]
                cv.create_text(x, chart_h-20, text=name_short,
                               font=("Consolas",8), fill=T["text3"])

        # ── Detailed stats table ───────────────────────────────────
        tk.Label(inner, text="✦  DETAILED STATS TABLE",
                 font=T["F_HEAD"], bg=T["bg"], fg=T["gold"]).pack(anchor="w", padx=22, pady=(16,4))

        tbl = tk.Frame(inner, bg=T["card"], padx=12, pady=10,
                       highlightbackground=T["border"], highlightthickness=1)
        tbl.pack(fill="x", padx=20, pady=4)
        hdrs = ["HABIT","Category","7-Day","30-Day","30-Day %","Streak","Best","Target"]
        col_w = [26, 10, 8, 8, 9, 8, 8, 8]
        for j,(h,w) in enumerate(zip(hdrs,col_w)):
            tk.Label(tbl, text=h, font=("Segoe UI",9,"bold"),
                     bg=T["card3"], fg=T["gold"], width=w,
                     anchor="center", pady=4).grid(row=0,column=j,padx=1,pady=1,sticky="ew")

        days7 = [(datetime.date.today()-datetime.timedelta(days=i)).isoformat() for i in range(6,-1,-1)]
        for i, habit in enumerate(active):
            row_bg = T["bg3"] if i%2==0 else T["card"]
            cat_col = CAT_COLORS.get(habit.get("category","Other"),T["teal"])
            c7  = sum(1 for d in days7  if habit["id"] in self.data["completions"].get(d,[]))
            c30 = sum(1 for d in days30 if habit["id"] in self.data["completions"].get(d,[]))
            p30 = f"{int(c30/30*100)}%"
            st  = self._habit_streak(habit["id"])
            bs  = self._habit_best_streak(habit["id"])
            tgt = habit.get("target",7)
            vals = [habit["name"], habit.get("category","Other"), c7, c30, p30, f"🔥{st}d", f"⭐{bs}d", f"{tgt}/wk"]
            fg_vals = [T["text"],cat_col,T["text"],T["text"],
                       T["emerald"] if int(c30/30*100)>=70 else T["amber"],
                       T["gold2"],T["teal"],T["text2"]]
            for j,(v,fw,fg) in enumerate(zip(vals,col_w,fg_vals)):
                tk.Label(tbl, text=str(v), font=("Segoe UI",9),
                         bg=row_bg, fg=fg, width=fw,
                         anchor="center", pady=5).grid(row=i+1,column=j,padx=1,pady=1,sticky="ew")

        # ── Mood correlation (if mood logged) ─────────────────────
        mood_log = self.data.get("mood_log", {})
        if mood_log:
            tk.Label(inner, text="✦  MOOD TREND (Last 14 Days)",
                     font=T["F_HEAD"], bg=T["bg"], fg=T["gold"]).pack(anchor="w", padx=22, pady=(16,4))
            mood_card = tk.Frame(inner, bg=T["card"], padx=20, pady=14,
                                 highlightbackground=T["border"], highlightthickness=1)
            mood_card.pack(fill="x", padx=20, pady=4)
            mood_cv = tk.Canvas(mood_card, width=chart_w, height=120,
                                bg=T["card"], highlightthickness=0)
            mood_cv.pack()
            moods = [mood_log.get(d, None) for d in days14]
            pts = [(i, m) for i, m in enumerate(moods) if m is not None]
            if len(pts) >= 2:
                W, H = chart_w, 100
                for (x1i, y1v), (x2i, y2v) in zip(pts, pts[1:]):
                    x1 = 40 + x1i * (W-60)//13
                    x2 = 40 + x2i * (W-60)//13
                    y1 = H - int(y1v/10*(H-20)) - 10
                    y2 = H - int(y2v/10*(H-20)) - 10
                    mood_cv.create_line(x1, y1, x2, y2, fill=T["teal"], width=2)
                for xi, yv in pts:
                    x = 40 + xi * (W-60)//13
                    y = H - int(yv/10*(H-20)) - 10
                    mood_cv.create_oval(x-4, y-4, x+4, y+4, fill=T["gold2"], outline="")
                    mood_cv.create_text(x, y-12, text=str(yv),
                                        font=("Consolas",8), fill=T["text3"])

        tk.Frame(inner, bg=T["bg"], height=40).pack()

    # ══════════════════════════════════════════════════════════════
    #  DAILY JOURNAL
    # ══════════════════════════════════════════════════════════════
    def _build_journal_page(self):
        page = self.pages["journal"]
        hdr = tk.Frame(page, bg=T["bg2"])
        hdr.pack(fill="x")
        tk.Frame(hdr, bg=T["gold"], height=3).pack(fill="x")
        ih = tk.Frame(hdr, bg=T["bg2"], pady=14)
        ih.pack(fill="x")
        tk.Label(ih, text="📓  DAILY JOURNAL",
                 font=T["F_TITLE"], bg=T["bg2"], fg=T["gold"]).pack(side="left", padx=24)
        _, _, self._journal_inner = self._scrollable(page)

    def _refresh_journal(self):
        for w in self._journal_inner.winfo_children(): w.destroy()
        inner = self._journal_inner
        today = today_str()

        # Today's entry
        entry_card = tk.Frame(inner, bg=T["card"], padx=24, pady=16,
                              highlightbackground=T["gold"], highlightthickness=1)
        entry_card.pack(fill="x", padx=20, pady=(16,6))
        tk.Label(entry_card, text=f"📓  TODAY'S JOURNAL — {today}",
                 font=T["F_HEAD"], bg=T["card"], fg=T["gold"]).pack(anchor="w")

        # Mood tracker
        mood_row = tk.Frame(entry_card, bg=T["card"])
        mood_row.pack(anchor="w", pady=8)
        tk.Label(mood_row, text="How are you feeling today?  ",
                 font=T["F_BODY"], bg=T["card"], fg=T["text2"]).pack(side="left")
        self._mood_var = tk.IntVar(value=self.data["mood_log"].get(today, 5))
        for v, emoji in [(1,"😞"),(2,"😕"),(3,"😐"),(4,"🙂"),(5,"😊"),(6,"😄"),(7,"🤩"),(8,"💫"),(9,"🔥"),(10,"✨")]:
            rb = tk.Radiobutton(mood_row, text=f"{emoji}", variable=self._mood_var,
                                value=v, bg=T["card"], fg=T["text"], selectcolor=T["teal3"],
                                activebackground=T["card"], font=("Segoe UI Emoji",12),
                                cursor="hand2")
            rb.pack(side="left", padx=1)

        # Journal prompts
        prompts_frame = tk.Frame(entry_card, bg=T["card"])
        prompts_frame.pack(fill="x", pady=4)
        self._journal_widgets = {}
        prompts = [
            ("wins",    "🌟  Top wins today:"),
            ("improve", "💡  What can I improve:"),
            ("grateful","❤️  I'm grateful for:"),
            ("tomorrow","📋  Tomorrow's top priority:"),
        ]
        existing = self.data["daily_notes"].get(today, {})
        for key, lbl in prompts:
            tk.Label(prompts_frame, text=lbl, font=T["F_SUB"],
                     bg=T["card"], fg=T["text2"]).pack(anchor="w", pady=(8,2))
            t = tk.Text(prompts_frame, font=T["F_BODY"], bg=T["card2"],
                        fg=T["text"], insertbackground=T["text"], relief="flat",
                        height=3, highlightbackground=T["border"], highlightthickness=1)
            t.pack(fill="x", pady=2)
            if existing.get(key):
                t.insert("1.0", existing[key])
            self._journal_widgets[key] = t

        def save_journal():
            mood = self._mood_var.get()
            self.data["mood_log"][today] = mood
            entry = {k: self._journal_widgets[k].get("1.0","end-1c").strip()
                     for k in self._journal_widgets}
            self.data["daily_notes"][today] = entry
            save_data(self.data)
            self._show_notification("📓 Journal saved!", T["emerald2"])

        GlowButton(entry_card, "  Save Journal Entry  ", command=save_journal,
                   bg=T["teal3"], glow_color=T["teal"],
                   font=("Segoe UI",10,"bold")).pack(pady=12, anchor="w")

        # Past entries
        past = {d:v for d,v in self.data["daily_notes"].items() if d != today}
        if past:
            tk.Label(inner, text="✦  PAST ENTRIES",
                     font=T["F_HEAD"], bg=T["bg"], fg=T["gold"]).pack(anchor="w", padx=22, pady=(16,4))
            for date_str in sorted(past.keys(), reverse=True)[:10]:
                mood_emoji = ""
                mv = self.data["mood_log"].get(date_str)
                if mv:
                    mood_emoji = ["","😞","😕","😐","🙂","😊","😄","🤩","💫","🔥","✨"][mv]
                pf = tk.Frame(inner, bg=T["card"], padx=16, pady=10,
                              highlightbackground=T["border"], highlightthickness=1)
                pf.pack(fill="x", padx=20, pady=3)
                tk.Label(pf, text=f"📅 {date_str}  {mood_emoji}",
                         font=T["F_SUB"], bg=T["card"], fg=T["gold2"]).pack(anchor="w")
                entry_data = past[date_str]
                for key, lbl in prompts:
                    val = entry_data.get(key,"")
                    if val:
                        tk.Label(pf, text=f"{lbl}  {val}",
                                 font=T["F_SMALL"], bg=T["card"], fg=T["text2"],
                                 wraplength=820, anchor="w").pack(anchor="w", pady=1)

        tk.Frame(inner, bg=T["bg"], height=40).pack()

    # ══════════════════════════════════════════════════════════════
    #  QUOTES PAGE
    # ══════════════════════════════════════════════════════════════
    def _build_quotes_page(self):
        page = self.pages["quotes"]
        hdr = tk.Frame(page, bg=T["bg2"])
        hdr.pack(fill="x")
        tk.Frame(hdr, bg=T["gold"], height=3).pack(fill="x")
        ih = tk.Frame(hdr, bg=T["bg2"], pady=14)
        ih.pack(fill="x")
        tk.Label(ih, text="💬  QUOTES LIBRARY",
                 font=T["F_TITLE"], bg=T["bg2"], fg=T["gold"]).pack(side="left", padx=24)
        self._rand_q_btn = GlowButton(ih, "🎲  Random Quote", command=self._show_random_quote,
                                       bg=T["teal3"], glow_color=T["teal"],
                                       font=("Segoe UI",10,"bold"))
        self._rand_q_btn.pack(side="right", padx=24)
        self._rand_quote_lbl = None
        _, _, self._quotes_inner = self._scrollable(page)

    def _show_random_quote(self):
        q, a = random.choice(QUOTES)
        dlg = tk.Toplevel(self)
        dlg.title("Random Inspiration")
        dlg.geometry("560x200")
        dlg.configure(bg=T["bg3"])
        dlg.grab_set()
        tk.Frame(dlg, bg=T["gold"], height=3).pack(fill="x")
        inner = tk.Frame(dlg, bg=T["bg3"], padx=30, pady=20)
        inner.pack(fill="both", expand=True)
        tk.Label(inner, text=f'"{q}"', font=T["F_QUOTE"],
                 bg=T["bg3"], fg=T["text"], wraplength=480, justify="center").pack(pady=8)
        tk.Label(inner, text=f"— {a}", font=("Segoe UI",11,"bold"),
                 bg=T["bg3"], fg=T["gold2"]).pack()
        GlowButton(inner, "Close", command=dlg.destroy,
                   bg=T["card3"], glow_color=T["teal"],
                   font=("Segoe UI",10)).pack(pady=12)

    def _refresh_quotes(self):
        for w in self._quotes_inner.winfo_children(): w.destroy()
        inner = self._quotes_inner
        today_idx = datetime.date.today().timetuple().tm_yday % len(QUOTES)
        q_text, q_author = QUOTES[today_idx]

        # Featured
        feat = tk.Frame(inner, bg=T["bg3"], padx=24, pady=20,
                        highlightbackground=T["gold"], highlightthickness=2)
        feat.pack(fill="x", padx=20, pady=(16,8))
        tk.Frame(feat, bg=T["gold"], height=2).pack(fill="x")
        fi = tk.Frame(feat, bg=T["bg3"], pady=14)
        fi.pack(fill="x")
        tk.Label(fi, text="⭐  TODAY'S FEATURED QUOTE",
                 font=("Segoe UI",9,"bold"), bg=T["bg3"], fg=T["gold"]).pack()
        tk.Label(fi, text=f'"{q_text}"',
                 font=("Palatino Linotype",15,"italic"), bg=T["bg3"],
                 fg=T["text"], wraplength=900, justify="center").pack(pady=10)
        tk.Label(fi, text=f"— {q_author}",
                 font=("Segoe UI",12,"bold"), bg=T["bg3"], fg=T["gold2"]).pack()
        tk.Frame(feat, bg=T["gold"], height=2).pack(fill="x")

        tk.Label(inner, text=f"✦  ALL {len(QUOTES)} QUOTES  —  Rotates daily",
                 font=T["F_HEAD"], bg=T["bg"], fg=T["gold"]).pack(anchor="w", padx=22, pady=(14,4))

        bg_cycle = [T["card"],T["card2"],T["bg3"],T["card3"]]
        for i, (q, author) in enumerate(QUOTES):
            is_today = (i == today_idx)
            bg = T["bg3"] if is_today else bg_cycle[i % len(bg_cycle)]
            border_col = T["gold"] if is_today else T["border"]

            qf = tk.Frame(inner, bg=bg, padx=18, pady=10,
                          highlightbackground=border_col,
                          highlightthickness=2 if is_today else 1)
            qf.pack(fill="x", padx=20, pady=3)
            tk.Label(qf, text=f"#{i+1}  " if not is_today else "⭐ TODAY  ",
                     font=T["F_MICRO"], bg=bg, fg=T["gold"]).pack(side="left", anchor="n", pady=2)
            text_f = tk.Frame(qf, bg=bg)
            text_f.pack(side="left", fill="x", expand=True)
            tk.Label(text_f, text=f'"{q}"',
                     font=("Palatino Linotype",11,"italic"), bg=bg,
                     fg=T["text"], wraplength=780, anchor="w", justify="left").pack(anchor="w")
            tk.Label(text_f, text=f"— {author}",
                     font=("Segoe UI",10,"bold"), bg=bg, fg=T["teal2"]).pack(anchor="e")

        tk.Frame(inner, bg=T["bg"], height=40).pack()

    # ══════════════════════════════════════════════════════════════
    #  SETTINGS PAGE
    # ══════════════════════════════════════════════════════════════
    def _build_settings_page(self):
        page = self.pages["settings"]
        hdr = tk.Frame(page, bg=T["bg2"])
        hdr.pack(fill="x")
        tk.Frame(hdr, bg=T["gold"], height=3).pack(fill="x")
        ih = tk.Frame(hdr, bg=T["bg2"], pady=14)
        ih.pack(fill="x")
        tk.Label(ih, text="⚙️  SETTINGS",
                 font=T["F_TITLE"], bg=T["bg2"], fg=T["gold"]).pack(side="left", padx=24)
        _, _, self._settings_inner = self._scrollable(page)

    def _refresh_settings(self):
        for w in self._settings_inner.winfo_children(): w.destroy()
        inner = self._settings_inner

        for section, items in [
            ("📁  DATA MANAGEMENT", [
                ("Export ALL Data (JSON)", self._export_all_json, T["emerald"]),
                ("Import Data (JSON)",     self._import_json,     T["sky"]),
                ("Reset All Data",         self._reset_data,      T["ruby"]),
            ]),
            ("📊  REPORTS", [
                ("Export Habits CSV",      self._export_habits_csv, T["emerald"]),
                ("Export Tasks CSV",       self._export_tasks_csv,  T["sky"]),
            ]),
            ("ℹ️  ABOUT", None),
        ]:
            sec_f = tk.Frame(inner, bg=T["card"], padx=20, pady=14,
                             highlightbackground=T["border"], highlightthickness=1)
            sec_f.pack(fill="x", padx=20, pady=(14,4))
            tk.Label(sec_f, text=section, font=T["F_HEAD"],
                     bg=T["card"], fg=T["gold"]).pack(anchor="w")
            if items:
                for lbl, cmd, col in items:
                    GlowButton(sec_f, f"  {lbl}  ", command=cmd,
                               bg=T["card3"], glow_color=col,
                               font=("Segoe UI",10)).pack(anchor="w", pady=4)
            else:
                lines = [
                    "ZENITH — Advanced Habit & Life Goals Tracker",
                    "Version 2.0  |  Python + Tkinter",
                    "Designed for daily excellence and consistent growth.",
                    f"Data file: {DATA_FILE}",
                ]
                for line in lines:
                    tk.Label(sec_f, text=line, font=T["F_BODY"],
                             bg=T["card"], fg=T["text2"]).pack(anchor="w", pady=2)

        # Stats summary
        sf = tk.Frame(inner, bg=T["card2"], padx=20, pady=14,
                      highlightbackground=T["border"], highlightthickness=1)
        sf.pack(fill="x", padx=20, pady=14)
        tk.Label(sf, text="📊  DATA SUMMARY", font=T["F_HEAD"],
                 bg=T["card2"], fg=T["gold"]).pack(anchor="w")
        d = self.data
        summaries = [
            ("Active Habits",     len([h for h in d["habits"] if h["active"]])),
            ("Total Tasks",       len(d["tasks"])),
            ("Life Goals",        len(d.get("goals",[]))),
            ("Days Tracked",      len(d["completions"])),
            ("Journal Entries",   len(d.get("daily_notes",{}))),
            ("Mood Logs",         len(d.get("mood_log",{}))),
        ]
        for lbl, val in summaries:
            row = tk.Frame(sf, bg=T["card2"])
            row.pack(fill="x", pady=2)
            tk.Label(row, text=lbl, font=T["F_BODY"],
                     bg=T["card2"], fg=T["text2"], anchor="w").pack(side="left")
            tk.Label(row, text=str(val), font=("Segoe UI",10,"bold"),
                     bg=T["card2"], fg=T["teal"]).pack(side="right")

        tk.Frame(inner, bg=T["bg"], height=40).pack()

    def _export_all_json(self):
        fp = filedialog.asksaveasfilename(defaultextension=".json",
                                          filetypes=[("JSON","*.json")],
                                          initialfile="zenith_backup.json")
        if not fp: return
        with open(fp,"w") as f: json.dump(self.data, f, indent=2)
        self._show_notification(f"✅ Backup saved!", T["emerald2"])

    def _import_json(self):
        fp = filedialog.askopenfilename(filetypes=[("JSON","*.json")])
        if not fp: return
        if messagebox.askyesno("Import","This will REPLACE all current data. Continue?"):
            try:
                with open(fp,"r") as f: self.data = json.load(f)
                save_data(self.data)
                self._show_notification("✅ Data imported!", T["emerald2"])
                self._switch_tab("dashboard")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to import: {e}")

    def _reset_data(self):
        if messagebox.askyesno("Reset","DELETE all data and start fresh? This cannot be undone."):
            if messagebox.askyesno("Confirm","Are you absolutely sure?"):
                self.data = load_data.__wrapped__() if hasattr(load_data,"__wrapped__") else {
                    "habits": DEFAULT_HABITS[:], "tasks": [], "goals": [],
                    "completions": {}, "daily_notes": {}, "mood_log": {},
                    "next_habit_id":11,"next_task_id":1,"next_goal_id":1,
                    "settings":{"theme":"obsidian","show_motivations":True,"daily_target":80},
                }
                save_data(self.data)
                self._show_notification("Data reset.", T["amber"])
                self._switch_tab("dashboard")

    # ══════════════════════════════════════════════════════════════
    #  HELPERS / STREAKS
    # ══════════════════════════════════════════════════════════════
    def _calc_streak(self):
        streak = 0
        check = datetime.date.today()
        active_ids = [h["id"] for h in self.data["habits"] if h["active"]]
        if not active_ids: return 0
        for _ in range(365):
            d = check.isoformat()
            done = self.data["completions"].get(d,[])
            cnt = sum(1 for hid in active_ids if hid in done)
            if cnt >= max(1, len(active_ids)//2):
                streak += 1
                check -= datetime.timedelta(days=1)
            else: break
        return streak

    def _habit_streak(self, hid):
        streak = 0
        check = datetime.date.today()
        for _ in range(365):
            if hid in self.data["completions"].get(check.isoformat(),[]):
                streak += 1
                check -= datetime.timedelta(days=1)
            else: break
        return streak

    def _habit_best_streak(self, hid):
        best = cur = 0
        check = datetime.date.today()
        for _ in range(365):
            if hid in self.data["completions"].get(check.isoformat(),[]):
                cur += 1; best = max(best, cur)
            else: cur = 0
            check -= datetime.timedelta(days=1)
        return best


# ══════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    app = ZenithApp()
    app.mainloop()
