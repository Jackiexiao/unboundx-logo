# UNBOUNDX Logo System

UNBOUNDX 品牌 Logo、视觉规范与设计过程归档仓库。

- 在线站点：`https://logo.unboundx.tech`
- GitHub 仓库：`https://github.com/jackiexiao/unboundx-logo`
- 最新规范页源文件：`index.html`
- 深色规范页别名：`unboundx-brand-guidelines-dark.html`
- 设计过程记录：`docs/logo-design-process.md`
- Gemini 设计复盘：`docs/gemini-logo-design.md`

## 仓库结构

- `index.html`：当前最新、最终采用的深色品牌规范页源码。
- `unboundx-brand-guidelines-dark.html`：与 `index.html` 同步的深色规范页别名。
- `public/`：当前最终方案的品牌交付物料包，含 `logos/`、`materials/` 与下载压缩包。
- `docs/`：设计过程、AI 协作文档与项目说明。
- `archive/history/`：历史探索稿、临时演进页、浏览器导出稿与生成脚本归档。

## 维护约定

- 日常编辑优先修改 `index.html`
- 发布深色规范页时同步到 `unboundx-brand-guidelines-dark.html`
- 静态资源统一只维护根目录下这一套 `public/`
- 历史版本与实验文件统一放在 `archive/history/`
- `unboundx-brand-guidelines-v4-final.html` 属于旧版方案，不再作为当前主稿

## 设计与协作

本项目采用「人类创意主导 + AI 协作生成」的工作流，主要涉及：

- Claude Code
- Codex CLI
- Gemini 3.1 Pro
- HTML / CSS / JS / SVG 纯代码绘制

最终交付为一个可直接浏览、可在线下载 Logo ZIP 资产包的静态品牌规范站点。

## 部署说明

- 托管平台：Vercel
- 访问域名：`logo.unboundx.tech`
- DNS：Cloudflare

## 权利说明

本仓库中的品牌设计、代码资产、文档内容及相关视觉素材著作权归：

**自由维度（深圳）科技有限公司**

保留所有权利。未经书面授权，不得复制、分发、商用或进行二次授权。
