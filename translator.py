import requests


#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(text, to_lang, from_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang: язык, на который переводить
    :param from_lang: язык, с которого переводить
    :param text: исходный текст
    :return: переведенный текст
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': from_lang+'-'+to_lang.format(to_lang),
    }
    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])


def new_file(filename, lang):
    """
    :param filename: имя файла из первого input
    :param lang: язык, на который переводить, из второго input
    :return: имя файла с переводом
    """
    input_lang = text_name[0:2]
    output_name = input_lang.upper() + '-' + output_lang.upper() + '.txt'
    try:
        with open(text_name, encoding="utf-8") as f:
            for line in f:
                line_tr = translate_it(line, output_lang, input_lang)
                with open(output_name, 'a', encoding='utf-8') as d:
                    d.write(line_tr)
        message = f'Перевод в файле: {output_name}'
    except FileNotFoundError:
        message = 'Такого файла не существует'
    except KeyError:
        message = 'Неправильно указан язык для перевода'
    return (message)


if __name__ == '__main__':
    text_name = input('Укажите имя файла для перевода, например, DE.txt ')
    output_lang = input('Укажите, на какой язык переводить, например, ru ')
    # text_name = 'de.txt' # отладка
    # output_lang = 'ru' # отладка
    print(new_file(text_name, output_lang))
