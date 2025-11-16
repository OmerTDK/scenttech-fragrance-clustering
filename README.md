# Fragrance Segmentation – Unsupervised Clustering Analysis

## 📋 Project Overview

This project performs an **unsupervised clustering analysis** on a comprehensive fragrance dataset to identify natural groupings of perfumes based on their characteristics, pricing, and market performance. The analysis helps understand fragrance market segmentation for targeted marketing and product positioning strategies.

### 🎯 Objectives
- **Market Segmentation**: Identify how perfumes naturally group together based on scent characteristics
- **Price Analysis**: Understand which fragrance segments are more affordable vs. premium/luxury
- **Business Insights**: Provide actionable insights for marketing, product positioning, and personalized recommendations

## 👨‍🎓 Author Information
- **Name**: Muhammad Umar Uz Zaman
- **Student ID**: STU1197819
- **Course**: Machine Learning

## 📊 Dataset
- **File**: `Fragrance Dataset.csv`
- **Records**: 4,037 perfume listings
- **Source**: Comprehensive fragrance market data
- **Features**: Brand, title, type, price, availability, sales data, and descriptive attributes

## 🛠️ Tech Stack & Dependencies

### Core Libraries
- **numpy** - Numerical computing
- **pandas** - Data manipulation and analysis
- **matplotlib** - Data visualization
- **seaborn** - Statistical data visualization

### Machine Learning & Analysis
- **scikit-learn** - Clustering algorithms (K-Means, Hierarchical, DBSCAN), preprocessing, PCA, t-SNE
- **scipy** - Hierarchical clustering and statistical functions

### Environment
- **Python 3.10+**
- **Jupyter Notebook** for interactive analysis

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/OmerTDK/scenttech-fragrance-clustering.git
cd scenttech-fragrance-clustering
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/Scripts/activate  # On Windows Git Bash
# OR
venv\Scripts\activate         # On Windows Command Prompt/PowerShell
```

### 3. Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt

# Optional: Install Jupyter if not included
pip install jupyter
```

### 4. Launch Jupyter Notebook
```bash
# Make sure virtual environment is activated
source venv/Scripts/activate

# Launch Jupyter
jupyter notebook
```

### 5. Open the Analysis
- Open `main.ipynb` in Jupyter
- Switch to the "Python (ML Project)" kernel if prompted
- Run cells sequentially to reproduce the analysis

### 📊 Visualization Preview
The notebook generates comprehensive visualizations including:
- **Evaluation Plots**: Silhouette and Davies-Bouldin curves for optimal cluster selection
- **Dendrograms**: Hierarchical clustering trees showing cluster relationships
- **Scatter Plots**: PCA and t-SNE projections with color-coded clusters
- **Business Charts**: Price segmentation and sales performance bar charts
- **Composition Analysis**: Stacked bar charts showing segment characteristics

## 📈 Analysis Phases

### Phase 1 – Data Loading & Structure Check
- Load fragrance dataset
- Initial data exploration
- Understand data structure and quality

### Phase 2 – Data Cleaning, Preparation & Feature Selection
- Handle missing values and outliers
- Feature engineering
- Select relevant features for clustering

### Phase 3 – Core EDA (Exploratory Data Analysis)
- Distribution analysis
- Relationship exploration
- Feature importance assessment

### Phase 4 – Clustering Models & Evaluation
- **K-Means Clustering**: Elbow method, silhouette analysis, and Davies-Bouldin evaluation plots
- **Hierarchical Clustering**: Ward linkage dendrogram with optimal cluster identification
- **DBSCAN**: Parameter tuning visualization (epsilon vs. clusters/noise ratio)
- **Model Comparison**: Silhouette scores and Davies-Bouldin indices across all algorithms
- **Dimensionality Reduction**: PCA and t-SNE visualizations for cluster validation

### Phase 5 – Cluster Profiling & Business Insights
- Analyze cluster characteristics
- Price segmentation analysis
- Brand and type distribution by cluster
- Business recommendations

