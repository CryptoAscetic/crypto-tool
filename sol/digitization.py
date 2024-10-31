import json


def base58_decode(cipher_input: str) -> str:
    """
    base58编码典型应用是比特币钱包，与base64相比，去除了0、I、O、l、/ +等不易辨认的6个字符
    :param cipher_input: 输入base58编码值
    :return: base58的解码值
    @author hongfeiyinxue 2022-04-30-1651329023.0065577
    """
    #  定义base58的58个编码
    base58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    cipher = cipher_input
    #  检查密文字符的有效性，密文字符必须是base58中的字符，否则返回提示
    bad = ''
    for item in cipher:
        if base58.find(item) == -1:
            bad += item
    if bad != '':
        return '不是有效的Base58编码，请仔留意如下字符：' + bad

    #    获取密文每个字符在base58中的下标值
    tmp = []
    for item in cipher:
        tmp.append(base58.find(item))
    temp = tmp[0]
    for i in range(len(tmp) - 1):
        temp = temp * 58 + tmp[i + 1]
    temp = bin(temp).replace('0b', '')
    #    print('temp=', temp, '-len-', len(temp))

    #   判断temp二进制编码数量能否被8整除，例如编码长度为18，首先截取（18%8）余数个字符求对应的ascii字符
    remainder = len(temp) % 8
    plain_text = ''

    if remainder != 0:
        temp_start = temp[0:remainder]
        plain_text = chr(int(temp[0:remainder], 2))

    for i in range(remainder, len(temp), 8):
        #    print(chr(int((temp[i:i+8]), 2)))
        plain_text += chr(int((temp[i:i + 8]), 2))
        i += 8
    return plain_text


def base58_encode(string_input):
    """
    base58编码典型应用是比特币钱包，与base64相比，去除了0、I、O、l、/ +等不易辨认的6个字符
    base58的编码思路是反复除以58取余数直至为0，base64的编码原理是64进制，2的6次方刚好等于64
    :param string_input: 输入待编码的字符
    :return: base58的编码值
    """
    base58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    string = string_input
    string_binary = ''
    #   获取输入字符ascii码值的二进制码字符串，8个bit为一组
    for i in range(len(string)):
        string_binary = string_binary + str('{:0>8}'.format(bin(ord(string[i])).replace('0b', '')))
    string_decimal = int(string_binary, 2)
    string_58_list = []
    while True:
        string_58_list.insert(0, string_decimal % 58)
        string_decimal = string_decimal // 58
        if string_decimal == 0:
            break
    string_58 = ""
    for i in string_58_list:
        string_58 += base58[i]
    return string_58


print()

