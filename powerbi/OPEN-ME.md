# Opening the Power BI report

`AdelaideLandUse.pbip` is a Power BI Project: the report (`AdelaideLandUse.Report`, PBIR format) and the semantic model (`AdelaideLandUse.SemanticModel`, TMDL) saved as text, so the repo can show every change. Power BI Desktop opens it like a `.pbix`.

## What you need

- Power BI Desktop for Windows, a recent version (2026). Projects and the PBIR report format are standard in current versions. If Desktop is older than about mid 2025, turn on **File, Options and settings, Options, Preview features, Power BI Project (.pbip) save option** and **Store reports using enhanced metadata format (PBIR)**, then restart Desktop.
- The repo folder on the Windows machine. In Parallels the Mac home folder is usually shared as `\\Mac\Home`.

## Open it

1. In Windows, go to the repo's `powerbi` folder and double-click `AdelaideLandUse.pbip`, or in Desktop use **File, Open report, Browse reports** with the file type set to *Power BI project files (\*.pbip)*.
2. The visuals are empty the first time. Select **Refresh** on the Home ribbon.
   - By default the data is read from the repo's public copy on GitHub (`DataFolder` is `https://raw.githubusercontent.com/cjmuldoon/plotlay-adelaide-land-use-change/main/data/`). If Desktop asks how to connect, choose **Anonymous** and then **Connect**.
   - To read the files from disk instead, go to **Home, Transform data, Edit parameters** and set `DataFolder` to the full path of the repo's `data` folder, **ending with a backslash** (for example `\\Mac\Home\plotlay-adelaide-land-use-change\data\`). Then select **OK** and **Apply changes**.
   - If Desktop warns about privacy levels, choose **Ignore privacy levels** (all the sources are public open data).
3. Check the numbers (below).

If the report was updated while open, close Power BI and reopen the .pbip rather than using Apply external changes.

## Check the numbers after Refresh

After **Refresh**, on **Greenfield and infill** (as the report opens):

| Card | Should read |
|---|---|
| Approved residential allotments | 85,145 |
| Greenfield share | 44% |
| Infill share | 39% |
| Farm and rural land now residential, ha | 1,101 |

The SA2 totals leave out the few allotments that fall outside every SA2 of Greater Adelaide, so they can sit a little under the README's 85,145.

## The model

- **SA2**: one row per Greater Adelaide SA2 (`data/tables/by_sa2.csv`): approved residential allotments by kind and the greenfield hectares. Measures: `Allotments`, `Greenfield allotments`, `Infill allotments`, `Greenfield share`, `Infill share`, `Greenfield hectares`.
- **Councils** (`by_council.csv`), **Years** (`by_year.csv`, by financial year lodged) and **Applications** (`applications.csv`, one row per land division with the allotments it made).

## The map

The Shape Map on page 1 has its custom map saved inside the report (`AdelaideLandUse.Report/StaticResources/RegisteredResources/`): Greater Adelaide's SA2s keyed by ABS code, with South Australia's councils round them in a pale ground tone. If it shows the world instead: select it, then **Format visual**, **Visual**, **Map settings**, **Map type: Custom map**, **Add map type**, and choose `..\data\geometry\sa2.topojson`. If the Shape Map is not in the Visualizations pane, turn it on in **File, Options and settings, Options, Preview features, Shape map visual** and restart Desktop.

## Save a .pbix too

After the refresh, use **File, Save as** with the type **Power BI file (\*.pbix)** to save `powerbi\AdelaideLandUse.pbix`. It includes the data, so it opens without a refresh.

## Publish (only if you choose to)

Use **Home, Publish**. In the Power BI service, set the semantic model's **Data source credentials** for the GitHub address to **Anonymous**. Scheduled refresh then works with no gateway. **Publish to web** makes a public link, so only use it if you mean the report to be public.

## Shot list for the website and the video

| # | Shot | How | Length |
|---|---|---|---|
| 1 | Greenfield and infill | As it opens | still |
| 2 | Infill | As it opens | still |
| 3 | Each year | As it opens | still |

Save page images into `powerbi/Screenshots/` (a PDF export of all pages is fine too).
