
"""Console script for py_sec_edgar."""

import sys

import feeds as py_sec_edgar_feeds
import etl as py_sec_edgar_etl

def main():

    py_sec_edgar_feeds.update_full_index_feed()

    df_filings = py_sec_edgar_feeds.load_filings_feed(ticker_list=True, form_list=True)

    for i, feed_item in df_filings.iterrows():

        py_sec_edgar_etl.broker(feed_item)

if __name__ == "__main__":

    main()

    sys.exit()