if __name__ == '__main__':

    response = ("{\"questionnaireId\":\"2f6e93d6-5b54-4b33-bb23-a6332cc462a9\",\"type\":\"\","
                "\"typeName\":\"中小企业数字化水平评测指标（2024年版）\",\"status\":1,\"versionNum\":\"2024\",\"storeList\":[{"
                "\"id\":\"6119e735-f386-4a38-854a-c5dabbcf986d\",\"questionTitle\":\"数字化基础\",\"titleType\":1,"
                "\"weight\":\"50\",\"children\":[{\"id\":\"37036e43-9576-41cc-a103-f206d705cae8\","
                "\"questionTitle\":\"设备系统\",\"titleType\":1,\"weight\":\"40\",\"children\":[{"
                "\"id\":\"0e8310e0-b8f2-4d8f-97f2-85adc146c180\",\"questionTitle\":\"网络建设\",\"titleType\":2,"
                "\"weight\":\"40\",\"children\":[{\"parentId\":\"0e8310e0-b8f2-4d8f-97f2-85adc146c180\","
                "\"id\":\"9e8c54eb-9848-4830-9d3f-8df530e47fdc\",\"weight\":\"100\",\"questionTitle\":\"企业网络建设连接情况\","
                "\"questionDescription\":\"\",\"questionType\":2,\"totalScore\":0,\"titleType\":3,"
                "\"calculateRule\":\"\",\"isTxt\":\"1\",\"isGl\":\"\",\"isDisabled\":false,\"sn\":\"\","
                "\"sceneType\":\"\",\"children\":[{\"id\":\"520e40ad-b27c-4191-89dd-71cd961a1ff1\","
                "\"questionId\":\"9e8c54eb-9848-4830-9d3f-8df530e47fdc\",\"titleType\":4,\"optionContent\":\"无\","
                "\"optionDescription\":\"\",\"weight\":\"0\",\"totalScore\":0,\"optionPrefix\":\"A\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0},"
                "{\"id\":\"94c34083-8d80-423b-9c70-0ba54976c2ea\","
                "\"questionId\":\"9e8c54eb-9848-4830-9d3f-8df530e47fdc\",\"titleType\":4,"
                "\"optionContent\":\"企业车间建成工控网络，支持自动化控制应用\",\"optionDescription\":\"\",\"weight\":\"25\","
                "\"totalScore\":0,\"optionPrefix\":\"B\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\","
                "\"score\":2},{\"id\":\"1d2517ef-0ae4-4ac8-8967-755ff64a35cb\","
                "\"questionId\":\"9e8c54eb-9848-4830-9d3f-8df530e47fdc\",\"titleType\":4,"
                "\"optionContent\":\"企业建成应用系统网络，实现大规模设备、人员与信息系统互联，可支持大规模设备、人员与信息系统互联\",\"optionDescription\":\"\","
                "\"weight\":\"25\",\"totalScore\":0,\"optionPrefix\":\"C\",\"gl\":\"\",\"isDisabled\":false,"
                "\"calculateRule\":\"\",\"score\":2},{\"id\":\"a5495c08-fa3b-4d13-b6d9-5190a25d343b\","
                "\"questionId\":\"9e8c54eb-9848-4830-9d3f-8df530e47fdc\",\"titleType\":4,"
                "\"optionContent\":\"企业建设/租用5G工业网络，支撑系统互联和网络协同应用，满足AGV、工业互联网等规模化移动应用场景需求\","
                "\"optionDescription\":\"\",\"weight\":\"25\",\"totalScore\":0,\"optionPrefix\":\"D\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":2},"
                "{\"id\":\"0d5805f3-db2d-4cbc-b7e7-c5710429eafc\","
                "\"questionId\":\"9e8c54eb-9848-4830-9d3f-8df530e47fdc\",\"titleType\":4,"
                "\"optionContent\":\"网络全面覆盖生产现场与环节，具备未来智能化新应用的扩展能力\",\"optionDescription\":\"\",\"weight\":\"25\","
                "\"totalScore\":0,\"optionPrefix\":\"E\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\","
                "\"score\":2}],\"formField\":[],\"score\":8}],\"parentId\":\"37036e43-9576-41cc-a103-f206d705cae8\","
                "\"score\":8,\"is\":2},{\"id\":\"a4f5b852-3381-4f92-83ac-c051c8362f77\",\"questionTitle\":\"设备数字化\","
                "\"titleType\":2,\"weight\":\"30\",\"children\":[{"
                "\"parentId\":\"a4f5b852-3381-4f92-83ac-c051c8362f77\","
                "\"id\":\"6d319e50-3d2d-460c-b355-f7e8c83f0d23\",\"weight\":\"100\","
                "\"questionTitle\":\"企业的生产设备数字化率\","
                "\"questionDescription\":\"设备数字化率：是指企业现有生产设备的数字化程度，即数字化生产设备占总生产设备数量的比例，其数值=数字化生产设备数量/总生产设备数量×100%\","
                "\"questionType\":1,\"totalScore\":0,\"titleType\":3,\"calculateRule\":\"\",\"isTxt\":\"1\","
                "\"isGl\":\"\",\"isDisabled\":false,\"sn\":\"\",\"sceneType\":\"\",\"children\":[{"
                "\"id\":\"36791ea1-f767-43a0-ad23-1612be5b31f0\","
                "\"questionId\":\"6d319e50-3d2d-460c-b355-f7e8c83f0d23\",\"titleType\":4,\"optionContent\":\"["
                "0-10%]\",\"optionDescription\":\"\",\"weight\":\"0\",\"totalScore\":0,\"optionPrefix\":\"A\","
                "\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0},"
                "{\"id\":\"70190183-558b-4d8a-9e5a-aacc469f64b2\","
                "\"questionId\":\"6d319e50-3d2d-460c-b355-f7e8c83f0d23\",\"titleType\":4,\"optionContent\":\"(10%,"
                "20%]\",\"optionDescription\":\"\",\"weight\":\"25\",\"totalScore\":0,\"optionPrefix\":\"B\","
                "\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":1.5},"
                "{\"id\":\"40e1eb2b-59e5-4940-b812-f37d789438d1\","
                "\"questionId\":\"6d319e50-3d2d-460c-b355-f7e8c83f0d23\",\"titleType\":4,\"optionContent\":\"(20%,"
                "40%] \",\"optionDescription\":\"\",\"weight\":\"50\",\"totalScore\":0,\"optionPrefix\":\"C\","
                "\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":3},"
                "{\"id\":\"332cbb39-019a-4b95-9895-ae966495af92\","
                "\"questionId\":\"6d319e50-3d2d-460c-b355-f7e8c83f0d23\",\"titleType\":4,\"optionContent\":\"(40%,"
                "60%] \",\"optionDescription\":\"\",\"weight\":\"75\",\"totalScore\":0,\"optionPrefix\":\"D\","
                "\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":4.5},"
                "{\"id\":\"59516c1d-69bf-4914-aa59-b6262c8b43b1\","
                "\"questionId\":\"6d319e50-3d2d-460c-b355-f7e8c83f0d23\",\"titleType\":4,\"optionContent\":\"(60%,"
                "100%]\",\"optionDescription\":\"\",\"weight\":\"100\",\"totalScore\":0,\"optionPrefix\":\"E\","
                "\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":6}],\"formField\":[{"
                "\"name\":\"具体数据\",\"value\":\"\"},{\"name\":\"其中生产设备数量为（台）\",\"value\":\"\"},"
                "{\"name\":\"实现数字化的生产设备数量为（台）\",\"value\":\"\"}],\"score\":6}],"
                "\"parentId\":\"37036e43-9576-41cc-a103-f206d705cae8\",\"score\":6,\"is\":2},"
                "{\"id\":\"e1859de9-dfab-49dd-b442-e4c1c98bb9f5\",\"questionTitle\":\"设备联网\",\"titleType\":2,"
                "\"weight\":\"30\",\"children\":[{\"parentId\":\"e1859de9-dfab-49dd-b442-e4c1c98bb9f5\","
                "\"id\":\"97a25f4e-2775-4ef0-8877-bb9c102af92a\",\"weight\":\"100\",\"questionTitle\":\"企业的生产设备联网率\","
                "\"questionDescription\":\"设备联网率：指联网设备占设备总数的比重，其数值=实现联网的生产设备数量/总生产设备数量×100%。\",\"questionType\":1,"
                "\"totalScore\":0,\"titleType\":3,\"calculateRule\":\"\",\"isTxt\":\"1\",\"isGl\":\"\","
                "\"isDisabled\":false,\"sn\":\"\",\"sceneType\":\"\",\"children\":[{"
                "\"id\":\"6bc7bea7-cef9-4082-b516-a733c70822d1\","
                "\"questionId\":\"97a25f4e-2775-4ef0-8877-bb9c102af92a\",\"titleType\":4,\"optionContent\":\"[0-10%] "
                "\",\"optionDescription\":\"\",\"weight\":\"0\",\"totalScore\":0,\"optionPrefix\":\"A\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0},"
                "{\"id\":\"8f09eb3f-6a1c-42ee-b28a-11c7790102cd\","
                "\"questionId\":\"97a25f4e-2775-4ef0-8877-bb9c102af92a\",\"titleType\":4,\"optionContent\":\"(10%,"
                "20%]\",\"optionDescription\":\"\",\"weight\":\"25\",\"totalScore\":0,\"optionPrefix\":\"B\","
                "\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":1.5},"
                "{\"id\":\"18e45546-11bc-4217-86e1-480cfc76aace\","
                "\"questionId\":\"97a25f4e-2775-4ef0-8877-bb9c102af92a\",\"titleType\":4,\"optionContent\":\"(20%,"
                "40%] \",\"optionDescription\":\"\",\"weight\":\"50\",\"totalScore\":0,\"optionPrefix\":\"C\","
                "\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":3},"
                "{\"id\":\"c37bce9e-4c8e-4460-b055-bbda27b70af4\","
                "\"questionId\":\"97a25f4e-2775-4ef0-8877-bb9c102af92a\",\"titleType\":4,\"optionContent\":\"(40%,"
                "60%] \",\"optionDescription\":\"\",\"weight\":\"75\",\"totalScore\":0,\"optionPrefix\":\"D\","
                "\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":4.5},"
                "{\"id\":\"061346a0-a212-4404-b93a-8b49e2c846ab\","
                "\"questionId\":\"97a25f4e-2775-4ef0-8877-bb9c102af92a\",\"titleType\":4,\"optionContent\":\"(60%,"
                "100%]\",\"optionDescription\":\"\",\"weight\":\"100\",\"totalScore\":0,\"optionPrefix\":\"E\","
                "\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":6}],\"formField\":[{"
                "\"name\":\"具体数据\",\"value\":\"\"},{\"name\":\"其中实现联网的生产设备数量为（台）\",\"value\":\"\"}],\"score\":6}],"
                "\"parentId\":\"37036e43-9576-41cc-a103-f206d705cae8\",\"score\":6,\"is\":2}],"
                "\"parentId\":\"6119e735-f386-4a38-854a-c5dabbcf986d\",\"is\":1,\"score\":20},"
                "{\"id\":\"8b9973dd-8b02-44eb-a98f-24e4992b2218\",\"questionTitle\":\"数据采集\",\"titleType\":1,"
                "\"weight\":\"20\",\"children\":[{\"id\":\"c142d261-9f0b-45b8-9c0b-d5bd4613ab05\","
                "\"questionTitle\":\"数据采集\",\"titleType\":2,\"weight\":\"100\",\"children\":[{"
                "\"parentId\":\"c142d261-9f0b-45b8-9c0b-d5bd4613ab05\","
                "\"id\":\"6f9a67a2-77d5-42a4-a21a-cb0cd892ae60\",\"weight\":\"100\","
                "\"questionTitle\":\"企业实现数据自动采集的业务环节覆盖范围\",\"questionDescription\":\"\",\"questionType\":2,"
                "\"totalScore\":0,\"titleType\":3,\"calculateRule\":\"\",\"isTxt\":\"1\",\"isGl\":\"\","
                "\"isDisabled\":false,\"sn\":\"\",\"sceneType\":\"\",\"children\":[{"
                "\"id\":\"c9b40982-1694-4816-b8ec-f3997cd4f39d\","
                "\"questionId\":\"6f9a67a2-77d5-42a4-a21a-cb0cd892ae60\",\"titleType\":4,\"optionContent\":\"无\","
                "\"optionDescription\":\"\",\"weight\":\"0\",\"totalScore\":0,\"optionPrefix\":\"A\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0},"
                "{\"id\":\"50be2480-6b7f-4e43-91cb-34d9ec5df848\","
                "\"questionId\":\"6f9a67a2-77d5-42a4-a21a-cb0cd892ae60\",\"titleType\":4,\"optionContent\":\"产品设计\","
                "\"optionDescription\":\"\",\"weight\":\"7\",\"totalScore\":0,\"optionPrefix\":\"B\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0.7000000000000001},"
                "{\"id\":\"c1c66d81-80cb-474e-8105-44289daf1375\","
                "\"questionId\":\"6f9a67a2-77d5-42a4-a21a-cb0cd892ae60\",\"titleType\":4,\"optionContent\":\"工艺设计\","
                "\"optionDescription\":\"\",\"weight\":\"7\",\"totalScore\":0,\"optionPrefix\":\"C\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0.7000000000000001},"
                "{\"id\":\"9a307c77-36ad-4fc4-a760-0043cdf0210b\","
                "\"questionId\":\"6f9a67a2-77d5-42a4-a21a-cb0cd892ae60\",\"titleType\":4,\"optionContent\":\"营销管理\","
                "\"optionDescription\":\"\",\"weight\":\"7\",\"totalScore\":0,\"optionPrefix\":\"D\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0.7000000000000001},"
                "{\"id\":\"736e4a46-7cdb-487f-8fc5-84fa230dc83e\","
                "\"questionId\":\"6f9a67a2-77d5-42a4-a21a-cb0cd892ae60\",\"titleType\":4,\"optionContent\":\"售后服务\","
                "\"optionDescription\":\"\",\"weight\":\"7\",\"totalScore\":0,\"optionPrefix\":\"E\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0.7000000000000001},"
                "{\"id\":\"71fcc99b-4fdc-4b15-81e6-04f7e6339d91\","
                "\"questionId\":\"6f9a67a2-77d5-42a4-a21a-cb0cd892ae60\",\"titleType\":4,\"optionContent\":\"计划排程\","
                "\"optionDescription\":\"\",\"weight\":\"7\",\"totalScore\":0,\"optionPrefix\":\"F\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0.7000000000000001},"
                "{\"id\":\"87abfafd-1694-43c4-aa68-c8b622732215\","
                "\"questionId\":\"6f9a67a2-77d5-42a4-a21a-cb0cd892ae60\",\"titleType\":4,\"optionContent\":\"生产管控\","
                "\"optionDescription\":\"\",\"weight\":\"7\",\"totalScore\":0,\"optionPrefix\":\"G\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0.7000000000000001},"
                "{\"id\":\"a78790ad-b1ea-4b75-a6a9-16ad8364ab33\","
                "\"questionId\":\"6f9a67a2-77d5-42a4-a21a-cb0cd892ae60\",\"titleType\":4,\"optionContent\":\"质量管理\","
                "\"optionDescription\":\"\",\"weight\":\"7\",\"totalScore\":0,\"optionPrefix\":\"H\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0.7000000000000001},"
                "{\"id\":\"b9086ea2-bfed-46ed-89ab-876787a18315\","
                "\"questionId\":\"6f9a67a2-77d5-42a4-a21a-cb0cd892ae60\",\"titleType\":4,\"optionContent\":\"设备管理\","
                "\"optionDescription\":\"\",\"weight\":\"7\",\"totalScore\":0,\"optionPrefix\":\"I\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0.7000000000000001},"
                "{\"id\":\"b68e53da-4ddc-4170-bf1f-3d9a5fb1bda7\","
                "\"questionId\":\"6f9a67a2-77d5-42a4-a21a-cb0cd892ae60\",\"titleType\":4,\"optionContent\":\"安全生产\","
                "\"optionDescription\":\"\",\"weight\":\"7\",\"totalScore\":0,\"optionPrefix\":\"J\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0.7000000000000001},"
                "{\"id\":\"f9152b12-d58d-410c-9c71-fec02066fe4d\","
                "\"questionId\":\"6f9a67a2-77d5-42a4-a21a-cb0cd892ae60\",\"titleType\":4,\"optionContent\":\"能耗管理\","
                "\"optionDescription\":\"\",\"weight\":\"7\",\"totalScore\":0,\"optionPrefix\":\"K\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0.7000000000000001},"
                "{\"id\":\"8d0187fb-a868-4289-bef7-d143df1a7e4d\","
                "\"questionId\":\"6f9a67a2-77d5-42a4-a21a-cb0cd892ae60\",\"titleType\":4,\"optionContent\":\"采购管理\","
                "\"optionDescription\":\"\",\"weight\":\"7\",\"totalScore\":0,\"optionPrefix\":\"L\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0.7000000000000001},"
                "{\"id\":\"cd23ce35-64c1-4020-b151-46629d6f0093\","
                "\"questionId\":\"6f9a67a2-77d5-42a4-a21a-cb0cd892ae60\",\"titleType\":4,\"optionContent\":\"仓储物流\","
                "\"optionDescription\":\"\",\"weight\":\"7\",\"totalScore\":0,\"optionPrefix\":\"M\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0.7000000000000001},"
                "{\"id\":\"7502f089-7fb1-42ca-8f50-dca926dc89db\","
                "\"questionId\":\"6f9a67a2-77d5-42a4-a21a-cb0cd892ae60\",\"titleType\":4,\"optionContent\":\"财务管理\","
                "\"optionDescription\":\"\",\"weight\":\"7\",\"totalScore\":0,\"optionPrefix\":\"N\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0.7000000000000001},"
                "{\"id\":\"b6ce89ce-d50b-4925-8356-a55de195854a\","
                "\"questionId\":\"6f9a67a2-77d5-42a4-a21a-cb0cd892ae60\",\"titleType\":4,\"optionContent\":\"人力资源\","
                "\"optionDescription\":\"\",\"weight\":\"9\",\"totalScore\":0,\"optionPrefix\":\"O\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0.8999999999999999}],\"formField\":[],"
                "\"score\":10}],\"parentId\":\"8b9973dd-8b02-44eb-a98f-24e4992b2218\",\"score\":10,\"is\":2}],"
                "\"parentId\":\"6119e735-f386-4a38-854a-c5dabbcf986d\",\"score\":10,\"is\":1},"
                "{\"id\":\"e152fc78-5ee2-4c09-891b-c2da4d207609\",\"questionTitle\":\"信息系统\",\"titleType\":1,"
                "\"weight\":\"20\",\"children\":[{\"id\":\"8e0805e1-e247-40d1-b533-775d60fd2f5f\","
                "\"questionTitle\":\"信息系统\",\"titleType\":2,\"weight\":\"100\",\"children\":[{"
                "\"parentId\":\"8e0805e1-e247-40d1-b533-775d60fd2f5f\","
                "\"id\":\"3f26d63f-4be6-4fb9-999f-3a86e46207b3\",\"weight\":\"100\","
                "\"questionTitle\":\"企业使用本地或云化部署的信息化服务，实现业务的数字化管理情况\",\"questionDescription\":\"\","
                "\"questionType\":1,\"totalScore\":0,\"titleType\":3,\"calculateRule\":\"\",\"isTxt\":\"1\","
                "\"isGl\":\"\",\"isDisabled\":false,\"sn\":\"\",\"sceneType\":\"\",\"children\":[{"
                "\"id\":\"e220e1cb-1c29-42a6-9c9d-e9e8c1507d50\","
                "\"questionId\":\"3f26d63f-4be6-4fb9-999f-3a86e46207b3\",\"titleType\":4,\"optionContent\":\"无\","
                "\"optionDescription\":\"\",\"weight\":\"0\",\"totalScore\":0,\"optionPrefix\":\"A\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0},"
                "{\"id\":\"d8d31c89-5efe-4203-ab1c-14a511bb55bf\","
                "\"questionId\":\"3f26d63f-4be6-4fb9-999f-3a86e46207b3\",\"titleType\":4,"
                "\"optionContent\":\"单个业务环节\",\"optionDescription\":\"\",\"weight\":\"25\",\"totalScore\":0,"
                "\"optionPrefix\":\"B\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":2.5},"
                "{\"id\":\"1cebca72-9909-40e0-ad86-496c417f5dcd\","
                "\"questionId\":\"3f26d63f-4be6-4fb9-999f-3a86e46207b3\",\"titleType\":4,"
                "\"optionContent\":\"多个业务环节（2个及以上）\",\"optionDescription\":\"\",\"weight\":\"50\",\"totalScore\":0,"
                "\"optionPrefix\":\"C\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":5},"
                "{\"id\":\"55c497bd-e174-4a44-a639-4bb2b6ed5234\","
                "\"questionId\":\"3f26d63f-4be6-4fb9-999f-3a86e46207b3\",\"titleType\":4,"
                "\"optionContent\":\"绝大部分业务环节（大于80%） \",\"optionDescription\":\"\",\"weight\":\"75\","
                "\"totalScore\":0,\"optionPrefix\":\"D\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\","
                "\"score\":7.5},{\"id\":\"52a2cd1c-c0a9-4e35-a3b0-b367ccb93c92\","
                "\"questionId\":\"3f26d63f-4be6-4fb9-999f-3a86e46207b3\",\"titleType\":4,\"optionContent\":\"全覆盖\","
                "\"optionDescription\":\"\",\"weight\":\"100\",\"totalScore\":0,\"optionPrefix\":\"E\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":10}],\"formField\":[],\"score\":10}],"
                "\"parentId\":\"e152fc78-5ee2-4c09-891b-c2da4d207609\",\"score\":10,\"is\":2}],"
                "\"parentId\":\"6119e735-f386-4a38-854a-c5dabbcf986d\",\"score\":10,\"is\":1},"
                "{\"id\":\"36e4733d-84d9-4f94-bec7-0fb6cfa0cd61\",\"questionTitle\":\"信息安全\",\"titleType\":1,"
                "\"weight\":\"20\",\"children\":[{\"id\":\"c1c51adc-9db0-4246-bc89-cda5b7e69292\","
                "\"questionTitle\":\"网络安全\",\"titleType\":2,\"weight\":\"50\",\"children\":[{"
                "\"parentId\":\"c1c51adc-9db0-4246-bc89-cda5b7e69292\","
                "\"id\":\"043f54e3-04b8-4369-bd66-befcd0f5f83e\",\"weight\":\"100\","
                "\"questionTitle\":\"企业在保障网络安全方面采取的举措\",\"questionDescription\":\"\",\"questionType\":2,"
                "\"totalScore\":0,\"titleType\":3,\"calculateRule\":\"\",\"isTxt\":\"1\",\"isGl\":\"\","
                "\"isDisabled\":false,\"sn\":\"\",\"sceneType\":\"\",\"children\":[{"
                "\"id\":\"69dc091a-27cf-4cd5-8c82-3ce047ce86c8\","
                "\"questionId\":\"043f54e3-04b8-4369-bd66-befcd0f5f83e\",\"titleType\":4,\"optionContent\":\"无\","
                "\"optionDescription\":\"\",\"weight\":\"0\",\"totalScore\":0,\"optionPrefix\":\"A\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0},"
                "{\"id\":\"b88bfb18-424e-403d-a46a-7d7e4190fe55\","
                "\"questionId\":\"043f54e3-04b8-4369-bd66-befcd0f5f83e\",\"titleType\":4,"
                "\"optionContent\":\"建立了网络安全管理制度\",\"optionDescription\":\"\",\"weight\":\"25\",\"totalScore\":0,"
                "\"optionPrefix\":\"B\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":1.25},"
                "{\"id\":\"030231ca-76a0-4e09-981d-88ad9529b4d2\","
                "\"questionId\":\"043f54e3-04b8-4369-bd66-befcd0f5f83e\",\"titleType\":4,"
                "\"optionContent\":\"使用了网络安全产品及服务（如防火墙、网络分区、入侵检测、身份认证等）\",\"optionDescription\":\"\","
                "\"weight\":\"25\",\"totalScore\":0,\"optionPrefix\":\"C\",\"gl\":\"\",\"isDisabled\":false,"
                "\"calculateRule\":\"\",\"score\":1.25},{\"id\":\"89f4ebe0-2169-4b15-ae73-a4f1ca1cfc7c\","
                "\"questionId\":\"043f54e3-04b8-4369-bd66-befcd0f5f83e\",\"titleType\":4,"
                "\"optionContent\":\"自行或委托专业评估机构实施网络安全风险评估\",\"optionDescription\":\"\",\"weight\":\"25\","
                "\"totalScore\":0,\"optionPrefix\":\"D\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\","
                "\"score\":1.25},{\"id\":\"3fa54a4c-925f-48f0-aae4-0b78eb5a4f18\","
                "\"questionId\":\"043f54e3-04b8-4369-bd66-befcd0f5f83e\",\"titleType\":4,"
                "\"optionContent\":\"建立网络边界安全访问控制能力，及网络关键节点入侵检测和恶意代码检测能力\",\"optionDescription\":\"\","
                "\"weight\":\"25\",\"totalScore\":0,\"optionPrefix\":\"E\",\"gl\":\"\",\"isDisabled\":false,"
                "\"calculateRule\":\"\",\"score\":1.25}],\"formField\":[],\"score\":5}],"
                "\"parentId\":\"36e4733d-84d9-4f94-bec7-0fb6cfa0cd61\",\"score\":5,\"is\":2},"
                "{\"id\":\"4effb0d5-5f3a-4a7c-a48f-e064c2fdb228\",\"questionTitle\":\"数据安全\",\"titleType\":2,"
                "\"weight\":\"50\",\"children\":[{\"parentId\":\"4effb0d5-5f3a-4a7c-a48f-e064c2fdb228\","
                "\"id\":\"f8a3ebc8-a318-4a18-9d09-02434bd17096\",\"weight\":\"100\","
                "\"questionTitle\":\"企业在保障数据安全方面采取的举措\",\"questionDescription\":\"\",\"questionType\":2,"
                "\"totalScore\":0,\"titleType\":3,\"calculateRule\":\"\",\"isTxt\":\"1\",\"isGl\":\"\","
                "\"isDisabled\":false,\"sn\":\"\",\"sceneType\":\"\",\"children\":[{"
                "\"id\":\"8086418a-6d11-407c-9f44-6dfd475e0a6f\","
                "\"questionId\":\"f8a3ebc8-a318-4a18-9d09-02434bd17096\",\"titleType\":4,\"optionContent\":\"无\","
                "\"optionDescription\":\"\",\"weight\":\"0\",\"totalScore\":0,\"optionPrefix\":\"A\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0},"
                "{\"id\":\"476c91d7-d158-4d32-be5e-a244b3dc2576\","
                "\"questionId\":\"f8a3ebc8-a318-4a18-9d09-02434bd17096\",\"titleType\":4,"
                "\"optionContent\":\"建立了数据安全管理制度\",\"optionDescription\":\"\",\"weight\":\"25\",\"totalScore\":0,"
                "\"optionPrefix\":\"B\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":1.25},"
                "{\"id\":\"cefa7ee9-d7af-42af-a4ce-e129dac9ddaf\","
                "\"questionId\":\"f8a3ebc8-a318-4a18-9d09-02434bd17096\",\"titleType\":4,"
                "\"optionContent\":\"使用了数据安全产品及服务（如数据加密、数据备份与恢复、数据脱敏、数据分级分类保护等）\",\"optionDescription\":\"\","
                "\"weight\":\"25\",\"totalScore\":0,\"optionPrefix\":\"C\",\"gl\":\"\",\"isDisabled\":false,"
                "\"calculateRule\":\"\",\"score\":1.25},{\"id\":\"29ccad78-2435-4392-9ea1-00733bf7e3a1\","
                "\"questionId\":\"f8a3ebc8-a318-4a18-9d09-02434bd17096\",\"titleType\":4,"
                "\"optionContent\":\"自行或委托专业评估机构实施数据安全风险评估\",\"optionDescription\":\"\",\"weight\":\"25\","
                "\"totalScore\":0,\"optionPrefix\":\"D\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\","
                "\"score\":1.25},{\"id\":\"191ca32b-2c69-43b2-a40f-5d8102cd9350\","
                "\"questionId\":\"f8a3ebc8-a318-4a18-9d09-02434bd17096\",\"titleType\":4,"
                "\"optionContent\":\"建立数据台账（类型、用途、数量、数据源单位、使用单位等），定期开展数据安全保障能力核验\",\"optionDescription\":\"\","
                "\"weight\":\"25\",\"totalScore\":0,\"optionPrefix\":\"E\",\"gl\":\"\",\"isDisabled\":false,"
                "\"calculateRule\":\"\",\"score\":1.25}],\"formField\":[],\"score\":5}],"
                "\"parentId\":\"36e4733d-84d9-4f94-bec7-0fb6cfa0cd61\",\"score\":5,\"is\":2}],"
                "\"parentId\":\"6119e735-f386-4a38-854a-c5dabbcf986d\",\"score\":10,\"is\":1}],\"is\":1,"
                "\"score\":50},{\"id\":\"a1d3532f-113d-4168-9944-a564551011b8\",\"questionTitle\":\"数字化管理\","
                "\"titleType\":1,\"weight\":\"30\",\"children\":[{\"id\":\"752c7137-3d88-4c92-934a-0feb10630cb6\","
                "\"questionTitle\":\"规划管理\",\"titleType\":1,\"weight\":\"50\",\"children\":[{"
                "\"id\":\"59f60cf1-9900-4da0-83e8-72916c4aa236\",\"questionTitle\":\"规划实施\",\"titleType\":2,"
                "\"weight\":\"50\",\"children\":[{\"parentId\":\"59f60cf1-9900-4da0-83e8-72916c4aa236\","
                "\"id\":\"9e0b56a3-39cd-4d0d-be80-f4b177f7e4ce\",\"weight\":\"100\","
                "\"questionTitle\":\"企业对数字化的认识与执行水平情况\",\"questionDescription\":\"\",\"questionType\":1,"
                "\"totalScore\":0,\"titleType\":3,\"calculateRule\":\"\",\"isTxt\":\"1\",\"isGl\":\"\","
                "\"isDisabled\":false,\"sn\":\"\",\"sceneType\":\"\",\"children\":[{"
                "\"id\":\"7dc33228-74ef-44b8-a202-7311d4607870\","
                "\"questionId\":\"9e0b56a3-39cd-4d0d-be80-f4b177f7e4ce\",\"titleType\":4,\"optionContent\":\"无\","
                "\"optionDescription\":\"\",\"weight\":\"0\",\"totalScore\":0,\"optionPrefix\":\"A\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0},"
                "{\"id\":\"0db229fa-ff47-43ef-9eb4-a427ebf9dce6\","
                "\"questionId\":\"9e0b56a3-39cd-4d0d-be80-f4b177f7e4ce\",\"titleType\":4,"
                "\"optionContent\":\"已经主动了解数字化相关内容\",\"optionDescription\":\"\",\"weight\":\"20\",\"totalScore\":0,"
                "\"optionPrefix\":\"B\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":1.5},"
                "{\"id\":\"4e27bc27-42db-4ad6-a8d5-6fa054cd0731\","
                "\"questionId\":\"9e0b56a3-39cd-4d0d-be80-f4b177f7e4ce\",\"titleType\":4,"
                "\"optionContent\":\"已经制定实施数字化的规划、计划及保障措施等\",\"optionDescription\":\"\",\"weight\":\"40\","
                "\"totalScore\":0,\"optionPrefix\":\"C\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\","
                "\"score\":3},{\"id\":\"522a1796-ca2b-464c-b478-6cd27546582c\","
                "\"questionId\":\"9e0b56a3-39cd-4d0d-be80-f4b177f7e4ce\",\"titleType\":4,"
                "\"optionContent\":\"已经着手开始进行单点或多点的数字化改造\",\"optionDescription\":\"\",\"weight\":\"60\","
                "\"totalScore\":0,\"optionPrefix\":\"D\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\","
                "\"score\":4.5},{\"id\":\"5435c6cd-85f7-4bee-a78c-05da922e00f4\","
                "\"questionId\":\"9e0b56a3-39cd-4d0d-be80-f4b177f7e4ce\",\"titleType\":4,"
                "\"optionContent\":\"已经通过数字化手段实现业务模式、管理决策方式的改变并取得成效\",\"optionDescription\":\"\",\"weight\":\"80\","
                "\"totalScore\":0,\"optionPrefix\":\"E\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\","
                "\"score\":6},{\"id\":\"9fe6310d-8adc-403c-bf87-cb2995ef92de\","
                "\"questionId\":\"9e0b56a3-39cd-4d0d-be80-f4b177f7e4ce\",\"titleType\":4,"
                "\"optionContent\":\"定期组织员工去数字化建设成效较好的同行业公司参观交流，增强数字化转型意识\",\"optionDescription\":\"\","
                "\"weight\":\"100\",\"totalScore\":0,\"optionPrefix\":\"F\",\"gl\":\"\",\"isDisabled\":false,"
                "\"calculateRule\":\"\",\"score\":7.5}],\"formField\":[],\"score\":7.5}],"
                "\"parentId\":\"752c7137-3d88-4c92-934a-0feb10630cb6\",\"score\":7.5,\"is\":2},"
                "{\"id\":\"efdbbb20-41d1-4f80-ad92-f7424b19324a\",\"questionTitle\":\"管理机制\",\"titleType\":2,"
                "\"weight\":\"50\",\"children\":[{\"parentId\":\"efdbbb20-41d1-4f80-ad92-f7424b19324a\","
                "\"id\":\"e19ec3cb-fd69-4abd-8b77-985e1d32ba3c\",\"weight\":\"100\","
                "\"questionTitle\":\"企业数字化管理制度的建立情况\",\"questionDescription\":\"\",\"questionType\":2,"
                "\"totalScore\":0,\"titleType\":3,\"calculateRule\":\"\",\"isTxt\":\"1\",\"isGl\":\"\","
                "\"isDisabled\":false,\"sn\":\"\",\"sceneType\":\"\",\"children\":[{"
                "\"id\":\"9243b2de-9e4a-4a21-b776-4fb977cf1475\","
                "\"questionId\":\"e19ec3cb-fd69-4abd-8b77-985e1d32ba3c\",\"titleType\":4,\"optionContent\":\"无\","
                "\"optionDescription\":\"\",\"weight\":\"0\",\"totalScore\":0,\"optionPrefix\":\"A\",\"gl\":\"\","
                "\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0},"
                "{\"id\":\"38e10d79-8649-4bca-bb52-e67860504841\","
                "\"questionId\":\"e19ec3cb-fd69-4abd-8b77-985e1d32ba3c\",\"titleType\":4,"
                "\"optionContent\":\"建立数字化转型实施工作流程\",\"optionDescription\":\"\",\"weight\":\"25\",\"totalScore\":0,"
                "\"optionPrefix\":\"B\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":1.875},"
                "{\"id\":\"66e285f1-e83f-42e4-aa30-da8736ffd4d9\","
                "\"questionId\":\"e19ec3cb-fd69-4abd-8b77-985e1d32ba3c\",\"titleType\":4,"
                "\"optionContent\":\"建立信息系统建设及运营管理制度\",\"optionDescription\":\"\",\"weight\":\"25\",\"totalScore\":0,"
                "\"optionPrefix\":\"C\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":1.875},"
                "{\"id\":\"6fd6c71d-8b52-433e-8d99-26d26ab82b75\","
                "\"questionId\":\"e19ec3cb-fd69-4abd-8b77-985e1d32ba3c\",\"titleType\":4,"
                "\"optionContent\":\"建立数据资源管理制度\",\"optionDescription\":\"\",\"weight\":\"25\",\"totalScore\":0,"
                "\"optionPrefix\":\"D\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":1.875},"
                "{\"id\":\"bfe38e27-36df-4954-800c-716843a7c9e7\","
                "\"questionId\":\"e19ec3cb-fd69-4abd-8b77-985e1d32ba3c\",\"titleType\":4,"
                "\"optionContent\":\"建立与数字化融合的科研、业务、产品等方面的创新激励制度\",\"optionDescription\":\"\",\"weight\":\"25\","
                "\"totalScore\":0,\"optionPrefix\":\"E\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\","
                "\"score\":1.875}],\"formField\":[],\"score\":7.5}],"
                "\"parentId\":\"752c7137-3d88-4c92-934a-0feb10630cb6\",\"score\":7.5,\"is\":2}],"
                "\"parentId\":\"a1d3532f-113d-4168-9944-a564551011b8\",\"score\":15,\"is\":1},"
                "{\"id\":\"75d956e8-e7e0-4ae3-801e-42ae4356444c\",\"questionTitle\":\"要素保障\",\"titleType\":1,"
                "\"weight\":\"50\",\"children\":[{\"id\":\"17a926b6-9f5a-4f4c-9118-49d311829a17\","
                "\"questionTitle\":\"人才建设\",\"titleType\":2,\"weight\":\"50\",\"children\":[{"
                "\"parentId\":\"17a926b6-9f5a-4f4c-9118-49d311829a17\","
                "\"id\":\"d95201c7-50fc-4c1f-b724-c70c4d163424\",\"weight\":\"100\","
                "\"questionTitle\":\"企业在数字化人才建设方面采取的举措\",\"questionDescription\":\"数字化人才：是指具备ICT("
                "信息通信技术)专业技能和补充技能的人才，他们在企业内部的各个岗位上发挥作用，包括传统信息技术部门的技术人员、业务部门中精通信息系统并熟练操作的专业人员，以及在数字化转型中新兴的横跨各种组织职能的角色。数字化人才通常划分三个层级：其一是数字化技术人才，掌握计算机、大数据、人工智能、通信等相关的数字化技术；其二是数字化管理人才，从战略上落地实施数字化战术，深谙商业价值、经营理念；其三是数字化应用人才，以企业核心资产的价值推动业务数字化应用能力增长，具有优化重构业务增长的分析能力。\",\"questionType\":2,\"totalScore\":0,\"titleType\":3,\"calculateRule\":\"\",\"isTxt\":\"1\",\"isGl\":\"\",\"isDisabled\":false,\"sn\":\"\",\"sceneType\":\"\",\"children\":[{\"id\":\"25a5b00a-c8c9-4911-8337-597dd5a65a25\",\"questionId\":\"d95201c7-50fc-4c1f-b724-c70c4d163424\",\"titleType\":4,\"optionContent\":\"无 \",\"optionDescription\":\"\",\"weight\":\"0\",\"totalScore\":0,\"optionPrefix\":\"A\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0},{\"id\":\"01c0c1ba-ab61-4b92-a2f7-d4395ecff323\",\"questionId\":\"d95201c7-50fc-4c1f-b724-c70c4d163424\",\"titleType\":4,\"optionContent\":\"配备专职/兼职的数字化人才\",\"optionDescription\":\"\",\"weight\":\"20\",\"totalScore\":0,\"optionPrefix\":\"B\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":1.5},{\"id\":\"a112ad78-ea57-46f9-a55b-23fe81c6a028\",\"questionId\":\"d95201c7-50fc-4c1f-b724-c70c4d163424\",\"titleType\":4,\"optionContent\":\"设置专门的数字化岗位/部门\",\"optionDescription\":\"\",\"weight\":\"20\",\"totalScore\":0,\"optionPrefix\":\"C\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":1.5},{\"id\":\"a165fe94-9d2c-4290-be47-1ed383a3f5fd\",\"questionId\":\"d95201c7-50fc-4c1f-b724-c70c4d163424\",\"titleType\":4,\"optionContent\":\"定期对员工开展数字化方面培训 \",\"optionDescription\":\"\",\"weight\":\"20\",\"totalScore\":0,\"optionPrefix\":\"D\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":1.5},{\"id\":\"053e39aa-53cf-44a5-aed0-1f7ee2977018\",\"questionId\":\"d95201c7-50fc-4c1f-b724-c70c4d163424\",\"titleType\":4,\"optionContent\":\"有明确的数字化人才绩效及薪酬管理\",\"optionDescription\":\"\",\"weight\":\"20\",\"totalScore\":0,\"optionPrefix\":\"E\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":1.5},{\"id\":\"39d57e8c-0d23-4c8c-8c23-e81bd8117bb6\",\"questionId\":\"d95201c7-50fc-4c1f-b724-c70c4d163424\",\"titleType\":4,\"optionContent\":\"有明确的数字化人才梯度培育机制\",\"optionDescription\":\"\",\"weight\":\"20\",\"totalScore\":0,\"optionPrefix\":\"F\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":1.5}],\"formField\":[],\"score\":7.5}],\"parentId\":\"75d956e8-e7e0-4ae3-801e-42ae4356444c\",\"score\":7.5,\"is\":2},{\"id\":\"846a1bf1-19cc-4f2f-9af3-6c7e700355b6\",\"questionTitle\":\"资金保障\",\"titleType\":2,\"weight\":\"50\",\"children\":[{\"parentId\":\"846a1bf1-19cc-4f2f-9af3-6c7e700355b6\",\"id\":\"c26a8b0e-ad89-41cd-90ae-1884ee9efa1b\",\"weight\":\"100\",\"questionTitle\":\"企业近三年平均数字化投入总额占营业额的平均比例（企业成立不满三年按照实际成立时长计算年均投入）\",\"questionDescription\":\"\",\"questionType\":1,\"totalScore\":0,\"titleType\":3,\"calculateRule\":\"\",\"isTxt\":\"1\",\"isGl\":\"\",\"isDisabled\":false,\"sn\":\"\",\"sceneType\":\"\",\"children\":[{\"id\":\"dcb87eed-e03a-4484-abcc-82cae2cd9930\",\"questionId\":\"c26a8b0e-ad89-41cd-90ae-1884ee9efa1b\",\"titleType\":4,\"optionContent\":\"[0-10%]\",\"optionDescription\":\"\",\"weight\":\"0\",\"totalScore\":0,\"optionPrefix\":\"A\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0},{\"id\":\"243f3e7b-6b74-422d-a181-d026f2f95574\",\"questionId\":\"c26a8b0e-ad89-41cd-90ae-1884ee9efa1b\",\"titleType\":4,\"optionContent\":\"(10%,20%]\",\"optionDescription\":\"\",\"weight\":\"25\",\"totalScore\":0,\"optionPrefix\":\"B\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":1.875},{\"id\":\"84228f5e-731d-422a-8367-0875dae566d2\",\"questionId\":\"c26a8b0e-ad89-41cd-90ae-1884ee9efa1b\",\"titleType\":4,\"optionContent\":\"(20%,40%]\",\"optionDescription\":\"\",\"weight\":\"50\",\"totalScore\":0,\"optionPrefix\":\"C\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":3.75},{\"id\":\"efefcaed-14fc-4be8-a407-2ff49996381e\",\"questionId\":\"c26a8b0e-ad89-41cd-90ae-1884ee9efa1b\",\"titleType\":4,\"optionContent\":\"(40%,60%]\",\"optionDescription\":\"\",\"weight\":\"75\",\"totalScore\":0,\"optionPrefix\":\"D\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":5.625},{\"id\":\"ba3de732-cc68-4110-a356-5b0906251178\",\"questionId\":\"c26a8b0e-ad89-41cd-90ae-1884ee9efa1b\",\"titleType\":4,\"optionContent\":\"(60%,100%]\",\"optionDescription\":\"\",\"weight\":\"100\",\"totalScore\":0,\"optionPrefix\":\"E\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":7.5}],\"formField\":[{\"name\":\"具体数据为（万元/年）\",\"value\":\"\"}],\"score\":7.5}],\"parentId\":\"75d956e8-e7e0-4ae3-801e-42ae4356444c\",\"score\":7.5,\"is\":2}],\"parentId\":\"a1d3532f-113d-4168-9944-a564551011b8\",\"score\":15,\"is\":1}],\"score\":30,\"is\":1},{\"id\":\"1ce35d2c-7ada-452f-b07f-8bca03ab398e\",\"questionTitle\":\"数字化成效\",\"titleType\":1,\"weight\":\"20\",\"children\":[{\"id\":\"40614433-a74b-47c4-bdea-532238ca9a57\",\"questionTitle\":\"绿色低碳\",\"titleType\":1,\"weight\":\"35\",\"children\":[{\"id\":\"1707161b-6a11-4e21-8843-10d287c985dd\",\"questionTitle\":\"绿色低碳\",\"titleType\":2,\"weight\":\"100\",\"children\":[{\"parentId\":\"1707161b-6a11-4e21-8843-10d287c985dd\",\"id\":\"846134f9-2e99-48e4-af12-94fa7643c939\",\"weight\":\"100\",\"questionTitle\":\"企业数字化改造后每百元营业收入中综合能源消费量相比于改造前的变化情况 \",\"questionDescription\":\"综合能源消费量：指企业（单位）在报告期内工业生产实际消费的各种能源(扣除能源加工转换产出和能源回收利用等重复因素)的总和。计算方法参考国家统计局制定的《能源报表统计制度》中的《能源购进、消费与库存》(205-1表)和《能源加工转换与回收利用》(205-2表)。\",\"questionType\":1,\"totalScore\":0,\"titleType\":3,\"calculateRule\":\"\",\"isTxt\":\"1\",\"isGl\":\"\",\"isDisabled\":false,\"sn\":\"\",\"sceneType\":\"\",\"children\":[{\"id\":\"3e073fd4-1bcc-4dd6-952c-21fa3e8cb8be\",\"questionId\":\"846134f9-2e99-48e4-af12-94fa7643c939\",\"titleType\":4,\"optionContent\":\"增加\",\"optionDescription\":\"\",\"weight\":\"0\",\"totalScore\":0,\"optionPrefix\":\"A\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0},{\"id\":\"bae0018d-4675-4390-8d90-8f461535c34e\",\"questionId\":\"846134f9-2e99-48e4-af12-94fa7643c939\",\"titleType\":4,\"optionContent\":\"持平\",\"optionDescription\":\"\",\"weight\":\"50\",\"totalScore\":0,\"optionPrefix\":\"B\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":3.5},{\"id\":\"6f82d0ca-02bf-4a60-91e0-ec571bccab1a\",\"questionId\":\"846134f9-2e99-48e4-af12-94fa7643c939\",\"titleType\":4,\"optionContent\":\"降低\",\"optionDescription\":\"\",\"weight\":\"100\",\"totalScore\":0,\"optionPrefix\":\"C\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":7}],\"formField\":[{\"name\":\"企业上年综合能源消费量为（吨标准煤）\",\"value\":\"\"},{\"name\":\"前年数据为（吨标准煤）\",\"value\":\"\"}],\"score\":7}],\"parentId\":\"40614433-a74b-47c4-bdea-532238ca9a57\",\"score\":7,\"is\":2}],\"parentId\":\"1ce35d2c-7ada-452f-b07f-8bca03ab398e\",\"score\":7,\"is\":1},{\"id\":\"70353531-e872-42b7-a0b3-bb62aba898b8\",\"questionTitle\":\"产品质量\",\"titleType\":1,\"weight\":\"35\",\"children\":[{\"id\":\"ca846a7f-da07-4399-aa9d-deea3cb16c2e\",\"questionTitle\":\"产品质量\",\"titleType\":2,\"weight\":\"100\",\"children\":[{\"parentId\":\"ca846a7f-da07-4399-aa9d-deea3cb16c2e\",\"id\":\"744fbe05-3bab-4161-ad9d-f231c6bf99e0\",\"weight\":\"100\",\"questionTitle\":\"企业数字化改造后月均产品合格率相比于改造前的变化情况\",\"questionDescription\":\"\",\"questionType\":1,\"totalScore\":0,\"titleType\":3,\"calculateRule\":\"\",\"isTxt\":\"1\",\"isGl\":\"\",\"isDisabled\":false,\"sn\":\"\",\"sceneType\":\"\",\"children\":[{\"id\":\"1dbe9228-e398-4829-a96d-f84f90d63e3e\",\"questionId\":\"744fbe05-3bab-4161-ad9d-f231c6bf99e0\",\"titleType\":4,\"optionContent\":\"降低\",\"optionDescription\":\"\",\"weight\":\"0\",\"totalScore\":0,\"optionPrefix\":\"A\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0},{\"id\":\"9381c429-a87a-47a9-8e49-dc91d66c5fe4\",\"questionId\":\"744fbe05-3bab-4161-ad9d-f231c6bf99e0\",\"titleType\":4,\"optionContent\":\"持平\",\"optionDescription\":\"\",\"weight\":\"50\",\"totalScore\":0,\"optionPrefix\":\"B\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":3.5},{\"id\":\"596c1be8-3666-4143-a282-9b8d7bde72a9\",\"questionId\":\"744fbe05-3bab-4161-ad9d-f231c6bf99e0\",\"titleType\":4,\"optionContent\":\"增加\",\"optionDescription\":\"\",\"weight\":\"100\",\"totalScore\":0,\"optionPrefix\":\"C\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":7}],\"formField\":[{\"name\":\"具体数值为\",\"value\":\"\"}],\"score\":7}],\"parentId\":\"70353531-e872-42b7-a0b3-bb62aba898b8\",\"score\":7,\"is\":2}],\"parentId\":\"1ce35d2c-7ada-452f-b07f-8bca03ab398e\",\"score\":7,\"is\":1},{\"id\":\"a9fc540b-bc3c-4ebf-83bf-815f187e9a4c\",\"questionTitle\":\"市场效益\",\"titleType\":1,\"weight\":\"30\",\"children\":[{\"id\":\"4b803ccb-fe07-43f8-9b9d-8c8f2140fde9\",\"questionTitle\":\"市场表现\",\"titleType\":2,\"weight\":\"50\",\"children\":[{\"parentId\":\"4b803ccb-fe07-43f8-9b9d-8c8f2140fde9\",\"id\":\"5e52a1be-c1cf-4e10-837a-9e42867b50a9\",\"weight\":\"100\",\"questionTitle\":\"企业上年度人均营业收入相比于前年变化情况\",\"questionDescription\":\"\",\"questionType\":1,\"totalScore\":0,\"titleType\":3,\"calculateRule\":\"\",\"isTxt\":\"1\",\"isGl\":\"\",\"isDisabled\":false,\"sn\":\"\",\"sceneType\":\"\",\"children\":[{\"id\":\"6a0db1bd-cb1d-4a4c-80b2-2511547d5560\",\"questionId\":\"5e52a1be-c1cf-4e10-837a-9e42867b50a9\",\"titleType\":4,\"optionContent\":\"降低\",\"optionDescription\":\"\",\"weight\":\"0\",\"totalScore\":0,\"optionPrefix\":\"A\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0},{\"id\":\"ae444c5f-e6b8-4214-807e-cdb868d1e779\",\"questionId\":\"5e52a1be-c1cf-4e10-837a-9e42867b50a9\",\"titleType\":4,\"optionContent\":\"持平\",\"optionDescription\":\"\",\"weight\":\"50\",\"totalScore\":0,\"optionPrefix\":\"B\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":1.5},{\"id\":\"4800a724-4587-4dbc-bf54-bf482fe047cb\",\"questionId\":\"5e52a1be-c1cf-4e10-837a-9e42867b50a9\",\"titleType\":4,\"optionContent\":\"增加\",\"optionDescription\":\"\",\"weight\":\"100\",\"totalScore\":0,\"optionPrefix\":\"C\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":3}],\"formField\":[{\"name\":\"企业上年员工人数为（人）\",\"value\":\"\"},{\"name\":\"营业收入为（万元）\",\"value\":\"\"},{\"name\":\"前年员工人数为（人）\",\"value\":\"\"},{\"name\":\"营业收入为（万元）\",\"value\":\"\"}],\"score\":3}],\"parentId\":\"a9fc540b-bc3c-4ebf-83bf-815f187e9a4c\",\"score\":3,\"is\":2},{\"id\":\"55d5e355-f649-4929-8b91-cfbe6a991404\",\"questionTitle\":\"价值效益\",\"titleType\":2,\"weight\":\"50\",\"children\":[{\"parentId\":\"55d5e355-f649-4929-8b91-cfbe6a991404\",\"id\":\"9a0c3c0e-5eb9-4323-875a-ce8cb89e196b\",\"weight\":\"100\",\"questionTitle\":\"企业上年度每百元营业收入中的成本相比于前年变化情况\",\"questionDescription\":\"\",\"questionType\":1,\"totalScore\":0,\"titleType\":3,\"calculateRule\":\"\",\"isTxt\":\"1\",\"isGl\":\"\",\"isDisabled\":false,\"sn\":\"\",\"sceneType\":\"\",\"children\":[{\"id\":\"a63733b4-60be-4b5c-9c96-fa55e10c4b46\",\"questionId\":\"9a0c3c0e-5eb9-4323-875a-ce8cb89e196b\",\"titleType\":4,\"optionContent\":\"增加\",\"optionDescription\":\"\",\"weight\":\"0\",\"totalScore\":0,\"optionPrefix\":\"A\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":0},{\"id\":\"058ac988-c5be-4261-8ebc-188531e75cde\",\"questionId\":\"9a0c3c0e-5eb9-4323-875a-ce8cb89e196b\",\"titleType\":4,\"optionContent\":\"持平\",\"optionDescription\":\"\",\"weight\":\"50\",\"totalScore\":0,\"optionPrefix\":\"B\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":1.5},{\"id\":\"6297653a-6c29-4b1e-b8f1-7d2df52a3beb\",\"questionId\":\"9a0c3c0e-5eb9-4323-875a-ce8cb89e196b\",\"titleType\":4,\"optionContent\":\"降低\",\"optionDescription\":\"\",\"weight\":\"100\",\"totalScore\":0,\"optionPrefix\":\"C\",\"gl\":\"\",\"isDisabled\":false,\"calculateRule\":\"\",\"score\":3}],\"formField\":[{\"name\":\"企业上年成本为（万元）\",\"value\":\"\"},{\"name\":\"前年成本为（万元）\",\"value\":\"\"}],\"score\":3}],\"parentId\":\"a9fc540b-bc3c-4ebf-83bf-815f187e9a4c\",\"score\":3,\"is\":2}],\"parentId\":\"1ce35d2c-7ada-452f-b07f-8bca03ab398e\",\"score\":6,\"is\":1}],\"score\":20,\"is\":1}],\"sceneStoreList\":[{\"titleType\":1,\"sceneType\":2,\"questionTitle\":\"产品生命周期数字化\",\"levelNumber\":\"\",\"children\":[{\"titleType\":1,\"sceneType\":1,\"questionTitle\":\"产品设计\",\"levelNumber\":\"\",\"children\":[{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"通过设计软件工具（如CAD、CAE、EDA等）辅助开展产品设计。\",\"levelNumber\":\"1\",\"children\":[],\"parentId\":\"b8448d72-4273-42f7-98b0-6d4d1ba1f7a7\",\"id\":\"8aa8d987-b15d-4ab7-bbd1-7a9a74b25b7d\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用信息化系统开展产品设计，实现产品设计过程或版本的数字化、规范化管理，形成完整的产品设计资料（如方案、图纸、模型、设计BOM、版本、技术变更等）管理标准，并有效执行。\",\"levelNumber\":\"2\",\"children\":[],\"parentId\":\"b8448d72-4273-42f7-98b0-6d4d1ba1f7a7\",\"id\":\"4d56d414-4cb7-4b4f-aa2a-e2c7c8d79d57\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"建立典型产品组件及关键零部件的标准库及典型产品设计知识库，并能在产品设计时进行匹配、引用或参考，实现产品设计与工艺设计的协同，实现数据跨部门共享。\",\"levelNumber\":\"3\",\"children\":[],\"parentId\":\"b8448d72-4273-42f7-98b0-6d4d1ba1f7a7\",\"id\":\"525da3d8-5b71-4641-9fe0-b3a3c60af547\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"运用仿真分析等技术实现对产品外观、结构、性能等进行试验验证或迭代优化等功能，并实现产业链上下游间的多方信息交互、协同设计或产品创新。\",\"levelNumber\":\"4\",\"children\":[],\"parentId\":\"b8448d72-4273-42f7-98b0-6d4d1ba1f7a7\",\"id\":\"1b2208aa-2b14-4c21-a271-19ac98a29f4c\"}],\"parentId\":\"6720cc80-6c4d-4a89-8e0b-7433515cd90e\",\"id\":\"b8448d72-4273-42f7-98b0-6d4d1ba1f7a7\",\"is\":1},{\"titleType\":1,\"sceneType\":2,\"questionTitle\":\"工艺设计\",\"levelNumber\":\"\",\"children\":[{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用设计软件工具（如CAM、CAPP等）基于产品设计数据辅助开展工艺设计。\",\"levelNumber\":\"1\",\"children\":[],\"parentId\":\"bf595fdb-5c37-4484-9fc0-5eb1cc7bb22f\",\"id\":\"c4bda1aa-ab08-4adc-9efc-2aa40c585816\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用信息化系统开展工艺设计，并实现设计过程的数字化、规范化管理，形成完整的工艺设计数据（工艺方案、工艺流程、工艺文件、制造BOM、版本、技术变更等）管理标准，并有效执行。\",\"levelNumber\":\"2\",\"children\":[],\"parentId\":\"bf595fdb-5c37-4484-9fc0-5eb1cc7bb22f\",\"id\":\"a1d2e4c1-5ae1-4e38-90df-e384fc54a250\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"建立典型制造工艺流程、参数、资源等关键要素的知识库，并能在新产品工艺设计时进行匹配、引用或参考；实现工艺设计与生产系统间的数据交互、并行协同。\",\"levelNumber\":\"3\",\"children\":[],\"parentId\":\"bf595fdb-5c37-4484-9fc0-5eb1cc7bb22f\",\"id\":\"55ad40fb-9c5b-4d56-9347-b48b9341cf68\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"建立数据模型，基于质量、成本等数据运用三维仿真等技术实现对于工艺设计的模拟仿真、迭代优化。\",\"levelNumber\":\"4\",\"children\":[],\"parentId\":\"bf595fdb-5c37-4484-9fc0-5eb1cc7bb22f\",\"id\":\"8f5c106a-7438-4f17-9a1d-73ad23f3dd92\"}],\"parentId\":\"6720cc80-6c4d-4a89-8e0b-7433515cd90e\",\"id\":\"bf595fdb-5c37-4484-9fc0-5eb1cc7bb22f\",\"is\":1},{\"titleType\":1,\"sceneType\":1,\"questionTitle\":\"营销管理\",\"levelNumber\":\"\",\"children\":[{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"借助信息技术工具（如电子表格、云存储等）对销售信息（如销售计划、销售订单、销售运行、客户信息或销售业绩等）进行辅助记录和管理。\",\"levelNumber\":\"1\",\"children\":[],\"parentId\":\"28081ee7-f30f-49da-972c-809dd364ab12\",\"id\":\"00e69f13-c2b5-477d-a6d8-4555abf5d2af\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"使用信息化系统对营销信息（如销售计划、销售订单、销售运行、客户信息或销售业绩等）进行规范化管理。\",\"levelNumber\":\"2\",\"children\":[],\"parentId\":\"28081ee7-f30f-49da-972c-809dd364ab12\",\"id\":\"be40a560-4ee9-485e-b59a-bb497c7115b5\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"基于销售信息化系统实现对营销信息（如销售计划、销售订单、销售运行、客户信息或销售业绩等）的实时管控，实现销售信息化系统与生产、库存、财务等系统的数字化协同。\",\"levelNumber\":\"3\",\"children\":[],\"parentId\":\"28081ee7-f30f-49da-972c-809dd364ab12\",\"id\":\"a8877ba8-a7ad-4957-b79b-ae49b95d2faf\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"使用人工智能等前沿技术，实现销售、财务、生产、供应链之间的数字化协同，实现实时销售预测，并自动或半自动制定采购、生产、物流等计划或方案，不断提升柔性化制造水平。\",\"levelNumber\":\"4\",\"children\":[],\"parentId\":\"28081ee7-f30f-49da-972c-809dd364ab12\",\"id\":\"124b4b80-7f48-4245-8ea5-23c3f585fec3\"}],\"parentId\":\"6720cc80-6c4d-4a89-8e0b-7433515cd90e\",\"id\":\"28081ee7-f30f-49da-972c-809dd364ab12\",\"is\":1},{\"titleType\":1,\"sceneType\":2,\"questionTitle\":\"售后服务\",\"levelNumber\":\"\",\"children\":[{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"运用信息技术工具（如小程序、APP等）对售后服务流程进行辅助管理。\",\"levelNumber\":\"1\",\"children\":[],\"parentId\":\"cf5d2027-c501-466e-889f-816b3c10993a\",\"id\":\"f8ec2fea-4b1a-44d7-83c0-6ee68f4fc7d5\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"运用信息化系统实现售后服务流程的数字化、规范化管理，并与设计、工艺、生产、销售部门进行信息共享。\",\"levelNumber\":\"2\",\"children\":[],\"parentId\":\"cf5d2027-c501-466e-889f-816b3c10993a\",\"id\":\"27084b15-e0aa-47e5-aa4c-b8edd2bdf71b\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"建立售后问题清单，实现售后问题的快速响应，并能够指导产品设计、工艺优化，实现售后服务与财务、质量等的系统的数字化协同（如供应商索赔、本厂质量考核账务处理等）。\",\"levelNumber\":\"3\",\"children\":[],\"parentId\":\"cf5d2027-c501-466e-889f-816b3c10993a\",\"id\":\"974ed3c2-d8b5-4136-b02f-bde3c7955174\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"基于信息系统实现面向客户的精细化管理（如远程运维、主动式客户服务等内容）； 或建立客户服务数据模型，实现满足客户需求的精准服务。\",\"levelNumber\":\"4\",\"children\":[],\"parentId\":\"cf5d2027-c501-466e-889f-816b3c10993a\",\"id\":\"8c169f76-0538-4162-bf7b-8acd6178177c\"}],\"parentId\":\"6720cc80-6c4d-4a89-8e0b-7433515cd90e\",\"id\":\"cf5d2027-c501-466e-889f-816b3c10993a\",\"is\":1}],\"id\":\"6720cc80-6c4d-4a89-8e0b-7433515cd90e\",\"is\":1},{\"titleType\":1,\"sceneType\":2,\"questionTitle\":\"生产执行数字化\",\"levelNumber\":\"\",\"children\":[{\"titleType\":1,\"sceneType\":2,\"questionTitle\":\"计划排程\",\"levelNumber\":\"\",\"children\":[{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用信息技术工具（如电子表格、云存储等）辅助人工编制生产计划。\",\"levelNumber\":\"1\",\"children\":[],\"parentId\":\"a00ca3b0-f7f5-495b-8ff5-294adf24bd22\",\"id\":\"48dc9964-a1b0-4bea-9a5c-a9453068c215\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用信息化系统辅助生成生产计划，基于生产计划进行生产准备检查（如物料、设备等），实现规范化管理。\",\"levelNumber\":\"2\",\"children\":[],\"parentId\":\"a00ca3b0-f7f5-495b-8ff5-294adf24bd22\",\"id\":\"2d7a2873-a40d-4113-99b7-601a10c46faa\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用信息化系统实现基于物料安全库存、销售订单、采购提前期、生产交期等多约束条件自动生成生产计划，并实现生产计划的下达与执行。\",\"levelNumber\":\"3\",\"children\":[],\"parentId\":\"a00ca3b0-f7f5-495b-8ff5-294adf24bd22\",\"id\":\"5ee7f6a7-17eb-402d-bc8b-50a431864adc\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"运用人工智能等前沿技术，建立生产排产与调度算法模型，实现自动给出满足多种约束条件的优化排产方案，形成优化的详细生产作业计划，生产情况实时监测，提前处理生产过程中的波动和风险，实现动态实时的生产排产和调度。\",\"levelNumber\":\"4\",\"children\":[],\"parentId\":\"a00ca3b0-f7f5-495b-8ff5-294adf24bd22\",\"id\":\"64593b3d-6d07-4153-b510-6916728e9050\"}],\"parentId\":\"c38819b0-a8d0-4ff8-b595-f49056499931\",\"id\":\"a00ca3b0-f7f5-495b-8ff5-294adf24bd22\",\"is\":1},{\"titleType\":1,\"sceneType\":1,\"questionTitle\":\"生产管控\",\"levelNumber\":\"\",\"children\":[{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用信息技术工具（如电子表格、云存储等）辅助人工进行生产工单数据的记录。\",\"levelNumber\":\"1\",\"children\":[],\"parentId\":\"338c1c3e-7bbd-4f75-8da9-801fbd00c8dc\",\"id\":\"5de045f4-c20c-400e-b2b0-14c714b39bf6\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用信息化系统实现生产工单信息（如生产工单进度、产量、物料领用/耗用等）录入、跟踪，实现规范化管理。\",\"levelNumber\":\"2\",\"children\":[],\"parentId\":\"338c1c3e-7bbd-4f75-8da9-801fbd00c8dc\",\"id\":\"46dcc7ae-5e94-454c-9e52-ba760dd2daba\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用信息化系统对生产工单信息、工艺参数进行数据采集，实现对生产过程中工单、物料、设备等的管控，实现信息化系统与其他系统（如生产计划、质量或设备等）的协同，实现数据共享。\",\"levelNumber\":\"3\",\"children\":[],\"parentId\":\"338c1c3e-7bbd-4f75-8da9-801fbd00c8dc\",\"id\":\"23c8d1b7-4ab9-4f1b-93a9-592878da4ae7\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"运用人工智能等前沿技术建立生产运行监测预警算法模型，实现对生产过程中工艺参数、设备状态、生产过程等生产作业数据的在线分析与实时监测预警，并驱动生产过程的迭代优化与闭环管控，不断优化生产管理。\",\"levelNumber\":\"4\",\"children\":[],\"parentId\":\"338c1c3e-7bbd-4f75-8da9-801fbd00c8dc\",\"id\":\"2c88eedd-faad-4898-a7e3-3f14554ff63f\"}],\"parentId\":\"c38819b0-a8d0-4ff8-b595-f49056499931\",\"id\":\"338c1c3e-7bbd-4f75-8da9-801fbd00c8dc\",\"is\":1},{\"titleType\":1,\"sceneType\":1,\"questionTitle\":\"质量管理\",\"levelNumber\":\"\",\"children\":[{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用信息技术工具（如电子表格、云存储等）辅助开展产品质量信息的管理。\",\"levelNumber\":\"1\",\"children\":[],\"parentId\":\"d2b05440-a40b-446e-97ff-6c89aff1a430\",\"id\":\"c9ff4b30-0ad7-4a57-853b-cf08fcccb44a\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"实现生产过程质量数据的数字化采集录入、统计与管理，基于信息化系统实现质量管理流程的规范化管理。\",\"levelNumber\":\"2\",\"children\":[],\"parentId\":\"d2b05440-a40b-446e-97ff-6c89aff1a430\",\"id\":\"32a1c8f9-ebad-4b62-9c00-135a2bf1e890\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用数字化检测设备及信息化系统实现关键工序质量检测，自动对检测结果判断和报警；或应用信息化系统实现对原材料、半成品、成品质量可追溯。\",\"levelNumber\":\"3\",\"children\":[],\"parentId\":\"d2b05440-a40b-446e-97ff-6c89aff1a430\",\"id\":\"468719de-15e1-4882-b744-a71f26237d5f\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用前沿技术（如视觉质检）开展产品质量检测，提升检测效率和检测水平，开展产业链上下游质量数据跨企业共享； 或构建产品质量管理模型，实现产品质量影响因素识别及缺陷预测性分析。\",\"levelNumber\":\"4\",\"children\":[],\"parentId\":\"d2b05440-a40b-446e-97ff-6c89aff1a430\",\"id\":\"b4488d22-8ac8-4e0a-856c-1324e6510f35\"}],\"parentId\":\"c38819b0-a8d0-4ff8-b595-f49056499931\",\"id\":\"d2b05440-a40b-446e-97ff-6c89aff1a430\",\"is\":1},{\"titleType\":1,\"sceneType\":1,\"questionTitle\":\"设备管理\",\"levelNumber\":\"\",\"children\":[{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"通过人工或手持仪器开展设备点巡检，并应用信息技术工具辅助制定设备管理台账。\",\"levelNumber\":\"1\",\"children\":[],\"parentId\":\"47368b31-0412-44c1-b6c0-876aab4f2eb1\",\"id\":\"5142afe6-c1cc-486d-994b-0f3e9e7cedbe\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"通过信息技术手段制定设备维护计划，开展设备点巡检、维护保养等功能，实现设备的规范化管理。\",\"levelNumber\":\"2\",\"children\":[],\"parentId\":\"47368b31-0412-44c1-b6c0-876aab4f2eb1\",\"id\":\"4e4f3239-de9f-477a-8828-a5098fb40f8b\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"基于信息化系统实现设备关键运行参数数据的实时采集、故障分析和远程诊断，并依据设备关键运行参数等，实现设备综合效率（OEE）统计。\",\"levelNumber\":\"3\",\"children\":[],\"parentId\":\"47368b31-0412-44c1-b6c0-876aab4f2eb1\",\"id\":\"7f07ed65-3795-41e2-9c75-492f029fbc1f\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"建立设备运行模型和设备故障知识库，实现设备故障自动预警及自动制定预测维护解决方案，并基于设备综合效率的分析等驱动工艺优化和生产作业计划优化。\",\"levelNumber\":\"4\",\"children\":[],\"parentId\":\"47368b31-0412-44c1-b6c0-876aab4f2eb1\",\"id\":\"8b058314-6431-4bd2-ba56-7ef3f687cb28\"}],\"parentId\":\"c38819b0-a8d0-4ff8-b595-f49056499931\",\"id\":\"47368b31-0412-44c1-b6c0-876aab4f2eb1\",\"is\":1},{\"titleType\":1,\"sceneType\":1,\"questionTitle\":\"安全生产\",\"levelNumber\":\"\",\"children\":[{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用信息技术工具辅助开展车间安全生产规范的制定及管理。\",\"levelNumber\":\"1\",\"children\":[],\"parentId\":\"b2097100-8510-462c-8b65-9e61dd415184\",\"id\":\"b6db7702-1044-4046-b570-8d3af2568dd6\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用信息技术手段实现安全作业规范化管理，开展安全风险数据、重大危险源等在线监测。\",\"levelNumber\":\"2\",\"children\":[],\"parentId\":\"b2097100-8510-462c-8b65-9e61dd415184\",\"id\":\"6ed601f4-3dca-4184-9403-031be8048420\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"实现危险废物存储、运输的全流程信息化管理，实现安全生产风险实时报警，建立安全应急预案，实现安全事故处理与相关部门及时协同。\",\"levelNumber\":\"3\",\"children\":[],\"parentId\":\"b2097100-8510-462c-8b65-9e61dd415184\",\"id\":\"756b4695-bb2c-433d-a0e0-ed6dfc0e74ca\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"基于安全作业、风险管控等数据的分析及建模，实现危险源的预防性管理、自动预警及响应处理。\",\"levelNumber\":\"4\",\"children\":[],\"parentId\":\"b2097100-8510-462c-8b65-9e61dd415184\",\"id\":\"dc689459-3f5e-467a-8b9e-a7d3465a6c3b\"}],\"parentId\":\"c38819b0-a8d0-4ff8-b595-f49056499931\",\"id\":\"b2097100-8510-462c-8b65-9e61dd415184\",\"is\":1},{\"titleType\":1,\"sceneType\":1,\"questionTitle\":\"能耗管理\",\"levelNumber\":\"\",\"children\":[{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用信息技术工具（如电子表格、云存储等）辅助人工进行能耗数据记录。\",\"levelNumber\":\"1\",\"children\":[],\"parentId\":\"662fccfa-0e1c-4e89-9f76-25768dfbb9ee\",\"id\":\"842caea8-cc2a-4fd4-9080-a2c6a555c66c\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用信息化系统收集和管理水、电、气、液等能耗数据，实现基于能耗数据的统计分析，实现规范化管理。\",\"levelNumber\":\"2\",\"children\":[],\"parentId\":\"662fccfa-0e1c-4e89-9f76-25768dfbb9ee\",\"id\":\"ed9defe7-462c-41ac-b8c8-641b6d452ca4\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用信息化系统或平台，实时采集和管理水、电、气、液以及影响设备能耗的关键数据，实现设备能耗的监测分析与相关部门协同管控优化。\",\"levelNumber\":\"3\",\"children\":[],\"parentId\":\"662fccfa-0e1c-4e89-9f76-25768dfbb9ee\",\"id\":\"70d6c745-149e-401c-bc82-ec74c2fe668b\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"建立设备能耗监测与优化算法模型，实现设备能耗实时监测、能源转化效率分析、未来能耗预测及能源优化调度等。\",\"levelNumber\":\"4\",\"children\":[],\"parentId\":\"662fccfa-0e1c-4e89-9f76-25768dfbb9ee\",\"id\":\"ff37df02-36e0-41aa-a094-06c954f18555\"}],\"parentId\":\"c38819b0-a8d0-4ff8-b595-f49056499931\",\"id\":\"662fccfa-0e1c-4e89-9f76-25768dfbb9ee\",\"is\":1}],\"id\":\"c38819b0-a8d0-4ff8-b595-f49056499931\",\"is\":1},{\"titleType\":1,\"sceneType\":2,\"questionTitle\":\"供应链数字化\",\"levelNumber\":\"\",\"children\":[{\"titleType\":1,\"sceneType\":1,\"questionTitle\":\"采购管理\",\"levelNumber\":\"\",\"children\":[{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"借助信息技术工具（如电子表格、云存储等），辅助记录采购订单信息和采购过程信息。\",\"levelNumber\":\"1\",\"children\":[],\"parentId\":\"9b3350dd-7600-4007-8653-ec58c332d0f1\",\"id\":\"30ebf81d-2cdf-4530-a56f-9ec07a5c1e0a\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用信息化系统对采购管理信息（如采购需求、采购订单、采购过程或供应商等）进行规范化管理。\",\"levelNumber\":\"2\",\"children\":[],\"parentId\":\"9b3350dd-7600-4007-8653-ec58c332d0f1\",\"id\":\"eb48e15a-ffb2-4b4a-bec7-eebad0d2883b\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"实现供应商管理、询报比价、采购计划、采购执行的全过程管理，实现应用采购信息化系统与生产、仓储、财务等信息化系统的数字化协同。\",\"levelNumber\":\"3\",\"children\":[],\"parentId\":\"9b3350dd-7600-4007-8653-ec58c332d0f1\",\"id\":\"f134d98f-508f-4637-afe4-18c33b246487\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"运用人工智能等前沿技术，实现采购与内外部供应链之间的数字化协同，并实现供应链风险预警预测，动态优化采购策略和方案。\",\"levelNumber\":\"4\",\"children\":[],\"parentId\":\"9b3350dd-7600-4007-8653-ec58c332d0f1\",\"id\":\"84c4bc77-7a88-46d6-8508-e2bf588007c2\"}],\"parentId\":\"e76dfaa3-123a-4623-b8fc-abf2390e3092\",\"id\":\"9b3350dd-7600-4007-8653-ec58c332d0f1\",\"is\":1},{\"titleType\":1,\"sceneType\":1,\"questionTitle\":\"仓储物流\",\"levelNumber\":\"\",\"children\":[{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"使用信息技术工具（如电子表格、云存储等）辅助记录出入库信息，实现对库存数据的采集管理。\",\"levelNumber\":\"1\",\"children\":[],\"parentId\":\"2f3d6002-6690-4641-9e51-24cd4fdf2acc\",\"id\":\"a22437eb-48c2-4ba6-baf1-987e680653e6\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"使用信息化系统，对物料、成品、半成品、耗材等出入库、库存等数据信息进行统计，实现规范化管理。\",\"levelNumber\":\"2\",\"children\":[],\"parentId\":\"2f3d6002-6690-4641-9e51-24cd4fdf2acc\",\"id\":\"6a2f664a-350b-4936-85be-704e75eb69df\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"实现仓储管理信息化系统与生产、采购、财务等信息化系统的数字化协同。\",\"levelNumber\":\"3\",\"children\":[],\"parentId\":\"2f3d6002-6690-4641-9e51-24cd4fdf2acc\",\"id\":\"e631a2f0-035f-474e-a571-efe821ee232b\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"使用人工智能等前沿技术，实现仓储物流与供应商库存或客户生产计划间的数字化协同，并能够自动实现物流计划的自动制定实施或厂内物料自动配送； 或按照产供销状况，实现智能仓储（如智能预测库存需求，自动调整库存补货策略等）及厂外智能物流（物流监测与策略优化）。\",\"levelNumber\":\"4\",\"children\":[],\"parentId\":\"2f3d6002-6690-4641-9e51-24cd4fdf2acc\",\"id\":\"8727fcd5-d81a-4c34-8590-11bce5a03294\"}],\"parentId\":\"e76dfaa3-123a-4623-b8fc-abf2390e3092\",\"id\":\"2f3d6002-6690-4641-9e51-24cd4fdf2acc\",\"is\":1}],\"id\":\"e76dfaa3-123a-4623-b8fc-abf2390e3092\",\"is\":1},{\"titleType\":1,\"sceneType\":2,\"questionTitle\":\"管理决策数字化\",\"levelNumber\":\"\",\"children\":[{\"titleType\":1,\"sceneType\":1,\"questionTitle\":\"财务管理\",\"levelNumber\":\"\",\"children\":[{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"使用信息化系统辅助实现日常财务记录，基本的总账管理和财务报表生成（如资产负债表、利润表、现金流量表）。\",\"levelNumber\":\"1\",\"children\":[],\"parentId\":\"e987df7a-4c65-479e-8987-89982c277c5c\",\"id\":\"67022b7c-8a4a-4a88-a348-7b122b18244c\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"使用信息化系统，实现总账、往来、存货、固定资产、出纳等与财务会计核算的协同，对财务实现规范化管理。\",\"levelNumber\":\"2\",\"children\":[],\"parentId\":\"e987df7a-4c65-479e-8987-89982c277c5c\",\"id\":\"61fc9d77-8bd2-410e-af76-bac339a4e8ae\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"实现业务数据与财务管理的协同，能支持企业的管理会计核算，实现通过财务的分析辅助决策，帮助企业快速掌握资产、负债、收入、成本、盈利能力等变动和使用情况，实现资产的优化配置和利用。\",\"levelNumber\":\"3\",\"children\":[],\"parentId\":\"e987df7a-4c65-479e-8987-89982c277c5c\",\"id\":\"e35d9f56-7a70-4be2-9158-6062d55fd550\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"实现企业内外部协同，实现企业财务管理全面智能化和数据驱动，并实现对企业未来的财务状况进行预测、规划和风险评估。\",\"levelNumber\":\"4\",\"children\":[],\"parentId\":\"e987df7a-4c65-479e-8987-89982c277c5c\",\"id\":\"31f28fcf-4e0a-4d63-80fd-c493d661e4f9\"}],\"parentId\":\"28447dab-f1fa-433c-8be2-78fb7cff3641\",\"id\":\"e987df7a-4c65-479e-8987-89982c277c5c\",\"is\":1},{\"titleType\":1,\"sceneType\":2,\"questionTitle\":\"人力资源\",\"levelNumber\":\"\",\"children\":[{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"采用信息技术工具（如电子表格、云存储等），辅助实现员工、流程的信息记录。\",\"levelNumber\":\"1\",\"children\":[],\"parentId\":\"361c12ed-ef01-4363-a921-fdff11d295fb\",\"id\":\"4a99fe4b-6090-4716-9738-aae5e7f59a39\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"基于信息化系统实现对考勤和薪酬福利等核心流程的规范化管理。\",\"levelNumber\":\"2\",\"children\":[],\"parentId\":\"361c12ed-ef01-4363-a921-fdff11d295fb\",\"id\":\"c6374389-361b-4672-8839-08bd3d05fc99\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"利用人力资源数据分析工具进行关键指标分析，数据驱动人力资源战略规划和决策制定。\",\"levelNumber\":\"3\",\"children\":[],\"parentId\":\"361c12ed-ef01-4363-a921-fdff11d295fb\",\"id\":\"2a3c364d-8e98-4351-8e52-6066ad28d0cd\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用人工智能等前沿技术，实现个性化绩效管理、智能招聘与人才画像、个性化的培训和发展计划，支持战略性人才管理。\",\"levelNumber\":\"4\",\"children\":[],\"parentId\":\"361c12ed-ef01-4363-a921-fdff11d295fb\",\"id\":\"959ed480-6e23-4971-81fa-e497bd5241a4\"}],\"parentId\":\"28447dab-f1fa-433c-8be2-78fb7cff3641\",\"id\":\"361c12ed-ef01-4363-a921-fdff11d295fb\",\"is\":1},{\"titleType\":1,\"sceneType\":2,\"questionTitle\":\"协同办公\",\"levelNumber\":\"\",\"children\":[{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用信息技术工具（如电子邮件或文档共享服务等通讯工具）辅助日常沟通和简单的信息共享文档处理。\",\"levelNumber\":\"1\",\"children\":[],\"parentId\":\"140f306a-3327-42b5-900c-54bfdc97284d\",\"id\":\"1070a7d9-b4ab-4902-95d1-628e14c4df35\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"部署具有更丰富功能的协同平台或办公软件，实现日常业务（如请假、报销、审批、通知、公告或新闻等）流程的数字化。\",\"levelNumber\":\"2\",\"children\":[],\"parentId\":\"140f306a-3327-42b5-900c-54bfdc97284d\",\"id\":\"86cc5ef0-d773-4db1-b1f2-629029acddc2\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用协同平台实现与财务、采购、生产、项目管理等专业业务管理系统集成，实现数据共享和业务流程的无缝对接，且利用移动工具，提升跨部门协作效率和响应速度。\",\"levelNumber\":\"3\",\"children\":[],\"parentId\":\"140f306a-3327-42b5-900c-54bfdc97284d\",\"id\":\"5f520b1d-7ad7-4ac8-96d2-853a4a7b516d\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"应用人工智能等前沿技术实现内部、外部数据的协同，在自动问答、智能推荐、智能预测分析和自适应工作流程等办公场景，组织员工在高度互联和智能化环境中实现无缝协作办公。\",\"levelNumber\":\"4\",\"children\":[],\"parentId\":\"140f306a-3327-42b5-900c-54bfdc97284d\",\"id\":\"66e32631-57f6-44cb-b9e4-8ce6a1d2e11f\"}],\"parentId\":\"28447dab-f1fa-433c-8be2-78fb7cff3641\",\"id\":\"140f306a-3327-42b5-900c-54bfdc97284d\",\"is\":1},{\"titleType\":1,\"sceneType\":2,\"questionTitle\":\"决策支持\",\"levelNumber\":\"\",\"children\":[{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"运用信息技术工具辅助收集企业生产经营过程基本数据，为管理者提供简单的决策建议或方向。\",\"levelNumber\":\"1\",\"children\":[],\"parentId\":\"e4b7f88c-a935-431b-9485-9cc694eab6cb\",\"id\":\"ca063fd6-4624-4b16-93c5-4dad03cc9ce3\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"运用信息化系统，整合关键业务环节的数据，使用业务关联分析和决策支持工具，提供直观的可视化数据。\",\"levelNumber\":\"2\",\"children\":[],\"parentId\":\"e4b7f88c-a935-431b-9485-9cc694eab6cb\",\"id\":\"7b677c20-2ac9-4448-95b2-42af9755a28e\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"利用数据驱动平台针对特定业务场景（如工艺设计、报价策略、生产计划、变更管理等）实施数据模拟与效能优化，助力决策者精准评估并采纳最佳实践方案。\",\"levelNumber\":\"3\",\"children\":[],\"parentId\":\"e4b7f88c-a935-431b-9485-9cc694eab6cb\",\"id\":\"ea57e825-f4e3-438d-95f7-7e46f2fa3bdd\"},{\"titleType\":2,\"sceneType\":2,\"questionTitle\":\"运用人工智能等前沿技术整合企业内外部数据，构建智能化的预测、预警和决策模型，辅助管理层或业务人员进行智能化流程决策，挖掘数据背后的深层次规律和价值。\",\"levelNumber\":\"4\",\"children\":[],\"parentId\":\"e4b7f88c-a935-431b-9485-9cc694eab6cb\",\"id\":\"7b8d0f7f-ea34-4552-b29d-f3486c2b0310\"}],\"parentId\":\"28447dab-f1fa-433c-8be2-78fb7cff3641\",\"id\":\"e4b7f88c-a935-431b-9485-9cc694eab6cb\",\"is\":1}],\"id\":\"28447dab-f1fa-433c-8be2-78fb7cff3641\",\"is\":1}]}")
    # print(response.text)
    data = json.loads(response)
    storeList = data["storeList"]
    for store in storeList:
        children = store["children"]
        for child in children:
            cl = child['children']
            for cil in cl:
                cc = cil['children']
                print(cc[0]["questionTitle"])
                for cci in cc:
                    c = cci['children']
                    for ci in c:
                        print(ci['optionPrefix'] + ":" + ci['optionContent'] + ":分数：" + str(ci['score']))
                        print("---------------------------------")
