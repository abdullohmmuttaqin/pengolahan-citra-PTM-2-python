import cv2
import matplotlib.pyplot as plt

# Membaca gambar
image = cv2.imread('hdpjkw.png')

if image is None:
    print("Error: File 'hdpjkw.png' tidak ditemukan di folder!")
else:
    # Konversi warna BGR ke RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Konversi ke Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Gaussian Blur
    blur = cv2.GaussianBlur(image_rgb, (15, 15), 0)

    # Edge Detection
    edges = cv2.Canny(gray, 100, 200)

    # Membuat figure dan subplot
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Judul utama
    fig.suptitle("Hasil Pengolahan Citra", fontsize=22, fontweight='bold')

    # Gambar Asli
    axes[0, 0].imshow(image_rgb)
    axes[0, 0].set_title("Gambar Asli", fontsize=14, pad=10)
    axes[0, 0].axis("off")

    # Grayscale
    axes[0, 1].imshow(gray, cmap='gray')
    axes[0, 1].set_title("Grayscale", fontsize=14, pad=10)
    axes[0, 1].axis("off")

    # Gaussian Blur
    axes[1, 0].imshow(blur)
    axes[1, 0].set_title("Gaussian Blur", fontsize=14, pad=10)
    axes[1, 0].axis("off")

    # Edge Detection
    axes[1, 1].imshow(edges, cmap='gray')
    axes[1, 1].set_title("Edge Detection", fontsize=14, pad=10)
    axes[1, 1].axis("off")

    # Mengatur jarak antar elemen
    plt.subplots_adjust(
        top=0.88,
        bottom=0.06,
        left=0.05,
        right=0.95,
        hspace=0.28,
        wspace=0.18
    )

    plt.show()