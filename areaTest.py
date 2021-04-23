import time
import unittest

from selenium.webdriver.common.by import By

import HTMLTestReport
import tool
# 请输入管理单位、请输入土地名称、请输入土地资产卡片编号、请输入地域分类、
# 请输入行政区域、请输入坐落位置、请输入土地证号、请输入产权单位、请输入土地用途、
# 请输入土地性质、请输入土地产权状况、请输入土地总面积（㎡）、请输入启用/停用未填写
class areaTest(unittest.TestCase):
    def test1(self):
        '''新增土地-成功测试'''
        print("========【case_0001】新增土地-成功测试 =============")
        b = tool.login("488235", "admin", "jx123456")
        tool.joinItem(b, "房屋土地信息", "土地基本信息", "土地信息维护")
        tool.wait(2)
        b.find_element_by_xpath('//button/span[text()="新增"]').click()

        tool.setObject(b, "orgId", "lyx-413") #管理单位
        tool.setText(b, "landName", "czy1")  #土地名称
        tool.setText(b, "landAssetCardCode", "001") #土地资产卡片编号
        tool.setObject(b, "basicsLandGeographicalClassificationId", "省内") #地域分类
        tool.setObject(b, "basicsHouseAdministrativeAreaId", "浙江省") #行政区域
        tool.setText(b, "address", "413") #坐落地址
        tool.setText(b, "landCertificateNumber", "42")  # 土地证号
        tool.setObject(b, "propertyBaseinfoUnitId", "lyx-413")  # 产权单位
        tool.setObject(b, "basicsLandPurposeId", "工业用地")  # 土地用途
        tool.setObject(b, "basicsLandNatureId", "划拨")  # 土地性质
        tool.setObject(b, "basicsLandPropertyRegistrationId", "无产权未办证")  # 土地产权状况
        tool.setNumber(b,"landTotalArea",1) #土地总面积
        tool.setDict(b,"freezeIs","启用") #启用/停用

        tool.wait(1)
        b.find_element_by_xpath("//div[@class='fromMenuBox']/button/span[text()='保存']").click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('操作成功!', addUnitMsg)
        tool.close(b)

    def test2(self):
        '''新增土地-管理单位未填写测试'''
        print("========【case_0002】新增土地-管理单位未填写测试 =============")
        b = tool.login("488235", "admin", "jx123456")
        tool.joinItem(b, "房屋土地信息", "土地基本信息", "土地信息维护")
        tool.wait(2)
        b.find_element_by_xpath('//button/span[text()="新增"]').click()

        # tool.setObject(b, "orgId", "lyx-413") #管理单位
        tool.setText(b, "landName", "czy2")  #土地名称
        tool.setText(b, "landAssetCardCode", "002") #土地资产卡片编号
        tool.setObject(b, "basicsLandGeographicalClassificationId", "省内") #地域分类
        tool.setObject(b, "basicsHouseAdministrativeAreaId", "浙江省") #行政区域
        tool.setText(b, "address", "413-1") #坐落地址
        tool.setText(b, "landCertificateNumber", "42")  # 土地证号
        tool.setObject(b, "propertyBaseinfoUnitId", "lyx-413")  # 产权单位
        tool.setObject(b, "basicsLandPurposeId", "工业用地")  # 土地用途
        tool.setObject(b, "basicsLandNatureId", "划拨")  # 土地性质
        tool.setObject(b, "basicsLandPropertyRegistrationId", "无产权未办证")  # 土地产权状况
        tool.setNumber(b,"landTotalArea",1) #土地总面积
        tool.setDict(b,"freezeIs","启用") #启用/停用

        tool.wait(1)
        b.find_element_by_xpath("//div[@class='fromMenuBox']/button/span[text()='保存']").click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('请输入管理单位未填写', addUnitMsg)
        tool.close(b)

    def test3(self):
        '''新增土地-土地名称未填写测试'''
        print("========【case_0003】新增土地-土地名称未填写测试 =============")
        b = tool.login("488235", "admin", "jx123456")
        tool.joinItem(b, "房屋土地信息", "土地基本信息", "土地信息维护")
        tool.wait(2)
        b.find_element_by_xpath('//button/span[text()="新增"]').click()

        tool.setObject(b, "orgId", "lyx-413") #管理单位
        # tool.setText(b, "landName", "czy2")  #土地名称
        tool.setText(b, "landAssetCardCode", "002") #土地资产卡片编号
        tool.setObject(b, "basicsLandGeographicalClassificationId", "省内") #地域分类
        tool.setObject(b, "basicsHouseAdministrativeAreaId", "浙江省") #行政区域
        tool.setText(b, "address", "413-1") #坐落地址
        tool.setText(b, "landCertificateNumber", "42")  # 土地证号
        tool.setObject(b, "propertyBaseinfoUnitId", "lyx-413")  # 产权单位
        tool.setObject(b, "basicsLandPurposeId", "工业用地")  # 土地用途
        tool.setObject(b, "basicsLandNatureId", "划拨")  # 土地性质
        tool.setObject(b, "basicsLandPropertyRegistrationId", "无产权未办证")  # 土地产权状况
        tool.setNumber(b,"landTotalArea",1) #土地总面积
        tool.setDict(b,"freezeIs","启用") #启用/停用

        tool.wait(1)
        b.find_element_by_xpath("//div[@class='fromMenuBox']/button/span[text()='保存']").click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('请输入土地名称未填写', addUnitMsg)
        tool.close(b)

    def test4(self):
        '''新增土地-土地名称重复测试'''
        print("========【case_0004】新增土地-土地名称重复测试 =============")
        b = tool.login("488235", "admin", "jx123456")
        tool.joinItem(b, "房屋土地信息", "土地基本信息", "土地信息维护")
        tool.wait(2)
        b.find_element_by_xpath('//button/span[text()="新增"]').click()

        tool.setObject(b, "orgId", "lyx-413") #管理单位
        tool.setText(b, "landName", "czy1")  #土地名称
        tool.setText(b, "landAssetCardCode", "002") #土地资产卡片编号
        tool.setObject(b, "basicsLandGeographicalClassificationId", "省内") #地域分类
        tool.setObject(b, "basicsHouseAdministrativeAreaId", "浙江省") #行政区域
        tool.setText(b, "address", "413-1") #坐落地址
        tool.setText(b, "landCertificateNumber", "42")  # 土地证号
        tool.setObject(b, "propertyBaseinfoUnitId", "lyx-413")  # 产权单位
        tool.setObject(b, "basicsLandPurposeId", "工业用地")  # 土地用途
        tool.setObject(b, "basicsLandNatureId", "划拨")  # 土地性质
        tool.setObject(b, "basicsLandPropertyRegistrationId", "无产权未办证")  # 土地产权状况
        tool.setNumber(b,"landTotalArea",1) #土地总面积
        tool.setDict(b,"freezeIs","启用") #启用/停用

        tool.wait(1)
        b.find_element_by_xpath("//div[@class='fromMenuBox']/button/span[text()='保存']").click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('土地名称已存在', addUnitMsg)
        tool.close(b)

    def test5(self):
        '''新增土地-土地资产卡片编号未填写测试'''
        print("========【case_0005】新增土地-土地资产卡片编号未填写测试 =============")
        b = tool.login("488235", "admin", "jx123456")
        tool.joinItem(b, "房屋土地信息", "土地基本信息", "土地信息维护")
        tool.wait(2)
        b.find_element_by_xpath('//button/span[text()="新增"]').click()

        tool.setObject(b, "orgId", "lyx-413") #管理单位
        tool.setText(b, "landName", "czy2")  #土地名称
        # tool.setText(b, "landAssetCardCode", "002") #土地资产卡片编号
        tool.setObject(b, "basicsLandGeographicalClassificationId", "省内") #地域分类
        tool.setObject(b, "basicsHouseAdministrativeAreaId", "浙江省") #行政区域
        tool.setText(b, "address", "413-1") #坐落地址
        tool.setText(b, "landCertificateNumber", "42")  # 土地证号
        tool.setObject(b, "propertyBaseinfoUnitId", "lyx-413")  # 产权单位
        tool.setObject(b, "basicsLandPurposeId", "工业用地")  # 土地用途
        tool.setObject(b, "basicsLandNatureId", "划拨")  # 土地性质
        tool.setObject(b, "basicsLandPropertyRegistrationId", "无产权未办证")  # 土地产权状况
        tool.setNumber(b,"landTotalArea",1) #土地总面积
        tool.setDict(b,"freezeIs","启用") #启用/停用

        tool.wait(1)
        b.find_element_by_xpath("//div[@class='fromMenuBox']/button/span[text()='保存']").click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('请输入土地资产卡片编号未填写', addUnitMsg)
        tool.close(b)

    def test6(self):
        '''新增土地-土地资产卡片编号重复测试'''
        print("========【case_0006】新增土地-土地资产卡片编号重复测试 =============")
        b = tool.login("488235", "admin", "jx123456")
        tool.joinItem(b, "房屋土地信息", "土地基本信息", "土地信息维护")
        tool.wait(2)
        b.find_element_by_xpath('//button/span[text()="新增"]').click()

        tool.setObject(b, "orgId", "lyx-413") #管理单位
        tool.setText(b, "landName", "czy2")  #土地名称
        tool.setText(b, "landAssetCardCode", "001") #土地资产卡片编号
        tool.setObject(b, "basicsLandGeographicalClassificationId", "省内") #地域分类
        tool.setObject(b, "basicsHouseAdministrativeAreaId", "浙江省") #行政区域
        tool.setText(b, "address", "413-1") #坐落地址
        tool.setText(b, "landCertificateNumber", "42")  # 土地证号
        tool.setObject(b, "propertyBaseinfoUnitId", "lyx-413")  # 产权单位
        tool.setObject(b, "basicsLandPurposeId", "工业用地")  # 土地用途
        tool.setObject(b, "basicsLandNatureId", "划拨")  # 土地性质
        tool.setObject(b, "basicsLandPropertyRegistrationId", "无产权未办证")  # 土地产权状况
        tool.setNumber(b,"landTotalArea",1) #土地总面积
        tool.setDict(b,"freezeIs","启用") #启用/停用

        tool.wait(1)
        b.find_element_by_xpath("//div[@class='fromMenuBox']/button/span[text()='保存']").click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('资产卡片编号已存在', addUnitMsg)
        tool.close(b)

    def test7(self):
        '''新增土地-地域分类未填写测试'''
        print("========【case_0007】新增土地-地域分类未填写测试 =============")
        b = tool.login("488235", "admin", "jx123456")
        tool.joinItem(b, "房屋土地信息", "土地基本信息", "土地信息维护")
        tool.wait(2)
        b.find_element_by_xpath('//button/span[text()="新增"]').click()

        tool.setObject(b, "orgId", "lyx-413") #管理单位
        tool.setText(b, "landName", "czy2")  #土地名称
        tool.setText(b, "landAssetCardCode", "002") #土地资产卡片编号
        # tool.setObject(b, "basicsLandGeographicalClassificationId", "省内") #地域分类
        tool.setObject(b, "basicsHouseAdministrativeAreaId", "浙江省") #行政区域
        tool.setText(b, "address", "413-1") #坐落地址
        tool.setText(b, "landCertificateNumber", "42")  # 土地证号
        tool.setObject(b, "propertyBaseinfoUnitId", "lyx-413")  # 产权单位
        tool.setObject(b, "basicsLandPurposeId", "工业用地")  # 土地用途
        tool.setObject(b, "basicsLandNatureId", "划拨")  # 土地性质
        tool.setObject(b, "basicsLandPropertyRegistrationId", "无产权未办证")  # 土地产权状况
        tool.setNumber(b,"landTotalArea",1) #土地总面积
        tool.setDict(b,"freezeIs","启用") #启用/停用

        tool.wait(1)
        b.find_element_by_xpath("//div[@class='fromMenuBox']/button/span[text()='保存']").click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('请输入地域分类未填写', addUnitMsg)
        tool.close(b)

    def test8(self):
        '''新增土地-行政区域未填写测试'''
        print("========【case_0008】新增土地-行政区域未填写测试 =============")
        b = tool.login("488235", "admin", "jx123456")
        tool.joinItem(b, "房屋土地信息", "土地基本信息", "土地信息维护")
        tool.wait(2)
        b.find_element_by_xpath('//button/span[text()="新增"]').click()

        tool.setObject(b, "orgId", "lyx-413") #管理单位
        tool.setText(b, "landName", "czy2")  #土地名称
        tool.setText(b, "landAssetCardCode", "002") #土地资产卡片编号
        tool.setObject(b, "basicsLandGeographicalClassificationId", "省内") #地域分类
        # tool.setObject(b, "basicsHouseAdministrativeAreaId", "浙江省") #行政区域
        tool.setText(b, "address", "413-1") #坐落地址
        tool.setText(b, "landCertificateNumber", "42")  # 土地证号
        tool.setObject(b, "propertyBaseinfoUnitId", "lyx-413")  # 产权单位
        tool.setObject(b, "basicsLandPurposeId", "工业用地")  # 土地用途
        tool.setObject(b, "basicsLandNatureId", "划拨")  # 土地性质
        tool.setObject(b, "basicsLandPropertyRegistrationId", "无产权未办证")  # 土地产权状况
        tool.setNumber(b,"landTotalArea",1) #土地总面积
        tool.setDict(b,"freezeIs","启用") #启用/停用

        tool.wait(1)
        b.find_element_by_xpath("//div[@class='fromMenuBox']/button/span[text()='保存']").click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('请输入行政区域未填写', addUnitMsg)
        tool.close(b)

    def test9(self):
        '''新增土地-坐落地址未填写测试'''
        print("========【case_0009】新增土地-坐落地址未填写测试 =============")
        b = tool.login("488235", "admin", "jx123456")
        tool.joinItem(b, "房屋土地信息", "土地基本信息", "土地信息维护")
        tool.wait(2)
        b.find_element_by_xpath('//button/span[text()="新增"]').click()

        tool.setObject(b, "orgId", "lyx-413") #管理单位
        tool.setText(b, "landName", "czy2")  #土地名称
        tool.setText(b, "landAssetCardCode", "002") #土地资产卡片编号
        tool.setObject(b, "basicsLandGeographicalClassificationId", "省内") #地域分类
        tool.setObject(b, "basicsHouseAdministrativeAreaId", "浙江省") #行政区域
        # tool.setText(b, "address", "413-1") #坐落地址
        tool.setText(b, "landCertificateNumber", "42")  # 土地证号
        tool.setObject(b, "propertyBaseinfoUnitId", "lyx-413")  # 产权单位
        tool.setObject(b, "basicsLandPurposeId", "工业用地")  # 土地用途
        tool.setObject(b, "basicsLandNatureId", "划拨")  # 土地性质
        tool.setObject(b, "basicsLandPropertyRegistrationId", "无产权未办证")  # 土地产权状况
        tool.setNumber(b,"landTotalArea",1) #土地总面积
        tool.setDict(b,"freezeIs","启用") #启用/停用

        tool.wait(1)
        b.find_element_by_xpath("//div[@class='fromMenuBox']/button/span[text()='保存']").click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('请输入坐落地址未填写', addUnitMsg)
        tool.close(b)

    def test10(self):
        '''新增土地-坐落地址重复测试'''
        print("========【case_0010】新增土地-坐落地址重复测试 =============")
        b = tool.login("488235", "admin", "jx123456")
        tool.joinItem(b, "房屋土地信息", "土地基本信息", "土地信息维护")
        tool.wait(2)
        b.find_element_by_xpath('//button/span[text()="新增"]').click()

        tool.setObject(b, "orgId", "lyx-413") #管理单位
        tool.setText(b, "landName", "czy2")  #土地名称
        tool.setText(b, "landAssetCardCode", "002") #土地资产卡片编号
        tool.setObject(b, "basicsLandGeographicalClassificationId", "省内") #地域分类
        tool.setObject(b, "basicsHouseAdministrativeAreaId", "浙江省") #行政区域
        tool.setText(b, "address", "413") #坐落地址
        tool.setText(b, "landCertificateNumber", "42")  # 土地证号
        tool.setObject(b, "propertyBaseinfoUnitId", "lyx-413")  # 产权单位
        tool.setObject(b, "basicsLandPurposeId", "工业用地")  # 土地用途
        tool.setObject(b, "basicsLandNatureId", "划拨")  # 土地性质
        tool.setObject(b, "basicsLandPropertyRegistrationId", "无产权未办证")  # 土地产权状况
        tool.setNumber(b,"landTotalArea",1) #土地总面积
        tool.setDict(b,"freezeIs","启用") #启用/停用

        tool.wait(1)
        b.find_element_by_xpath("//div[@class='fromMenuBox']/button/span[text()='保存']").click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('土地地址已存在', addUnitMsg)
        tool.close(b)

    def test11(self):
        '''新增土地-土地证号未填写测试'''
        print("========【case_0011】新增土地-土地证号未填写测试 =============")
        b = tool.login("488235", "admin", "jx123456")
        tool.joinItem(b, "房屋土地信息", "土地基本信息", "土地信息维护")
        tool.wait(2)
        b.find_element_by_xpath('//button/span[text()="新增"]').click()

        tool.setObject(b, "orgId", "lyx-413") #管理单位
        tool.setText(b, "landName", "czy2")  #土地名称
        tool.setText(b, "landAssetCardCode", "002") #土地资产卡片编号
        tool.setObject(b, "basicsLandGeographicalClassificationId", "省内") #地域分类
        tool.setObject(b, "basicsHouseAdministrativeAreaId", "浙江省") #行政区域
        tool.setText(b, "address", "413-1") #坐落地址
        # tool.setText(b, "landCertificateNumber", "42")  # 土地证号
        tool.setObject(b, "propertyBaseinfoUnitId", "lyx-413")  # 产权单位
        tool.setObject(b, "basicsLandPurposeId", "工业用地")  # 土地用途
        tool.setObject(b, "basicsLandNatureId", "划拨")  # 土地性质
        tool.setObject(b, "basicsLandPropertyRegistrationId", "无产权未办证")  # 土地产权状况
        tool.setNumber(b,"landTotalArea",1) #土地总面积
        tool.setDict(b,"freezeIs","启用") #启用/停用

        tool.wait(1)
        b.find_element_by_xpath("//div[@class='fromMenuBox']/button/span[text()='保存']").click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('请输入土地证号未填写', addUnitMsg)
        tool.close(b)

    def test12(self):
        '''新增土地-产权单位未填写测试'''
        print("========【case_0011】新增土地-产权单位未填写测试 =============")
        b = tool.login("488235", "admin", "jx123456")
        tool.joinItem(b, "房屋土地信息", "土地基本信息", "土地信息维护")
        tool.wait(2)
        b.find_element_by_xpath('//button/span[text()="新增"]').click()

        tool.setObject(b, "orgId", "lyx-413") #管理单位
        tool.setText(b, "landName", "czy2")  #土地名称
        tool.setText(b, "landAssetCardCode", "002") #土地资产卡片编号
        tool.setObject(b, "basicsLandGeographicalClassificationId", "省内") #地域分类
        tool.setObject(b, "basicsHouseAdministrativeAreaId", "浙江省") #行政区域
        tool.setText(b, "address", "413-1") #坐落地址
        tool.setText(b, "landCertificateNumber", "42")  # 土地证号
        # tool.setObject(b, "propertyBaseinfoUnitId", "lyx-413")  # 产权单位
        tool.setObject(b, "basicsLandPurposeId", "工业用地")  # 土地用途
        tool.setObject(b, "basicsLandNatureId", "划拨")  # 土地性质
        tool.setObject(b, "basicsLandPropertyRegistrationId", "无产权未办证")  # 土地产权状况
        tool.setNumber(b,"landTotalArea",1) #土地总面积
        tool.setDict(b,"freezeIs","启用") #启用/停用

        tool.wait(1)
        b.find_element_by_xpath("//div[@class='fromMenuBox']/button/span[text()='保存']").click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('请输入产权单位未填写', addUnitMsg)
        tool.close(b)

    def test13(self):
        '''新增土地-土地用途未填写测试'''
        print("========【case_0011】新增土地-土地用途未填写测试 =============")
        b = tool.login("488235", "admin", "jx123456")
        tool.joinItem(b, "房屋土地信息", "土地基本信息", "土地信息维护")
        tool.wait(2)
        b.find_element_by_xpath('//button/span[text()="新增"]').click()

        tool.setObject(b, "orgId", "lyx-413") #管理单位
        tool.setText(b, "landName", "czy2")  #土地名称
        tool.setText(b, "landAssetCardCode", "002") #土地资产卡片编号
        tool.setObject(b, "basicsLandGeographicalClassificationId", "省内") #地域分类
        tool.setObject(b, "basicsHouseAdministrativeAreaId", "浙江省") #行政区域
        tool.setText(b, "address", "413-1") #坐落地址
        tool.setText(b, "landCertificateNumber", "42")  # 土地证号
        tool.setObject(b, "propertyBaseinfoUnitId", "lyx-413")  # 产权单位
        # tool.setObject(b, "basicsLandPurposeId", "工业用地")  # 土地用途
        tool.setObject(b, "basicsLandNatureId", "划拨")  # 土地性质
        tool.setObject(b, "basicsLandPropertyRegistrationId", "无产权未办证")  # 土地产权状况
        tool.setNumber(b,"landTotalArea",1) #土地总面积
        tool.setDict(b,"freezeIs","启用") #启用/停用

        tool.wait(1)
        b.find_element_by_xpath("//div[@class='fromMenuBox']/button/span[text()='保存']").click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('请输入土地用途未填写', addUnitMsg)
        tool.close(b)

    def test14(self):
        '''新增土地-土地性质未填写测试'''
        print("========【case_0014】新增土地-土地性质未填写测试 =============")
        b = tool.login("488235", "admin", "jx123456")
        tool.joinItem(b, "房屋土地信息", "土地基本信息", "土地信息维护")
        tool.wait(2)
        b.find_element_by_xpath('//button/span[text()="新增"]').click()

        tool.setObject(b, "orgId", "lyx-413") #管理单位
        tool.setText(b, "landName", "czy2")  #土地名称
        tool.setText(b, "landAssetCardCode", "002") #土地资产卡片编号
        tool.setObject(b, "basicsLandGeographicalClassificationId", "省内") #地域分类
        tool.setObject(b, "basicsHouseAdministrativeAreaId", "浙江省") #行政区域
        tool.setText(b, "address", "413-1") #坐落地址
        tool.setText(b, "landCertificateNumber", "42")  # 土地证号
        tool.setObject(b, "propertyBaseinfoUnitId", "lyx-413")  # 产权单位
        tool.setObject(b, "basicsLandPurposeId", "工业用地")  # 土地用途
        # tool.setObject(b, "basicsLandNatureId", "划拨")  # 土地性质
        tool.setObject(b, "basicsLandPropertyRegistrationId", "无产权未办证")  # 土地产权状况
        tool.setNumber(b,"landTotalArea",1) #土地总面积
        tool.setDict(b,"freezeIs","启用") #启用/停用

        tool.wait(1)
        b.find_element_by_xpath("//div[@class='fromMenuBox']/button/span[text()='保存']").click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('请输入土地性质未填写', addUnitMsg)
        tool.close(b)

    def test15(self):
        '''新增土地-土地产权状况未填写测试'''
        print("========【case_0015】新增土地-土地产权状况未填写测试 =============")
        b = tool.login("488235", "admin", "jx123456")
        tool.joinItem(b, "房屋土地信息", "土地基本信息", "土地信息维护")
        tool.wait(2)
        b.find_element_by_xpath('//button/span[text()="新增"]').click()

        tool.setObject(b, "orgId", "lyx-413") #管理单位
        tool.setText(b, "landName", "czy2")  #土地名称
        tool.setText(b, "landAssetCardCode", "002") #土地资产卡片编号
        tool.setObject(b, "basicsLandGeographicalClassificationId", "省内") #地域分类
        tool.setObject(b, "basicsHouseAdministrativeAreaId", "浙江省") #行政区域
        tool.setText(b, "address", "413-1") #坐落地址
        tool.setText(b, "landCertificateNumber", "42")  # 土地证号
        tool.setObject(b, "propertyBaseinfoUnitId", "lyx-413")  # 产权单位
        tool.setObject(b, "basicsLandPurposeId", "工业用地")  # 土地用途
        tool.setObject(b, "basicsLandNatureId", "划拨")  # 土地性质
        # tool.setObject(b, "basicsLandPropertyRegistrationId", "无产权未办证")  # 土地产权状况
        tool.setNumber(b,"landTotalArea",1) #土地总面积
        tool.setDict(b,"freezeIs","启用") #启用/停用

        tool.wait(1)
        b.find_element_by_xpath("//div[@class='fromMenuBox']/button/span[text()='保存']").click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('请输入土地产权状况未填写', addUnitMsg)
        tool.close(b)

    def test16(self):
        '''新增土地-土地总面积未填写测试'''
        print("========【case_0016】新增土地-土地总面积未填写测试 =============")
        b = tool.login("488235", "admin", "jx123456")
        tool.joinItem(b, "房屋土地信息", "土地基本信息", "土地信息维护")
        tool.wait(2)
        b.find_element_by_xpath('//button/span[text()="新增"]').click()

        tool.setObject(b, "orgId", "lyx-413") #管理单位
        tool.setText(b, "landName", "czy2")  #土地名称
        tool.setText(b, "landAssetCardCode", "002") #土地资产卡片编号
        tool.setObject(b, "basicsLandGeographicalClassificationId", "省内") #地域分类
        tool.setObject(b, "basicsHouseAdministrativeAreaId", "浙江省") #行政区域
        tool.setText(b, "address", "413-1") #坐落地址
        tool.setText(b, "landCertificateNumber", "42")  # 土地证号
        tool.setObject(b, "propertyBaseinfoUnitId", "lyx-413")  # 产权单位
        tool.setObject(b, "basicsLandPurposeId", "工业用地")  # 土地用途
        tool.setObject(b, "basicsLandNatureId", "划拨")  # 土地性质
        tool.setObject(b, "basicsLandPropertyRegistrationId", "无产权未办证")  # 土地产权状况
        # tool.setNumber(b,"landTotalArea",1) #土地总面积
        tool.setDict(b,"freezeIs","启用") #启用/停用

        tool.wait(1)
        b.find_element_by_xpath("//div[@class='fromMenuBox']/button/span[text()='保存']").click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('请输入土地总面积（㎡）未填写', addUnitMsg)
        tool.close(b)

    def test17(self):
        '''新增土地-启用\停用未填写测试'''
        print("========【case_0017】新增土地-启用\停用未填写测试 =============")
        b = tool.login("488235", "admin", "jx123456")
        tool.joinItem(b, "房屋土地信息", "土地基本信息", "土地信息维护")
        tool.wait(2)
        b.find_element_by_xpath('//button/span[text()="新增"]').click()

        tool.setObject(b, "orgId", "lyx-413") #管理单位
        tool.setText(b, "landName", "czy2")  #土地名称
        tool.setText(b, "landAssetCardCode", "002") #土地资产卡片编号
        tool.setObject(b, "basicsLandGeographicalClassificationId", "省内") #地域分类
        tool.setObject(b, "basicsHouseAdministrativeAreaId", "浙江省") #行政区域
        tool.setText(b, "address", "413-1") #坐落地址
        tool.setText(b, "landCertificateNumber", "42")  # 土地证号
        tool.setObject(b, "propertyBaseinfoUnitId", "lyx-413")  # 产权单位
        tool.setObject(b, "basicsLandPurposeId", "工业用地")  # 土地用途
        tool.setObject(b, "basicsLandNatureId", "划拨")  # 土地性质
        tool.setObject(b, "basicsLandPropertyRegistrationId", "无产权未办证")  # 土地产权状况
        tool.setNumber(b,"landTotalArea",1) #土地总面积
        # tool.setDict(b,"freezeIs","启用") #启用/停用

        tool.wait(1)
        b.find_element_by_xpath("//div[@class='fromMenuBox']/button/span[text()='保存']").click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('请输入启用\停用未填写', addUnitMsg)
        tool.close(b)



