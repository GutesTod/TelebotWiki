import wikipedia, re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

clf,vectorizer = None, None
alphabet = ' 1234567890-=qwertyuiop[]asdfghjkl;zxcvbnm,.\/йцукенгшщзхъфывапролджэячсмитьбю.'


async def clean_str(r):
    r = r.lower()
    r = [c for c in r if c in alphabet]
    return await ''.join(r)


async def update():
    with open('dialogues.txt', encoding='utf-8') as f:
        content = f.read()
    blocks = content.split('\n')
    dataset = []
    for block in blocks:
        replicas = block.split('\\')[:2]
        if len(replicas) == 2:
            pair = [clean_str(replicas[0]), clean_str(replicas[1])]
            if pair[0] in pair[1]:
                dataset.append(pair)
    X_test = []
    Y = []
    for question, answer in dataset[:10000]:
        X_test.append(question)
        Y += [answer]
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(X_test)
    clf = LogisticRegression()
    clf.fit(X, Y)


async def get_generative_replica(text):
    text_vector = vectorizer.transform([text]).toarray()[0]
    question = clf.predict([text_vector])[0]
    return await question


async def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        return await wikitext2
    except Exception as e:
        return await 'В Википедии нет информации об этом'
