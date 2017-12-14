#!/usr/bin/python3
import time
import fdb
# import datetime
# import xmltodict
import dicttoxml
from settings import logger
import settings


async def check_account(account):
    SELECT = ('select d.id from drivers d '
              'where (d.term_account=?) '
              'and ((d.deleted=0) and (d.is_dismiss=0))')
    driver_id, state = 0, 0
    try:
        with fdb.connect(**settings.FDB) as db:
            c = db.cursor()
            c.execute(SELECT, (account, ))
            driver_id, state = c.fetchone(), 0
            driver_id = int(driver_id[0]) if driver_id else 0
            c.close()
            logger.debug(f'{state} {driver_id}')
        # logger.debug(f'{state} {driver_id}')
    except Exception as e:
        logger.debug(e)
        driver_id, state = -1, 5
    return driver_id, state


async def check(**kwargs):
    logger.debug(kwargs)
    command = kwargs['command']
    txn_id = kwargs['txn_id']
    account = kwargs['account']
    summa = kwargs['sum']
    result = {'response': {'kit_txn_id': txn_id,
                           'result': 0,
                           'comment': '', }, }
    driver_id, state = await check_account(account)
    logger.debug(f'{state} {driver_id}')
    if state == 0:
        SELECT = ('select opertime, oper_type, term_id, '
                  'term_pay_system_id, deleted '
                  'from driver_oper '
                  'where (driverid=?)'
                  ' and (term_operation=1)'
                  ' and (term_id=?)'
                  ' and (deleted=0)'
                  ' and (oper_type=0)'
                  ' and (oper_type=0)')
        logger.debug(f'{SELECT}')
        try:
            with fdb.connect(**settings.FDB) as db:
                c = db.cursor()
                c.execute(SELECT, (driver_id, txn_id))
                oper = c.fetchone()
                if oper:
                    result['response'].update({'result': 1})
                    logger.debug(f'{oper}')
                c.close()
        except Exception as e:
            logger.debug(e)
    else:
        result['response'].update({'result': state})
    dicttoxml.set_debug(False)
    return dicttoxml.dicttoxml(result, root=False, attr_type=False)


async def pay(**kwargs):
    logger.debug(kwargs)
    command = kwargs['command']
    txn_id = kwargs['txn_id']
    summa = kwargs['sum']
    txn_date = kwargs['txn_date']
    account = kwargs['account']
    result = ''
    result = {'response': {'kit_txn_id': txn_id,
                           'prv_txn': time.time(),
                           'sum': summa,
                           'result': 0,
                           'comment': '', }, }
    driver_id, state = await check_account(account)
    if state == 0:
        pass
    else:
        result['response'].update({'result': state})
    dicttoxml.set_debug(False)
    return dicttoxml.dicttoxml(result, root=False, attr_type=False)
