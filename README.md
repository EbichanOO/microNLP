# microNLP
言語系APIサーバー群を作成中...\
将来的にk8sで管理する為にdockerfileも作成しています

## word2vec API Server
word2vecを利用した機能を実装したサーバを作成\
モデルのハイパーパラメータ等は[wiki entity vectors](https://github.com/singletongue/WikiEntVec/tree/38a767015675c423075c780ef550777a77aa45b5)を参照
* 単語をベクトルに変換して返す (/word2vec POST)