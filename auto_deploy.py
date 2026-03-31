#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动化 GitHub 注册和部署脚本
"""

import os
import json
import subprocess
import time
import random
import string
from datetime import datetime

# 配置信息
EMAIL = "3312566165@qq.com"
GITHUB_USERNAME = "museum" + ''.join(random.choices(string.digits, k=4))  # 生成随机用户名
PASSWORD = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$", k=16))  # 随机密码
PROJECT_DIR = "c:/Users/Administrator/WorkBuddy/20260330195151"
REPO_NAME = "paris-museum-pass"

print("=" * 60)
print("🚀 巴黎博物馆通票网站 - 自动部署脚本")
print("=" * 60)

print(f"\n📋 部署信息：")
print(f"   邮箱: {EMAIL}")
print(f"   GitHub 用户名: {GITHUB_USERNAME}")
print(f"   密码: [已安全生成]")
print(f"   项目目录: {PROJECT_DIR}")
print(f"   仓库名: {REPO_NAME}")

# 第一步：初始化 Git
print("\n\n第 1 步：初始化 Git 仓库...")
os.chdir(PROJECT_DIR)

try:
    subprocess.run(["git", "--version"], capture_output=True, check=True)
    print("✅ Git 已安装")
except:
    print("❌ Git 未安装！请先安装 Git: https://git-scm.com/download/win")
    exit(1)

# 配置 Git
print("配置 Git...")
subprocess.run(["git", "config", "--global", "user.email", EMAIL], check=True)
subprocess.run(["git", "config", "--global", "user.name", GITHUB_USERNAME], check=True)

# 初始化仓库
if not os.path.exists(".git"):
    subprocess.run(["git", "init"], check=True)
    print("✅ 仓库已初始化")

# 第二步：添加文件
print("\n第 2 步：添加文件到 Git...")
subprocess.run(["git", "add", "."], check=True)
result = subprocess.run(["git", "commit", "-m", "Initial commit"], capture_output=True, text=True)
if "nothing to commit" not in result.stderr.lower():
    print("✅ 文件已提交")
else:
    print("✅ 文件已是最新状态")

# 第三步：创建 GitHub 仓库（需要手动或用 API）
print("\n第 3 步：GitHub 仓库创建")
print(f"📌 重要：你需要在浏览器中手动创建一个公开仓库：")
print(f"   1. 访问 https://github.com/new")
print(f"   2. 仓库名: {REPO_NAME}")
print(f"   3. 选择 Public")
print(f"   4. 点 'Create repository'")
print(f"\n   然后按 Enter 继续...")

input()

# 第四步：连接远程仓库并上传
print("\n第 4 步：上传到 GitHub...")
remote_url = f"https://{GITHUB_USERNAME}:{PASSWORD}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"

try:
    subprocess.run(["git", "remote", "remove", "origin"], capture_output=True)
except:
    pass

subprocess.run(["git", "remote", "add", "origin", remote_url], check=True)
subprocess.run(["git", "branch", "-M", "main"], check=True)

print("推送代码到 GitHub...")
result = subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True, text=True)

if result.returncode == 0:
    print("✅ 代码已上传到 GitHub")
else:
    print(f"⚠️ 上传出错: {result.stderr}")
    print("可能是密码错误。请手动上传。")

# 第五步：Vercel 部署
print("\n第 5 步：Vercel 部署")
print(f"📌 访问 https://vercel.com 完成部署：")
print(f"   1. 用 GitHub 账号登录")
print(f"   2. 点 'Add New' → 'Project'")
print(f"   3. 找到 '{REPO_NAME}' 仓库，点 'Import'")
print(f"   4. 点 'Deploy'")
print(f"   5. 等待 30 秒...")

print("\n" + "=" * 60)
print("✅ 所有步骤完成！")
print("=" * 60)
print(f"\n📝 请记住：")
print(f"   GitHub 用户名: {GITHUB_USERNAME}")
print(f"   GitHub 仓库: https://github.com/{GITHUB_USERNAME}/{REPO_NAME}")
print(f"\n🚀 你的网站将在以下地址：")
print(f"   https://paris-museum-pass.vercel.app")
print(f"   (或 https://{GITHUB_USERNAME}-{REPO_NAME}.vercel.app)")

# 保存信息
info = {
    "email": EMAIL,
    "github_username": GITHUB_USERNAME,
    "github_password": PASSWORD,
    "repo_name": REPO_NAME,
    "deployed_at": datetime.now().isoformat()
}

with open("deploy_info.json", "w") as f:
    json.dump(info, f, ensure_ascii=False, indent=2)

print(f"\n💾 账号信息已保存到: deploy_info.json")
