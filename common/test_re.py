import re
# admin_user='15309694829'
# admin_pwd='123456'
# s='{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'
# # p="\$\{(admin_user)}"       #需要增加转义字符
# # r=re.search(p,s)
# # key=re.group(1)
# if s.find("${admin_user}") > -1:      #字符串查找，然后手动替换
#     s = s.replace("${admin_user}",'15309694829')
# if s.find("${admin_pwd}") > -1:      #字符串查找，然后手动替换
#     s = s.replace("${admin_pwd}",'123456')
# print(s)


# #()代表组的意思
# data= {"admin_user":"15309694829","admin_pwd":"123456"}
# s='{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'
# p="\$\{(.*?)}"     #记得加转义字符\      ?找到一个就停止 不要贪婪匹配
# m=re.search(p,s)        #search 找到一个就返回
# g = m.group()    #返回的是整个匹配的字符串
# g1 = m.group(1)  #取一个组的匹配字符串
# value = data[g1]
# #while re.search(p,s):
# m=re.sub(p,value,s,count=1)   #查找全部
# print(m)
# print(g)
# print(g1)

#s 是目标字符串
#d 是替换的内容
#找到目标字符串里面的标识符key，去d里面拿到替换的值
#替换到s里面去，然后再返回
#()代表组的意思
from conf.conf1 import ConFig
class context_1:    #上下文类，数据的管理和准备
    admin_mobilephone = ConFig().get_conf('admin','mobilephone')
    admin_pwd = ConFig().get_conf('admin','pwd')
    admin_id = ConFig().get_conf('admin','memberId')
    invest_mobilephone = ConFig().get_conf('invest','invest_mobilephone')
    invest_pwd = ConFig().get_conf('invest','invest_pwd')
    invest_id = ConFig().get_conf('invest', 'invest_id')


    #11642


    # def replace(s,d):
    #     p = "\$\{(.*?)}"
    #     while re.search(p,s):      #rearch 没有的时候，就返回none，找到一个就返回match，找到一个返回一个
    #         m=re.search(p,s)
    #         key = m.group(1)
    #         value = d[key]
    #         s = re.sub(p,value,s,count=1)
    #     return s
    #print(replace())

    def replace_1(self,s):
        p = "\$\{(.*?)}"
        while re.search(p,s):      #rearch 没有的时候，就返回none，找到一个就返回match，找到一个返回一个
            m=re.search(p,s)
            key = m.group(1)
            if hasattr(context_1,key):   #判断是否有key这个属性
             value = getattr(context_1, key)  # 利用反射动态的获取属性
             s = re.sub(p,value,s,count=1)
            else:
             return None # 没有就抛出一个异常，告知没有这个属性
        return s
if __name__ == '__main__':
    s1 = '{"mobilephone":"${admin_id}"," invest_id":"${invest_id}"}'
    #g = context()   #不需要实例化context
    n = context_1().replace_1(s1)
    print(n)
