from configparser import ConfigParser


def read_db_con(filename='db_config.ini', section='oracle'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db


def print_db():
    try:
        print(read_db_con())
    except Exception as error:
        print("Error has occurred :" + error.args[0])
