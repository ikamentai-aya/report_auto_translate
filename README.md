# Deeplを使った2カラムの論文の自動翻訳プログラム

## ファイル構造

---doc (翻訳したいファイルや翻訳結果が出てくる)  
 |-module (サブ関数)  
 |-app.py (メイン関数)  
 |_requirements.txt (必要なライブラリのインポート用)  
 
## 使い方

Pythonの仮想環境でこのディレクトリに入り、`pip install -r requirements.txt`を実行  

Deepl Free APIでユーザーIDを取得する  
Deepl公式サイト:https://www.deepl.com/ja/pro/change-plan?cta=menu-login-signup/#team  
参考サイト：https://qiita.com/rihok/items/962890b4b86ea052e54c  

コードの一部を書き換える  
- app.pyのAPIキーを書くコードを自分のものに書き換え  

実行する  
`python app.py`  
その後、翻訳したい論文のパスを入力する

翻訳結果はコンソール上で教えてくれるパス上のテキストファイルとして保存される  

