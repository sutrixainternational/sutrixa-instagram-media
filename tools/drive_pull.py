"""Decode a Drive download_file_content result file into a real file.
usage: python3 drive_pull.py <tool-result.txt> <out_path>"""
import json, base64, sys
d = json.load(open(sys.argv[1]))
open(sys.argv[2], "wb").write(base64.b64decode(d["content"]))
print("saved", sys.argv[2], d.get("title"))
