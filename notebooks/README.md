# Notebook Order

1. `01_data_preprocessing.ipynb`  
   Load raw tables, audit data quality, build `event_master` and `purchase_master`.

2. `02_eda_kpi_funnel_segments.ipynb`  
   Explore baseline KPIs, funnel behavior, segment performance, and cohorts.

3. `03_experiment_analysis.ipynb`  
   Summarize overall A/B performance, segment-level differences, and business recommendations.

4. `04_uplift_modeling.ipynb`  
   Build uplift-style ranking analyses and export targeting / incrementality summaries.

## Important note

The current uploaded notebook set expects `session_level_funnel.csv` and `customer_level_features.csv` to already exist in `../data/processed/`. They are referenced by notebooks 02-04 but are not generated in the uploaded preprocessing export.
