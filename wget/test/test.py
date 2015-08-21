import os
import unittest
from wget.pget import download_file, get_checksum

__author__ = 'igomez'


class TestDownload(unittest.TestCase):
    def test_download_complete_file(self):
        url = "http://ipv4.download.thinkbroadband.com/5MB.zip"
        filename = "5mb.zip"
        download_file(url, 0, filename)

        self.assertEqual(get_checksum(filename), "b3215c06647bc550406a9c8ccc378756")

    def test_continue_download(self):
        url = "http://ipv4.download.thinkbroadband.com/5MB.zip"
        filename = "test_incomplete"
        download_file(url, os.path.getsize(filename), filename)

        self.assertEqual(get_checksum(filename), "b3215c06647bc550406a9c8ccc378756")
