import os
from typing import List
import requests
import webbrowser as wb
from bs4 import BeautifulSoup


def make_problem_files(_contest: str, _problems: List[str]):
    """
    :param _contest: コンテスト名（大小文字区別なし）
    :param _problems: 問題名（大小文字区別なし）のリスト
    :return: なし
    """
    for p in _problems:
        # URLを指定
        url = 'https://atcoder.jp/contests/{0}/tasks/{0}_{1}'.format(contest.lower(), p.lower())
        # ディレクトリ名を指定
        directory = _contest.upper()
        # HTMLからタイトルを取得
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.find('title').text.replace(' ', '').replace('-', '_')
        # スクリプト名を指定
        script = '{0}/{1}.py'.format(directory, title)

        if not os.path.exists(directory):
            # ディレクトリが存在しない場合新規作成
            os.makedirs(directory)
        if not os.path.exists(script):
            # ファイルが存在しない場合新規作成
            try:
                with open(script, 'w', encoding='utf-8') as f:
                    # 先頭にURLを追記
                    f.write('# ' + url + '\n')
                print('Files Created.   File: {0}'.format(script))
            except:
                print('ERROR: Files Not Created.   File: {0}'.format(script))
        # ブラウザで問題ページを開く（new=2:新しいタブ）
        wb.open(url, new=2, autoraise=True)


if __name__ == '__main__':
    # コンテスト名の入力
    contest = input('Contest(ex. abc123): ')
    # 問題を指定
    problems = input('Problems: ')
    prob_list = []
    if problems.lower() == 'a-f' or problems.lower() == 'all':
        prob_list = ['a', 'b', 'c', 'd', 'e', 'f']
    else:
        prob_list = problems.split(',')
    # ファイルの作成
    make_problem_files(contest, prob_list)
