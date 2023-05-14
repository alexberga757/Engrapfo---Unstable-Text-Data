"""
Engrapfo TextData Viewer
Version: 1.0.1_unstable_view

Contact me on: lengoccuong.carrd.com
"""

import Engrapfo.stringParse as mparse
import Engrapfo.Except as Except

import os;

class load:
	#a:b\nc:d => "a:b","c:d"
	def __init__(self,val):
		self.value = val.split('\n');




	def GetValue(self,name):
		token = "";
		#read
		for line in self.value:
			toarr = line.split(':');
			#verify name
			if (mparse.RemoveFirstSpace(toarr[0]) == name):
				for lst in range(len(toarr)):

					#skip name
					if lst == 0:
						pass;
					else:
						#add token
						token += ":{0}".format(toarr[lst]);
				break;
			else:
				pass;

		#Confirm the string has not been received or received
		if (token == ""):
			return None;
		else:
			return mparse.RemoveFirst(token);

	#check exists true or false?
	def existsval(self,name):
		ExistsYN = False;
		name_fix = mparse.RemoveFirstSpace(name);
		for line in self.value:
			toarr = line.split(':');
			if (mparse.RemoveFirstSpace(toarr[0]) == name_fix):
				ExistsYN = True;
				break;
			else:
				ExistsYN = False;

		return ExistsYN;

	#add new value
	def  push(self,name,val):
		value = self.value; 
		name_fix = mparse.RemoveFirstSpace(name);

		#check no exists or exists
		if (self.existsval(name_fix)):
			raise Except.EngrapfoErr("this value exists");
		else:
			value.append("{0}:{1}".format(name_fix,val));

		self.value = value;

	#remove value
	def remove(self,name):
		value = self.value;
		name_fix = mparse.RemoveFirstSpace(name);

		val = [];
		if (self.existsval(name_fix)):
			for line in value:
				s = line.split(':');
				#if value exist then remove this value
				if (s[0] == name_fix):
					pass;
				else:
					val.append(line);

			self.value = val;
		else:
			raise Except.EngrapfoErr("this value not exists");

	#list name
	def list(self,name):
		arr = [];
		for line in self.value:
			arr.append(line.split(':')[0]);
		return arr;

	def reget(self):
		tok = "";
		st = 0;
		for line in self.value:
			st += 1;
			if (st == 1):
				tok += line;
			else:
				tok += "\n{0}".format(line);

		return tok; 

	def export(self,path):
		with open(path,"w") as file:
			file.write(self.reget());





