from module.deriveReportContent import deriveReport
import pickle
import requests

print('翻訳したいファイルのパスを教えてください')
path = input()
deriveReport(path)

file_name = path.split('/')[-1].split('.')[0]
pickle_save_path = f'doc/{file_name}/content.pickle'
with open(pickle_save_path, mode='rb') as f:
  [content, section_title, addtion] = pickle.load(f)

## 英語の翻訳
translate_content = []
API_KEY = 'bfc6a8ca-e35f-2062-627b-7466d6c3d5fa:fx' # 自身の API キーを指定
source_lang = 'EN'
target_lang = 'JA'

for c in content:
  text = c.replace('[', '(').replace(']', ')')
  # パラメータの指定
  params = {
              'auth_key' : API_KEY,
              'text' : text,
              'source_lang' : source_lang, # 翻訳対象の言語
              "target_lang": target_lang  # 翻訳後の言語
          }

  # リクエストを投げる
  request = requests.post("https://api-free.deepl.com/v2/translate", data=params) # URIは有償版, 無償版で異なるため要注意
  result = request.json()
  translate_content.append(text+'\n'+result["translations"][0]["text"])

##翻訳内容をテキストとして保存
with open(f'doc/{file_name}/translate.txt', mode='w') as f:
  f.write('\n\n'.join(translate_content))

print(f'翻訳した内容は"doc/{file_name}/translate.txt"に保存されました')