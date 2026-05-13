import cv2
import matplotlib.pyplot as plt

# Membaca gambar
image = cv2.imread('hdpjkw.png')

if image is None:
    print("Error: File 'hdpjkw.png' tidak ditemukan di folder!")
else:
    # Proses pengolahan citra
    # Konversi ke RGB 
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Konversi ke Grayscale 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Efek Blur
    blur = cv2.GaussianBlur(image_rgb, (15, 15), 0)

    # Edge detection 
    edges = cv2.Canny(image, 100, 200)

    # Menampilkan hasil dengan subplot
    plt.figure(figsize=(12, 8))

    # Gambar asli
    plt.subplot(2, 2, 1)
    plt.imshow(image_rgb)
    plt.title('Gambar Asli')
    plt.axis('off')

    # Gambar Grayscale
    plt.subplot(2, 2, 2)
    plt.imshow(gray, cmap='gray')
    plt.title('Grayscale')
    plt.axis('off')

    # Gambar Blur
    plt.subplot(2, 2, 3)
    plt.imshow(blur)
    plt.title('Gaussian Blur')
    plt.axis('off')

    # Edge Detection
    plt.subplot(2, 2, 4)
    plt.imshow(edges, cmap='gray')
    plt.title('Edge Detection')
    plt.axis('off')

    # Merapikan tata letak
    plt.tight_layout()
    plt.show()
