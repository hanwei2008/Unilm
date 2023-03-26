# coding=utf-8

if __name__ == '__main__':
    import sys
    import pandas as pd
    import json
    import random

    SEP = '\u2558'

    p_in = sys.argv[1]
    p_out = sys.argv[2]

    df_data = pd.read_csv(p_in, sep=SEP)

    with open(p_out, 'w') as fw:
        for _, row in df_data.iterrows():
            if row['label']==1:
                q1 = row['query1']
                q2 = row['query2']
                n1 = len(q1)
                n2 = len(q2)
                if n1 > 20 and n2 < 20:
                    pass
                elif n1 < 20 and n2 > 20:
                    q1, q2 = q2, q1
                else:
                    q1, q2 = (q1, q2) if random.random()<0.5 else (q2, q1)

                json_info = {'src_text':q1, 'tgt_text':q2}
                fw.write(json.dumps(json_info, ensure_ascii=False))
                fw.write('\n')
