# IELTS Practice

一个结构化的IELTS练习仓库，包含阅读、写作、语法和听力模块的学习材料、进度跟踪和辅助工具。

## 📋 项目概览

这是一个个人使用的IELTS学习管理系统，帮助用户：
- 📚 系统化地组织和跟踪每日练习
- 🤖️ 使用AI辅助工具分析和标注学习材料
- 📊 按月/日结构管理练习记录
- 📖️ 存储标准化的练习材料

## ✨ 主要功能

- **IELTS文章标注器** - 自动提取和标注阅读文章的主题、词汇和语法点
- **练习进度跟踪** - 按日期和类型组织每日练习（早间、午间、晚间卡片）
- **标准化练习材料** - 包含阅读理解、写作任务、语法练习等
- **学习笔记管理** - 按主题分类（语法、听力、摘要、技术笔记）
- **辅助工具集** - 自动化处理文章、生成演示和创建技能定义

## 🚀 快速开始

### 前置要求

- 查看阅读材料：`practice/reading/`
- 查看写作练习：`practice/writing/`
- 运行标注工具：查看 `docs/IELTS_ANNOTATOR_GUIDE.md`
- 查看每日记录：`practice/daily/`

### 文件结构

```
IELTS_Practice/
├── *.py                          # Python工具脚本
├── docs/                         # 项目文档
│   ├── README.md              # 详细文档（本文件）
│   ├── IELTS_ANNOTATOR_GUIDE.md
│   ├── MATERIAL-EXTRACTION-STANDARDS.md
│   ├── REVIEW-STRATEGY.md
│   ├── TOOLS_SUMMARY.md
│   └── VALIDATION-REPORT.md
├── practice/                      # 练习材料
│   ├── README.md
│   ├── daily/                 # 每日练习记录（按月组织）
│   │   ├── YYYY-MM/           # 月度目录
│   │   │   ├── YYYY-MM-DD-sync.md
│   │   │   ├── YYYY-MM-DD-noon-card.md
│   │   │   └── YYYY-MM-DD-evening-card.md
│   ├── reading/               # 阅读练习材料
│   └── writing/               # 写作练习材料
├── notes/                        # 学习笔记
│   ├── README.md
│   ├── grammar/               # 语法笔记
│   ├── listening/             # 听力笔记
│   ├── summaries/             # 学习摘要
│   ├── tech-notes/            # 技术笔记
│   └── writing-structures/     # 写作结构笔记
├── progress/                     # 进度跟踪
│   └── README.md
├── reference/                    # 参考材料
│   └── README.md
├── scripts/                      # 工具脚本
│   ├── README.md
│   ├── annotate_article.py
│   ├── annotate_article_simple.py
│   ├── annotate_demo.py
│   ├── generate_demo.py
│   ├── skill_create.py
│   ├── test_annotator.py
│   └── use_annotator_example.py
└── .sisyphus/                   # 任务规划和工作流
    ├── plans/
    ├── drafts/
    └── notepads/
```

## 📚 使用指南

### 每日练习

每日练习记录存储在 `practice/daily/` 目录下，按月组织：

```bash
practice/daily/
├── 2026-02/              # 2月份的所有练习记录
│   ├── 2026-02-09-sync.md
│   ├── 2026-02-09-noon-card.md
│   ├── 2026-02-09-evening-card.md
│   └── ...
└── 2026-03/              # 3月份的所有练习记录
    ├── 2026-03-12-evening-card.md
    └── ...
```

文件类型：
- `sync.md` - 同步进度和总结
- `noon-card.md` - 中午练习卡片
- `evening-card.md` - 晚间练习卡片

### 阅读和写作练习

标准化练习材料存储在 `practice/reading/` 和 `practice/writing/` 目录：

**阅读练习**：
- 命名格式：`YYYY-MM-DD-ielts-reading.md`
- 包含：阅读理解练习和测试材料

