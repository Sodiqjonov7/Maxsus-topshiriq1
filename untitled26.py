# -*- coding: utf-8 -*-
"""Untitled26.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VoRHT4BA8nkBNMIHedYcwQPgZuTWntM9
"""

import numpy as np
import matplotlib.pyplot as plt

# Sinus funksiyasi uchun x qiymatlari va y = sin(x) ni aniqlash
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.sin(x)

# Grafikni yaratish
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="y = sin(x)", color="blue")
plt.title("Sinus Funktsiyasi Grafigi", fontsize=14)
plt.xlabel("x qiymati", fontsize=12)
plt.ylabel("y qiymati", fontsize=12)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.grid(alpha=0.3)
plt.legend(fontsize=12)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x_random = np.random.rand(100) * 10
y_random = np.random.rand(100) * 10

plt.figure(figsize=(10, 6))
plt.scatter(x_random, y_random, color="red", alpha=0.7, marker="o", edgecolors="black")
plt.title("Tasodifiy Nuqtalar Scatter Grafigi (Nuqtalar orqali)", fontsize=14)
plt.xlabel("X qiymatlari", fontsize=12)
plt.ylabel("Y qiymatlari", fontsize=12)
plt.grid(alpha=0.3)
plt.show()