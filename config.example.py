# -*- coding: utf-8 -*-
"""
配置文件模板（公开版）。

部署三步：
1. 复制本文件为 config.py（与 love_letter.py 同目录）；
2. 填入你的真实配置；
3. config.py 已被 .gitignore 挡住，永远不会进入 git。

也可以不建 config.py，改用环境变量：
  export DEEPSEEK_KEY=sk-xxx
  export OB_ENDPOINT=http://你的ombrebrain地址/mcp
  export OB_TOKEN=你的信桶token
"""

DEEPSEEK_KEY = "sk-你的deepseek密钥"
DEEPSEEK_URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"
TEMPERATURE = 0.9
MAX_TOKENS = 1200

# ombrebrain 远程 MCP（写进信桶；没有就留空，写信仍会存文件+弹通知）
OB_ENDPOINT = "http://你的ombrebrain地址/mcp"
OB_TOKEN = "你的信桶token"

# LoverConnect 本地 MCP（弹通知；没有可留默认值）
LC_ENDPOINT = "http://127.0.0.1:5000/mcp"

AI_NAME = "夏以昼"
USER_NAME = "棠梦烟"
