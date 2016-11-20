#!/usr/bin/python
#-*-coding:utf-8-*-

import MySQLdb,sys

class TransferMoney(object):
    def __init__(self,conn):
        with conn:
            self.conn = conn
            cur = self.conn.cursor()
            cur.execute("DROP TABLE IF EXISTS account")
            cur.execute("CREATE TABLE account(acctid INT (11) DEFAULT NULL,money INT (11) DEFAULT NULL) ENGINE = INNODB")
            cur.execute("insert into account(acctid,money) values(6,110)")
            cur.execute("insert into account(acctid,money) values(7,10)")
            cur.close()

    def check_acct_available(self,acctid):
        try:
            cur = self.conn.cursor()
            sql = "select * from account where acctid = %s" % acctid
            cur.execute(sql)
            print 'check_acct_available:acctid = %s' % acctid
            rs = cur.fetchall()
            if len(rs) != 1:
                raise Exception("account:%s not exist" % acctid)
        finally:
            cur.close()

    def has_enough_money(self,acctid,money):
        try:
            cur = self.conn.cursor()
            sql = "select * from account where acctid = %s and money > %s" % (acctid,money)
            cur.execute(sql)
            print 'has_enough_money:acctid= %s,money = %s' % (acctid,money)
            rs = cur.fetchall()
            if len(rs) != 1:
                raise Exception("account:%s not has enough money" % acctid)
        finally:
            cur.close()

    def reduce_money(self,acctid,money):
        try:
            cur = self.conn.cursor()
            sql = "update account set money = money - %s where acctid = %s" % (money,acctid)
            cur.execute(sql)
            print 'reduce money:acctid = %s' % acctid
            if cur.rowcount != 1:
                raise Exception("account:%s reduce failed" % acctid)
        finally:
            cur.close()

    def add_money(self,acctid,money):
        try:
            cur = self.conn.cursor()
            sql = "update account set money = money + %s where acctid = %s" % (money,acctid)
            cur.execute(sql)
            print 'add money:acctid = %s' % acctid
            if cur.rowcount != 1:
                raise Exception("account:%s add failed" % acctid)
        finally:
            cur.close()

    def transfer(self,source_acctid,target_acctid,money):
        try:
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid,money)
            self.reduce_money(source_acctid,money)
            self.add_money(target_acctid,money)
            self.conn.commit()
        except Exception,e:
            self.conn.rollback()
            raise e


if __name__ == '__main__':
    source_acctid = sys.argv[1]
    target_acctid = sys.argv[2]
    money = sys.argv[3]    

    conn = MySQLdb.connect('127.0.0.1','testuser','test123','testdb')
    tr_money = TransferMoney(conn)
    
    try:
        tr_money.transfer(source_acctid,target_acctid,money)
    except Exception,e:
        print 'error:' + str(e)
    finally:
        conn.close()
