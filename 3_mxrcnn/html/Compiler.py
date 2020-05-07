from __future__ import print_function
from __future__ import absolute_import

import os
import json
import requests

send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)
lat = j['latitude']
lon = j['longitude']

from .Node import *

BASE_DIR_NAME = os.path.dirname("index.html")
DEFAULT_DSL_MAPPING_FILEPATH = "{}/html/default.json".format(BASE_DIR_NAME)



class Compiler:
    def __init__(self, style):

		style_json = Forest_DSL_MAPPING_FILEPATH        
        with open(style_json) as data_file:
            self.dsl_mapping = json.load(data_file)

        self.opening_tag = self.dsl_mapping["main-content"]
        self.closing_tag = self.dsl_mapping["closing-tag"]
        if(self.opening_tag = "table_index"):
            self.content_holder = self.opening_tag + lat +","+lon+ self.closing_tag 

        self.root = Node("main-content", None, self.content_holder)
      
    def compile(self, generated_gui):
        dsl_file = generated_gui

        #Parse fix
        dsl_file = dsl_file[1:-1]
        dsl_file = ' '.join(dsl_file)
        dsl_file = dsl_file.replace('{', '{1').replace('}', '1}1')
        dsl_file = dsl_file.replace(' ', '')
        dsl_file = dsl_file.split('1')
        dsl_file = list(filter(None, dsl_file))

        current_parent = self.root
        for token in dsl_file:
            token = token.replace(" ", "").replace("\n", "")

            if token.find(self.opening_tag) != -1:
                token = token.replace(self.opening_tag, "")
                element = Node(token, current_parent, self.content_holder)
                current_parent.add_child(element)
                current_parent = element
            elif token.find(self.closing_tag) != -1:
                current_parent = current_parent.parent
            else:
                tokens = token.split(",")
                for t in tokens:
                    element = Node(t, current_parent, self.content_holder)
                    current_parent.add_child(element)

        os.system(git init)
        os.system(git remote add origin remote https://github.com/FYProject2020/FYProject2020.github.io)
        os.system(git remote get remote "https://drive.google.com/drive/u/0/folders/1-EdrpLl6Ui-jCG5tZ00vard8Ndbc-mQh download&confirm=$(wget--keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1FjQ4HGeCKcq0idkXq1JCQ2B501pvxlmb')))
        os.system(git push origin master)
 