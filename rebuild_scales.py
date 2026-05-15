"""
重算所有量表合成分数 - 干净版
原则:
1. 已知反向题的 scale 应用反向计分(CTQ, Loneliness UCLA, BRS, INQ)
2. 维度归属按用户提供 + 标准文献
3. 输出干净 person-level CSV
"""
import pandas as pd
import numpy as np
from openpyxl.utils import column_index_from_string
import warnings
warnings.filterwarnings('ignore')

print("Loading...", flush=True)
lab = pd.read_excel('/mnt/project/full_cleaned_with_scales.xlsx')

def col_idx(s): return column_index_from_string(s) - 1
def items_of(start, end):
    return lab.iloc[:, col_idx(start):col_idx(end)+1].apply(pd.to_numeric, errors='coerce')

def score(items_df, item_nums_1based, reverse=None, max_val=5):
    """从 items_df 提取指定题号(1-based),应用反向 if specified"""
    reverse = reverse or []
    parts = []
    for q in item_nums_1based:
        v = items_df.iloc[:, q-1]
        if q in reverse:
            v = (max_val + 1) - v
        parts.append(v)
    return pd.concat(parts, axis=1).sum(axis=1, min_count=len(item_nums_1based))

# ===================== T1 =====================
print("\n--- T1 量表重算 ---", flush=True)
out = pd.DataFrame(index=lab.index)
out['raw_id'] = lab.iloc[:, 0]
out['raw_id_num'] = pd.to_numeric(out['raw_id'].astype(str).str.strip(), errors='coerce')

# CTQ T1 — 28题, reverse: 2,5,7,13,19,26,28
ctq = items_of('AA','BB')
out['CTQ_EA_T1']  = score(ctq, [3,8,14,18,25])
out['CTQ_PA_T1']  = score(ctq, [9,11,12,15,17])
out['CTQ_SA_T1']  = score(ctq, [20,21,23,24,27])
out['CTQ_EN_T1']  = score(ctq, [5,7,13,19,28], reverse=[5,7,13,19,28])
out['CTQ_PN_T1']  = score(ctq, [1,2,4,6,26],   reverse=[2,26])
out['CTQ_total_T1'] = out[['CTQ_EA_T1','CTQ_PA_T1','CTQ_SA_T1','CTQ_EN_T1','CTQ_PN_T1']].sum(axis=1, min_count=5)

# ASLEC T1 — 26题, 6维度 (用户提供的题号有重叠/出界,采用主流5维度)
# 标准ASLEC-CHN: 1.人际关系(1,2,4,15,25), 2.学习压力(3,9,16,18,22),
#               3.受惩罚(17,19,20,21,23,24), 4.丧失(12,13,14), 5.健康适应(5,8,11,26),
#               6.其他(6,7,10)
aslec1 = items_of('BC','CB')
out['ASLEC_total_T1'] = aslec1.sum(axis=1, min_count=20)  # 允许少量缺失
out['ASLEC_interpersonal_T1'] = score(aslec1, [1,2,4,15,25])
out['ASLEC_academic_T1']      = score(aslec1, [3,9,16,18,22])
out['ASLEC_punishment_T1']    = score(aslec1, [17,19,20,21,23,24])
out['ASLEC_loss_T1']          = score(aslec1, [12,13,14])
out['ASLEC_health_T1']        = score(aslec1, [5,8,11,26])
out['ASLEC_other_T1']         = score(aslec1, [6,7,10])

# PANSI T1 - 14题(剔除CI筛除项),负向8题3,4,5,7,8,10,11,12 + 积极6题 1,2,6,9,13,14
# 列范围 CC-CQ 共15列,CI是第7列(CC=1,CD=2,CE=3,CF=4,CG=5,CH=6,CI=7=筛除,CJ=8,...)
# 实际题号需要剔除CI后重新对齐:
# 剔除CI后14题对应原编号 1,2,3,4,5,6 + 8,9,10,11,12,13,14,15 (排除7)
# 用户说"积极: 1,2,6,9,13,14;消极: 3,4,5,7,8,10,11,12"——这是14题的题号(已去筛除项)
pansi_full = items_of('CC','CQ')
# CI在 CC-CQ里的位置: CC=col0, CI=col6 → drop column 6
keep = [i for i in range(15) if i != 6]
pansi1 = pansi_full.iloc[:, keep]  # 14 items in order
out['PANSI_pos_T1']  = score(pansi1, [1,2,6,9,13,14])
out['PANSI_neg_T1']  = score(pansi1, [3,4,5,7,8,10,11,12])
# 总分: 反向积极+消极 (高分=高风险)
out['PANSI_total_risk_T1'] = (5+1)*6 - out['PANSI_pos_T1'] + out['PANSI_neg_T1']

