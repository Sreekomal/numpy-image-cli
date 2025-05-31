Sure, Sreek! Here's your complete `README.md` content again — ready to copy and paste:

---

# 🖼️ PGM Image Processor CLI

A simple command-line image processing tool built using **Python** and **NumPy** that supports grayscale `.pgm` (Portable GrayMap) images. Features include inversion, thresholding, contrast stretching, statistics, and ASCII art preview.

---

## 📌 Features

* ✅ Invert grayscale images
* ✅ Apply thresholding
* ✅ Contrast stretching
* ✅ ASCII preview of images in terminal
* ✅ Show image statistics (mean, std, min, max)

---

## 📂 Usage

```bash
python image_processor.py input.pgm output.pgm [options]
```

### 📋 Options

| Flag              | Description                             |
| ----------------- | --------------------------------------- |
| `--invert`        | Inverts the image                       |
| `--threshold VAL` | Applies thresholding at a given value   |
| `--contrast`      | Enhances contrast via linear stretching |
| `--ascii`         | Shows an ASCII preview before and after |
| `--stats`         | Prints image statistics                 |

---

## 🚀 Example

```bash
python image_processor.py sample.pgm output.pgm --invert --ascii --stats
```

---

## 📦 Requirements

* Python 3.x
* NumPy

Install NumPy with:

```bash
pip install numpy
```

---

## 📁 Sample Output

**ASCII Preview (original and processed)**

```
🖼️ Original Image Preview:
@%%#**+=-:
...
🎨 Processed Image Preview:
@@%%%##**-
```

**Statistics:**

```
Dimensions: 256 x 256  
Mean brightness: 127.53  
Standard deviation: 20.42  
Min pixel: 0  
Max pixel: 255  
```

---

## 🎯 My Learning Milestone

In my journey of learning, this project marks my **first milestone** — a project built entirely using **Python and NumPy**! 📈
It helped me understand image processing basics and file manipulation in a hands-on way.

---

## 🤝 Contributions

Pull requests are welcome! Feel free to fork and build on this.

---

## 📄 License

This project is licensed under the MIT License.

---
Absolutely! Here's a clean **"How to Run"** section you can add to your GitHub README:

---

## 🚀 How to Run

### 📋 Prerequisites

* Python 3.x installed
* `numpy` library installed (you can install it via pip)

```bash
pip install numpy
```

---

### ▶️ Run the Program

1. Open a terminal and navigate to the project directory.

2. Use the following command format:

```bash
python image_processor.py input.pgm output.pgm [options]
```

### 🛠️ Available Options

* `--invert` → Invert the image colors
* `--threshold VALUE` → Apply binary thresholding at a given value (0–255)
* `--contrast` → Apply contrast stretching
* `--ascii` → Show ASCII art preview
* `--stats` → Show image statistics

---

### 💡 Example Command

```bash
python image_processor.py sample.pgm result.pgm --invert --ascii --stats
```

This will:

* Invert the grayscale image
* Show ASCII previews (before & after)
* Print image statistics to the terminal

---


