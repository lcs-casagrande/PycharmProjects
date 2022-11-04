from translate import Translator
translator = Translator(from_lang = 'Spanish',to_lang='english')
result = translator.translate('Como vai você?')
print(result)