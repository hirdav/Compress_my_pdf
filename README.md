# Compress_my_pdf




---

## A Text Compression Project

## Project Overview

This project applies and analyzes various **lossless compression** algorithms on a text file, focusing on `gzip`, `bz2`, and `zlib` compression methods. Using a cleaned text file, the project evaluates each algorithm's **compression ratio** and **execution time**, offering insights into the efficiency of each technique.

### Key Features
- **Text Extraction**: Extracts text from PDF and prepares it for compression.
- **Compression & Decompression**: Uses multiple lossless compression methods.
- **Performance Analysis**: Measures compression ratio and execution time.
- **Visualization**: Plots comparative charts to visualize algorithm performance.

---

## Types of Compression Used

This project specifically uses **lossless compression**, which reduces file size without losing any data. The compression methods used here are essential for applications where the integrity of text data is critical, such as documents, code, and structured data files.

### Compression Algorithms Implemented

1. **Gzip (DEFLATE Algorithm)**:
   - Combines the **LZ77** (dictionary-based) algorithm with **Huffman coding** (frequency-based).
   - Ideal for general-purpose compression, providing a balance of **compression ratio** and **speed**.

2. **Bz2 (Burrows-Wheeler Transform + Huffman Coding)**:
   - Often achieves higher compression ratios than gzip but takes more time.
   - Rearranges blocks of text so similar characters are grouped together for more efficient encoding, making it suitable for large files where high compression is critical.

3. **Zlib (DEFLATE Algorithm)**:
   - Similar to gzip but generally faster, making it ideal for streaming data.
   - Balances compression ratio and speed, often used for high-performance applications.

---

## What the Results Mean

For each compression algorithm, we calculate the following:

- **Compression Ratio**: Measures how effectively the file size is reduced.
   - Calculated as:
     \[
     \text{Compression Ratio} = \frac{\text{Compressed Size}}{\text{Original Size}}
     \]
   - A lower compression ratio means a greater reduction in file size. For instance, a ratio of `0.3` indicates that the file was compressed to 30% of its original size.

- **Compression and Decompression Time**: Indicates how fast each algorithm can compress and decompress the file.
   - This varies based on the machine and system resources but provides insight into each algorithm's efficiency.
   - For consistent timing, you can take an average over multiple runs to get more stable measurements.

### Trade-Offs to Consider

- **Compression Ratio vs. Speed**: Higher compression ratios can require more time, so the choice of algorithm depends on whether the focus is on saving storage space or on processing speed.
- **Use Case Sensitivity**: Faster algorithms (like zlib) are preferred for real-time applications, while algorithms with better ratios (like bz2) are suitable for archival storage.

---

## Installation and Setup

### Prerequisites
1. **Python 3.x** is required.
2. **Install required libraries** from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

### Dependencies
- `pymupdf`: For PDF text extraction
- `matplotlib`: For result visualization

### Project Structure

```plaintext
compression_project/
│
├── README.md               # Project overview and instructions
├── requirements.txt        # List of dependencies
├── data/
│   └── Sample.pdf # Original PDF file
│   └── text_data.txt       # Cleaned text data file
│
├── src/
│   ├── extract_text.py     # Script for extracting text from PDF
│   ├── compression.py      # Main script for compression methods
│   ├── analysis.py         # Visualization script for compression analysis
│   └── __init__.py         # Makes src a Python package
│
└── tests/
    ├── test_compression.py # Unit tests for compression methods
    └── __init__.py         # Makes tests a package
```

---

## Usage Instructions

1. **Extract Text from PDF**:
   ```bash
   python src/extract_text.py
   ```

2. **Run Compression Analysis**:
   ```bash
   python src/compression.py
   ```

3. **Visualize Results**:
   ```bash
   python src/analysis.py
   ```

---

## 📚 Resources for Learning

### To Understand Compression Algorithms and Theory:
- **Books**:
   - *"Data Compression: The Complete Reference"* by David Salomon
   - *"Introduction to Data Compression"* by Khalid Sayood
- **Courses**:
   - Coursera: "Information Theory" by the University of Illinois
   - YouTube & Khan Academy: Search for videos on Huffman Coding, LZ77, and entropy encoding.

### Python and Algorithm Knowledge:
- **Data Structures**:
   - *"Algorithms, Part I"* on Coursera by Princeton University
   - *"Algorithms"* by Robert Sedgewick and Kevin Wayne
- **Python Optimization**:
   - *"High Performance Python"* by Micha Gorelick and Ian Ozsvald

---



---

## License

This project is licensed under the MIT License.

---