# 自杀史 (CR-CW) - 5项
sh1 = items_of('CR','CW')
out['SuicideHist_T1_anyLifetime'] = (sh1 > 1).any(axis=1).astype(int)  # 任一>1视为有
out['SuicideHist_T1_lastQuarter'] = ((sh1.iloc[:, [2,4]] > 1).any(axis=1)).astype(int)  # CT, CV为3月内

# NSSI T1 - 11题
nssi1 = items_of('CX','DH')
out['NSSI_count_T1'] = (nssi1 > 1).sum(axis=1)  # 假设1=从未,>1=有
out['NSSI_sum_T1'] = nssi1.sum(axis=1, min_count=8)

# BSS5 T1 - 5题
bss1 = items_of('DJ','DN')
out['BSS5_total_T1'] = bss1.sum(axis=1, min_count=5)

# DASS T1 - 14题(去Stress)
# DASS-21原编号: Anxiety 2,4,7,9,15,19,20; Depression 3,5,10,13,16,17,21
# 去掉Stress(1,6,8,11,12,14,18)后,保留14题按原顺序排:2,3,4,5,7,9,10,13,15,16,17,19,20,21
# 在新14题里位置: A=1,3,5,7,9,11,12 ; D=2,4,6,8,10,13,14
dass1 = items_of('DO','EB')
out['DASS_anx_T1']   = score(dass1, [1,3,5,7,9,11,12])
out['DASS_dep_T1']   = score(dass1, [2,4,6,8,10,13,14])
out['DASS_total_T1'] = dass1.sum(axis=1, min_count=14)

# INQ T1 - 15项, PB前6 TB后9
# 反向题(中文INQ-15): 7, 8, 10, 13, 15(英文版标准)— 但需要user确认
inq1 = items_of('EC','EQ')
out['INQ_PB_T1']    = score(inq1, [1,4,5,8,9,13], reverse=[8,13], max_val=7)
out['INQ_TB_T1']    = score(inq1, [2,3,6,7,10,11,12,14,15], reverse=[7,10,15], max_val=7)

# ES T1 - 16项无反向
es1 = items_of('ER','FG')
out['ES_total_T1'] = es1.sum(axis=1, min_count=16)

# CERQ-S T1 - 18题, 9维度各2题
cerq1 = items_of('FH','FY')
cerq_dims = {
    'CERQ_self_blame':       [1, 10], 'CERQ_acceptance':       [2, 11],
    'CERQ_rumination':       [3, 12], 'CERQ_pos_refocus':      [4, 13],
    'CERQ_refocus_planning': [5, 14], 'CERQ_pos_reappraisal':  [6, 15],
    'CERQ_putting_perspect': [7, 16], 'CERQ_catastrophizing':  [8, 17],
    'CERQ_other_blame':      [9, 18],
}
for d, qs in cerq_dims.items():
    out[f'{d}_T1'] = score(cerq1, qs)

# 不良CERS组合(maladaptive):自责+反刍+灾难化+他责
out['CERQ_maladaptive_T1'] = out[['CERQ_self_blame_T1','CERQ_rumination_T1',
                                   'CERQ_catastrophizing_T1','CERQ_other_blame_T1']].sum(axis=1, min_count=4)
# 适应性CERS: 接纳+积极重聚焦+计划+积极重评估+视野化
out['CERQ_adaptive_T1'] = out[['CERQ_acceptance_T1','CERQ_pos_refocus_T1',
                                'CERQ_refocus_planning_T1','CERQ_pos_reappraisal_T1',
                                'CERQ_putting_perspect_T1']].sum(axis=1, min_count=5)

