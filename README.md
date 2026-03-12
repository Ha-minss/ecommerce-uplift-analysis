# Ecommerce Uplift Analysis

A portfolio-style analytics project built on a synthetic ecommerce marketing dataset.  
The repository connects **data preprocessing → EDA → experiment analysis → uplift-style targeting** in one workflow.

## What this project covers
- Raw data audit and cleaning
- Event / transaction master table construction
- KPI, funnel, cohort, and segment analysis
- A/B experiment performance comparison
- Business recommendation tables for campaign operation
- Uplift-style ranking analysis with decile reports, Qini/AUUC summaries, bootstrap CI, and campaign incrementality tables

## Repository structure

```text
ecommerce-uplift-analysis/
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ notebooks/
│  ├─ 01_data_preprocessing.ipynb
│  ├─ 02_eda_kpi_funnel_segments.ipynb
│  ├─ 03_experiment_analysis.ipynb
│  ├─ 04_uplift_modeling.ipynb
│  └─ README.md
├─ data/
│  ├─ raw/
│  │  ├─ .gitkeep
│  │  └─ README.md
│  └─ processed/
│     ├─ .gitkeep
│     └─ README.md
├─ docs/
│  └─ project_snapshot.md
└─ scripts/
   └─ repo_check.py
```

## Expected workflow

1. Put the original raw CSV files into `data/raw/`.
2. Run `notebooks/01_data_preprocessing.ipynb` to build `event_master` and `purchase_master`.
3. Ensure `session_level_funnel.csv` and `customer_level_features.csv` are available under `data/processed/`.
4. Run:
   - `02_eda_kpi_funnel_segments.ipynb`
   - `03_experiment_analysis.ipynb`
   - `04_uplift_modeling.ipynb`

## Key numeric outputs

The project is designed so that the main numbers from experiment analysis and uplift modeling can be saved as CSV files under `data/processed/`.

### Experiment analysis outputs
- `part4a_default_variant_recommendation.csv`
- `part4a_segment_recommendation.csv`
- `part4a_campaign_priority_plan.csv`
- `part4a_guardrails.csv`

### Uplift modeling outputs
Examples include:
- decile uplift reports
- cumulative uplift reports
- scored session tables
- Qini / AUUC summaries
- bootstrap CI tables
- campaign incrementality summaries
- strategy pivot tables

See `data/processed/README.md` for the full file list.

## Important limitation

Based on the uploaded code bundle, the preprocessing export currently writes only:
- `event_master`
- `purchase_master`

The notebooks for EDA, experiment analysis, and uplift modeling also expect:
- `session_level_funnel.csv`
- `customer_level_features.csv`

So this repository is **GitHub-ready and structurally consistent**, but a full rerun still requires those processed inputs to be present.

## Why the repository is still useful
Even with that limitation, the repository clearly shows the full analysis storyline:
- data preparation
- business exploration
- average treatment effect analysis
- incremental targeting / uplift analysis

That makes it suitable as a portfolio repository once the final result CSVs from notebooks 03 and 04 are included.
