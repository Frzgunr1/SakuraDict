
# SakuraDict

## TODO List

- [ ] 修正现有的 **base_dict** 内容，并且扩展更多常用词汇。
- [ ] 更新 **游戏操作界面词汇字典**，补充更多游戏中常见的UI元素。
- [ ] 扩充 **人名字典**，包括更多日本常见人名和昵称。（考虑到同社团人物有时会客串，也应添加常见作品中的角色姓名）
- [O] 支持 json -> txt 的双向转换功能。
- [O] 编写详细的项目使用文档，包括安装与使用说明。
- [ ] 增加对外部API的支持，以实现在线字典更新功能。

---
这是一个主要用于sakura模型的字典库，适合翻译游戏中的文本内容，旨在提高各大资源站的AI翻译质量。项目包含多个字典类别，以帮助更有效地翻译游戏对话、操作界面等特定内容。此外，还提供了字典格式转换工具，用于将不同格式的字典文件（如txt和json）相互转换，方便使用和管理。（目前转换后的json格式为[AITranslator](https://github.com/jxq1997216/AITranslator)翻译器的标准字典格式）。
---

## 项目特点
- 包含多种类型的字典，支持多样化的翻译需求。
- 可扩展字典内容，以支持更多游戏和文本场景。
- 格式转换工具，支持txt和json的相互转换，方便在不同项目中集成使用。

## 字典分类
1. **通用字典**：用于翻译一般的日常用语，适合所有类型的恋爱游戏文本。
2. **游戏操作界面词汇字典**：用于翻译游戏中的菜单、按钮、选项等UI元素。
3. **人名字典**：包含常见的日本名字和昵称，适合快速匹配游戏角色名称。
4. **专有名词字典**（可选）：游戏中可能出现的专有名词、游戏背景特有词汇。

每个字典文件将按照不同游戏的需求不断扩充和更新。

## 字典格式转换工具

为了便于使用和共享，项目还包含一个字典格式转换工具。它的功能是**将同目录下的所有txt文档和json文档相互转换**

### 使用方法
- 直接运行txt_json_converter.exe.


## 安装与使用

1. 克隆项目仓库到本地：
   ```bash
   git clone https://github.com/Frzgunr1/SakuraDict.git
   ```

2. 运行格式转换工具：
   ```bash
   python txt_json_converter.py
   ```

3. 使用你的字典


## 贡献指南

欢迎对本项目进行贡献！你可以通过以下方式参与：

1. **提交新字典**：如果你进行了字典勘误，或者编写了新的词汇字典，欢迎提交PR。
2. **完善现有字典**：如果发现翻译不准确或词汇遗漏，请帮助我们改进。
3. **工具改进**：如果你对字典格式转换工具有改进建议，欢迎提交你的代码。


## 相关项目

以下是一些相关的翻译项目，涵盖了轻小说、Galgame、RPG游戏、音声的翻译工具和资源：

- [SakuraLLM](https://github.com/SakuraLLM/SakuraLLM)：SakuraLLM项目，提供文本生成和翻译的高级工具，适合用于游戏翻译等场景。
 
- [Text-generation-webui](https://github.com/oobabooga/text-generation-webui)：原始的文本生成项目，提供了基础的文本生成框架，适合各类文本翻译和生成应用的搭建。

- **[AITranslator](https://github.com/jxq1997216/AITranslator)**：本项目最推荐使用的翻译器。支持包括json、srt、txt格式的文本翻译，支持队列翻译。

- [轻小说机翻机器人](https://books.fishhawk.top/)：用于轻小说的机器翻译，方便快速获取小说内容的翻译结果。
  
- [LunaTranslator](https://github.com/HIllya51/LunaTranslator)：一个在线Galgame翻译工具，支持通过在线方式对游戏文本进行实时翻译。
  
- [GalTransl](https://github.com/XD2333/GalTransl)：离线Galgame翻译工具，支持制作翻译补丁，方便离线情况下对游戏文本进行翻译。
  
- [AiNiee](https://github.com/NEKOparapa/AiNiee-chatgpt)：基于AI的RPG游戏翻译项目，旨在通过AI技术实现更高效的游戏文本翻译。

## License

本项目基于[MIT License](LICENSE)发布，您可以自由使用、修改和分发代码和字典。

## 加入社群

如果你有任何问题，或者想交流ai翻译，请加入我们的Telegram群组。

[加入Telegram群组](https://t.me/+G0kcBnxHj585MmRl)

## 鸣谢

感谢某+论坛的同好提供初版字典，希望能提高大家AI翻译的质量。

