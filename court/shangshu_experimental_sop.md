# 尚书省: Experimental Design and SOP

Use for `兴工：实验推演` after a pathway is selected.

## Required Outputs

1. Selected pathway restatement.
2. Variable operationalization table from `templates/variable_table_template.md`.
3. Data inventory: data, year, resolution, source, purpose, preprocessing, risk.
4. SOP using `templates/sop_template.md`.
5. Method justification: why each method fits, assumptions, alternatives, and why alternatives are not primary.
6. Robustness and validation plan.
7. Plan B if key data or software is unavailable.
8. `锦衣卫按语`.

## SOP Rules

Each step must include:

- 做什么;
- 为什么;
- 推荐工具;
- 预期输出;
- 质控检查.

Do not write "use Python/GIS" generically. Name the task: projection, resampling, cloud masking, buffer construction, network distance, model tuning, residual diagnosis, etc.

## Scientific Caution

- Separate correlation, prediction, and causal explanation.
- State spatial unit and possible MAUP risk.
- Check spatial autocorrelation when using spatial data.
- Include sensitivity analysis for thresholds, resistance weights, buffer radii, and model hyperparameters.
