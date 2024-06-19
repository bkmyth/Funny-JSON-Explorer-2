from abc import ABC, abstractmethod

"""
这里使用了迭代器模式.
迭代器模式的使用:
我先定义了一个抽象基类 Iterator , 定义了 get_next() 和 has_next()方法.
然后实现了其具体子类 ComponentAggregateIterator , 实现了在 Iterator 中定义的get_next() 和 has_next()方法/接口.
使用 ComponentAggregateIterator 便可遍历含有多个 Component (Container 和 Leaf) 的聚合对象.
  ComponentAggregateIterator的使用:
  比如, Container本身就是一个聚合对象(它的children可包括多个 Component ,即包括多个Container 或 Leaf), 在实际运用中,
  通过在Container这个聚合对象中定义实现一个创建ComponentAggregateIterator迭代器的方法,聚合对象外部便可借由这个方法创建的
  迭代器通过统一的方式遍历Container中的children(Component 列表)的元素Container或Leaf.
"""


class Iterator(ABC):
    @abstractmethod
    def get_next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass


class ComponentAggregateIterator(Iterator):
    def __init__(self, component_list):
        self.component_list = component_list
        self.idx_cur = 0
        self.length = len(self.component_list)

    def get_next(self):
        if self.has_next():
            next_component = self.component_list[self.idx_cur]
            self.idx_cur += 1
            return next_component
        else:
            raise StopIteration

    def has_next(self):
        return self.idx_cur < self.length
