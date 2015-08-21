import hashlib
import logging
import urllib2
from urllib2 import HTTPError

__author__ = 'igomez'

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('pget.download')

# Size of the block read from the stream
BLOCK_SIZE = 8192


def get_checksum(filename):
    hash_ = hashlib.md5()
    with open(filename) as f:
        for chunk in iter(lambda: f.read(4096), ""):
            hash_.update(chunk)
    return hash_.hexdigest()


def download_file(url, offset=0, filename='tmp', verbosity=True):
    """
    Intended for simulating the wget linux command
    :param url: The URL for the resource to be downloaded
    :param offset: Number of bytes to be skipped
    :param filename: Name of file where the content downloaded will be stored
    :param verbosity: Boolean value that indicates the verbosity in logger
    :return: None
    """
    logger.setLevel(logging.DEBUG) if verbosity else logger.setLevel(logging.INFO)

    headers = {'Range': "bytes=%s-" % offset, 'Accept': '*/*', 'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) '
                             'Chrome/23.0.1271.64 Safari/537.11'}
    logger.debug("Setting Range Header for HTTP Request")

    if offset != 0:
        logger.info("This download is being resumed")

    req = urllib2.Request(url, headers=headers)

    try:
        logger.debug("Opening URL")
        u = urllib2.urlopen(req)

        to_download = int(u.info().getheaders("Content-Length")[0])
        logger.debug("The program will download %s bytes" % to_download)

        f = open(filename, 'ab') if offset != 0 else open(filename, 'wb')
        logger.debug("The file is going to be downloaded with a block size of %s bytes" % BLOCK_SIZE)

        buffer_ = u.read(BLOCK_SIZE)
        downloaded = 0

        while buffer_:
            downloaded += len(buffer_)
            logger.debug("%d  %3.2f%%" % (downloaded, downloaded * 100. / to_download))

            f.write(buffer_)
            buffer_ = u.read(BLOCK_SIZE)

        f.close()

        logger.info("The download has finished")
        return True

    except HTTPError, e:
        if e.code == 416:
            logger.info("This file has been downloaded already")

    except ValueError:
        logger.exception("The string %s is not a valid url" % url)

    return False
