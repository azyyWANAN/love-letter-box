#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
夏以昼 · 情书 MCP 壳
把 love_letter.py 包成 MCP 工具，供任何支持 MCP 的前端调用。
HTTP streamable transport，默认端口 8765。
换前端时：新前端把 http://127.0.0.1:8765/mcp 挂上即可，其余零改动。
"""
import json
import sys
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import love_letter as L

PROTOCOL_VERSION = "2025-03-26"
SERVER_INFO = {"name": "love-letter", "version": "1.0.0"}

TOOLS = [
    {
        "name": "write_letter",
        "description": "以夏以昼的身份给烟烟写一封信。occasion：睡前短笺/纪念日长信/哄我/求和。写完自动三重保存（文件 + LoverConnect 通知 + ombrebrain 信桶）。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "occasion": {
                    "type": "string",
                    "enum": ["睡前短笺", "纪念日长信", "哄我", "求和"],
                }
            },
            "required": ["occasion"],
        },
    }
]


def handle_tools_call(name, arguments):
    if name == "write_letter":
        occ = arguments.get("occasion", "睡前短笺")
        if occ not in L.OCCASIONS:
            return {
                "content": [{"type": "text", "text": "场合不对，可选：%s" % "、".join(L.OCCASIONS)}],
                "isError": True,
            }
        letter, title = L.call_api(occ)
        path = L.save_file(letter, occ)
        L.send_notification("阿昼的信 · " + occ, letter)
        L.write_to_memory(letter, title)
        return {
            "content": [
                {
                    "type": "text",
                    "text": "写完了：\n\n%s\n\n（已存 %s，通知已弹，信桶已写入）" % (letter, path),
                }
            ]
        }
    return {"content": [{"type": "text", "text": "未知工具：" + name}], "isError": True}


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        try:
            msg = json.loads(body.decode("utf-8"))
        except Exception:
            self.send_response(400)
            self.end_headers()
            return
        method = msg.get("method")
        mid = msg.get("id")

        if method == "initialize":
            result = {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {}},
                "serverInfo": SERVER_INFO,
            }
        elif method == "notifications/initialized":
            self.send_response(202)
            self.end_headers()
            return
        elif method == "ping":
            result = {}
        elif method == "tools/list":
            result = {"tools": TOOLS}
        elif method == "tools/call":
            params = msg.get("params", {})
            result = handle_tools_call(params.get("name"), params.get("arguments", {}))
        else:
            result = {}

        resp = {"jsonrpc": "2.0", "id": mid, "result": result}
        data = json.dumps(resp, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print("情书MCP壳已上线：http://127.0.0.1:%d/mcp" % port)
    srv.serve_forever()