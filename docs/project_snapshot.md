# Project Snapshot

## Theme
Experiment analysis and uplift-style targeting for a synthetic ecommerce marketing dataset.

## Workflow
1. Audit and clean raw event / transaction tables.
2. Build analysis-ready master tables.
3. Diagnose baseline KPIs, funnel behavior, and segment differences.
4. Compare experiment variants and export business recommendation tables.
5. Extend the analysis into uplift ranking, Qini/AUUC evaluation, bootstrap uncertainty checks, and campaign incrementality summaries.

## What makes the project interesting
- Connects descriptive analytics, experiment analysis, and personalized targeting in one workflow.
- Includes business-facing recommendation tables instead of stopping at model training.
- Exports lightweight summary CSVs so key numeric results from experiment and uplift analysis can be versioned separately.

## Current limitation
The uploaded notebook bundle references `session_level_funnel.csv` and `customer_level_features.csv`, but those tables are not generated inside the uploaded preprocessing export. End-to-end reruns therefore require those processed inputs to be available.
