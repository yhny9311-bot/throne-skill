# Landscape Method Library

## Table of Contents

1. Urban heat environment
2. Green-space equity
3. Street-view semantics
4. Ecological networks
5. Ecosystem services
6. Urban scaling and complex systems
7. Design generation and competition expression
8. Manuscript structure archetypes

## 1. Urban Heat Environment

| Research problem | Common data | Common methods | Watch-outs |
|---|---|---|---|
| LST drivers | Landsat LST, MODIS LST, NDVI, NDBI, MNDWI, DEM, slope, NTL, population, POI | Random forest, XGBoost-SHAP, GeoDetector, MGWR, SEM | Match temporal scale; avoid predictor leakage; explain model assumptions |
| Cooling effect of green space | LST, green patch boundary, NDVI, land cover, buffer rings | Buffer gradient, cooling distance/intensity, threshold analysis | Control for water, elevation, urban density |
| Heat exposure and vulnerability | LST, population, age, income, housing, green access | Exposure index, vulnerability index, Gini, Theil, spatial regression | Avoid causal overclaim; report group definitions |
| Heat-source/cool-source network | LST/CNTI, MSPA patches, resistance surfaces | MSPA, Conefor, dPC, Linkage Mapper, Circuitscape | Justify resistance surface construction |

## 2. Green-Space Equity

| Research problem | Common data | Common methods | Watch-outs |
|---|---|---|---|
| Park accessibility | Park polygons, road network, population grid | 2SFCA, E2SFCA, KD2SFCA, network analysis | Network distance beats Euclidean distance when available |
| Supply-demand mismatch | NDVI, park area, population, vulnerable groups | Lorenz curve, Gini, Theil, spatial mismatch index | Define supply, demand, and service radius clearly |
| Socioeconomic disparity | Housing price, GDP, NTL, POI, census | MGWR, spatial Durbin model, stratified regression | Check spatial autocorrelation and multicollinearity |

## 3. Street-View Semantics

| Research problem | Common data | Common methods | Watch-outs |
|---|---|---|---|
| Visual greenery | Baidu/Tencent street view, road sampling points | GVI, semantic segmentation, SAM/SAM2/SAM3, DeepLab, Mask2Former | Sampling interval, camera angle, season, occlusion |
| Safety/comfort perception | Street view, survey, comments | Perception scoring, CLIP/multimodal models, NLP sentiment | Validate machine perception with human labels |
| Visual equity | Street-view indicators plus socioeconomic data | Clustering, MGWR, equity index | Report spatial unit and MAUP risk |

## 4. Ecological Networks

| Research problem | Common data | Common methods | Watch-outs |
|---|---|---|---|
| Source identification | LUCC, NDVI, MSPA, InVEST services | MSPA, habitat quality, ecological quality index | Avoid arbitrary source thresholds |
| Corridor identification | Sources, resistance surface | MCR, Linkage Mapper, Circuitscape, Omniscape | Resistance weights need sensitivity testing |
| Resilience assessment | Nodes, edges, corridors, patches | Complex network metrics, node attack, edge removal, robustness | Explain ecological meaning of graph metrics |
| Optimization simulation | LUCC, PLUS, ecological network | PLUS + network reconstruction, scenario simulation | Calibrate and validate simulation accuracy |

## 5. Ecosystem Services

| Service | Data | Methods | Watch-outs |
|---|---|---|---|
| Carbon storage | LUCC, carbon density table | InVEST Carbon | Carbon density source must be credible |
| Water yield | Precipitation, ET, soil, LUCC | InVEST Water Yield | Temporal mismatch affects interpretation |
| Habitat quality | LUCC, threat factors | InVEST Habitat Quality | Threat weights and distances require justification |
| Trade-off/synergy | Multiple service rasters | Correlation, bivariate Moran's I, cluster analysis | Correlation is not mechanism |

## 6. Urban Scaling and Complex Systems

| Research problem | Common data | Common methods | Watch-outs |
|---|---|---|---|
| City size and heat exposure | Population, LST, NTL | Power-law scaling, log-log regression | Define city boundary consistently |
| Economic gap and green service | GDP, housing price, green space, population | Superlinear/sublinear scaling, residual analysis | Test heteroscedasticity and influential cases |
| Night activity fluctuation | NTL time series, POI, population | Time-series metrics, volatility index, spatial heterogeneity | Distinguish observation noise from real fluctuation |

## 7. Design Generation and Competition Expression

| Task | Tools | Output |
|---|---|---|
| Technical route diagram | Mermaid, Illustrator, PPT, Python | Horizontal/vertical workflow diagram |
| A0 board | ComfyUI, Photoshop, Illustrator | Competition-grade layout, visual hierarchy |
| Landscape rendering prompt | SDXL, LoRA, ControlNet | Bird's-eye, node rendering, seasonal views |
| Hand-drawn analysis diagram | SD/PS/AI | Hand-drawn annotation and spatial decomposition |

## 8. Manuscript Structure Archetypes

| Article type | Recommended structure |
|---|---|
| Remote-sensing driver paper | Background -> indicator construction -> model explanation -> spatial mechanism -> planning implication |
| Ecological network paper | Source identification -> resistance surface -> corridors -> pinch points/barriers -> optimization |
| Equity paper | Service supply -> population demand -> spatial mismatch -> driving mechanism -> policy recommendation |
| Street-view semantics paper | Visual indicators -> spatial distribution -> group disparity -> mechanism -> micro-renewal implication |
| Complex systems paper | Scaling phenomenon -> nonlinear law -> spatial heterogeneity -> mechanism -> governance implication |
