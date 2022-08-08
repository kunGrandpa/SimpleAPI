#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time: 2022-08-08 09:50:44
# @author: 鹰眼测试


import pytest
import allure


# 标记模块名称，最后会在报告中显示
@allure.feature("XX模块")
class TestBaidu:

    @allure.story("百度请求")  # 用例名称，可以直接写接口名称
    pass
    @allure.title("")  # 用例标题
    @pytest.mark.parametrize()
    def test_case_1(self):
        pass
