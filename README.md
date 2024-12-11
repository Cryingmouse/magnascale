<!-- TOC -->
* [poetry 配置文档](#poetry-配置文档)
    * [配置poetry变量](#配置poetry变量)
    * [安装 poetry-dynamic-versioning 插件](#安装-poetry-dynamic-versioning-插件)
    * [查看配置](#查看配置)
    * [安装项目依赖](#安装项目依赖)
    * [添加新依赖](#添加新依赖)
    * [添加开发依赖](#添加开发依赖)
    * [更新所有依赖](#更新所有依赖)
    * [更新特定包](#更新特定包)
    * [创建并激活虚拟环境](#创建并激活虚拟环境)
    * [在虚拟环境中运行命令](#在虚拟环境中运行命令)
    * [查看虚拟环境信息](#查看虚拟环境信息)
    * [重置虚拟环境](#重置虚拟环境)
    * [清理缓存](#清理缓存)
<!-- TOC -->

# poetry 配置文档

### 配置poetry变量
```bash
poetry config virtualenvs.in-project true
poetry config repositories.tsinghua https://pypi.tuan.tsinghua.edu.cn/simple
```

### 安装 poetry-dynamic-versioning 插件
```bash
poetry self add "poetry-dynamic-versioning[plugin]"
```

### 查看配置
```bash
poetry config --list
```

### 安装项目依赖
```bash
poetry install
```

### 添加新依赖
```bash
poetry add requests pandas
```

### 添加开发依赖
```bash
poetry add --group dev pytest black
```

### 更新所有依赖
```bash
poetry update
```

### 更新特定包
```bash
poetry update requests
```

### 创建并激活虚拟环境
```bash
poetry shell
```

### 在虚拟环境中运行命令
```bash
poetry run python script.py
```

### 查看虚拟环境信息
```bash
poetry env info
```

### 重置虚拟环境
```bash
poetry env remove python
poetry install --remove-untracked
```

### 清理缓存
```bash
poetry cache clear . --all
```