# ☀️ Solar Potential Calculator (V2)
### *From Pure Python to the High-Performance NumPy Engine*

![Solar Calculator Banner](assets/banner.png)

> [!NOTE]
> **The V2 Transformation**: This project transitions from basic scalar OOP to a **vectorized NumPy engine**, enabling high-speed calculation of solar generation across 12 months and 25-year lifecycles in a single operation.

## 🚀 Key Features

| Feature | Description | Why it Matters? |
| :--- | :--- | :--- |
| **Data Structure** | **NumPy Structured Arrays** | Row-based record filtering & efficient memory mapping |
| **Time Analysis** | **12-Month Array (Vectorized)** | Seasonal variations handled in one operation (no loops!) |
| **Life Cycle** | **25-Year Degradation Array** | Models real-world efficiency loss (0.5% yearly decay) |
| **Indexing** | **Boolean Search & Masking** | Professional data-science method for location retrieval |

---

## 🏗 Architecture: The "NumPy Core"
The core engine has been "supercharged" to handle complex data modeling:

1.  **`config.py`**: Centralized configuration using `np.array` with custom `dtypes` for Cities, States, and Subsidies.
2.  **`Solar/Location`**: Implements **Boolean Masking** (`np.where`) to retrieve solar irradiation data instantly.
3.  **`Solar/EnergyGeneration`**: Calculates energy yield for all 12 months simultaneously—**zero Python loops**.
4.  **`Solar/Finance`**: Models a 25-year financial horizon considering cumulative performance degradation using `np.cumprod`.

---

## 📊 Technical Highlights

### **1. Dynamic Leap Years & Vectorized Timelines**
The engine builds an exact 25-year physical history timeline natively tracking standard formatting and exact leap year alterations utilizing fast `np.where` boolean logical operations.

### **2. Concurrent Hardware Physics & Utility Economics**
We model 25 years of investment by generating multiple compounded arrays concurrently, simultaneously forecasting hardware decay and geometric monetary inflation (`(1 + r)**t`):
```python
# Concurrently calculates 25-years of hardware efficiency loss and utility price inflation
energy_decay = 0.995 ** np.arange(25)
utility_escalation = (1 + 0.03) ** np.arange(25)
annual_savings_array = (base_annual_energy * energy_decay) * utility_escalation * slab_rate
```

### **3. The NPV Financial Risk Engine**
Replaced basic static division arithmetic with advanced Time Value of Money (TVM) calculations. The program determines true **Net Present Value (NPV)** against a 7% market opportunity cost baseline, while querying dynamic cumulative payback periods using array masking:
```python
# Extracting the exact payback year from a cumulative ROI matrix instantly
payback_year = np.where(yearly_roi_array >= 100)[0][0] + 1
```
---

## 🛣 Learning Roadmap
- [x] **V1: Core Python & OOP** (The Foundation)
- [x] **V2: NumPy Integration** (The Engine - *Current*)
- [ ] **V3: Pandas DataFrames** (Enhanced Analysis)
- [ ] **V4: Matplotlib & Seaborn** (Visual Dashboard)
- [ ] **V5: NSRDB/NASA APIs** (Real-World Data Integration)

---

## 💻 Installation & Usage

1.  **Clone the Repository**:
    ```bash
    git clone <your-repo-link>
    cd V2_SOLAR_POTENTIAL_CALCULATOR
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Calculator**:
    ```bash
    python main.py
    ```

---

## ✍️ Author
**Built for Climate Physical Risk Intelligence** — demonstrating the transition from standard algorithmic logic to high-performance data modeling.