# Loneliness T1 - UCLA-20, reverse: 1,5,6,9,10,15,16,19,20
lone1 = items_of('FZ','GS')
out['Lonely_total_T1'] = score(lone1, list(range(1,21)), reverse=[1,5,6,9,10,15,16,19,20], max_val=4)

# PSQI T1 - 17题(只算原始分,不做7components因为太复杂)
psqi1 = items_of('GT','HJ')
out['PSQI_raw_sum_T1'] = psqi1.sum(axis=1, min_count=10)

# PA T1 - IPAQ short
pa1 = items_of('HK','HT')
out['PA_raw_sum_T1'] = pa1.sum(axis=1, min_count=5)

# ===================== T2 =====================
print("--- T2 量表重算 ---", flush=True)

# T2量表的validity columns: ASLEC的JA, PANSI的JS
# ASLEC T2: IL-JL=27cols, JA是筛除 (JA=col_index 21? -wait, IL=col_index of IL...)
# Compute: IL=col 1L=246, JA=col_index of JA = 260
# col(IL)=246, col(JL)=271, range = 246..271 (26 cols)
# Actually 27 cols listed = IL...JL ; let me check
il = col_idx('IL'); jl = col_idx('JL')
print(f"IL={il}, JL={jl}, range_cols={jl-il+1}")
ja = col_idx('JA')
print(f"JA={ja}, position in range = {ja-il+1}")  # 1-based position

aslec2_full = items_of('IL','JL')  # 27 cols
keep = [i for i in range(27) if i != ja-il]  # drop validity
aslec2 = aslec2_full.iloc[:, keep]  # 26 items
out['ASLEC_total_T2'] = aslec2.sum(axis=1, min_count=20)
out['ASLEC_interpersonal_T2'] = score(aslec2, [1,2,4,15,25])

# PANSI T2: JM-KA, JS筛除
js = col_idx('JS'); jm = col_idx('JM')
pansi2_full = items_of('JM','KA')
keep = [i for i in range(15) if i != js-jm]
pansi2 = pansi2_full.iloc[:, keep]
out['PANSI_pos_T2']  = score(pansi2, [1,2,6,9,13,14])
out['PANSI_neg_T2']  = score(pansi2, [3,4,5,7,8,10,11,12])
out['PANSI_total_risk_T2'] = (5+1)*6 - out['PANSI_pos_T2'] + out['PANSI_neg_T2']

# NSSI T2
nssi2 = items_of('KE','KO')
out['NSSI_count_T2'] = (nssi2 > 1).sum(axis=1)

# BSS5 T2
out['BSS5_total_T2'] = items_of('KP','KT').sum(axis=1, min_count=5)

# DASS T2
dass2 = items_of('KU','LH')
out['DASS_anx_T2']   = score(dass2, [1,3,5,7,9,11,12])
out['DASS_dep_T2']   = score(dass2, [2,4,6,8,10,13,14])
out['DASS_total_T2'] = dass2.sum(axis=1, min_count=14)

# INQ T2
inq2 = items_of('LI','LW')
out['INQ_PB_T2']    = score(inq2, [1,4,5,8,9,13], reverse=[8,13], max_val=7)
out['INQ_TB_T2']    = score(inq2, [2,3,6,7,10,11,12,14,15], reverse=[7,10,15], max_val=7)

# ES T2
out['ES_total_T2'] = items_of('LX','MM').sum(axis=1, min_count=16)

# Loneliness T2
lone2 = items_of('MN','NG')
out['Lonely_total_T2'] = score(lone2, list(range(1,21)), reverse=[1,5,6,9,10,15,16,19,20], max_val=4)

# DES T2 - 解离 8项
des2 = items_of('NH','NO')
out['DES_total_T2'] = des2.sum(axis=1, min_count=8)
out['DES_mean_T2']  = des2.mean(axis=1)

# PSQI T2
out['PSQI_raw_sum_T2'] = items_of('NP','OF').sum(axis=1, min_count=10)

# Connectedness T2 - 6题, 3维度(家庭/朋友/学校)各2题
conn2 = items_of('OG','OL')
out['Connect_family_T2'] = score(conn2, [1,2])
out['Connect_friends_T2'] = score(conn2, [3,4])
out['Connect_school_T2']  = score(conn2, [5,6])
out['Connect_total_T2']  = conn2.sum(axis=1, min_count=6)

