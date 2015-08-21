import logging
import argparse
import os
from wget import pget

__author__ = 'igomez'


def get_size(file_name):
    """
    Get the file size of file_name
    :param file_name: Name of the file to measure
    :return: size of the file if it exists otherwise returns 0
    """
    return os.path.getsize(file_name) if os.path.isfile(file_name) else 0


if __name__ == '__main__':

    FORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.INFO)
    logger = logging.getLogger('pget.client')

    parser = argparse.ArgumentParser(description='Program that works like wget')
    parser.add_argument('url', help='URL to resource to be downloaded')
    parser.add_argument('-c', '--continue', action='store_true', help='Continue an incomplete download from this url')
    parser.add_argument('-o', '--outfile', nargs='?',
                        help='Set the file name where the content be stored. This param is optional')
    parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity')

    args = vars(parser.parse_args())

    url = args.get("url")
    filename = args.get("outfile", None) or url.split('/')[-1]

    logger.info('Starting download')
    if args.get("continue", False):
        pget.download_file(url, get_size(filename), filename=filename, verbosity=args.get("verbose"))
    else:
        pget.download_file(url, filename=filename, verbosity=args.get("verbose"))
