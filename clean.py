import pandas as pd

# Cleanup process
# 1. Movies whose status != Released should be removed
# 2. Movies with 0 rating are removed 
# 3. Movies deemed duplicate i.e. having same title, date, language and country are removed
# 4. Movies with missing genre are removed

# Consists of scripts to clean data
class DataCleaner:
    def __init__(self, df) -> None:
        self.df = df

    def _clean_status(self):
        self.df.drop(self.df[self.df['status'] != ' Released'].index, inplace=True)

    def _remove_null_scores(self):
        self.df.drop(self.df[self.df['score'] == 0].index, inplace=True)
    
    def _remove_duplicate_movies(self):
        # Create comparison keys without changing the original columns
        movie_keys = pd.DataFrame({
            "title": self.df["orig_title"].str.strip().str.casefold(),
            "date": self.df["date_x"],
            "language": self.df["orig_lang"].str.strip().str.casefold(),
            "country": self.df['country'].str.strip().str.casefold()
        })

        duplicates = movie_keys.duplicated(keep="first")

        # Keep the first occurrence of each matching movie
        self.df = self.df.loc[~duplicates].copy()
    
    def _remove_missing_genres(self):
        # Remove missing genre
        # Find missing, empty, or whitespace-only genres
        missing_genre = self.df["genre"].isna() | self.df["genre"].str.strip().eq("")

        self.df.drop(self.df.index[missing_genre], inplace=True)
    
    def clean(self):

        # cleaning pipeline(order)
        self._clean_status()
        self._remove_null_scores()
        self._remove_duplicate_movies()
        self._remove_missing_genres()

        return self.df