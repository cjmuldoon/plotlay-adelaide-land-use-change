# The data

Made from the Department for Housing and Urban Development's Land Use Generalised and Land Division Applications and ABS boundaries (all CC BY), see [`../NOTICE`](../NOTICE); our tables and shapes are CC BY 4.0.

- `tables/allotments.csv`: every approved residential allotment (purpose RES or CRES) in a land division lodged 1 July 2018 to 30 June 2025 in Greater Adelaide (85,145). `edalaid` (the application), `lotno`, `year` (lodged), `fy` (financial year lodged), `apptyp`, `propstatus`, `kind`, `c2018` and `c2025` (the land use class at the allotment's inside point in each year's layer), `sa2_code`, `sa2_name`, `lga_code`, `lga_name`, `lat`, `lon`. `kind`: Infill (residential in 2018), Greenfield (farmland, vacant land or rural living in 2018), Vacant residential land (vacant urban land in 2018), Brownfield and other (industry, commerce, institutions), Not in the 2018 layer.
- `tables/applications.csv`: one row per application: `lots` (the allotments its footprint became), `kind` (most of its allotments), `year`, `size_band`.
- `tables/by_sa2.csv`, `tables/by_council.csv`: allotments by kind and `greenfield_ha` (land that was farm, vacant or rural living in 2018, residential in 2025, with a residential land division over it) and `recoded_ha` (the same change with no division: likely a change of valuation code).
- `tables/by_year.csv`: allotments by financial year lodged and kind.
- `tables/transitions_ha.csv`: Greater Adelaide's land, the 2018 class (rows) against the 2025 class (columns), hectares.
- `tables/area_by_year.csv`: Greater Adelaide's area in each class each year, 2015 to 2025, hectares: the check for whole-area jumps.
- `tables/class_words.json`: the layer's class codes in words.
- `geometry/greenfield.geojson`: the greenfield pieces, `confirmed` true where a residential land division overlaps.
- `geometry/sa2.*`, `geometry/mount_barker.*` (the Mount Barker SA2's land in pieces, each with its 2018 and 2025 class), `geometry/hex_infill.*`, `geometry/hex_greenfield.*` (1 km hexagons with their allotment counts): as Plotlay made and exported them.

The state-wide land use layers are not copied here (about 1 GB): `python/download.py` fetches them.
