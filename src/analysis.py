import matplotlib.pyplot as plt

# results as per compression data
methods = ["gzip", "bz2", "zlib"]
ratios = [0.26, 0.20, 0.20]  
times = [0.0475, 0.0542, 0.0319]  
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.barh(methods, ratios, color='skyblue')
plt.xlabel("Compression Ratio")
plt.title("Compression Ratio by Method")

plt.subplot(1, 2, 2)
plt.barh(methods, times, color='salmon')
plt.xlabel("Time (seconds)")
plt.title("Compression Time by Method")

plt.tight_layout()
plt.show()



