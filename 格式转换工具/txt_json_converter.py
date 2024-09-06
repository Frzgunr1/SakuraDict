"""
文件格式转换脚本：txt和json互转

txt文件格式（每行的格式）：
レンタルビデオショップ=影碟出租店
シチュエーションプレイ=情景表演
ファイブドローポーカー=五张抽
立っているのがやっと=差点就站不住

json文件格式(使用较广的sakura翻译器字典格式)：
[
  {
    "Item1": "レンタルビデオショップ",
    "Item2": "影碟出租店"
  },
  {
    "Item1": "シチュエーションプレイ",
    "Item2": "情景表演"
  },
  {
    "Item1": "ファイブドローポーカー",
    "Item2": "五张抽"
  }
]
"""

import json
import os
import chardet

def detect_encoding(file_path):
    """检测编码"""
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        return result['encoding']

def txt_to_json(txt_file, json_file):
    """单txt文件转json"""
    data = []
    encoding = detect_encoding(txt_file)
    
    with open(txt_file, 'r', encoding=encoding) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if '=' in line:
                item1, item2 = line.split('=', 1)
                data.append({
                    "Item1": item1,
                    "Item2": item2
                })

    with open(json_file, 'w', encoding='utf-8') as json_out:
        json.dump(data, json_out, ensure_ascii=False, indent=2)

def json_to_txt(json_file, txt_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    with open(txt_file, 'w', encoding='utf-8') as file:
        for entry in data:
            line = f"{entry['Item1']}={entry['Item2']}\n"
            file.write(line)

def convert_all_txt_in_folder(folder_path):
    """转换文件夹下所有txt文件为json文件"""
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            txt_file = os.path.join(folder_path, filename)
            json_file = os.path.join(folder_path, filename.replace('.txt', '.json'))
            txt_to_json(txt_file, json_file)
            print(f"转换完成: {txt_file} -> {json_file}")

def convert_all_json_in_folder(folder_path):
    """转换文件夹下所有json文件为txt文件"""
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            json_file = os.path.join(folder_path, filename)
            txt_file = os.path.join(folder_path, filename.replace('.json', '.txt'))
            json_to_txt(json_file, txt_file)
            print(f"转换完成: {json_file} -> {txt_file}")

def main():
    print("请选择功能:")
    print("1: txt 转 json")
    print("2: json 转 txt")
    choice = input("输入 1 或 2: ")

    folder_path = './'  # 当前文件夹

    if choice == '1':
        convert_all_txt_in_folder(folder_path)
    elif choice == '2':
        convert_all_json_in_folder(folder_path)
    else:
        print("无效选择，请输入 1 或 2")

if __name__ == "__main__":
    main()
