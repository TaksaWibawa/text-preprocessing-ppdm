import re
import nltk
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

nltk.download('stopwords')
nltk.download('punkt')

factory = StemmerFactory()
stemmer = factory.create_stemmer()

norms = {
    'telat': 'terlambat',
    'pakett': 'paket',
    'bahanya': 'bahannya',
    'baguss': 'bagus',
    'disaya': 'di saya',
    'gak': 'tidak',
    'mantul': 'mantap betul',
    'kalo': 'kalau',
    'disini': 'di sini',
    'makasih': 'terima kasih',
    'maap': 'maaf',
    'kaya': 'seperti',
    'difotoo': 'di foto',
    'yg': 'yang',
    'udah': 'sudah',
    'expect': 'mengira',
    'gatau': 'tidak tahu',
    'krn': 'karena',
    'ga': 'tidak',
    'dateng': 'datang',
    'ya': 'iya',
    'direturn': 'dikembalikan',
    'jg': 'juga',
    'ribet': 'susah',
    'tau': 'tahu',
    'akunya': 'aku nya',
    'kok': 'kenapa',
    'pasan': 'pas-pasan',
    'tp': 'tetapi',
    'bgt': 'sekali',
    'pertma': 'pertama',
    'sm': 'seperti',
    'inii': 'ini',
    'karna': 'karena',
    'bngt': 'sekali',
    'tetep': 'tetap',
    'aja': 'saja',
    'retur': 'kembalikan',
    'chat': 'sampaikan',
    'diingetin': 'diingatkan',
    'item': 'hitam',
    'salahh': 'salah',
    'utk': 'untuk',
    'pesenan': 'pesanan',
    'pesen': 'pesan',
    'size': 'ukuran',
    'dqtang': 'datang',
    'pke': 'pakai',
    'mantsp': 'mantap',
    'rekomended': 'direkomendasikan',
    'bnget': 'sekali',
    'segitu': 'seperti itu',
    'sgitu': 'seperti itu',
    'udah': 'sudah',
    'gitu': 'seperti itu',
    'cmn': 'hanya',
    'agak': 'cukup',
    'dkit': 'sedikit',
    'nii': 'ini',
    'ni': 'ini',
    'pdhl': 'padahal',
    'dh': 'sudah',
    'tapi': 'tetapi',
    'la': 'lah',
    'thank you': 'Terima kasih',
    'top markotop': 'terbaik',
    'jeans nya': 'jeansnya',
    'sii': 'sih',
    'tp': 'tetapi',
    'ko': 'kok',
    'dateng': 'datang',
    'sobek²': 'sobek',
    'begini': 'seperti ini',
    'mantep': 'mantap',
    'sm': 'sama',
    'cpt': 'cepat',
    'bgtsih': 'banget sih',
    'mantul': 'mantap sekali',
    'thanks': 'terima kasih',
    'seller': 'penjual',
    'banget': 'sekali',
    'fast respon': 'respon cepat',
    'next': 'selanjutnya',
    'bakal': 'akan',
    'order': 'pesan',
    'sekli': 'sekali',
    'nnti': 'nanti',
    'lagi': 'kembali',
    'cepet': 'cepat',
    'kan': 'itu',
    'pas': 'waktu'
}


def case_folding(sentence):

    def normalization(match):
        return norms[match.group(0)]

    sentence = re.sub(r'[^\w\s]', '', sentence)  # Menghilangkan tanda baca
    sentence = re.sub(r'[0-9]', '', sentence)  # Menghilangkan angka
    sentence = sentence.lower()  # Mengubah ke huruf kecil
    sentence = sentence.strip()  # Menghilangkan spasi di awal dan akhir kalimat
    sentence = re.sub(r'\s+', ' ', sentence)  # Menghilangkan spasi ganda
    sentence = re.sub(r'\n', ' ', sentence)  # Menghilangkan enter
    sentence = re.sub('|'.join(r'\b%s\b' % re.escape(s) for s in norms), normalization, sentence)  # Mengubah kata yang tidak baku
    return sentence


def tokenize(sentence):
    tokens = nltk.word_tokenize(sentence)
    return tokens


def remove_stopwords(tokens):
    stopwords = StopWordRemoverFactory().get_stop_words()
    filtered_tokens = [token for token in tokens if token not in stopwords]
    return filtered_tokens

def stemming(filtered_tokens):
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    # menghilangkan huruf berulang di awal
    stemmed_tokens = [re.sub(r'^(\w)\1+', r'\1', token)
                      for token in stemmed_tokens]
    # menghilangkan huruf berulang di akhir
    stemmed_tokens = [re.sub(r'(\w)\1+$', r'\1', token)
                      for token in stemmed_tokens]
    stemmed_text = ' '.join(stemmed_tokens)
    return stemmed_text
