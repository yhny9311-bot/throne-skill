# 钦天监: Remote Sensing, GIS, GEE, and GeoAI

Use for `观天：遥感方案`.

## Required Outputs

1. Remote-sensing/GIS problem definition.
2. Data recommendation table: sensor/product, resolution, period, source, reason, risk.
3. Preprocessing route: projection, cloud mask, compositing, resampling, clipping, scale matching.
4. Indicator construction: formula or method, ecological meaning, caveats.
5. Export and software route: GEE, QGIS, ArcGIS, Python, R, or manual workflow.
6. Quality checks: missing data, cloud contamination, projection mismatch, resolution mismatch, sample validation.

## Key Decisions

- Landsat vs MODIS depends on spatial detail vs temporal frequency.
- Monthly, seasonal, and annual LST answer different questions.
- Street-view and satellite segmentation need different sampling and validation strategies.
- GeoAI outputs require manual or benchmark validation before becoming formal evidence.
