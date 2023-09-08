from main import purchase_info, add_info
import configparser


if __name__ == '__main__':
  config = configparser.ConfigParser()
  config.read('settings.ini')
  login = config['ORM']['login']
  password = config['ORM']['password']
  name_bd = config['ORM']['name_bd']
  name_file = 'tests_data.json'
  add_info(login, password, name_bd, name_file)
  publisher = input('Введите id или имя автора: ')
  purchase_info(login, password, name_bd, publisher)
