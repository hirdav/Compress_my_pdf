import unittest
import os
import sys
import os


# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from src.extract_text_and_ascii_from_pdf import extract_text_and_ascii_from_pdf
from src.compression import gzip_compress, bz2_compress, zlib_compress, gzip_decompress, bz2_decompress, zlib_decompress

class TestCompressionProject(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up paths
        cls.project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        cls.pdf_path = os.path.join(cls.project_root, "data", "sample4.pdf")
        cls.text_path = os.path.join(cls.project_root, "data", "text_data_with_ascii.txt")

        # Extract text from PDF if not already done
        if not os.path.exists(cls.text_path):
            extract_text_and_ascii_from_pdf(cls.pdf_path, cls.text_path)

        # Load the text data for testing
        with open(cls.text_path, "r", encoding="utf-8") as file:
            cls.text_data = file.read()

    def test_text_extraction(self):
        """Test that text extraction produces non-empty output."""
        self.assertTrue(len(self.text_data) > 0, "Text extraction failed; output is empty.")

    def test_gzip_compression(self):
        """Test gzip compression and decompression."""
        compressed_data, _ = gzip_compress(self.text_data)
        decompressed_data = gzip_decompress(compressed_data)
        self.assertTrue(len(compressed_data) < len(self.text_data.encode('utf-8')), "gzip compression did not reduce size.")
        self.assertEqual(self.text_data, decompressed_data, "gzip decompression did not return original text.")

    def test_bz2_compression(self):
        """Test bz2 compression and decompression."""
        compressed_data, _ = bz2_compress(self.text_data)
        decompressed_data = bz2_decompress(compressed_data)
        self.assertTrue(len(compressed_data) < len(self.text_data.encode('utf-8')), "bz2 compression did not reduce size.")
        self.assertEqual(self.text_data, decompressed_data, "bz2 decompression did not return original text.")

    def test_zlib_compression(self):
        """Test zlib compression and decompression."""
        compressed_data, _ = zlib_compress(self.text_data)
        decompressed_data = zlib_decompress(compressed_data)
        self.assertTrue(len(compressed_data) < len(self.text_data.encode('utf-8')), "zlib compression did not reduce size.")
        self.assertEqual(self.text_data, decompressed_data, "zlib decompression did not return original text.")

if __name__ == "__main__":
    unittest.main()
