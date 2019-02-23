#静态---运行前，如果要调用类的属性或者方法，我需要实例化他的对象
#动态---运行时，就获取类的属性或方法，甚至更改他的属性或方法

class girls:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def singe(self):
        print(self.name+"会唱歌")
if __name__ == '__main__':
    g=girls('娟娟','18')
    print(g.name)
    setattr(g,'可可','2')              #这样写是不对的
    setattr(g,'hub','swimming')      #给类或者实例对象动态的去添加属性或者方法
    print(g.hub)
    print(g.name)
    print(getattr(g,'hub'))           #根据属性名获取类的属性，当属性不存在的时候，报AttributeError
    print(hasattr(g,'name'))           #判断当前这个类有没有这个属性，有就返回True,没有就返回flase
    setattr(g,'single','yes')
    print(g.single)                    #给对象添加single属性
    print(hasattr(g,'single'))
    delattr(g,'name')                  #删除属性
    print(hasattr(g,'name'))           #判断是否有这个属性
    print(getattr(g,'name'))            #现在报错了 因为name被删除了
