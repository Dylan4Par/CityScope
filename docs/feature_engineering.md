# Feature Engineering Notes (Public Demo)

This document outlines **public** feature concepts used in the synthetic MVP.  
Production features, private data sources, and proprietary transformations are intentionally excluded.

## Temporal
- Hour of day, day of week, holiday flags
- Rolling traffic congestion deltas (planned)
- Event proximity windows (start/end ± 2h)

## Weather & Environment
- Temperature, precipitation, wind, visibility (proxy)
- Severe alerts (binary flags)
- Air quality / smoke indicators (planned)

## Spatial
- Tile index (H3), neighbors aggregation
- Proximity to key venues (stadiums, arenas)
- Road centrality, intersection density (planned)

## Targets
- Binary incident risk in next 30–60 minutes (synthetic in MVP)
- ETA minutes for apparatus (planned)
