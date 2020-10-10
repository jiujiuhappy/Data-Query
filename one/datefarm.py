import pandas as pd
import numpy as np
from one.getallother import GetAllOther

def DateFarm(path, sheet, dtimes, zhanghaos):
    '''此方法用于计算业务量并返回一个表'''
    jifei_all = ['jifei', 'jifei2', 'jifei3', 'jifei4', 'jifei5']
    mmsc_all = ['hwmmsc1', 'hwmmsc2', 'hwmmsc3', 'hwmmsc4',
                'jyhmmsc04', 'jyhmmsc1', 'JYHMMSC1', 'jyhmmsc2',
                'JYHMMSC2', 'jyhmmsc3', 'JYHMMSC3', 'JYHMMSC4',
                'KJGMMSC1', 'KJGMMSC2', 'KJGMMSC3', 'KJGMMSC4']
    df = pd.read_excel(path, sheet_name=sheet)
    at_zhanghao_all = df['账号'].values.tolist()
    at_zhanghao =  list(set(at_zhanghao_all))
    other_zh = GetAllOther(at_zhanghao)# 获取其他账号
    df['时间'] = df['时间'].apply(lambda x: x.strftime('%Y/%m/%d'))
    ywlsum = []
    b = []
    timelen = len(dtimes)
    zhlen = len(zhanghaos)
    zongliang = ['总量']
    for dtime in dtimes:
        a = []
        for zhanghao in zhanghaos:
            if zhanghao == '空白':
                ywl = df.query('时间 == @dtime')
                df_k = ywl[ywl.isnull().T.any()]
                one_num = df_k.业务量.agg(np.sum)
                a.append(one_num)
            elif zhanghao == 'jifei':
                jifei_sum = []
                for jifei in jifei_all:
                    ywl_jifei = df.query('时间 == @dtime and  账号 == @jifei')
                    num_jifei = ywl_jifei.业务量.agg(np.sum)
                    jifei_sum.append(num_jifei)
                a.append(sum(jifei_sum))
            elif zhanghao == '其他':
                other_sum = []
                for other in other_zh:
                    ywl_other = df.query('时间 == @dtime and  账号 == @other')
                    num_other = ywl_other.业务量.agg(np.sum)
                    other_sum.append(num_other)
                a.append(sum(other_sum))
            elif zhanghao == 'mmsc':
                mmsc_sum = []
                for mmsc in mmsc_all:
                    ywl_mmsc = df.query('时间 == @dtime and  账号 == @mmsc')
                    num_mmsc = ywl_mmsc.业务量.agg(np.sum)
                    mmsc_sum.append(num_mmsc)
                a.append(sum(mmsc_sum))
            else:
                ywl = df.query('时间 == @dtime and  账号 == @zhanghao')
                num = ywl.业务量.agg(np.sum)
                a.append(num)
        ywlsum.append(a)
        zongliang.append(sum(a))

    for zh, m in zip(zhanghaos, range(zhlen)):
        e = [zh]
        for su, i in zip(ywlsum, range(timelen)):
            sum_m = su[m]
            e.append(sum_m)
        b.append(e)
    b.append(zongliang)

    # 此循环求单账号的总量
    for i in b:
        i.append(sum(i[1:]))
    # 此循环将创造一个字典
    dtimes.append('总量')
    c = {'时间': dtimes}
    for i in b:
        name = i[0]
        del i[0]
        a = {name: i}
        c.update(a)
    return c


if __name__ == '__main__':
    shaixuan_3('6月数据.xlsx', 'ORG', ['2018/06/01','2018/06/02','2018/06/03'], ['hangye', 'dianshang', 'mmsc'])
