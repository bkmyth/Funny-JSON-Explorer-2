from abc import ABC, abstractmethod

"""
这里使用了访问者模式.
访问者模式的使用:
Visitor 是一个抽象基类,定义声明了对节点元素 Container 和 Leaf 的访问方法 visit_container 和 visit_leaf.
DrawVisitor 是 Visitor 的具体实现,实现了 visit_container 和 visit_leaf 方法,
DrawVisitor 实现的这两个方法将会以特定的样式配置(style_config)来访问并绘制 Container 或 Leaf.
Container 或 Leaf 可接收DrawVisitor的访问，并根据访问者的逻辑来被展示.
"""


class Visitor:
    def visit_container(self, container, style_config, depth=0, prefix="", is_child_last=False):
        pass

    def visit_leaf(self, leaf, style_config, depth=0, prefix="", is_child_last=False):
        pass


class DrawVisitor(Visitor):
    def visit_container(self, container, style_config, depth=0, prefix="", is_child_last=False):
        if depth != 0:
            if container.is_first:
                connector = style_config["first"]["start"]["last" if is_child_last else "open"]
                pre_str = f"{prefix}{connector} {container.icon}{container.name} "
                pre_len = len(pre_str)
                pad = str(style_config["first"]["padding"]) * (40 - pre_len)
                pad = pad + str(style_config["first"]["end"])
            elif container.is_last:
                prefix = (style_config["last"]["start"]["open"] + prefix[2:])
                connector = style_config["last"]["follow"]["last" if is_child_last else "open"]
                pre_str = f"{prefix}{connector} {container.icon}{container.name} "
                pre_len = len(pre_str)
                pad = str(style_config["last"]["padding"]) * (40 - pre_len)
                pad = pad + str(style_config["last"]["end"])
            else:
                connector = style_config["body"]["follow"]["last" if is_child_last else "open"]
                pre_str = f"{prefix}{connector} {container.icon}{container.name} "
                pre_len = len(pre_str)
                pad = str(style_config["body"]["padding"]) * (40 - pre_len)
                pad = pad + str(style_config["body"]["end"])
            print(f"{prefix}{connector} {container.icon}{container.name} {pad}")

            if depth > 1 or is_child_last:
                prefix += style_config["body"]["follow"]["lasting"]
            else:
                prefix += style_config["body"]["follow"]["opening"]

        child_iterator = container.create_child_iterator()
        while child_iterator.has_next():
            child = child_iterator.get_next()
            if child_iterator.has_next():
                child_last = False
            else:
                child_last = True
            child.accept(self, style_config, depth + 1, prefix, child_last)

    def visit_leaf(self, leaf, style_config, depth=0, prefix="", is_child_last=False):
        if depth != 0:
            if leaf.is_first:
                connector = style_config["first"]["start"]["last" if is_child_last else "open"]
                if leaf.value is None:
                    pre_str = f"{prefix}{connector} {leaf.icon}{leaf.name} "
                else:
                    pre_str = f"{prefix}{connector} {leaf.icon}{leaf.name}: {leaf.value} "
                pre_len = len(pre_str)
                pad = str(style_config["first"]["padding"]) * (40 - pre_len)
                pad = pad + str(style_config["first"]["end"])
            elif leaf.is_last:
                prefix = (style_config["last"]["start"]["lasting" if is_child_last else "opening"] +
                          prefix[2:])
                connector = style_config["last"]["follow"]["last" if is_child_last else "open"]
                if leaf.value is None:
                    pre_str = f"{prefix}{connector} {leaf.icon}{leaf.name} "
                else:
                    pre_str = f"{prefix}{connector} {leaf.icon}{leaf.name}: {leaf.value} "
                pre_len = len(pre_str)
                pad = str(style_config["last"]["padding"]) * (40 - pre_len)
                pad = pad + str(style_config["last"]["end"])
            else:
                connector = style_config["body"]["follow"]["last" if is_child_last else "open"]
                if leaf.value is None:
                    pre_str = f"{prefix}{connector} {leaf.icon}{leaf.name} "
                else:
                    pre_str = f"{prefix}{connector} {leaf.icon}{leaf.name}: {leaf.value} "
                pre_len = len(pre_str)
                pad = str(style_config["body"]["padding"]) * (40 - pre_len)
                pad = pad + str(style_config["body"]["end"])
            if leaf.value is None:
                print(f"{prefix}{connector} {leaf.icon}{leaf.name} {pad}")
            else:
                print(f"{prefix}{connector} {leaf.icon}{leaf.name}: {leaf.value} {pad}")

            if depth > 1 or is_child_last:
                prefix += style_config["body"]["follow"]["lasting"]
            else:
                prefix += style_config["body"]["follow"]["opening"]
