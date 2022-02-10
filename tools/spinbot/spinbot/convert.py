"""This module implements the format conversion."""
import abc
import logging
import re

logger = logging.getLogger(__name__)


class Converter(metaclass=abc.ABCMeta):
    def __init__(self, path):
        self.path = path

    @abc.abstractmethod
    def on_convert(self):
        pass


class XMLConverter(Converter):
    def on_convert(self):
        with open(self.path, "r") as origin, open(f"{self.path}.override", "w") as override:
            contents = ""
            for line in origin:
                # 移除语言文件中的空行
                if line.isspace():
                    continue

                # 替换 br 标签
                line = line.replace("<", "&lt;").replace(">", "&gt;").replace("&", "&amp;").strip()

                # 重新处理翻译文件空行
                if any(x in line for x in ["ucdt", "ugdt"]):
                    contents += f"\n{line}"
                else:
                    contents += f"{line}"

            # 保存写入
            override.writelines(contents.strip())

        with open(f"{self.path}.override", "r") as origin, open(f"{self.path}.xml", "w") as output:
            # 添加 XML 标头
            output.writelines("<?xml version='1.0' encoding='UTF-8'?>\n")
            output.writelines("<root>\n")

            for line in origin:
                # 分割原始行并转为 XML 格式
                components = re.split(r"\s", line, maxsplit=2)
                key, types, string = components[0].strip(), components[1].strip(), components[2].strip()
                output.writelines(f"  <str key=\"{key}\" type=\"{types}\">{string}</str>\n")

            # 添加 XML 结束标签
            output.writelines("</root>")


class JSONConverter(Converter):
    def on_convert(self):
        pass


class CreateConverter:
    @staticmethod
    def get_converter(path, target):
        if target == "xml":
            return XMLConverter(path)
        elif target == "json":
            return JSONConverter(path)
        else:
            raise TypeError("The Converter does not exist.")


if __name__ == '__main__':
    pass
