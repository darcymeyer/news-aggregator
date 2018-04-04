import nltk
import pandas as pd
import numpy as np
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
from sklearn.preprocessing import normalize


def cleaner(text):
    bad = re.compile("[,.'`]")
    eng_stopwords = stopwords.words('english')
    text = text.replace(u'\u2019', "'").replace(u'\u2018', "'").replace(u'\u201c', '"').replace(u'\u201d', '"')
    words = nltk.word_tokenize(text)
    words = [w.lower() for w in words if w[0] in "QWERTYUIOPASDFGHJKLZXCVBNM"]
    words = [re.sub(bad, "", word) for word in words]
    words_cleaned = ' '.join([word for word in words if word not in string.punctuation 
            and word not in eng_stopwords+[u'\u2014', "nt"]
#             and not word.isdigit() # should be taken care of by checking for capital case
            and not word==""])
    return words_cleaned


def organize(lst):
	df = pd.DataFrame(lst)
	df['cleaned'] = df['text'].apply(cleaner)
	tfidf_vectorizer = TfidfVectorizer(ngram_range=(1,2),max_df=0.6, min_df=2, analyzer='word', max_features=1000)
	vectorized = tfidf_vectorizer.fit_transform(df['cleaned'])
	normalized = normalize(vectorized, axis=1) # uses l2 (squares stuff), axis=1 to compute along columns
	num_topics = 20 # TODO: MOVE TO A SETTINGS FILE
	model = NMF(n_components=num_topics)
	W = model.fit_transform(normalized)

	final = [{} for _ in range(num_topics)]
	for i, art in enumerate(W):
		not_sm = normalize(X=np.array(art).reshape(-1,1), norm='l1', axis=0)
		arr = not_sm.reshape(1, -1)[0]
		two_max = np.argsort(arr)[-2:]
		first_guess = two_max[1]#not_sm[two_max].max()
		second_guess = two_max[0]#not_sm[two_max].min()
		if arr[first_guess] > 2*arr[second_guess] or arr[first_guess] > 0.5:
			article = df.loc[i].to_dict()
			article['score'] = arr[first_guess]
			article['score_raw'] = art[first_guess]
			article['pubdate'] = str(article['pubdate'])+" UTC"
			article.pop('cleaned', None)
			article.pop('text', None)
			try:
				final[first_guess]['sources'].append(article)
			except:
				final[first_guess]['sources'] = [article]

	for i in range(len(final)):
		story = final[i]
		largest_score_sum = 0
		largest_score_sum_index = 0
		for j in range(len(story['sources'])):
			source = story['sources'][j]
			score_sum = source['score']+source['score_raw']/10.0
			if score_sum > largest_score_sum:
				largest_score_sum = score_sum
				largest_score_sum_index = j
		cover_article = story['sources'][largest_score_sum_index]
		temp = story['sources'][0]
		story['sources'][0] = cover_article
		story['sources'][largest_score_sum_index] = temp
		story['title'] = cover_article['title']
		story['brief'] = cover_article['blurb'] # TODO: make this better

	for_api = {'stories':final}
	return for_api