### Phase 6 – Wrap-up, Limitations & Export
- Summary of findings
- Methodology limitations
- Export results for management reporting

## 🔍 Key Features

### Clustering Algorithms Implemented
1. **K-Means**: Optimal k selection using elbow method and silhouette analysis
2. **Hierarchical Clustering**: Complete linkage with dendrogram visualization
3. **DBSCAN**: Density-based clustering with parameter optimization

### Dimensionality Reduction
- **PCA (Principal Component Analysis)**: Linear dimensionality reduction
- **t-SNE**: Non-linear dimensionality reduction for visualization

### Evaluation Metrics
- Silhouette Score
- Davies-Bouldin Index
- Elbow Method (within-cluster sum of squares)

### Key Visualizations
- **Correlation Heatmap**: Feature relationships and multicollinearity analysis
- **K-Means Evaluation**: Silhouette scores and Davies-Bouldin index across different k values
- **Hierarchical Clustering Dendrogram**: Ward linkage clustering tree with optimal cut-point
- **DBSCAN Parameter Tuning**: Clusters vs noise ratio analysis for epsilon selection
- **PCA Scatter Plot**: 2D visualization of K-means clusters in principal component space
- **t-SNE Visualization**: Non-linear dimensionality reduction showing cluster separation
- **Price Segmentation**: Mean price comparison across identified fragrance segments
- **Sales Performance**: Units sold analysis by segment with business insights
- **Format Distribution**: Stacked bar chart showing fragrance type composition within each cluster

## 📁 Project Structure
```
scenttech-fragrance-clustering/
│
├── main.ipynb                    # Main analysis notebook
├── requirements.txt              # Python dependencies
├── .gitignore                   # Git ignore rules
├── README.md                    # Project documentation
│
├── Fragrance Dataset.csv        # Main dataset (4,037 records)
├── dataset.xlsx                 # Alternative dataset format
├── Task.pdf                     # Project requirements/task description
│
└── venv/                        # Virtual environment (ignored by git)
    ├── Scripts/                 # Windows executables
    └── Lib/site-packages/       # Installed packages
```

## 🎯 Expected Outcomes

### Key Findings & Visual Insights

#### **Clustering Results**
- **Optimal K-Means solution**: k=3 clusters identified through silhouette analysis
- **Cluster separation**: Clear visual separation in both PCA and t-SNE projections
- **Hierarchical validation**: Dendrogram confirms 3-cluster structure with Ward linkage

#### **Segment Characteristics**
- **Price Segmentation**: Distinct pricing tiers from budget to premium segments
- **Sales Performance**: Differential velocity across segments (bestsellers vs. slow-movers)
- **Format Distribution**: Each cluster shows unique fragrance type preferences
- **Brand Concentration**: Luxury vs. accessible brand positioning within segments

#### **Business Insights**
- **Market Gaps**: Identification of underserved price points and fragrance types
- **Inventory Strategy**: Segment-specific stock allocation recommendations
- **Marketing Targeting**: Cluster-based customer profiling for personalized campaigns

### Business Applications
- **Targeted Marketing**: Segment-specific marketing strategies
- **Product Positioning**: Optimal pricing and positioning recommendations
- **Inventory Management**: Stock allocation based on segment performance
- **Customer Recommendations**: Personalized fragrance suggestions

## ⚠️ Known Limitations
- Dataset represents specific market segment (eBay fragrance listings)
- Analysis based on available structured data only
- External factors (seasonality, trends) not considered
- Geographic market limitations

## 🤝 Contributing
This is an educational project for machine learning coursework. For suggestions or improvements:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License
This project is for educational purposes as part of a machine learning course.

## 📞 Contact
- **GitHub**: [OmerTDK](https://github.com/OmerTDK)
- **Email**: omerzaman98@gmail.com

---

**⭐ Star this repository if you found it helpful for understanding unsupervised clustering in market segmentation!**
