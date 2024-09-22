# streamlit-template
Streamlit 模板，最大程度精简。

## 使用方式

### 1. 创建初始环境 
```bash
#conda
conda create -n my_streamlit_env python=3.9
conda activate my_streamlit_env

#venv
python -m venv streamlit_env
source streamlit_env/bin/activate #linux
streamlit_env\Scripts\activate    #win

#不需要虚拟环境的可以直接下一步
```
### 2. 安装依赖包
```bash
conda env update -f environment.yml --prune #conda安装,注意修改environment.yml里的一些数据
pip install -r requirements.txt #pip安装
```
### 3.运行
```bash
streamlit run streamlit_app.py
```

## 欢迎提建议

enjoy!