import os
import gzip
import bz2
import zlib
import time

# Get the absolute path to the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Define path to the text file
text_file_path = os.path.join(project_root, "data", "text_data_with_ascii.txt")

def gzip_compress(text):
    start_time = time.time()
    compressed_data = gzip.compress(text.encode('utf-8'))
    return compressed_data, time.time() - start_time

def bz2_compress(text):
    start_time = time.time()
    compressed_data = bz2.compress(text.encode('utf-8'))
    return compressed_data, time.time() - start_time

def zlib_compress(text):
    start_time = time.time()
    compressed_data = zlib.compress(text.encode('utf-8'))
    return compressed_data, time.time() - start_time

if __name__ == "__main__":
    # Check if the text file exists before attempting compression
    if not os.path.exists(text_file_path):
        print(f"Error: Text file not found at {text_file_path}")
    else:
        # Load text data
        with open(text_file_path, "r", encoding="utf-8") as file:
            text_data = file.read()

        # Compression analysis
        for compress_func, name in [
            (gzip_compress, 'gzip'),
            (bz2_compress, 'bz2'),
            (zlib_compress, 'zlib')
        ]:
            compressed_data, compress_time = compress_func(text_data)
            compression_ratio = len(compressed_data) / len(text_data.encode('utf-8'))
            print(f"{name} - Compression Ratio: {compression_ratio:.2f}, Time: {compress_time:.4f}s")
