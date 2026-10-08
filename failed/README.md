# Movie rating prediction — archived experiment

This folder preserves the original movie EDA, cleaning, preprocessing, models and unseen-movie examples. Both notebooks were executed from a fresh kernel before this archive was committed.

Run notebooks with this folder as the working directory and the repository environment. The original CSV is retained locally at `data/movies.csv`; datasets are excluded from Git. The three unseen-movie inputs and predictions are in `results/`.

The final saved movie experiment used linear regression, Ridge, random forest and histogram gradient boosting. Its limitations include ambiguous zero ratings, suspicious financial values, a metadata-only rating prediction task, and repeated model comparisons on the same test split. The folder name records the project pivot, not proof that its models have no predictive value.
