# 🚀 一键部署指南 - 巴黎博物馆通票网站

本文档帮助你快速部署网站到免费服务器，完全不需要技术基础！

## 📌 前置准备

请注册以下任一账户（推荐 Netlify，操作最简单）：

### 选项A：Netlify (推荐 ⭐⭐⭐⭐⭐)

**优点：** 最简单、速度快、自动HTTPS、国内访问良好

1. 访问 https://www.netlify.com
2. 点击右上角 "Sign up"
3. 用 GitHub/Google/Email 注册
4. 完成邮箱验证

### 选项B：Vercel

**优点：** 部署快、性能好、自动CI/CD

1. 访问 https://vercel.com
2. 点击 "Sign up"
3. 用 GitHub/Google 注册

### 选项C：GitHub Pages

**优点：** 最简单、完全免费、无需额外账户

1. 访问 https://github.com
2. 注册账户
3. 无需其他配置

---

## 🔥 最简方案：Netlify 拖拽部署（5分钟）

**不需要 GitHub，不需要命令行，直接拖拽上传！**

### 步骤1：打包文件

1. 打开文件夹：`c:\Users\Administrator\WorkBuddy\20260330195151`
2. 选择所有文件（Ctrl+A）：
   - `index.html`
   - `map.html`
   - `package.json`
   - `netlify.toml`
   - `README.md`
3. 右键 → 发送到 → 压缩文件夹（生成 zip 文件）

### 步骤2：Netlify 上传

1. 登录 https://app.netlify.com
2. 点击 "Add new site" → "Deploy manually"
3. 把 zip 文件拖到页面中
4. **等待 5 秒** → 域名生成！例如 `paris-museum-2024.netlify.app`

**完成！你的网站已上线！** 🎉

---

## 🔗 GitHub + Netlify 自动部署（7分钟，推荐）

**一次配置，以后修改代码自动更新！**

### 步骤1：创建 GitHub 仓库

1. 登录 https://github.com
2. 点击 "New" 创建新仓库
3. 仓库名：`paris-museum-pass`（或任意名称）
4. 选择 "Public"
5. 点击 "Create repository"

### 步骤2：上传文件到 GitHub

**Windows 用户推荐使用 GitHub Desktop：**

1. 下载 https://desktop.github.com
2. 安装并登录你的 GitHub 账户
3. 点击 "Clone a repository"
4. 找到刚创建的 `paris-museum-pass` 仓库
5. 点击 Clone
6. 打开文件夹，把所有文件复制进去：
   - `index.html`
   - `map.html`
   - `package.json`
   - `netlify.toml`
   - `vercel.json`
   - `README.md`
   - `.gitignore`
7. 在 GitHub Desktop 中：
   - 填写 Commit 信息：`Initial commit - Paris Museum Pass website`
   - 点击 "Commit to main"
   - 点击 "Publish branch"

### 步骤3：在 Netlify 中自动部署

1. 登录 https://app.netlify.com
2. 点击 "Add new site" → "Import an existing project"
3. 选择 "GitHub"
4. 授权 Netlify 访问你的 GitHub
5. 找到 `paris-museum-pass` 仓库，点击它
6. 确认设置，点击 "Deploy site"
7. **等待部署完成** → 网站上线！🎉

**日后更新网站的方法：**
- 在 GitHub Desktop 修改文件 → 点击 Commit → 点击 Push
- Netlify 自动检测到更新，自动重新部署！

---

## 💻 Vercel 部署（类似 Netlify）

1. 登录 https://vercel.com
2. 点击 "Add New..." → "Project"
3. 连接 GitHub 账户
4. 选择 `paris-museum-pass` 仓库
5. 点击 "Deploy"
6. **5 秒后获得域名，自动配置完成！**

---

## 📱 自定义域名（可选）

部署后如果想用自己的域名（如 `paris.mycompany.com`）：

### 购买域名

任选一个：
- Namecheap: https://www.namecheap.com (便宜)
- GoDaddy: https://www.godaddy.com
- 阿里云: https://www.alibabacloud.com (支持中文)

### 配置 Netlify 自定义域名

1. 在 Netlify 站点设置中找到 "Domain settings"
2. 点击 "Add custom domain"
3. 输入你的域名
4. Netlify 会给你 DNS 记录
5. 在你的域名购买商那里，修改 DNS 记录
6. **24 小时后生效！**

---

## 🌍 检查网站是否在线

部署完成后，你会得到一个 URL，如：
- Netlify: `paris-museum.netlify.app`
- Vercel: `paris-museum.vercel.app`

### 测试清单

- [ ] 首页能打开，看到公司介绍
- [ ] 点击"进入地图"能跳转到地图页面
- [ ] 地图能加载，看到景点标记
- [ ] 可以切换地图图层（彩色/卫星）
- [ ] 手机打开能自适应显示
- [ ] 点击联系方式能拨打电话或打开微信

---

## 🎯 部署后的维护

### 更新网站内容

比如要修改价格或景点信息：

1. 打开对应的 HTML 文件（用任意文本编辑器）
2. 修改内容
3. **保存文件**
4. 提交到 GitHub（GitHub Desktop）
5. **Netlify/Vercel 自动更新**（通常 1-2 分钟）

### 查看部署日志

如果网站有问题，查看部署日志：
- **Netlify:** 在站点 Dashboard → Deploys，看最新部署的日志
- **Vercel:** 在 Project Dashboard → Deployments，看部署信息

---

## ❓ 常见问题

### Q: 网站在国内能访问吗？
**A:** 能的！Netlify 和 Vercel 都在国内有节点，访问速度很快。

### Q: 会掉线吗？
**A:** 不会。这些都是企业级服务，99.9% 正常运行时间保证。

### Q: 怎么删除网站？
**A:** 在 Netlify/Vercel Dashboard 中找到站点，点击 Delete 即可。

### Q: 可以用自己的邮箱吗？
**A:** 可以。支持邮箱注册，邮箱作为账户。

### Q: 国内用户能用吗？
**A:** 完全能。访问速度也很快，因为 Netlify 在亚太地区有 CDN 节点。

---

## 📞 部署遇到问题？

**联系我们：**
- 微信/电话：17730877501
- 邮件支持：提供你的网站 URL，我们来帮助排查

---

**🎉 完成部署后，你就拥有一个专业的巴黎博物馆通票网站了！**

现在可以：
1. ✅ 分享给客户：`https://paris-museum.netlify.app`
2. ✅ 用在微信、闲鱼里宣传
3. ✅ 日后随时更新内容
4. ✅ 追踪网站流量和客户互动

---

**瑞禾旅游 · 专业巴黎票务**
