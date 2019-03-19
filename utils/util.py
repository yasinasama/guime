from datetime import datetime


# 自动生成单号
def generate_id(conn):
    today = datetime.strftime(datetime.now(), '%Y%m%d')
    begin = '001'
    sql = 'select max(order_id) from orders'
    try:
        res = conn.query(sql)[0][0]
        if res is None or not res.startswith(today):
            return today + begin
        else:
            inx = int(res[-3:]) + 1
            return '%s%03d' % (today, inx)
    except:
        raise Exception('单号生成错误!')