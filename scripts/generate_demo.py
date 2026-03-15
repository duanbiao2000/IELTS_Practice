#!/usr/bin/env python3
"""
IELTS Article Generator - 快速生成雅思阅读文章和试卷
"""

import sys
import os

# 添加skills目录到路径
skills_dir = os.path.join(os.path.dirname(__file__), ".skills")
sys.path.insert(0, skills_dir)

from ielts_article_generator import (
    IELTSArticleGenerator,
    create_ielts_test,
    create_passage_messages,
    create_answer_key,
)


# ===== 模拟Agent CLI =====
class MockAgentCLI:
    """
    模拟的Agent CLI LLM接口。
    """

    def llm_call(self, messages, **kwargs):
        """
        统一的LLM调用接口。

        Args:
            messages: 消息列表 [{"role": "system", "content": "..."}]
            **kwargs: 额外参数

        Returns:
            LLM响应文本

        注意：这里使用模拟响应，真实环境中会调用实际LLM。
        """
        print("\n📡 调用LLM...")
        print(f"   消息数量: {len(messages)}")

        # 提取用户文本
        user_text = ""
        for msg in messages:
            if msg["role"] == "user":
                user_text = msg["content"]
                break

        text_length = len(user_text)

        # 模拟响应（用于演示）
        mock_passage = f"""# IELTS Reading Practice Test 1

**Time: 60 minutes**
**Passages: 1**
**Questions: 13**

---

## Reading Passage 1

### Andrea Palladio: Italian architect

**A.** Vicenza is a pleasant, prosperous city in the Veneto, 60km west of Venice. Its grand families settled and farmed the area from the 16th century. But its principal claim to fame is Andrea Palladio, who is such an influential architect that a neoclassical style is known as Palladian. The city is a permanent exhibition of some of his finest buildings, and as he was born—in Padua, to be precise—500 years ago, the International Centre for the Study of Palladio's Architecture has an excellent excuse for mounting la grande mostra, the big show.

**B.** The exhibition has the special advantage of being held in one of Palladio's buildings, Palazzo Barbaran da Porto. Its bold facade is a mixture of rustication and decoration set between two rows of elegant columns. On the second floor the pediments are alternately curved or pointed, a Palladian trademark. The harmonious proportions of the atrium at the entrance lead through to a dramatic interior of fine fireplaces and painted ceilings. Palladio's design is simple, clear and not over-crowded. The show has been organised on the same principles, according to Howard Burns, the architectural historian who co-curated it.

**C.** Palladio's father was a miller who settled in Vicenza, where the young Andrea was apprenticed to a skilled stonemason. How did a humble miller's son become a world renowned architect? The answer in the exhibition is that, as a young man, Palladio excelled at carving decorative stonework on columns, doorways and fireplaces. He was plainly intelligent, and lucky enough to come across a rich patron, Gian Giorgio Trissino, a landowner and scholar, who organised his education, taking him to Rome in the 1540s, where he studied the masterpieces of classical Roman and Greek architecture and the work of other influential architects of the time, such as Donato Bramante and Raphael.

**D.** Burns argues that social mobility was also important. Entrepreneurs, prosperous from agriculture in the Veneto, commissioned the promising local architect to design their country villas and their urban mansions. In Venice the aristocracy were anxious to co-opt talented artists, and Palladio was given the chance to design the buildings that have made him famous—the churches of San Giorgio Maggiore and the Redentore, both easy to admire because they can be seen from the city's historical centre across a stretch of water.

**E.** He tried his hand at bridges—his unbuilt version of the Rialto Bridge was decorated with the large pediment and columns of a temple—and, after a fire at the Ducal Palace, he offered an alternative design which bears an uncanny resemblance to the Banqueting House in Whitehall in London. Since it was designed by Inigo Jones, Palladio's first foreign disciple, this is not as surprising as it sounds.

**F.** Jones, who visited Italy in 1614, bought a trunk full of the master's architectural drawings; they passed through the hands of the Dukes of Burlington and Devonshire before settling at the Royal Institute of British Architects in 1894. Many are now on display at Palazzo Barbaran. What they show is how Palladio drew on the buildings of ancient Rome as models. The major theme of both his rural and urban building was temple architecture, with a strong pointed pediment supported by columns and approached by wide steps.

**G.** Palladio's work for rich landowners alienates unreconstructed critics on the Italian left, but among the papers in the show are designs for cheap housing in Venice. In the wider world, Palladio's reputation has been nurtured by a text he wrote and illustrated, "Quattro Libri dell' Architettura". His influence spread to St Petersburg and to Charlottesville in Virginia, where Thomas Jefferson commissioned a Palladian villa he called Monticello.

**H.** Vicenza's show contains detailed models of the major buildings and is leavened by portraits of Palladio's teachers and clients by Titian, Veronese and Tintoretto; the paintings of his Venetian buildings are all by Canaletto, no less. This is an uncompromising exhibition; many of the drawings are small and faint, and there are no sideshows for children, but the impact of harmonious lines and satisfying proportions is to impart in a viewer a feeling of benevolent calm. Palladio is history's most therapeutic architect.

**I.** "Palladio, 500 Anni: La Grande Mostra" is at Palazzo Barbaran da Porto, Vicenza, until January 6th 2009. The exhibition continues at the Royal Academy of Arts, London, from January 31st to April 13th, and travels afterwards to Barcelona and Madrid.

---

### Questions 1-7

Do the following statements agree with the information given in Reading Passage 1?

In boxes 1-7 on your answer sheet write:

| TRUE | if the statement agrees with the information |
| FALSE | if the statement contradicts the information |
| NOT GIVEN | If there is no information on this |

1. The building where the exhibition is staged has been newly renovated
2. Palazzo Barbaran da Porto typically represent the Palladio's design
3. Palladio's father worked as an architect.
4. Palladio's family refused to pay for his architectural studies
5. Palladio's alternative design for the Ducal Palace in Venice was based on an English building.
6. Palladio designed both wealthy and poor people
7. The exhibition includes paintings of people by famous artists

---

### Questions 8-13

Answer the questions below.

Choose NO MORE THAN THREE WORDS from the passage for each answer. Write your answers in boxes 8-13 on your answer sheet.

8. What job was Palladio training for before he became an architect?
9. Who arranged Palladio's architectural studies?
10. Who was the first non-Italian architect influenced by Palladio?
11. What type of Ancient Roman buildings most heavily influenced Palladio's work?
12. What did Palladio write that strengthened his reputation?
13. In the writer's opinion, what feeling will visitors to the exhibition experience?

---

### Questions 14-19

Do the following statements reflect the claims of the writer in Reading Passage 1?

In boxes 14-19 on your answer sheet write:

| YES | if the statement is true |
| NO | if the statement is false |
| NOT GIVEN | if the information is not given in the passage |

14. It seems predictable that some species will disappear.
15. The nature of the Earth and human biology make it impossible for human beings to survive another million years.
16. An eruption by Yellowstone is likely to be more destructive than previous volcanic eruptions.
17. There is a greater chance of the Earth being hit by small asteroids than by large ones.
18. If the world becomes uninhabitable, it is most likely to be as a result of a natural disaster.
19. Politicians currently in power seem unlikely to change their way of thinking.

---

### Questions 20-25

Complete the summary below.

Choose NO MORE THAN TWO WORDS from the passage for each answer. Write your answers in boxes 20-25 on your answer sheet.

The Earth could become uninhabitable, like other planets, through a major change in the 20.................. Volcanic eruptions of 21.................. can lead to shortages of 22.................. in a wide area.

An asteroid hitting the Earth could create a 23.................. that would result in a new 24.................. Plans are being made to use 25.................. to deflect asteroids heading for the Earth.

---

### Question 26

Choose the correct letter A, B, C or D.

Write your answer in box 26 on your answer sheet.

What is the writer's purpose in Reading Passage 1?

A. to propose a new theory about the causes of natural disasters
B. to prove that generally held beliefs about the future are all mistaken
C. to present a range of opinions currently held by scientists
D. to argue the need for a general change in behavior

---

## Answer Key

1. FALSE
2. FALSE
3. FALSE
4. NOT GIVEN
5. FALSE
6. FALSE
7. FALSE

8. stonemason
9. Gian Giorgio Trissino
10. Donato Bramante
11. Temple architecture
12. Quattro Libri dell' Architettura
13. benevolent calm

14. NOT GIVEN
15. NOT GIVEN
16. NOT GIVEN
17. NOT GIVEN
18. NOT GIVEN
19. NOT GIVEN

20. atmosphere
21. food production
22. shortages
23. tidal wave
24. ice age
25. rockets

26. D

**Source:** AI Generated using IELTS Article Generator v1.0
**Conversion Date:** 2026-02-09
**Extraction Method:** AI Generated
---

## Notes for Students

1. **Time Management:**
   - Passage 1: 20 minutes
   - Questions 1-7: 10 minutes
   - Questions 8-13: 10 minutes
   - Questions 14-19: 10 minutes
   - Summary Completion: 5 minutes
   - Question 26: 5 minutes

2. **Question Types:**
   - True/False/Not Given (Questions 1-7)
   - Short Answer (Questions 8-13)
   - Yes/No/Not Given (Questions 14-19)
   - Summary Completion (Questions 20-25)
   - Multiple Choice (Question 26)

3. **Tips:**
   - Read the questions before reading the passage
   - Underline keywords in both questions and passage
   - Pay attention to synonyms and paraphrasing
   - For True/False/Not Given questions: check if the information is explicitly stated or not mentioned at all
   - For Short Answer questions: NO MORE THAN TWO/THREE WORDS per answer
   - For Summary Completion: Choose words EXACTLY from the passage
   - For Multiple Choice: Read all options before choosing
"""

        print(f"   模拟响应长度: {len(mock_passage)} 字符")
        print("   ✓ LLM调用完成（模拟）")

        return mock_passage


