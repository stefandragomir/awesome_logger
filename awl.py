
import os
from datetime  import datetime
from functools import partial

"""********************************************************************************
***********************************************************************************
********************************************************************************"""
class AwLog(object):

	def __init__(self,name,levels=["error","warning","info","debug"],path=None):

		self.__path          = path
		self.__is_path       = os.path.exists(self.__path) if self.__path != None else False
		self.__name          = name
		self.__file          = os.path.join(self.__path,"%s.log" % (self.__name,)) if self.__is_path else None
		self.__file_max_size = 50000000 # 50MB

		for _level in levels:

			self.__dict__.update({"%s" % (_level,)        : partial(self.__log,level=_level)})
			self.__dict__.update({"with_%s" % (_level,)   : True})

	def __log(self,txt,level):

		if self.__dict__["with_%s" % (level,)]:

			_text = "[%s][%s] %s" % (datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f"),level.upper(),txt)

			self.__log_to_console(_text)

			if self.__is_path:

				self.__log_to_file(_text)

	def __log_to_console(self,txt):

		print(txt)

	def __get_log_file(self):

		if self.__is_path:

			if os.path.getsize(self.__file) >= self.__file_max_size:

				

			if not os.path.exists(self.__file):

				with open(_path,'w+') as _log_file:

					_log_file.write("")

		return _path

	def __log_to_file(self,txt):

		_path = self.__get_log_file()

		if _path != None:

			with open(_path,"a") as _log_file:

				_log_file.write("%s\n" % (txt,))

"""********************************************************************************
***********************************************************************************
********************************************************************************"""

_log = AwLog("app",path="c:\\temp")

_log.error("test")
_log.warning("test")
_log.info("test")
_log.debug("test")

	