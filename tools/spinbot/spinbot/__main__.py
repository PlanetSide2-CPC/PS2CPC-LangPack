"""This module implements the functionality of the command line."""
import logging

from spinbot.convert import CreateConverter

logger = logging.getLogger(__name__)

path = str(input("源文件路径：") or "../en_us_data.dat")
types = str(input("转换成（xml/json）：") or "xml")

try:
    converter = CreateConverter.get_converter(path, types)
    converter.on_convert()
except FileNotFoundError:
    raise FileNotFoundError("你故意找茬是不？你要不要把！")