# ===== 主程序 =====
def main():
    """主函数。"""
    print("\n" + "=" * 70)
    print("📝 IELTS Article Generator - 快速生成示例")
    print("=" * 70)

    # 初始化模拟Agent CLI
    agent = MockAgentCLI()
    print("✅ Agent CLI已初始化（模拟）")

    # 生成文章
    print("\n📖 步骤1：生成IELTS阅读文章")
    topic = "Ancient Rome Architecture"

    # 创建LLM消息
    messages = create_passage_messages(topic)

    # 调用LLM
    passage_and_questions = agent.llm_call(messages)

    # 生成答案
    print("\n📋 步骤2：生成答案键")
    # 这里简单模拟，实际会调用第二个LLM
    answer_key_mock = f"""## Answer Key

1. FALSE
2. FALSE
3. FALSE
4. NOT GIVEN
5. FALSE
6. FALSE
7. FALSE

8. stonemason
9. Gian Giorgio Trissino
10. Donato Bramante
11. Temple architecture
12. Quattro Libri dell' Architettura
13. benevolent calm

14. NOT GIVEN
15. NOT GIVEN
16. NOT GIVEN
17. NOT GIVEN
18. NOT GIVEN
19. NOT GIVEN

20. atmosphere
21. food production
22. shortages
23. tidal wave
24. ice age
25. rockets

26. D

**Source:** AI Generated using IELTS Article Generator v1.0
**Conversion Date:** 2026-02-09
**Extraction Method:** AI Generated
"""

    # 保存到文件
    output_path = "generated-ielts-test-demo.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(passage_and_questions)
        f.write("\n" + "=" * 70 + "\n")
        f.write(answer_key_mock)

    print(f"\n✅ 已保存: {output_path}")

    # 显示预览
    print("\n📄 生成的内容预览（前50行）:")
    print("-" * 70)
    lines = passage_and_questions.split("\n")
    for i, line in enumerate(lines[:50]):
        print(f"  {i + 1:2d}: {line[:80]}")

    print("\n" + "=" * 70)
    print("✅ 生成完成！")
    print("=" * 70)

    print("\n💡 在真实Agent CLI中使用：")
    print("""
```python
# 1. 导入生成器
from ielts_article_generator import create_ielts_test

# 2. 一行生成（调用Agent CLI的LLM）
test = create_ielts_test("您的主题")

# 3. 保存
with open("my-test.md", 'w') as f:
    f.write(test)

print("✅ 完成！")
```
""")

    print("\n" + "=" * 70)
    print("🎯 核心特点：")
    print("=" * 70)
    print("""
1. ✅ 零依赖 - 只用Python标准库
2. ✅ Agent CLI原生 - 完美适配您的LLM接口
3. ✅ 纯提示词引擎 - 专注文章和题目生成
4. ✅ 自动格式化 - 完全匹配IELTS官方格式
5. ✅ 完整配套 - 文章+题目+答案一应俱全

6. ✅ 快速生成 - 一键生成完整雅思测试
7. ✅ 主题多样 - 支持建筑、历史、科技、环保等主题
""")

    print("=" * 70)


if __name__ == "__main__":
    main()
