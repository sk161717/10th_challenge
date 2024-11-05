from PIL import Image
import numpy as np

# 画像を開く
image_path = '10th-anniversary-challenge.png'  # ここに画像のパスを指定
img = Image.open(image_path)
img = img.convert('RGB')  # RGBモードに変換

# 画像データをnumpy配列に変換
img_array = np.array(img)

# 各ビットプレーンを保存するための関数
def save_bit_plane(channel_array, channel_name):
    height, width = channel_array.shape
    for bit in range(8):
        bit_plane = (channel_array >> bit) & 1  # 指定されたビットの抽出
        bit_plane = bit_plane * 255  # 0と1を0と255にスケール
        bit_img = Image.fromarray(np.uint8(bit_plane))  # 画像に変換
        bit_img.save(f'{channel_name}_bit_{bit}.png')  # ファイルに保存

# R, G, Bチャンネルごとにビットプレーン分解して保存
red_channel = img_array[:, :, 0]  # Rチャンネル
green_channel = img_array[:, :, 1]  # Gチャンネル
blue_channel = img_array[:, :, 2]  # Bチャンネル

save_bit_plane(red_channel, 'red')
save_bit_plane(green_channel, 'green')
save_bit_plane(blue_channel, 'blue')

print("ビットプレーン分解画像を保存しました。")
