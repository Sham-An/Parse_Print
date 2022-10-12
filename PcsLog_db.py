import psycopg2
import sqlite3
import os
# from os import path
from pathlib import Path
import pathlib
from pathlib import Path
import sqlite3
from contextlib import closing
import json  # json.dumps(['please','help','me']) json.loads(s)

datamain = 'PcsLog2.db'
conn_PCS_main = sqlite3.connect(datamain)

database = 'Pcsparse.db'
conn_PCS_db = sqlite3.connect(database)


def open_cur():
    # with closing(sqlite3.connect(database)) as connection:
    with closing(conn_PCS_db) as connection:
        cursor = connection.cursor()

    return cursor


def clearparse():
    with sqlite3.connect('Pcsparse.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM PCSparse;', )  # cursor.com
        connection.commit()


def check_database(PCS_in):
    PCS = PCS_in
    print('!!!!!!!!!!!!!!!!check_database\n')
    print(f'PCS = {PCS}')
    PCS__id = PCS_in['PCS_id']
    # if result is None:
    with sqlite3.connect('Pcsparse.db') as connection:
        cursor = connection.cursor()

        # cursor.execute('DELETE FROM PCSparse;', )        #cursor.com
        # connection.commit()

        cursor.execute("""
            SELECT PCS_id FROM PCSparse WHERE PCS_id = (?)
        """, (PCS__id,))
        result = cursor.fetchone()
        print(f'!!!!!!!!!!!!!!   result cursor.fetchone() = {result}')

        if result is None:
            cursor.execute("""
                     INSERT INTO PCSparse
                     VALUES (NULL, :PCS_id, :kod_start, :kod_stop, :start, :start, :stop, :Full_path,
                     :file_name, :kalibr, :kog_group, :file_dir, :Full_path, :file_name, :GTIN_kod, :GTIN_name,  
                     :last_kod_id, :last_kod, :status)
                     """, PCS)
            connection.commit()
            print(f'добавлено в базу данных')


