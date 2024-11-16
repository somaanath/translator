
from traceback import print_tb
from transformers import *
classifier = pipeline("translation_en_to_fr", model="trans_en_fa/")


def translator(x):
    trans_text = classifier([x])[0]['translation_text']
    return(trans_text)



