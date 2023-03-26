# coding=utf-8

if __name__ == '__main__':
    import sys
    import json

    p_train = sys.argv[1]
    p_test = sys.argv[2]
    p_test_f = sys.argv[3]

    with open(p_train, 'r') as fr:
        all_queries = set()
        for line in fr:
            data_info = json.loads(line)
            query1 = data_info['src_text']
            query2 = data_info['tgt_text']
            all_queries.add(query1)
            all_queries.add(query2)

    with open(p_test_f, 'w') as fw:
        with open(p_test, 'r') as fr:
            for line in fr:
                data_info = json.loads(line)
                query = data_info['src_text']
                if query in all_queries:
                    continue
                fw.write(json.dumps(data_info, ensure_ascii=False))
                fw.write('\n')