def prnpcs():
    # offer = {}
    #
    # offer["offer_id"] = id_item
    # offer["id_item"] = id_item

    # cursor.execute("""
    #     INSERT INTO offers
    #     VALUES (NULL,: id_item,: category_name,: category_kod,
    #     : date,: time,: title_desk,: title_full,: img,: price,
    #     : address,: coords,: url,: uri_mweb,: offer_id,: area,
    #     : rooms,: floor,: total_floor)
    # """, offer)

    # with closing(conn_PCS_db) as connpcs:
    # conn = sqlite3.connect
    connpcs = sqlite3.connect('Pcsparse.db')
    cur = connpcs.cursor()

    # select LogContext from PCSLog
    database = 'PcsLog.db'
    key1 = 'Печать работы:'  # Печать работы: C:\Users\Solmark\Desktop\СЕРИИ\Омепразол 30\бланк1.VDF
    key2 = 'Старт Печати Индекс текущей записи'  # Старт Печати Индекс текущей записи 2636.
    key3 = 'Стоп печати Индекс текущей записи'  # Стоп печати Индекс текущей записи 2666.
    insert_db = ''
    control_db = 'Insert  '
    PCS = {}  # "" #{}
    PCS["start"] = ''
    PCS["kod_start"] = ''
    blank = 'бланк'
    # with closing(sqlite3.connect(database)) as connection:
    with closing(conn_PCS_main) as connection:
        # conn = sqlite3.connect

        cursor = connection.cursor()
        # cursor = open_cur()
        cursor.execute("""
                       select * from PCSLog
                       """)
        # получаем все значения
        rows = cursor.fetchall()
        for row in rows:
            ##PCS = {}
            # ID_PCS = row[0]
            Log_Time = row[3]
            cont = str(row[4])
            # blank = 'бланк'
            insert_db = ''

            if key1 in cont:

                # print(f'UPPER {PCS}')
                PCS = {}
                PCS["PCS_id"] = '--'
                PCS["kod_start"] = '--'
                PCS["Log_Time"] = '--'  # Log_Time
                PCS["start"] = '--'
                PCS["kod_stop"] = '--'
                PCS["stop"] = "--"
                PCS["parent_group_file"] = '--'
                PCS["kalibr"] = "--"
                PCS["kog_group"] = "--"
                PCS["file_dir"] = '--'
                PCS["Full_path"] = '--'
                PCS["file_name"] = '--'
                PCS["GTIN_kod"] = '--'
                PCS["GTIN_name"] = '--'
                PCS["last_kod_id"] = '--'
                PCS["last_kod"] = '--'
                PCS["status"] = '--'
                if blank in cont:
                    continue
                    cont = cont.replace('бланк', "бланк бланк бланк")
                    # print('############################################################', cont)

                ID_PCS = row[0]
                PCS["PCS_id"] = ID_PCS
                PCS["Log_Time"] = row[3]  # Log_Time
                # PCS["cont"] = cont
                # 'C:\\Users\\Solmark\\Desktop\\СЕРИИ\\Омепразол 30\\бланк1.VDF')
                cont_txt = cont
                full_path = str(Path(cont.replace(key1, "").strip()))

                #                print('full_path !!! ', full_path)
                #################################################
                ###!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                # filename = os.path.basename(full_path).split('\\')[-1]
                path = Path(full_path)
                print(f' path path path path path path path path {path}')
                list_path = path.parts[:]  # json.dumps(['please','help','me']) json.loads(s) path.parts[1:]

                print(f'list_path list_pathlist_pathlist_pathlist_pathlist_path {list_path}')
                name_dir = list_path[-2]
                if name_dir == 'CheckNozzle':
                    continue
                filename = list_path[-1]
                kod_name = pathlib.Path(filename).stem
                length_kod = int(len(kod_name) - int('9'))
                # kod = os.path.basename(kod_name).split(' ')[-1]
                kod1 = kod_name[length_kod:]
                group_dict1 = kod_name.replace('-', " ")
                group_dict = group_dict1.replace('  ', " ")
                parent_group = os.path.basename(kod_name).split('-')  # [0]
                parent_group2 = group_dict.split(' ')  # [0]
                # print(f'parent_group2  === === {parent_group2} NAME {parent_group2[0]} trotil {parent_group2[-1]} kod {parent_group2[-1]}')
                if len(parent_group2) != 3:
                    print(
                        f'parent_group2  !!! === === {parent_group2} NAME {parent_group2[0]} trotil {parent_group2[-1]} kod {parent_group2[-1]}')
                    name_group = parent_group2[0]
                    trotil = 'Не определен'
                    kog_group = parent_group2[-1]
                else:
                    name_group = parent_group2[0].upper()
                    trotil = parent_group2[-2]
                    kog_group = parent_group2[-1]

                    # continue
                    # print(f'$$$$$$$$$$$$$$$$$$$$$$$   len(parent_group2)  {parent_group2}  len {len(parent_group2)}')
                # print(f'parent_group2  === === {parent_group2} NAME {parent_group2[0]} trotil {parent_group2[-2]} kod {parent_group2[-1]}')
                # name_group = (parent_group[0]).upper()
                # kog_group = (parent_group[-1]).upper()
                #                name_group = parent_group2[0].upper()
                #                trotil = parent_group2[-2]
                #                kog_group = parent_group2[-1]

                #                print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% kog_group {kog_group}')
                #                kod = os.path.basename(filename).split('-')[-1]

                print(f'\n \n -----------___--Path_path {path}'
                      f' \n name_dir                              {name_dir} '
                      f' \n filename                              {filename} '
                      f' \n kod(-9)                               {kod1} '
                      f' \n GROUP file NAME {parent_group} \n '
                      f' \n GROUP {name_group} '
                      f' \n kod from file NAME {kog_group} \n \n')

                # parentname = os.path.basename(cont_txt).split('\\')#[-1]
                #####################################################
                PCS["Full_path"] = json.dumps(list_path)  #json.loads(s) # "FULL PATH"#list_path[-3:]#"FULL PATH"  # path  # str(full_path) #path# path #os.path.basename(full_path)
                PCS["file_dir"] = name_dir
                PCS["file_name"] = filename  # name
                PCS["parent_group_file"] = name_group  # parent_group #parentname
                PCS["kalibr"] = trotil
                PCS["kog_group"] = kog_group

                # PCS["start"] = ""
                # PCS["kod_start"] = ''
                # PCS["stop"] = ""
                # PCS["kod_stop"] = ''
                # print(' \n Печать работы:   ')
                insert_db = 'Insert  '

                ## "INSERT INTO PCSparse (PCS_time,PCS_context) VALUES (Log_Time, cont)"
                # cur.execute(
                #     """INSERT INTO PCSparse (PCS_time,PCS_context) VALUES (Log_Time, cont);"""
                # )
                #
                # connpcs.commit()
                # print("Record inserted successfully")

            elif key2 in cont:

                kod_start = cont.replace('.', "").split(' ')[-1]
                PCS["start"] = row[3]  # cont
                PCS["kod_start"] = kod_start  # cont
                print('key2', cont, PCS)
                # cur.execute("UPDATE STUDENT set AGE = 20 where ADMISSION = 3420")
                # con.commit()
                insert_db = "Update 1"

            elif key3 in cont:
                # cur.execute("UPDATE STUDENT set AGE = 20 where ADMISSION = 3420")
                # con.commit()
                PCS["stop"] = row[3]  # cont
                kod_stop = cont.replace('.', "").split(' ')[-1]
                PCS["kod_stop"] = kod_stop
                insert_db = "Update 2"

            # else:
            # state3
            # else: #delete
            if insert_db == 'Insert  ':
                print(f'PCS {insert_db} == {PCS}')
                insert_db = ''
            if insert_db == "Update 2":
                print(f'PCS UUUUUUpdate  {insert_db} == {PCS} \n \n')
                check_database(PCS)
                # insert_db = ''

            insert_db = ''

        print(f'\n \n \n !!! !!!! !!!! {insert_db}  Finish     {PCS}')

        # cur.execute("DELETE from STUDENT where ADMISSION=3420;")
        # con.commit()
        # print("ID =", row[0], ' \n')
        # print("Log_Time =", row[3])
        # print("Log_Context =", cont)


