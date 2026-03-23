# ☀️ Solar Potential Calculator (V2)
### *From Pure Python to the NumPy Data Engine*

![Solar Calculator V2](file:///C:/Users/anujs/.gemini/antigravity/brain/b4b2add4-25be-4de5-babb-ed6a26126c07/solar_calculator_banner_v2.png)

## 🚀 The V2 Transformation
Phase 2 of my learning roadmap transitions this professional solar tool from basic scalar calculations to a **high-performance NumPy engine**. While V1 demonstrated clean **OOP design**, V2 leverages **vectorization** to handle multi-dimensional data and life-cycle analytics.

---

## 🛠 What's New in V2?

| Feature | V1 (Basic Python) | V2 (NumPy Powered) | Why it Matters? |
| :--- | :--- | :--- | :--- |
| **Data Structure** | Python Dictionaries | **NumPy Structured Arrays** | Efficient memory and row-based record filtering. |
| **Time Analysis** | Annual Average (Scalar) | **12-Month Array (Vectorized)** | Monthly seasonal variation handled in one operation. |
| **Life Cycle** | Constant Performance | **25-Year Degradation Array** | Models real-world efficiency loss (0.5% yearly decay). |
| **Indexing** | Key-Value Lookups | **Boolean Search & Masking** | Professional data-science method for record retrieval. |

---

## 🏗 Architecture: The "NumPy Core"
The core classes from V1 remain, but their internal logic has been "supercharged":

1.  **`config.py`**: Now uses `np.array` with custom `dtypes` for Cities, States, and Subsidies.
2.  **`Solar/Location`**: Uses NumPy **Boolean Masking** (`np.where`) to find location data instantly.
3.  **`Solar/EnergyGeneration`**: Calculates energy for all 12 months in a single vectorized calculation—**zero loops**.
4.  **`Solar/Finance`**: Models a 25-year financial horizon considering panel wear-and-tear using `np.cumprod`.

---

## 📊 Technical Highlights

### **1. Vectorized Month Analytics**
Instead of calculating one day and multiplying by 30, V2 uses a "Days-Per-Month" array:
```python
# One line calculates specific energy for every month in the year
monthly_gen = daily_energy * np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
```

### **2. Lifecycle Performance Decay**
We model 25 years of investment by creating a degradation curve:
```python
# Each year is 0.5% less efficient than the last
degradation = 0.995 ** np.arange(25)
total_lifetime_energy = np.sum(annual_energy * degradation)
```

---

## 🛣 Learning Roadmap
- [x] **V1: Core Python & OOP** (The Foundation)
- [x] **V2: NumPy Integration** (The Engine - *Current*)
- [ ] **V3: Pandas DataFrames** (The Analysis Suite)
- [ ] **V4: Matplotlib & Seaborn** (The Visual Dashboard)
- [ ] **V5: NSRDB/NASA APIs** (The Real-World Data)

---

## 💻 How to Run
```bash
# Clone the repository
cd V2_SOLAR_POTENTIAL_CALCULATOR

# Install dependencies (NumPy is all you need!)
pip install numpy

# Run the analyzer
python main.py
```

---

## ✍️ Author
Built as part of a **Climate Physical Risk Intelligence** roadmap — demonstrating the transition from algorithmic logic to data-driven performance modeling.