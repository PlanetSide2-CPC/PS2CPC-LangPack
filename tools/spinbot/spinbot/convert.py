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
        with open(self.path, "r") as origin:
            with open(f"{self.path}.xml", "w") as result:
                result.writelines("<?xml version='1.0' encoding='UTF-8'?>\n")
                result.writelines("<root>\n")
                for line in origin:
                    components = re.split(r"\s", line, maxsplit=2)
                    try:
                        _key, _type, _str = components[0], components[1], components[2].strip()
                    except IndexError:
                        continue
                    _str = _str.replace("<br>", "\n").replace("<br \\>", "\n").replace("<BR>", "\n")
                    result.writelines(f"  <str key=\"{_key}\" type=\"{_type}\">{_str}</str>\n")
                result.writelines("</root>")


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
