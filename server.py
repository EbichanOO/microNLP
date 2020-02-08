param_path = "./params/entity_vector/entity_vector.model.bin"

# The model has a long times of loading params.
import gensim
model = gensim.models.KeyedVectors.load_word2vec_format(param_path, binary=True)

'''
# if cannot load params, use this
from gensim.models import word2vec
model = word2vec.Word2Vec.load(param_path)
'''
'''
# use case
word = "車"
# word to numpy vector
vector = model[word]
'''


from flask import Flask, request, abort
app = Flask(__name__)

@app.route('/word2vec', methods=['POST'])
def word2vec():
    word = request.form['word']
    if word == "":
        abort(404, {'message':'need any words'})
    else:
        return str(model[word])

app.run(port=8080)