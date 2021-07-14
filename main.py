"""Entry point for Tweet Collector."""

import argparse as ap
import os
import signal
import typing


def main() -> None:
    """Initialize TweetCollector.

    Entry point for tweet collector.
    Parsing of command line input, reading
    environment variables, setup of signal
    handling, and reconnection.
    """
    parser: ap.ArgumentParser = ap.ArgumentParser(
        description="Tweet Collector.",
        epilog="REEEEEEEEEEEEEEEEEE")
    parser.add_argument(
        '-fh',
        '--fileHashtags',
        required=True,
        help="File of hashtags in each line without '#'",
        type=str,
        dest='fh')
    parser.add_argument(
        '-db',
        '--dataBase',
        required=True,
        help="Name of the database.",
        type=str,
        dest='db')
    args = vars(parser.parse_args())

    # hashtag file
    path: str = args['fh']
    f: typing.TextIO = open(path, 'r')
    hashtags: list = f.read().splitlines()

    # signal processing
    def signal_handler(sig, frame):

        print('You pressed Ctrl+C!')
        # db.close()
        print('Database connection closed')
        sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)

    # load environment
    TWITTER_CONSUMER_KEY: str = os.getenv('TWITTER_CONSUMER_KEY'),
    TWITTER_CONSUMER_SECRET: str = os.getenv('TWITTER_CONSUMER_SECRET')
    TWITTER_ACCESS_TOKEN: str = os.getenv('TWITTER_ACCESS_TOKEN'),
    TWITTER_ACCESS_TOKEN_SECRET: str = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')


    # reconnecting


if __name__ == "__main__":
    main()
