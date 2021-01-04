import requests

URL = 'http://translate.google.com/translate_tts'
DEFAULT_LANG = 'English'
LANGUAGES = {	'Afrikaans' : 'af',
				'Albanian' : 'sq',
				'Arabic' : 'ar',
				'Armenian' : 'hy',
				'Bengali' : 'bn',
				'Bosnian' : 'bs',
				'Catalan' : 'ca',
				'Chinese' : 'zh-CN',
				'Chinese (taiwan)' : 'zh-TW',
				'Croatian' : 'hr',
				'Czech' : 'cs',
				'Danish' : 'da',
				'Dutch' : 'nl',
				'English' : 'en',
				'Esperanto' : 'eo',
				'Estonian' : 'et',
				'Finnish' : 'fi',
				'French' : 'fr',
				'German' : 'de',
				'Greek' : 'el',
				'Hindi' : 'hi',
				'Hungarian' : 'hu',
				'Icelandic' : 'is',
				'Indonesian': 'id',
				'Italian' : 'it',
				'Japanese' : 'ja',
				'Javanese' : 'jv',
				'Kannada' : 'kn',
				'Khmer' : 'km',
				'Korean' : 'ko',
				'Latin' : 'la',
				'Latvian' : 'lv',
				'Macedonian' : 'mk',
				'Malayalam' : 'ml',
				'Marathi' : 'mr',
				'Myanmar (burmese)' : 'my',
				'Nepali' : 'ne',
				'Norwegian' : 'no',
				'Polish' : 'po',
				'Portugese' : 'pt',
				'Romanian' : 'ro',
				'Russian' : 'ru',
				'Serbian' : 'sr',
				'Sinhala (sinhalese)' : 'si',
				'Slovak' : 'sk',
				'Spanish' : 'es',
				'Sundanese' : 'su',
				'Swahili' : 'sw',
				'Swedish' : 'sv',
				'Tagalog (filipino)' : 'tl',
				'Tamil' : 'ta',
				'Telegu' : 'te',
				'Thai' : 'th',
				'Turkish' : 'tr',
				'Ukrainian' : 'uk',
				'Urdu' : 'ur',
				'Vietnamese' : 'vi',
				'Welsh' : 'cy'
}
PARAMS = {	'ie' : 'UTF-8',
			'client' : 'tw-ob'
}

def text_to_speech(language, text):
	global URL
	global PARAMS
	global LANGUAGES
	PARAMS['tl'] = LANGUAGES[language]
	PARAMS['q'] = text
	r = requests.get(url = URL, params = PARAMS)
	if r.status_code == 200:
		open('tts.mp3', 'wb').write(r.content)