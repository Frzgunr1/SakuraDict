
# SakuraDict

这是一个主要用于sakura模型的字典库，适合翻译游戏中的文本内容，旨在提高各大资源站的AI翻译质量。项目包含多个字典类别，以帮助更有效地翻译游戏对话、操作界面等特定内容。此外，还提供了字典格式转换工具，用于将不同格式的字典文件（如txt）转换为json格式，方便使用和管理。

## 项目特点
- 包含多种类型的字典，支持多样化的翻译需求。
- 可扩展字典内容，以支持更多游戏和文本场景。
- 格式转换工具，支持txt到json的转换，方便在不同项目中集成使用。

## 字典分类
1. **通用字典**：用于翻译一般的日常用语，适合所有类型的恋爱游戏文本。
2. **游戏操作界面词汇字典**：用于翻译游戏中的菜单、按钮、选项等UI元素。
3. **人名字典**：包含常见的日本名字和昵称，适合快速匹配游戏角色名称。
4. **专有名词字典**（可选）：游戏中可能出现的专有名词、游戏背景特有词汇。

每个字典文件将按照不同游戏的需求不断扩充和更新。

## 字典格式转换工具

为了便于使用和共享，项目还包含一个字典格式转换工具。此工具可以将txt格式的字典转换为json格式。json格式更便于在程序中处理，并能够被多数编程语言和框架支持。

### 使用方法
- 将txt格式字典放置在`input`文件夹下。
- 运行`converter.py`脚本。
- 输出的json文件将存储在`output`文件夹中。

转换工具支持自定义配置，如转换规则、格式校验等。

## 安装与使用

1. 克隆项目仓库到本地：
   ```bash
   git clone https://github.com/Frzgunr1/SakuraDict.git
   ```

2. 运行格式转换工具：
   ```bash
   python tools/converter.py input/yourfile.txt output/yourfile.json
   ```

3. 导入字典到你的项目：
   ```python
   import json

   with open('path_to_dictionary.json', 'r', encoding='utf-8') as f:
       dictionary = json.load(f)
   ```

## 贡献指南

欢迎对本项目进行贡献！你可以通过以下方式参与：

1. **提交新字典**：如果你进行了字典勘误，或者编写了新的词汇字典，欢迎提交PR。
2. **完善现有字典**：如果发现翻译不准确或词汇遗漏，请帮助我们改进。
3. **工具改进**：如果你对字典格式转换工具有改进建议，欢迎提交你的代码。

请确保在贡献之前阅读[贡献指南](CONTRIBUTING.md)。

## 相关项目

- [翻译工具库](https://github.com/example/translation-tool): 相关文本翻译工具。
- [日本游戏翻译字典](https://github.com/example/japanese-game-dictionary): 提供更多游戏场景的翻译支持。

## License

本项目基于[MIT License](LICENSE)发布，您可以自由使用、修改和分发代码和字典。

## 加入社群

如果你有任何问题，或者想参与讨论，请加入我们的Telegram群组。

[加入Telegram群组](https://t.me/+G0kcBnxHj585MmRl)

