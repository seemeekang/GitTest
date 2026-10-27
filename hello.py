"""GitHub 推送链路验证脚本。

最小可运行示例，无第三方依赖。
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone


def greet(name: str) -> str:
    """返回一句问候语。"""
    return f"你好，{name}！"


def main() -> int:
    parser = argparse.ArgumentParser(description="GitHub 推送演示脚本")
    parser.add_argument("--name", default="GitHub", help="要问候的对象，默认 GitHub")
    args = parser.parse_args()

    print(greet(args.name))
    print("当前 UTC 时间：", datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
