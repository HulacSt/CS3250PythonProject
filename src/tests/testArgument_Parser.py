import unittest
from mock import Mock
import sys
import src.argument_parser as argument_parser

class test_URL(unittest.TestCase):
    def test_single_url(self):
        sys.argv[1:] = ["--url", "google.com"]
        args = argument_parser.parse_args()
        self.assertEqual(args.url, ['google.com'])
        self.assertEqual(args.file, None)
        self.assertEqual(args.config, "")

    def test_single_file(self):
        sys.argv[1:] = ["--file", "some_file.json"]
        args = argument_parser.parse_args()
        self.assertEqual(args.file, ['some_file.json'])
        self.assertEqual(args.url, None)
        self.assertEqual(args.config, "")

    def test_single_config(self):
        sys.argv[1:] = ["--config", "some_config.yaml"]
        args = argument_parser.parse_args()
        self.assertEqual(args.config, ['some_config.yaml'])
        self.assertEqual(args.url, None)
        self.assertEqual(args.file, None)

    def test_multiple_url(self):
        sys.argv[1:] = ["--url", "google.com", "duckduckgo.com"]
        args = argument_parser.parse_args()
        self.assertEqual(args.url, ['google.com', "duckduckgo.com"])
        self.assertEqual(args.file, None)
        self.assertEqual(args.config, "")

    def test_urls_and_files(self):
        sys.argv[1:] = ["--url", "google.com", "duckduckgo.com", "--file", "some_file.json", "another_file.json"]
        args = argument_parser.parse_args()
        self.assertEqual(args.url, ['google.com', "duckduckgo.com"])
        self.assertEqual(args.file, ["some_file.json", "another_file.json"])
        self.assertEqual(args.config, "")

