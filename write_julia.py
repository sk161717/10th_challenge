import numpy as np
import matplotlib.pyplot as plt

def julia_set(c_real, c_imag, top, left, width, height, img_width=797, img_height=797, max_iter=256):
    # 計算領域の座標を設定
    x = np.linspace(left, left + width, img_width)
    y = np.linspace(top, top + height, img_height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    C = complex(c_real, c_imag)
    
    # 繰り返し回数を計算
    img = np.zeros(Z.shape, dtype=int)
    mask = np.ones(Z.shape, dtype=bool)
    
    for i in range(max_iter):
        Z[mask] = Z[mask] ** 2 + C
        mask = np.abs(Z) < 2
        img += mask
    
    return img

def save_julia_set(c_real, c_imag, top, left, width, height, filename='julia_set.png'):
    # ジュリア集合の計算
    img = julia_set(c_real, c_imag, top, left, width, height)
    
    # プロットしてファイル保存
    plt.imshow(img, cmap='Blues_r', extent=(left, left + width, top - height, top))
    plt.colorbar()
    plt.title(f"Julia Set: c = {c_real} + {c_imag}i")
    plt.savefig(filename, dpi=300)
    plt.close()

# パラメータを指定して呼び出し
c_real = -0.7012  # x方向のc
c_imag = 0.2701  # y方向のc
top = -0.75  # 上端
left = 0.0  # 左端
width = 1.5  # 幅
height = 1.5  # 高さ

# 画像ファイルとして保存
save_julia_set(c_real, c_imag, top, left, width, height, filename='julia_set2.png')
