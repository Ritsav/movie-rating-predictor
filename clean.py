# Cleanup process
# 1. Rows with 0 humidity are removed (sensor failure, all 22 are from 2011-03-10)
# 2. Rows sharing the same date and hour are removed
# 3. Leakage and index columns are removed (casual + registered = cnt, instant is just a row number)

# Consists of scripts to clean data
class DataCleaner:
    def __init__(self, df) -> None:
        self.df = df

    def _remove_zero_humidity(self):
        self.df.drop(self.df[self.df['hum'] == 0].index, inplace=True)

    def _remove_duplicate_hours(self):
        # Keep the first occurrence of each date + hour
        duplicates = self.df.duplicated(subset=["dteday", "hr"], keep="first")

        self.df = self.df.loc[~duplicates].copy()

    def _drop_leakage_columns(self):
        # casual + registered add up to cnt, so keeping them would hand the model the answer
        self.df.drop(columns=['casual', 'registered', 'instant'], inplace=True)

    def clean(self):

        # cleaning pipeline(order)
        self._remove_zero_humidity()
        self._remove_duplicate_hours()
        self._drop_leakage_columns()

        return self.df
