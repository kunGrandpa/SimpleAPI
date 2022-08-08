#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2022-08-08 09:29:44
# @author: 鹰眼测试


import yaml
import os


class YAMLAction:
    def __init__(self, yamlFile):
        if not os.path.exists(yamlFile):
            raise FileExistsError(f"{yamlFile} 目录或文件不存在")
        else:
            if not os.path.isfile(yamlFile):
                raise FileNotFoundError(f"{yamlFile} 这是一个目录，而不是文件")
            else:
                # 获取文件后缀，如果不是YAML或YML，就给个报错
                suffix = os.path.split(yamlFile)[-1].lower().split(".")[-1]
                if suffix not in ("yml", "yaml"):
                    raise FileExistsError(f"仅接收YAML文件，不支持 {suffix} 格式的文件")
                else:
                    self.yamlFile = yamlFile

    def read_yaml(self):
        with open(self.yamlFile, "r", encoding="utf-8") as f:
            return yaml.safe_load(f.read())


if __name__ == '__main__':
    a = YAMLAction("/Users/kun/Desktop/SimpleAPI/Data/baiduModule/baidu.yaml").read_yaml()
    print(a)
