# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)


def res_user_migrate(
    rsock, ruid, remote_admin_user_pw, remote_dbname,
    lsock, luid, local_admin_user_pw, local_dbname
):

    remote_object_fields = ['id', 'name', 'partner_id', 'company_id', 'tz', 'lang',
                            'login', 'password', 'image_1920', 'groups_id', 'active']

    count = 0
    execute = True
    while execute:
        try:
            remote_objects = rsock.execute(remote_dbname, ruid, remote_admin_user_pw,
                                           'res.users', 'search_read',
                                           [],
                                           remote_object_fields)
            execute = False
        except Exception as err:
            count = count + 1
            if count > 5:
                raise err
            else:
                _logger.info(u'%s %s\n', '(01)--> Exception:', err)

    _logger.info(u'%s %s\n', '--> remote_objects', len(remote_objects))

    local_object_fields = ['id', 'name', 'partner_id', 'company_id',
                           'login', 'password', 'image_1920', 'groups_id', 'active']

    count = 0
    execute = True
    while execute:
        try:
            local_objects = lsock.execute(local_dbname, luid, local_admin_user_pw,
                                          'res.users', 'search_read',
                                          [],
                                          local_object_fields)
            execute = False
        except Exception as err:
            count = count + 1
            if count > 5:
                raise err
            else:
                _logger.info(u'%s %s\n', '(02)--> Exception:', err)

    _logger.info(u'%s %s\n', '--> local_objects', len(local_objects))

    for remote_object in remote_objects:

        count = 0
        execute = True
        while execute:
            try:
                local_object = lsock.execute(local_dbname, luid, local_admin_user_pw,
                                             'res.users', 'search_read',
                                             [('login', '=', remote_object['login'])],
                                             local_object_fields)
                execute = False
            except Exception as err:
                count = count + 1
                if count > 5:
                    raise err
                else:
                    _logger.info(u'%s %s\n', '(03)--> Exception:', err)
        _logger.info(u'%s %s', '-->', remote_object['name'])

        if local_object != []:
            _logger.info(u'%s %s', '----->', '*** Skipped ***')

        else:
            # count = 0
            # execute = True
            # while execute:
            #     try:
            #         res_company = lsock.execute(local_dbname, luid, local_admin_user_pw,
            #                                     'res.company', 'search_read',
            #                                     [('name', 'in', remote_object['company_id'])],
            #                                     ['id'])
            #         execute = False
            #     except Exception as err:
            #         count = count + 1
            #         if count > 5:
            #             raise err
            #         else:
            #             _logger.info(u'%s %s\n', '(04)--> Exception:', err)
            # company_id = res_company[0]['id']
            company_id = 1

            # count = 0
            # execute = True
            # while execute:
            #     try:
            #         res_partner = lsock.execute(local_dbname, luid, local_admin_user_pw,
            #                                     'res.partner', 'search_read',
            #                                     [('name', 'in', remote_object['company_id'])],
            #                                     ['id'])
            #         execute = False
            #     except Exception as err:
            #         count = count + 1
            #         if count > 5:
            #             raise err
            #         else:
            #             _logger.info(u'%s %s\n', '(05)--> Exception:', err)
            # parent_id = res_partner[0]['id']
            parent_id = 1

            res_user_record = {}
            res_user_record['name'] = remote_object['name']
            res_user_record['login'] = remote_object['login']
            res_user_record['password'] = remote_object['password']
            if remote_object['image_1920'] is not False:
                res_user_record['image_1920'] = remote_object['image_1920']
            res_user_record['lang'] = remote_object['lang']
            res_user_record['tz'] = remote_object['tz']
            res_user_record['active'] = remote_object['active']
            count = 0
            execute = True
            while execute:
                try:
                    user_id = lsock.execute(local_dbname, luid, local_admin_user_pw,
                                            'res.users', 'create',
                                            res_user_record)

                    execute = False
                except Exception as err:
                    count = count + 1
                    if count > 5:
                        raise err
                    else:
                        _logger.info(u'%s %s\n', '(06)--> Exception:', err)
            _logger.info(u'%s %s', '----->', user_id)

            count = 0
            execute = True
            while execute:
                try:
                    res_user = lsock.execute(local_dbname, luid, local_admin_user_pw,
                                             'res.users', 'search_read',
                                             [('id', '=', user_id)],
                                             ['id', 'name', 'partner_id'])

                    execute = False
                except Exception as err:
                    count = count + 1
                    if count > 5:
                        raise err
                    else:
                        _logger.info(u'%s %s\n', '(07)--> Exception:', err)
            count = 0
            execute = True
            while execute:
                try:
                    res_partner = lsock.execute(local_dbname, luid, local_admin_user_pw,
                                                'res.partner', 'search_read',
                                                [('name', 'in', res_user[0]['partner_id'])],
                                                ['id'])
                    execute = False
                except Exception as err:
                    count = count + 1
                    if count > 5:
                        raise err
                    else:
                        _logger.info(u'%s %s\n', '(08)--> Exception:', err)
            partner_id = res_partner[0]['id']

            _logger.info(u'%s %s', '----->', partner_id)

            res_partner_record = {}
            res_partner_record['email'] = remote_object['login']
            res_partner_record['parent_id'] = parent_id
            res_partner_record['company_id'] = company_id

            count = 0
            execute = True
            while execute:
                try:
                    result = lsock.execute(local_dbname, luid, local_admin_user_pw,
                                           'res.partner', 'write',
                                           partner_id,
                                           res_partner_record)

                    execute = False
                except Exception as err:
                    count = count + 1
                    if count > 5:
                        raise err
                    else:
                        _logger.info(u'%s %s\n', '(09)--> Exception:', err)
            _logger.info(u'%s %s', '----->', result)
