# Bike sharing demand prediction

This project predicts the number of bikes rented per hour (`cnt`) from time and weather features, using the hourly Capital Bikeshare data (Washington D.C., 2011-2012, 17,379 rows) from the UCI Bike Sharing dataset. It replaces the movie rating experiment, which is archived in `failed/` because its features had very little signal.

Run notebooks with this folder as the working directory and the repository environment. The CSV is kept locally at `data/bike_hour.csv` (copied from the dataset's `hour.csv`); datasets are excluded from Git.

Cleaning (`clean.py`) removes 22 zero-humidity rows (a sensor failure on 2011-03-10), duplicate date + hour rows (none found) and the `casual`, `registered` and `instant` columns, since casual + registered add up to the target. Preprocessing (`preprocess.py`) converts the normalized weather columns back to real units and adds sin/cos month columns. `atemp` and `season` are left out of the features because they mostly repeat `temp` and `mnth`.

Three models are compared in `models.ipynb`: linear regression, random forest and histogram gradient boosting, on one random 80/20 split (RMSE and R² on the test set, plus how often the prediction is within 25 and 50 rentals). Its limitations: a random split on hourly data is optimistic because neighbouring hours of the same day end up in both train and test, windspeed zeros are kept although they may be missing readings, hours with 0 rentals are not in the data at all (the lowest count is 1), and the same test split was used to compare all three models.
