data = [input() for i in range(5)]

m_count = int(data[0].strip())
m_list = data[1:]
print(data)
print('회원 수: ', m_count)
print('회원 리스트 : ', m_list)


def age(string):
    result = string.split()
    return result[0]
# print(age(m_list[0]))


new_list = []
# print(len(new_list))
for i in range(m_count):
    if len(new_list) == 0:
        new_list.append(m_list[i])
    else:
        if age(m_list[i]) < age(new_list[0]):
            new_list.insert(0, m_list[i])
        elif age(m_list[i]) > age(new_list[-1]):
            new_list.append(m_list[i])
        else:
            for j in range(m_count):
                if age(m_list[i]) >= age(new_list[j]):
                    new_list.insert(j+1, m_list[i])
                    break
print(new_list)
