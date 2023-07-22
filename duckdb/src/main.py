import duckdb

def describe_table(in_filepath):
    query = f"describe table '{in_filepath}'"
    return query

def aggregations_(in_filepath):
    query = f"""
select
    timestamp::date as day,
    min(low) as min_,
    max(high) as max_
from
    '{in_filepath}'
group by
    1
order by
    1 desc
    """

    return query

def window_functions(in_filepath):

    """
        Adds a new column having hour's high
    """

    query = f"""
select 
    timestamp,
    high,
    max(high) over (partition by date_part('hour', timestamp)) as high_hour
from 
    '{in_filepath}'
where
    timestamp::date = date '2017-01-02' and
    date_part('hour', timestamp) = 8
    """

    return query

def cte_(in_filepath):

    """
        extracted hour-wise highs - only 1 row per hour is displayed - by increasing readability of complex SQL queries with CTEs.
    """

    query = f"""
with one as (
    select 
        date_part('hour', timestamp) as hour_,
        max(high) over (partition by date_part('hour', timestamp)) as high_hour
    from 
        '{in_filepath}'
    where
        timestamp::date = date '2017-01-02'
)
select
    *
from
    one
group by
    1,
    2
order by
    1
    """

    return query

def subquery_(in_filepath):

    """
        adds a new column telling if the current row is day's high
    """

    query = f"""
with one as (
    select
        max(high) as day_high
    from
        '{in_filepath}'
    where
        timestamp::date = date '2021-01-01'
), two as (
    select 
        date_part('hour', timestamp) as hour_,
        max(high) as hour_high
    from 
        '{in_filepath}'
    where
        timestamp::date = date '2021-01-01'
    group by
        1
)
select
    *,
    case
        when hour_high = (select day_high from one) then 'yes'
        else 'no'
    end as is_day_high
from
    two
    """

    return query

def main():
    print(f"duckdb-poc: starting...")

    in_filepath = '../in/stock-market-india/FullDataCsv/NIFTY_BANK__EQ__INDICES__NSE__MINUTE.csv'
    # in_filepath = '../in/stock-market-india/FullDataCsv/*.csv'

    query = subquery_(in_filepath)

    raw_df = duckdb.sql(query).df()
    print(raw_df)

    print(f"duckdb-poc: ending...")

if __name__ == '__main__':
    main()