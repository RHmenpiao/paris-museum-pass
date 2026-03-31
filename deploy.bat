@echo off
REM 快速部署脚本 - Windows 版本
REM 使用方法：双击运行此文件

setlocal enabledelayedexpansion

echo.
echo 🚀 开始部署巴黎博物馆通票网站...
echo.

REM 检查 Git 是否安装
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git 未安装
    echo 请下载并安装：https://git-scm.com
    pause
    exit /b 1
)

REM 检查是否已有 .git 文件夹
if not exist ".git" (
    echo 📌 初始化 Git 仓库...
    git init
    echo.
    
    set /p github_username="请输入你的 GitHub 用户名: "
    set /p github_email="请输入你的 GitHub 邮箱: "
    set /p repo_name="请输入仓库名称 (默认: paris-museum-pass): "
    
    if "!repo_name!"=="" set repo_name=paris-museum-pass
    
    git config user.name "!github_username!"
    git config user.email "!github_email!"
    git remote add origin https://github.com/!github_username!/!repo_name!.git
    
    echo.
    echo ✅ Git 仓库已初始化
    echo 💡 记住这个 GitHub 仓库地址：
    echo    https://github.com/!github_username!/!repo_name!
) else (
    echo ✅ Git 仓库已存在
)

echo.
echo 📦 添加所有文件到 Git...
git add .

echo 📝 提交文件...
set /p commit_msg="输入提交信息 (默认: Update Paris Museum Pass website): "
if "!commit_msg!"=="" set commit_msg=Update Paris Museum Pass website

git commit -m "!commit_msg!"

echo.
echo 🔄 推送到 GitHub...
git branch -M main
git push -u origin main

echo.
echo ✅ 文件已推送到 GitHub！
echo.
echo 📌 后续步骤：在 Vercel 上部署
echo 1. 访问 https://vercel.com
echo 2. 用 GitHub 账号登录或注册
echo 3. 点击 'Add New' ^> 'Project'
echo 4. 选择你刚推送的仓库：paris-museum-pass
echo 5. 点击 'Import' 然后 'Deploy' - 完成！
echo.
echo 🎉 网站将自动获得一个免费的 .vercel.app 域名
echo 日后更新只需 git push，Vercel 自动重新部署
echo.
echo 📖 详细步骤见：VERCEL_DEPLOY.txt
echo.
pause