# print("Operation done successfully")

def CreateLogDB():
    # При подключении к базе, автоматически создается realty.db
    connection = sqlite3.connect('Pcsparse.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE PCSparse (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            PCS_id text,
            PCS_kod_start integer,
            PCS_kod_stop integer,
            PCS_time_print text,
            PCS_time_start text,
            PCS_time_stop text,
            PCS_context text,            
            Parent_name_file text,
            Parent_kalibr text,
            Parent_kog_group text,
            PCS_file_dir text,
            PCS_Full_path text,
            PCS_file_name text,
            gtin_kod text,
            gtin_name text,
            last_kod_id text,
            last_kod text,
            status text            
            )     
    """)
    connection.close()
    #     {'PCS_id': 78800,
    #     'kod_start': '2802',
    #     'Log_Time': '2022-09-16 09:37:59.952',
    #     'start': '2022-09-16 09:38:00.186',
    #     'kod_stop': '4886',
    #     'stop': '2022-09-16 09:42:35.963',
    #     'parent_group_file': 'АЗИТРОМИЦИН',
    #     'kalibr': '500',
    #     'kog_group': '000000661',
    #     'file_dir': 'Азитрмицин 500',
    #     'Full_path': WindowsPath('C:/Users/Solmark/Desktop/СЕРИИ/Азитрмицин 500/АЗИТРОМИЦИН 500 000000661.VDF'),
    #     'file_name': 'АЗИТРОМИЦИН 500 000000661.VDF'}


def CreateParentDB():
    # При подключении к базе, автоматически создается realty.db
    connection = sqlite3.connect('Pcsparent.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE PCSparent(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            PAR_id text,
            PAR_kod text,
            PAR_NAME_FULL text,
            PAR_NAME_short text,
            PAR_kalibr text,
            PAR_trotil text,
            PAR_count text,
            PAR_tara text,
            PAR_Name_Dir text,
            Parent_kog_group text,
            gtin_kod text,
            gtin_name text
            )     
    """)


    cursor.execute('''
              INSERT INTO PCSparent (
              id, PAR_id, PAR_kod, PAR_NAME_FULL, PAR_NAME_short, PAR_kalibr, PAR_trotil, PAR_count, PAR_tara,
              PAR_Name_Dir, Parent_kog_group, gtin_kod, gtin_name)

                    VALUES
                    (NULL, '1', '', 'Азитромицин 500', 'Азитромицин', '500', '500', '3', 'small', 'Азитромицин 500', 'Parent_kog_group', 'gtin_kod', 'gtin_name'),
                    (NULL, '2', '', 'Азитромицин 250', 'Азитромицин', '250', '250', '6',  'small', 'Азитромицин 250', 'Parent_kog_group', 'gtin_kod', 'gtin_name'),
                    (NULL, '3', '', 'Индапамид 2.5', 'Индапамид', '2.5', '2.5', '30',  'big', 'Индапамид 2.5', 'Parent_kog_group', 'gtin_kod', 'gtin_name'),
                    (NULL, '4', '', 'ИТРАКОНАЗОЛ 100', 'ИТРАКОНАЗОЛ', '100', '100', '14',  'small', 'ИТРАКОНАЗОЛ 100', 'Parent_kog_group', 'gtin_kod', 'gtin_name'),
                    (NULL, '5', '', 'ЛЕВОФЛОКСАЦИН 500', 'ЛЕВОФЛОКСАЦИН', '500', '500', '',  'small', 'ЛЕВОФЛОКСАЦИН 500', 'Parent_kog_group', 'gtin_kod', 'gtin_name'),
                    (NULL, '6', '', 'Лоперамид 10', 'Лоперамид', '10', '2',  '10',  'small', 'Лоперамид 10', 'Parent_kog_group', 'gtin_kod', 'gtin_name'),
                    (NULL, '6', '', 'Линкомицин 250', 'Линкомицин', '250', '250',  '20',  'small', 'Линкомицин 250', 'Parent_kog_group', 'gtin_kod', 'gtin_name'),
                    (NULL, '7', '', 'НИФУРОКСАЗИД  100 №30', 'НИФУРОКСАЗИД', '100', '100', '30',  'big', 'НИФУРОКСАЗИД  100 №30', 'Parent_kog_group', 'gtin_kod', 'gtin_name'),
                    (NULL, '8', '', 'НИФУРОКСАЗИД  200 №20', 'НИФУРОКСАЗИД', '200', '200', '20',  'small', 'НИФУРОКСАЗИД  200 №20', 'Parent_kog_group', 'gtin_kod', 'gtin_name'),
                    (NULL, '9', '', 'Омепразол 30', 'Омепразол', '30', '20', '30',  'big', 'Омепразол 30', 'Parent_kog_group', 'gtin_kod', 'gtin_name'),
                    (NULL, '10', '', 'Пироксикам 10', 'Пироксикам', '10',  '10', '20',  'small', 'Пироксикам 10', 'Parent_kog_group', 'gtin_kod', 'gtin_name'),
                    (NULL, '11', '', 'Пироксикам 20', 'Пироксикам', '20',  '20', '20',  'small', 'Пироксикам 20', 'Parent_kog_group', 'gtin_kod', 'gtin_name'),
                    (NULL, '12', '', 'Флуконазол 150', 'Флуконазол', '150',  '150', '1',  'small', 'Флуконазол 150', 'Parent_kog_group', 'gtin_kod', 'gtin_name'),
                    (NULL, '13', '', 'Флуконазол 50', 'Флуконазол', '50',  '50', '7',  'small', 'Флуконазол 50', 'Parent_kog_group', 'gtin_kod', 'gtin_name'),
                    (NULL, '14', '', 'Флуоксетин', 'Флуоксетин', '20',  '20', '20',  'small', 'Флуоксетин', 'Parent_kog_group', 'gtin_kod', 'gtin_name')
              ''') #  1     2     3      4             5          6    7        8           9                  10            11
    connection.commit()
    # Азитрмицин 500
    # Азитромицин 250
    # Индапамид 2.5
    # ИТРАКОНАЗОЛ 100
    # ЛЕВОФЛОКСАЦИН 500
    # Лоперамид 10
    # НИФУРОКСАЗИД  100 №30
    # НИФУРОКСАЗИД  200 №20
    # Омепразол 30
    # Пироксикам 10
    # Пироксикам 20
    # Флуконазол 150
    # Флуконазол 50
    # Флуоксетин

    connection.commit()

    connection.close()


if __name__ == '__main__':
    # CreateLogDB()
    #clearparse()
    #prnpcs()
    CreateParentDB()
