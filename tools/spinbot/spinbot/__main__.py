"""This module implements the functionality of the command line."""
import logging

from spinbot.convert import CreateConverter

logger = logging.getLogger(__name__)

converter = CreateConverter.get_converter(r"D:\PycharmProjects\PS2CPC-LangPack\tools\spinbot\en_us_data.dat", "xml")
converter.on_convert()
