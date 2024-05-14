from datetime import timedelta

# 可以随便写 越长越安全解密越慢
SECRET_KEY = 'Flat-White'

# 访问令牌的过期时间为60分钟
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=60)
# 刷新令牌的过期时间为30天
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

# 数据库配置
HOSTNAME = '43.136.109.225'
PORT = 3306
USERNAME = 'root'
# 注意 数据库密码中若带特殊字符，需要输入转义后的
PASSWORD = 'HANGshengAE%402023#0110De'
DATABASE = 'Hyolo9_wg_240500'
#DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
# MAIL_SERVER = 'smtp.qq.com'
# MAIL_USE_SSL = True
# MAIL_PORT = 465
# MAIL_USERNAME = '1695503143@qq.com'
# MAIL_PASSWORD = 'ucqgiattnbfedcfi'
# MAIL_DEFAULT_SENDER = ("基于深度学习算法的垃圾检测系统", "1695503143@qq.com")