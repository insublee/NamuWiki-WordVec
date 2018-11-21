from gensim.models import word2vec
import ijson
from konlpy.tag import Twitter
import re
from libs.mail import send
from datetime import datetime

twitter = Twitter()
s = datetime.now()
print("[LOG] Start File Preprocessing")


def get_learn_data(content):
    content = re.sub('[-=.#/?:$}]', '', content)
    morphs = twitter.pos(content)

    results = []

    for word in morphs:
        if not word[1] in ["Josa", "Eomi", "Punctuation"]:
            results.append(word[0])

    return (" ".join(results)).strip()


wataki_file = 'namu_wiki.wataki'


def load_json(filename):
    with open(filename, 'r') as fd:
        parser = ijson.parse(fd)
        with open(wataki_file, 'w', encoding='utf-8') as w:
            for prefix, event, value in parser:
                if prefix.endswith('.text'):
                    lines = value.split('\n')
                    for l in lines:
                        result = get_learn_data(l)
                        try:
                            w.write(result+"\n")
                        except:
                            pass


load_json("namuwiki_20180326.json")

e = datetime.now()
send("[WordVec] Preprocessing is Finished", "전처리 과정이 완료되었습니다.", s, e)
s = datetime.now()

data = word2vec.LineSentence(wataki_file)
model = word2vec.Word2Vec(data, size=1000, window=10, hs=1, sg=1)
model.save("namu.model")

e = datetime.now()
send("[WordVec] Learning is Finished", "워드벡터 학습이 완료되었습니다.", s, e)
