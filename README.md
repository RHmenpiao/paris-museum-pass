# 🗺️ 巴黎博物馆通票景点导览 - 瑞禾旅游

专业的巴黎博物馆通票景点位置地图和购票指南。

## 📍 功能特性

- 🗺️ **交互式地图** - 彩色/卫星双图层，精确标注33个景点
- 💰 **票价对比** - 2026年最新官方价格，通票 vs 单票对比
- 🔍 **快速搜索** - 按名称、分类、预约需求搜索景点
- 📱 **响应式设计** - 完美适配手机、平板、桌面
- 🎯 **一键定位** - 侧边栏景点列表支持地图快速定位
- ⭐ **必去推荐** - 标注景点重要程度和特色亮点

## 🌐 网站结构

```
index.html          - 首页（品牌展示、功能介绍、价格指南）
map.html            - 交互式景点地图
package.json        - 项目配置
netlify.toml        - Netlify部署配置
vercel.json         - Vercel部署配置
```

## 🚀 快速部署

### 方案1: Netlify (推荐，完全免费)

1. 访问 [Netlify](https://www.netlify.com)
2. 点击 "Deploy" 或 "New site from Git"
3. 连接你的 GitHub 账户（需要先将文件推送到 GitHub）
4. 选择此仓库
5. 点击 "Deploy" - 完成！

自动生成域名：`{random-name}.netlify.app`

### 方案2: Vercel (也完全免费)

1. 访问 [Vercel](https://vercel.com)
2. 点击 "New Project"
3. 导入 GitHub 仓库
4. 点击 "Deploy" - 完成！

自动生成域名：`{project-name}.vercel.app`

### 方案3: GitHub Pages (最简单，免费)

1. 在 GitHub 上创建名为 `{username}.github.io` 的仓库
2. 上传所有文件到此仓库
3. 访问 `https://{username}.github.io` 即可

### 方案4: 本地运行

```bash
# 简单方式 - 使用Python
python -m http.server 8000

# 或使用Node.js
npx serve

# 然后访问 http://localhost:8000 或 http://localhost:3000
```

## 📋 景点列表

包含33个热门景点，涵盖：
- 🏛️ **13个博物馆** - 卢浮宫、奥赛、毕加索等
- 🏛️ **9个历史古迹** - 凯旋门、先贤祠、圣礼拜堂等
- 🏰 **7个宫殿城堡** - 凡尔赛、枫丹白露等
- 🌿 **4个近郊景点** - 文森城堡、马尔迈松等

## 💰 通票价格 (2026年)

| 天数 | 价格 | 描述 |
|------|------|------|
| 2日 | €70 | 连续2天有效 |
| 4日 | €90 | 连续4天有效 |
| 6日 | €110 | 连续6天有效 |

## 📞 联系方式

**瑞禾旅游 - 巴黎本地票务专家**

- 📱 微信/电话：**17730877501**
- 🛍️ 闲鱼店铺：搜索 "瑞禾旅游" 或 "欧洲小张"
- 💬 工作时间：09:00-21:00 (巴黎时间)

## 🔧 技术栈

- HTML5 + CSS3 + JavaScript
- Leaflet.js - 开源地图库
- CartoDB + Esri - 地图瓦片服务
- 响应式设计，无需依赖

## 📄 许可证

MIT License - 详见 LICENSE 文件

---

**© 2026 瑞禾旅游 All Rights Reserved**

专业提供：巴黎通票、欧洲景点代理、本地导览服务

客服微信：17730877501