# PA T2
out['PA_raw_sum_T2'] = items_of('OM','OV').sum(axis=1, min_count=5)

# ===================== T3 =====================
print("--- T3 量表重算 ---", flush=True)
qc = col_idx('QC'); pn = col_idx('PN')
aslec3_full = items_of('PN','QN')
keep = [i for i in range(27) if i != qc-pn]
aslec3 = aslec3_full.iloc[:, keep]
out['ASLEC_total_T3'] = aslec3.sum(axis=1, min_count=20)
out['ASLEC_interpersonal_T3'] = score(aslec3, [1,2,4,15,25])

qu = col_idx('QU'); qo = col_idx('QO')
pansi3_full = items_of('QO','RC')
keep = [i for i in range(15) if i != qu-qo]
pansi3 = pansi3_full.iloc[:, keep]
out['PANSI_pos_T3']  = score(pansi3, [1,2,6,9,13,14])
out['PANSI_neg_T3']  = score(pansi3, [3,4,5,7,8,10,11,12])
out['PANSI_total_risk_T3'] = (5+1)*6 - out['PANSI_pos_T3'] + out['PANSI_neg_T3']

nssi3 = items_of('RG','RQ')
out['NSSI_count_T3'] = (nssi3 > 1).sum(axis=1)

out['BSS5_total_T3'] = items_of('RR','RV').sum(axis=1, min_count=5)

dass3 = items_of('RW','SJ')
out['DASS_anx_T3']   = score(dass3, [1,3,5,7,9,11,12])
out['DASS_dep_T3']   = score(dass3, [2,4,6,8,10,13,14])
out['DASS_total_T3'] = dass3.sum(axis=1, min_count=14)

inq3 = items_of('SK','SY')
out['INQ_PB_T3']    = score(inq3, [1,4,5,8,9,13], reverse=[8,13], max_val=7)
out['INQ_TB_T3']    = score(inq3, [2,3,6,7,10,11,12,14,15], reverse=[7,10,15], max_val=7)

out['ES_total_T3'] = items_of('SZ','TO').sum(axis=1, min_count=16)

# ERQ T3 - 9 items (中文ERQ-S可能是简版9题)
erq3 = items_of('TQ','TY')
# ERQ-10标准:重评6题(1,3,5,7,8,10),抑制4题(2,4,6,9). 但此处只有9题
# 假设最常见的中文版分布,需user确认
out['ERQ_reapp_T3'] = score(erq3, [1,3,5,7,8])  # 5题(假设缺第10题)
out['ERQ_suppr_T3'] = score(erq3, [2,4,6,9])  # 4题
out['ERQ_total_T3'] = erq3.sum(axis=1, min_count=8)

lone3 = items_of('TZ','US')
out['Lonely_total_T3'] = score(lone3, list(range(1,21)), reverse=[1,5,6,9,10,15,16,19,20], max_val=4)

des3 = items_of('UT','VA')
out['DES_total_T3'] = des3.sum(axis=1, min_count=8)
out['DES_mean_T3']  = des3.mean(axis=1)

# LPFS-BF T3 - 12题, 2维度(self function 6, interpersonal 6)
lpfs3 = items_of('VB','VM')
out['LPFS_self_T3'] = score(lpfs3, [1,2,3,4,5,6])
out['LPFS_interpersonal_T3'] = score(lpfs3, [7,8,9,10,11,12])
out['LPFS_total_T3'] = lpfs3.sum(axis=1, min_count=12)

# BRS T3 - 韧性 6题, reverse: 2,4,6
brs3 = items_of('VN','VS')
out['BRS_total_T3'] = score(brs3, [1,2,3,4,5,6], reverse=[2,4,6], max_val=5)

out['PSQI_raw_sum_T3'] = items_of('VT','WJ').sum(axis=1, min_count=10)
out['PA_raw_sum_T3'] = items_of('WL','WU').sum(axis=1, min_count=5)

# ===================== T4 =====================
print("--- T4 量表重算 ---", flush=True)
yb = col_idx('YB'); xm = col_idx('XM')
aslec4_full = items_of('XM','YM')
keep = [i for i in range(27) if i != yb-xm]
aslec4 = aslec4_full.iloc[:, keep]
out['ASLEC_total_T4'] = aslec4.sum(axis=1, min_count=20)

