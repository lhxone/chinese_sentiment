import os
import codecs

POS = os.path.join(os.getcwd(), 'corpus', 'pos')
NEG = os.path.join(os.getcwd(), 'corpus', 'neg')
FIX_POS = os.path.join(os.getcwd(), 'fix_pos')
FIX_NEG = os.path.join(os.getcwd(), 'fix_neg')


def fix_corpus(dir_s, dir_t):
    for item in os.listdir(dir_s):
        with open(os.path.join(dir_s, item), 'r') as f:
            try:
                s = f.read()
                fix_s = s
            except UnicodeDecodeError:
                try:
                    fix_s = s
                except UnicodeDecodeError:
                    fix_s = s
            with codecs.open(os.path.join(dir_t, item), 'w', encoding='utf8') as ff:
                ff.write(fix_s)


if __name__ == "__main__":
    if not os.path.isdir(FIX_POS):
        os.mkdir(FIX_POS)
    if not os.path.isdir(FIX_NEG):
        os.mkdir(FIX_NEG)
    fix_corpus(POS, FIX_POS)
    fix_corpus(NEG, FIX_NEG)
