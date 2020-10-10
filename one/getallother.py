

def GetAllOther(zhanghao):
    '''次方法用于获取其他账号'''
    otherzh = []
    mainzh = ['jifei', 'jifei2', 'jifei3', 'jifei4', 'jifei5',
              'hwmmsc1', 'hwmmsc2', 'hwmmsc3', 'hwmmsc4',
              'jyhmmsc04', 'jyhmmsc1', 'JYHMMSC1', 'jyhmmsc2',
              'JYHMMSC2', 'jyhmmsc3', 'JYHMMSC3', 'JYHMMSC4',
              'KJGMMSC1', 'KJGMMSC2', 'KJGMMSC3', 'KJGMMSC4',
              'dianshang', 'hangye', 'kzyx', 'YJDX',
              'Gateway', 'guwanght', 'localgate2', 'ocs_smc2',
              'openet', 'zxsmg'
              ]
    for i in zhanghao:
        if i not in mainzh:
            otherzh.append(i)
    return otherzh