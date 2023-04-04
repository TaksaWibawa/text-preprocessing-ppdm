import re
import nltk
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

nltk.download('stopwords')
nltk.download('punkt')

factory = StemmerFactory()
stemmer = factory.create_stemmer()


def case_folding(sentence):
    sentence = re.sub(r'[^\w\s]', '', sentence)  # Menghilangkan tanda baca
    sentence = re.sub(r'[0-9]', '', sentence)  # Menghilangkan angka
    sentence = sentence.lower()  # Mengubah ke huruf kecil
    sentence = sentence.strip()  # Menghilangkan spasi di awal dan akhir kalimat
    sentence = re.sub(r'\s+', ' ', sentence)  # Menghilangkan spasi ganda
    sentence = re.sub(r'\n', ' ', sentence)  # Menghilangkan enter
    return sentence


def tokenize(sentence):
    tokens = nltk.word_tokenize(sentence)
    return tokens


def remove_stopwords(tokens):
    # stopwords = nltk.corpus.stopwords.words('indonesian')
    # filtered_tokens = [token for token in tokens if token not in stopwords]
    stopwords = StopWordRemoverFactory().get_stop_words()
    filtered_tokens = [token for token in tokens if token not in stopwords]
    return filtered_tokens


# mengubah menjadi kata baku bahasa indonesia
# perlu update!
def stemming(filtered_tokens):
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    # # stemmed_tokens = [re.sub(r'(.)\1+', r'\1', token) for token in stemmed_tokens]
    stemmed_tokens = [re.sub(r'^(\w)\1+', r'\1', token) for token in stemmed_tokens] # menghilangkan huruf berulang di awal
    stemmed_tokens = [re.sub(r'(\w)\1+$', r'\1', token) for token in stemmed_tokens] # menghilangkan huruf berulang di akhir
    stemmed_text = ' '.join(stemmed_tokens)
    return stemmed_text