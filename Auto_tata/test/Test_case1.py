def baoshu(n, m):
    """
    :param n: n个人
    :param m: 报数为m出列
    :return:
    """
    baoshu = 0
    child = [i for i in range(1, n + 1)]  # 给小孩编号
    print(child)
    while len(child) > 1:
        baoshu += 1
        child.append(child.pop(0))  # 将list第一个数放到list的末尾，将list围成一个圈
        if baoshu == m:  # 判断报数与M是否相等，相等则移除该小孩
            baoshu = 0
            child.pop()
    # print(child)


if __name__ == '__main__':
    baoshu(5, 2)

count = 0
while (count < 9):
    print('The count is:', count)
    count = count + 1

print("Good bye!")
