import pandas  as pd
# 1：读取指定行
print("----读取指定的单行，数据会存在列表里面----")
df = pd.read_excel(u"/Users/rtmap/Desktop/vip_info_t1小程序.xlsx")  # 这个会直接默认读取到这个Excel的第一个表单
data = df.loc[0].values  # 0表示第一行 这里读取数据并不包含表头，要注意哦！
print("读取指定行的数据：\n{0}".format(data))

print("\n------读取指定的多行，数据会存在嵌套的列表里面----------")
df = pd.read_excel(u"/Users/rtmap/Desktop/vip_info_t1小程序.xlsx")  # 这个会直接默认读取到这个Excel的第一个表单
data = df.loc[[1, 2]].values  # 读取指定多行的话，就要在loc[]里面嵌套列表指定行数
print("读取指定行的数据：\n{0}".format(data))

print("\n----------------读取指定的行列-----------------------")
df = pd.read_excel(u"/Users/rtmap/Desktop/vip_info_t1小程序.xlsx")  # 这个会直接默认读取到这个Excel的第一个表单
data = df.iloc[1, 2]  # 读取第一行第二列的值，这里不需要嵌套列表
print("读取指定行的数据：\n{0}".format(data))

print("\n----------------读取指定的多行多列值-----------------------")
df = pd.read_excel(u"/Users/rtmap/Desktop/vip_info_t1小程序.xlsx")  # 这个会直接默认读取到这个Excel的第一个表单
data = df.loc[[1, 2], ['商品总价', '会员折扣']].values  # 读取第一行第二行的title以及data列的值，这里需要嵌套列表
print("读取指定行的数据：\n{0}".format(data))

print("\n-----------获取所有行的指定列----------------------------")
df = pd.read_excel(u"/Users/rtmap/Desktop/vip_info_t1小程序.xlsx")  # 这个会直接默认读取到这个Excel的第一个表单
data = df.loc[:, ['商品总价', '会员折扣']].values  # 读所有行的title以及data列的值，这里需要嵌套列表
print("读取指定行的数据：\n{0}".format(data))

print("\n------------获取行号并打印输出---------------------------")
df = pd.read_excel(u"/Users/rtmap/Desktop/vip_info_t1小程序.xlsx")  # 这个会直接默认读取到这个Excel的第一个表单
print("输出行号列表", df.index.values)

print("\n-------------获取列名并打印输出--------------------------")
df = pd.read_excel(u"/Users/rtmap/Desktop/vip_info_t1小程序.xlsx")  # 这个会直接默认读取到这个Excel的第一个表单
print("输出列标题", df.columns.values)

print("\n------------获取指定行数的值---------------------------")
df = pd.read_excel(u"/Users/rtmap/Desktop/vip_info_t1小程序.xlsx")  # 这个会直接默认读取到这个Excel的第一个表单
print("输出值", df.sample(1).values)  # 这个方法类似于head()方法以及df.values方法

print("\n-----------获取指定列的值----------------------------")
df = pd.read_excel(u"/Users/rtmap/Desktop/vip_info_t1小程序.xlsx")  # 这个会直接默认读取到这个Excel的第一个表单
print("输出值\n", df['商品总价'].values)