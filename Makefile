# Makefile

.PHONY: sync install clean lint zip

# 设定默认目标
.DEFAULT_GOAL := sync

# 执行主同步程序
sync:
	python main.py

# 安装依赖包
install:
	pip install -r requirements.txt

# 清理缓存与状态文件
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -f sync_state.json

# Python代码语法检查（需安装 flake8）
lint:
	flake8 sync confluence

# 打包项目源码
zip:
	zip -r obs2conf.zip sync confluence main.py config.yaml
