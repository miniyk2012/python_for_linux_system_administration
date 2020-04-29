import configparser

if __name__ == "__main__":
    cf = configparser.ConfigParser(allow_no_value=True)
    cf.read('./my.cnf')

    print(cf.sections())
    print(cf.has_section('client'))
    print(cf.has_option('client', 'host'))
    print(cf.get('mysqld', 'skip-external-locking'))
    print(type(cf.get('client', 'port')))
    print(cf.get('client', 'port'))
    print(cf.get('mysqld', 'has-data'))
    print(cf.getboolean('mysqld', 'has-data'))