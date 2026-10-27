# github-demo

一个用于验证 **GitHub SSH 推送链路**的最小示例仓库。

它本身没有业务价值——存在的唯一目的是确认这台机器的 `git push` 真的能把代码送上 GitHub。

## 快速运行

```bash
python hello.py
python hello.py --name 世界
```

输出示例：

```
你好，GitHub！
当前 UTC 时间： 2026-10-27 10:07:33
```

无第三方依赖，Python 3.9+ 即可运行。

## 仓库结构

```
github-demo/
├── README.md      本文件
├── .gitignore     Python 常见忽略项
└── hello.py       示例脚本
```

## 为什么需要这个仓库

这台机器连接 GitHub 遇到过一个特殊问题：

| 目标 | 结果 |
|---|---|
| `github.com:443` | 静默丢包，TCP 握手超时 |
| `github.com:22` | 同样超时 |
| `ssh.github.com:443` | 正常可达 |

因此本机 `~/.ssh/config` 把 `github.com` 重定向到了 `ssh.github.com:443`：

```
Host github.com
  HostName ssh.github.com
  Port 443
  User git
  IdentityFile ~/.ssh/id_ed25519
```

对外表现与普通 GitHub 完全一致，仍然使用 `git@github.com:owner/repo.git` 这种标准地址。

## 验证推送是否成功

```bash
git clone git@github.com:seemeekang/github-demo.git
cd github-demo
python hello.py
```

能克隆下来并跑通，就说明整条链路（SSH 认证 → 对象传输 → 本地执行）都是通的。
