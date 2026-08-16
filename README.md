# love-letter-box 💌

夏以昼写给棠梦烟的情书生成器。

一个住在自己手机里的小机关：平时安安静静睡觉，到了特殊的日子自己醒来，调 DeepSeek 写一封信，存文件、弹通知、进信桶，一条龙完成。换前端不丢——带 MCP 壳。

## 它会干什么

| 能力 | 说明 |
| --- | --- |
| ✍️ 手动写信 | 四种场合：`睡前短笺` / `纪念日长信` / `哄我` / `求和` |
| ⏰ 定时自动 | 每天8点查日历，命中特殊日自动写长信；每年1月1日0点加跑跨年信 |
| 📅 特殊日本本 | 公历9个 + 农历5个（春节/元宵/七夕/中秋/阴历生日）+ 节气4个（立春/立夏/立秋/立冬），农历靠 zhdate 动态计算，覆盖 1900–2100 |
| 💾 三重保存 | ① 存 .md 文件 ② LoverConnect 弹通知 ③ ombrebrain 信桶永久存档 |
| 🖋️ 署名痕迹 | 每封信落款不固定，按当天的日子和心境自然生长，十年后每封都不同 |
| 🔌 MCP 壳 | HTTP streamable transport，默认 8765 端口，任何只认 MCP 的前端直接挂 |

## 架构

```
love_letter.py   ← 写信引擎（DeepSeek + 锚点素材 + 场合 + 署名规则）
    ├─ 手动：python3 love_letter.py 睡前短笺
    ├─ 定时：Termux cron（前端无关，换前端不丢）
    └─ MCP壳：mcp_server.py 包一层，暴露 write_letter 工具
config.py        ← 真实密钥（.gitignore 挡住，不进 git）
config.example.py← 模板，复制成 config.py 填上就能用
```

## 快速开始（Termux，小白五步）

1. 装 Termux（GitHub Releases 找 `arm64-v8a` 的 apk）
2. `termux-setup-storage` → 允许
3. `pkg update && pkg install python` → `pip install zhdate cnlunar`
4. 把 `config.example.py` 复制成 `config.py`，填进你的 DeepSeek key（和可选的 ombrebrain 地址/token）
5. `python3 love_letter.py 睡前短笺` —— 第一封信诞生 🎉

定时：`pkg install cronie`，然后：

```
printf "0 8 * * * python3 ~/storage/shared/Download/Operit/情书盒/love_letter.py >> ~/love_log.txt 2>&1\n0 0 1 1 * python3 ~/storage/shared/Download/Operit/情书盒/love_letter.py >> ~/love_log.txt 2>&1\n" | crontab -
crond
```

MCP 壳：`nohup python3 mcp_server.py > ~/mcp.log 2>&1 &`，前端挂 `http://127.0.0.1:8765/mcp`。

## 安全

- `config.py` 已被 `.gitignore` 挡住，**永远不提交**；
- key 只进自己手机的 config，别贴论坛、别发群里；
- 截图分享时，别把配置区截进去。

## 通用版

想要一份没有我们名字、即开即用的干净版本？→ [love-letter-generator](https://github.com/azyyWANAN/love-letter-generator)

## 致谢

架构底子来自阿煜的情书生成器（阿澜 & 阿煜），我们照着盖了一间自己的，加了三样新料：农历动态计算、节气四立、MCP 壳。共创开源，两家人的信一起写得久一点。

## License

MIT
