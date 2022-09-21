
# 考研信息查询网站

- 本仓库为项目**后端**基于 **Django4.0**
- Django REST framework (**DRF**)
- [前端仓库](https://github.com/TIANYUZHOU/KaoYan-InfoWeb_CS)

## 预览

### 用户端

- 主界面
![主界面](https://pic.zty.plus/%E6%AF%95%E8%AE%BE%E5%BC%80%E6%BA%90%E5%9B%BE/%E4%B8%BB%E7%95%8C%E9%9D%A2.png)
- 地区院校查询
![主界面](https://pic.zty.plus/%E6%AF%95%E8%AE%BE%E5%BC%80%E6%BA%90%E5%9B%BE/%E5%9C%B0%E5%8C%BA-%E9%99%A2%E6%A0%A1%E6%9F%A5%E8%AF%A2.png)
- 科目院校查询
![详细信息](https://pic.zty.plus/%E6%AF%95%E8%AE%BE%E5%BC%80%E6%BA%90%E5%9B%BE/%E8%AF%A6%E7%BB%86%E4%BF%A1%E6%81%AF.png)
- 资料分享
![资料分享](https://pic.zty.plus/%E6%AF%95%E8%AE%BE%E5%BC%80%E6%BA%90%E5%9B%BE/%E8%B5%84%E6%96%99%E5%88%86%E4%BA%AB.png)

### 管理端
- 主界面
![管理端主界面](https://pic.zty.plus/%E6%AF%95%E8%AE%BE%E5%BC%80%E6%BA%90%E5%9B%BE/%E7%AE%A1%E7%90%86%E7%AB%AF-%E4%B8%BB%E7%95%8C%E9%9D%A2.png)
- 院校数据
![院校数据](https://pic.zty.plus/%E6%AF%95%E8%AE%BE%E5%BC%80%E6%BA%90%E5%9B%BE/%E7%AE%A1%E7%90%86%E7%AB%AF-%E9%99%A2%E6%A0%A1%E6%95%B0%E6%8D%AE.png)

### 更多演示

- 没有服务器放Demo，请自行本地运行。

## 快速开始

### 项目构建环境

- Python (3.8)
- Django (4.0)
- MySQL (8.0)
- Redis

#### Tips

- 以上为开发环境，与上环境版本有差距也不一定不行。
- 数据库使用**Django**默认的**SQLite**应该也可以，在**setting.py**中配置一下就好了。

### 运行项目

#### 克隆代码仓库

```shell
git clone https://github.com/TIANYUZHOU/KaoYan-InfoWeb_CS_Backend.git
```

#### 安装依赖

- 进入项目根目录
- 执行`requirements.txt`文件

```shell
pip install -r requirements.txt
```

#### 生成数据库表结构

- 将model层转为迁移文件migration。

```shell
python manage.py makemigrations
```
- 新版本的迁移文件执行，更新数据库。

```shell
python manage.py migrate
```

#### 启动项目

```shell
python manage.py runserver
```

