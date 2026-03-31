#!/bin/bash
# 快速部署脚本 - 将网站部署到 GitHub 和 Netlify
# 使用方法：bash deploy.sh

set -e

echo "🚀 开始部署巴黎博物馆通票网站..."
echo ""

# 检查 Git 是否安装
if ! command -v git &> /dev/null; then
    echo "❌ Git 未安装，请先下载 Git：https://git-scm.com"
    exit 1
fi

# 检查是否已有 .git 文件夹
if [ ! -d ".git" ]; then
    echo "📌 初始化 Git 仓库..."
    git init
    echo ""
    
    read -p "请输入你的 GitHub 用户名：" github_username
    read -p "请输入你的 GitHub 邮箱：" github_email
    read -p "请输入仓库名称（默认：paris-museum-pass）：" repo_name
    repo_name=${repo_name:-paris-museum-pass}
    
    git config user.name "$github_username"
    git config user.email "$github_email"
    git remote add origin "https://github.com/$github_username/$repo_name.git"
    
    echo "✅ Git 仓库已初始化"
    echo "💡 记住这个 GitHub 仓库地址："
    echo "   https://github.com/$github_username/$repo_name"
else
    echo "✅ Git 仓库已存在"
fi

echo ""
echo "📦 添加所有文件到 Git..."
git add .

echo "📝 提交文件..."
read -p "输入提交信息（默认：Update Paris Museum Pass website）：" commit_msg
commit_msg=${commit_msg:-"Update Paris Museum Pass website"}
git commit -m "$commit_msg"

echo "🔄 推送到 GitHub..."
git branch -M main
git push -u origin main

echo ""
echo "✅ 文件已推送到 GitHub！"
echo ""
echo "📌 后续步骤：在 Netlify 上部署"
echo "1. 访问 https://app.netlify.com"
echo "2. 点击 'Add new site' → 'Import an existing project'"
echo "3. 选择 GitHub，授权后找到你的仓库"
echo "4. 点击 'Deploy' - 完成！"
echo ""
echo "🎉 网站将自动获得一个免费的 .netlify.app 域名"
echo "日后更新只需 git push，Netlify 自动重新部署"
