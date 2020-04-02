"""
涉及到数据库的常用操作
"""


def get_query_args_by_item(item, table, filter_keys=None):
    """根据 item 生成存储的 sql 语句和 args 并返回
    自动过滤值为空的字段（不含 0 ）

    :param item: item 对象
    :param table: 表名称
    :param filter_keys: 要过滤的键
    """
    # kw_list中的key为mysql关键字，形成sql语句时需要做处理
    kw_list = [
        'name', 'staring'
    ]

    fields, args = [], []
    filter_keys = filter_keys or ()

    for k, v in item.items():
        if k in filter_keys:
            continue
        if not v and v is not 0:
            continue
        fields.append('`'+k+'`')
        args.append(v)

    # 格式化 keys -> (k1, k2, ...)
    fields = f"({', '.join(fields)})"
    values = f"({', '.join('%s' for _ in args)})"

    return f'INSERT INTO {table} {fields} VALUES {values}', args