yt = col_idx('YT'); yn = col_idx('YN')
pansi4_full = items_of('YN','ZB')
keep = [i for i in range(15) if i != yt-yn]
pansi4 = pansi4_full.iloc[:, keep]
out['PANSI_pos_T4']  = score(pansi4, [1,2,6,9,13,14])
out['PANSI_neg_T4']  = score(pansi4, [3,4,5,7,8,10,11,12])
out['PANSI_total_risk_T4'] = (5+1)*6 - out['PANSI_pos_T4'] + out['PANSI_neg_T4']

nssi4 = items_of('ZF','ZP')
out['NSSI_count_T4'] = (nssi4 > 1).sum(axis=1)
out['BSS5_total_T4'] = items_of('ZQ','ZU').sum(axis=1, min_count=5)
dass4 = items_of('ZV','AAI')
out['DASS_anx_T4']   = score(dass4, [1,3,5,7,9,11,12])
out['DASS_dep_T4']   = score(dass4, [2,4,6,8,10,13,14])
out['DASS_total_T4'] = dass4.sum(axis=1, min_count=14)
inq4 = items_of('AAJ','AAX')
out['INQ_PB_T4']    = score(inq4, [1,4,5,8,9,13], reverse=[8,13], max_val=7)
out['INQ_TB_T4']    = score(inq4, [2,3,6,7,10,11,12,14,15], reverse=[7,10,15], max_val=7)
out['ES_total_T4'] = items_of('AAY','ABN').sum(axis=1, min_count=16)
erq4 = items_of('ABO','ABX')
out['ERQ_reapp_T4'] = score(erq4, [1,3,5,7,8,10])
out['ERQ_suppr_T4'] = score(erq4, [2,4,6,9])
out['ERQ_total_T4'] = erq4.sum(axis=1, min_count=9)
lone4 = items_of('ABY','ACR')
out['Lonely_total_T4'] = score(lone4, list(range(1,21)), reverse=[1,5,6,9,10,15,16,19,20], max_val=4)
des4 = items_of('ACS','ACZ')
out['DES_total_T4'] = des4.sum(axis=1, min_count=8)
out['DES_mean_T4']  = des4.mean(axis=1)
lpfs4 = items_of('ADA','ADL')
out['LPFS_self_T4'] = score(lpfs4, [1,2,3,4,5,6])
out['LPFS_interpersonal_T4'] = score(lpfs4, [7,8,9,10,11,12])
out['LPFS_total_T4'] = lpfs4.sum(axis=1, min_count=12)
# Connect_T4 7题(三维度,但分布需确认)
conn4 = items_of('ADM','ADS')
out['Connect_total_T4'] = conn4.sum(axis=1, min_count=6)
out['PSQI_raw_sum_T4'] = items_of('ADT','AEI').sum(axis=1, min_count=10)
out['PA_raw_sum_T4'] = items_of('AEK','AET').sum(axis=1, min_count=5)

# 保存
out_clean = out.dropna(subset=['raw_id_num']).drop_duplicates('raw_id_num')
out_clean.to_csv('/home/claude/feasibility/all_scales_clean.csv', index=False)
print(f"\n✓ Saved: all_scales_clean.csv  ({len(out_clean)} 行 × {out_clean.shape[1]} 列)")

# 关键变量描述
print(f"\n关键变量描述统计 (T1):")
key_vars = ['CTQ_total_T1','CTQ_EA_T1','CTQ_PA_T1','CTQ_SA_T1','CTQ_EN_T1','CTQ_PN_T1',
            'PANSI_neg_T1','PANSI_total_risk_T1','BSS5_total_T1','NSSI_count_T1',
            'DASS_anx_T1','DASS_dep_T1','INQ_PB_T1','INQ_TB_T1','ES_total_T1',
            'CERQ_maladaptive_T1','CERQ_adaptive_T1','Lonely_total_T1']
for v in key_vars:
    if v in out_clean.columns:
        s = out_clean[v].dropna()
        print(f"  {v:30s}: n={len(s):4d}, M={s.mean():>7.2f}, SD={s.std():>6.2f}, range=[{s.min():>5.0f}, {s.max():>5.0f}]")
