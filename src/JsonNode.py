from abc import ABC, abstractmethod
from Iterator import ComponentAggregateIterator

"""
这里使用了组合模式.
组合模式的使用:
  Component 类是抽象基类,定义了所有组件的公共接⼝, 如方法 draw .
  Container 类是容器节点,为复合对象, 可以包含其他 Component 对象, 其重写的 draw 能够递归地绘制其子组件.
  Leaf 类是叶子节点, 其不会包含其他 Component 对象.
  
访问者模式的体现:
Container 或 Leaf 可接收DrawVisitor的访问，并根据访问者的逻辑来被展示.
(注:Visitor 和 DrawVisitor的实现在Visitor.py中)
"""


class Component(ABC):
    def __init__(self, icon, name, is_first, is_leaf, is_last):
        self.icon = icon
        self.name = name
        # self.level = level
        self.is_first = is_first
        self.is_leaf = is_leaf
        self.is_last = is_last

    @abstractmethod
    def accept(self, visitor, style_config):
        pass


class Container(Component):
    def __init__(self, icon, name, is_first, is_leaf, is_last, level):
        super().__init__(icon, name, is_first, is_leaf, is_last)
        self.level = level
        self.children = []

    def add(self, component):
        self.children.append(component)

    def create_child_iterator(self):
        return ComponentAggregateIterator(self.children)

    def accept(self, visitor, style_config, depth=0, prefix="", is_child_last=False):
        visitor.visit_container(self, style_config, depth, prefix, is_child_last)


class Leaf(Component):
    def __init__(self, icon, name, is_first, is_leaf, is_last, value):
        super().__init__(icon, name, is_first, is_leaf, is_last)
        self.value = value

    def accept(self, visitor, style_config, depth=0, prefix="", is_child_last=False):
        visitor.visit_leaf(self, style_config, depth, prefix, is_child_last)
