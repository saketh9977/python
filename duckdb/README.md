### Purpose
1. Query tabular data (eg. CSV) using SQL interface in Python for single-node computation
2. For SQL interface in distributed computation (multi-node), you may consider using AWS Athena (Presto), Hive SQL in PySpark etc.

### Why `duckdb`?
1. Looks like `duckdb` is [more efficient](https://stackoverflow.com/a/70538527/8279892) than `pandasql`
2. Opensource (MIT License) with [11k+ stars on github](https://github.com/duckdb/duckdb) as of 22 July 2023 with [PRs getting merged almost daily](https://github.com/duckdb/duckdb/pulls?q=is%3Apr+is%3Aclosed) & 500+ 😁 open issues
3. Easy to start with, as `duckdb` [offers many of the same SQL features as Postgres](https://duckdb.org/2021/05/14/sql-on-pandas.html), which many of us are familiar with

### Dataset
1. NSE-India data - [link](https://www.kaggle.com/datasets/hk7797/stock-market-india)
2. About 3.1 GB in size
3. 57M rows (56917962)
4. Available in 2 formats: CSV & h5

### Exploration
1. Window Functions: Adds a new column having hour's high
2. CTEs: extracted hour-wise highs - only 1 row per hour is displayed - by increasing readability of complex SQL queries with CTEs.
3. subqueries: adds a new column telling if the current row is day's high
4. Didn't test joins but `duckdb` [supports](https://duckdb.org/docs/sql/query_syntax/from.html#joins) Joins.
5. Aggregations, group-by, describing a table etc. are tested

