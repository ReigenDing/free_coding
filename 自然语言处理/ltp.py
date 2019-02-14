import os
import pyltp

# 模型的路径
LTP_DATA_DIR = r'D:\work\data_collectors\ltp_data'
# 分词模型
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')
# 词性标注模型
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')
# 实体识别模型
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')
# 依存句法分析模型#
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')

def test_first():
    LTP_DATA_DIR = r'D:\work\data_collectors\ltp_data'
    pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`

    from pyltp import Postagger
    postagger = Postagger() # 初始化实例
    postagger.load(pos_model_path)  # 加载模型

    words = ['欧几里得', '是', '西元前', '三', '世纪', '的', '希腊', '数学家', '。']
    postags = postagger.postag(words)  # 词性标注

    print(' '.join(postags))
    postagger.release()  # 释放模型


# 基于LTP的分词
def word_segmentation(sentence):
    cws_ = pyltp.Segmentor()
    cws_.load(cws_model_path)
    words = cws_.segment(sentence)
    print('\t'.join(words))
    cws_.release()
    return words


# 基于LTP的词性标注
def word_posttagger(sentence):
    pos_ = pyltp.Postagger()
    pos_.load(pos_model_path)
    result = pos_.postag(sentence)
    print(type(result))
    print('\t'.join(result))
    pos_.release()
    return result


# 基于LTP的实体识别
def word_ner(words, pos_tags):
    ner_ = pyltp.NamedEntityRecognizer()
    ner_.load(ner_model_path)
    name_entity = ner_.recognize(words, pos_tags)
    print('\t'.join(name_entity))
    ner_.release()
    return name_entity


# 基于LTP的依存句法分析#
def word_par(words, pos_tags):
    par_ = pyltp.Parser()
    par_.load(par_model_path)
    arcs = par_.parse(words, pos_tags)
    print('\t'.join('%d:%s' % (arc.head, arc.relation) for arc in arcs))
    par_.release()
    return arcs


if __name__ == '__main__':
    word_parse = word_segmentation('国务院总理李克强调研上海外高桥时提出，支持上海积极探索新机制。')
    word_property_list = word_posttagger(word_parse)
    for item in zip(word_parse, word_property_list):
        print(item)
    word_ner(word_parse, word_property_list)
    word_par(word_parse, word_property_list)




