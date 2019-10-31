# s6-lastpass-csv-parser

The `lastpass.py` script parses out the exported csv file from Lastpass into separated csv files for
each folder. It helps that you could import specific folder/csv file into 1Password.

## How to use
1. Save and named your exported Lastpass csv file as `lastpass.csv`
2. Run `python3 lastpass.py`
3. `lastpass.csv` will be split up to many csv files by the folder names. Secrets without folder name will be put into `default.csv`