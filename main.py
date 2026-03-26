#!/usr/bin/env python3
"""
AI产品助手 Demo
我曾参与“智能会议记录仪”的B端AI硬件产品项目。我协助团队通过用户访谈梳理了核心需求，并利用大模型技术优化了实时语音转写与摘要功能。在产品设计阶段，我配合输出了产品原型与功能规划文档，并跟进供应链物料采购与生产进度。产品上线后，通过收集反
"""
import json
from datetime import datetime

class AIProductAssistant:
    def __init__(self):
        self.queries = 0
        self.start_time = datetime.now().isoformat()

    def analyze_intent(self, text):
        keywords = {"分析": "analyze", "推荐": "recommend", "查询": "query", "帮我": "assist"}
        for kw, intent in keywords.items():
            if kw in text:
                return {"intent": intent, "confidence": 0.88}
        return {"intent": "general", "confidence": 0.75}

    def respond(self, user_input):
        self.queries += 1
        result = self.analyze_intent(user_input)
        return f"[{result['intent']}] 已处理：{user_input}"

def main():
    print("=== AI产品助手 Demo ===")
    bot = AIProductAssistant()
    demos = ["帮我分析用户增长数据", "推荐AI功能方向", "查询本月活跃用户"]
    for q in demos:
        print(f"用户: {q}")
        print(f"AI: {bot.respond(q)}\n")
    print(json.dumps({"queries": bot.queries, "uptime": bot.start_time}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
