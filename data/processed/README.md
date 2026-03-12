# Processed Data

This folder stores analysis-ready tables and lightweight result summaries.

## Core processed inputs referenced by the notebooks
- `event_master.csv` / `event_master.parquet`
- `purchase_master.csv` / `purchase_master.parquet`
- `session_level_funnel.csv`
- `customer_level_features.csv`

## Recommendation tables exported by `03_experiment_analysis.ipynb`
- `part4a_default_variant_recommendation.csv`
- `part4a_segment_recommendation.csv`
- `part4a_campaign_priority_plan.csv`
- `part4a_guardrails.csv`

## Uplift summaries exported by `04_uplift_modeling.ipynb`
- `part4b_variantB_uplift_decile_report_v2.csv`
- `part4b_variantB_uplift_cumulative_report_v2.csv`
- `part4b_variantB_scored_sessions_v2.csv`
- `part4b_variantB_top20_targets_v2.csv`
- `part4b_uplift_tree_decile_report.csv`
- `part4b_uplift_tree_cumulative_report.csv`
- `part4b_uplift_tree_leaf_report.csv`
- `part4b_uplift_tree_scored_sessions.csv`
- `part4b_uplift_tree_top20_targets.csv`
- `part4b_uplift_qini_curve_data.csv`
- `part4b_uplift_qini_auuc_summary.csv`
- `part4b_uplift_bootstrap_detail.csv`
- `part4b_uplift_bootstrap_ci_summary.csv`
- `part4b_campaign_incrementality_overall_summary.csv`
- `part4b_campaign_incrementality_by_campaign.csv`
- `part4b_campaign_incrementality_by_channel.csv`
- `part4b_campaign_incrementality_by_objective.csv`
- `part4b_campaign_incrementality_by_target_segment.csv`
- `part4b_campaign_expected_vs_actual_summary.csv`
- `part4b_campaign_incrementality_overall_summary_clean.csv`
- `part4b_campaign_incrementality_by_campaign_clean.csv`
- `part4b_campaign_incrementality_by_channel_clean.csv`
- `part4b_campaign_incrementality_by_objective_clean.csv`
- `part4b_campaign_incrementality_by_target_segment_clean.csv`
- `part4b_campaign_expected_vs_actual_summary_clean.csv`
- `part4b_first_page_category_segment_channel_actual_uplift.csv`
- `part4b_first_page_category_segment_channel_strategy_table.csv`
- `part4b_channel_segment_weighted_uplift_pivot_from_first_page_category.csv`
- `part4b_first_page_category_channel_weighted_uplift_pivot.csv`

## Important note
The uploaded preprocessing export currently writes only `event_master` and `purchase_master`.  
`session_level_funnel.csv` and `customer_level_features.csv` are still assumed to exist as prepared processed inputs.
