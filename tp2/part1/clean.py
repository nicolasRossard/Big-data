#! /usr/bin/python
with open("../datas/forum_node.tsv","r") as _in:
	with open("../datas/clean_forum.tsv", "w") as _out:
		for l in _in.readlines():
			_out.write(l.strip()+"\n")
