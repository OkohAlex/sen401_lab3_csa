# SEN 401 Lab 3: Configuration Status Accounting

An individual inventory project demonstrating corrective, adaptive,
perfective, and preventive maintenance together with Git-based configuration
status accounting.

## Project structure

- `app.py` displays inventory quantities and stock valuation.
- `inventory.py` contains the sample inventory records.
- `models.py` defines the validated inventory item type.
- `utils/helpers.py` contains reusable inventory calculations.
- `tests/` covers calculations and invalid inventory data.
- `status_accounting.csv` maps maintenance work to actual Git commits.
- `changelog.txt` is exported from the Git history.

## Run

Python 3.10 or later is recommended. The application uses only the standard
library.

```powershell
python app.py
python -m unittest discover -s tests -v
```

## Version control

The `dev` branch contains the maintenance work. The `v1.0` tag marks the
completed Lab 3 baseline.