**写作练习**：
- 命名格式：`YYYY-MM-DD-ielts-writing.md`
- 包含：Task 1和Task 2写作练习

### 文章标注工具

项目包含AI辅助的IELTS文章标注工具：

1. **基础标注器** (`annotate_article.py`) - 完整功能
2. **简化版** (`annotate_article_simple.py`) - 快速标注
3. **演示工具** (`annotate_demo.py`, `generate_demo.py`) - 生成示例
4. **测试工具** (`test_annotator.py`, `use_annotator_example.py`) - 验证和示例

详细使用说明请参考：`docs/IELTS_ANNOTATOR_GUIDE.md`

## 🔧 工具安装

### Python依赖

```bash
# 查看requirements（如果有的话）
pip install -r requirements.txt

# 手动安装依赖（根据实际使用情况）
pip install pandas  # 用于文章分析
pip install pandoc  # 用于文档转换
```

### 运行工具

```bash
# 标注IELTS文章
python scripts/annotate_article.py <article_file>

# 生成标注示例
python scripts/generate_demo.py

# 运行测试
python scripts/test_annotator.py
```

## 📖️ 学习笔记

笔记按主题组织在 `notes/` 目录：

- **语法笔记** - IELTS动词短语、习语汇总
- **听力笔记** - 听力主题关键词和高质量内容
- **学习摘要** - 每周学习总结
- **技术笔记** - 学习方法和工具使用记录
- **写作结构** - 写作框架和模板

## 📊 进度跟踪

- 计划和进度安排在 `progress/` 目录
- 包含4周计划（WEEK-1到WEEK-4）
- 支持月度评估和目标设定

## 🎯 学习建议

### 每日练习流程

1. **早晨** - 查看计划，开始阅读练习
2. **中午** - 完成中午练习卡片
3. **下午/晚上** - 完成写作或听力练习
4. **晚间** - 更新sync.md，总结当天学习

### 内容管理策略

- **周回顾** - 每周在 `notes/summaries/` 创建学习总结
- **月评估** - 月底评估进步，调整下月计划
- **持续改进** - 根据练习反馈调整学习策略

## 📄 项目状态

- ✅ **核心功能** - 可用于日常IELTS练习
- 🔄 **AI工具** - 文章标注功能可用，持续改进中
- 📚 **文档** - 完整的项目文档和使用指南
- 🚧 **测试** - 包含测试用例和示例

## 🚧 未来计划

- [ ] 扩展文章标注器的AI能力
- [ ] 添加更多练习材料模板
- [ ] 集成语音识别用于口语练习
- [ ] 添加自动化进度报告
- [ ] 支持多种语言的学习材料

## 📝 贡献

欢迎提交问题报告、功能建议或改进意见：

- **Bug报告** - 发现工具使用问题
- **功能请求** - 建议新的功能或材料
- **文档改进** - 修正文档错误或添加说明
- **练习材料** - 分享高质量的练习材料

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源协议。

### 许可摘要

```
MIT License

Copyright (c) 2026 IELTS Practice Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### 使用说明

- ✅ **商业使用** - 允许在商业产品中使用
- ✅ **修改和分发** - 可以自由修改、复制和分发代码
- ✅ **专利使用** - 可以基于本代码申请专利
- ✅ **私有使用** - 可以在私有项目中使用
- ⚠️ **免责声明** - 按原样提供，不提供任何担保
- 📄 **版权声明** - 保留原作者版权声明

## 🔗 相关链接

- [详细文档](docs/README.md) - 完整的项目文档
- [标注工具指南](docs/IELTS_ANNOTATOR_GUIDE.md) - IELTS文章标注器使用说明
- [材料标准](docs/MATERIAL-EXTRACTION-STANDARDS.md) - 学习材料提取标准
- [审核策略](docs/REVIEW-STRATEGY.md) - 学习内容审核方法

---

**开始你的IELTS学习之旅！** 🎓

有疑问或需要帮助？查看 [详细文档](docs/README.md) 或查看 `practice/` 目录中的示例。
