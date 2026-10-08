import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer, OneHotEncoder

# Preprocessing logic of data

def split_date_to_year_and_month(df):
    # convert the str date column into datetime
    df['date_x'] = pd.to_datetime(df['date_x'])

    # extract new year and month columns from date
    df['year'] = df['date_x'].dt.year
    df['month'] = df['date_x'].dt.month

    return df

def split_genre(df):
    genres = df["genre"].fillna("").apply(
        lambda s: [g.strip() for g in s.split(",") if g.strip()]
    )

    mlb = MultiLabelBinarizer()
    return pd.DataFrame(
        mlb.fit_transform(genres),
        columns=mlb.classes_,
        index=df.index
    )