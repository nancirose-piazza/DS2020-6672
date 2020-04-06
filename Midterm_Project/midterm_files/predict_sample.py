#!/usr/bin/env python

#import all the needed libraries
import os
import sys
import warnings
warnings.filterwarnings("ignore")
try:
	import ember
except:
	os.system('wget https://github.com/endgameinc/ember/archive/master.zip')
	os.system('unzip master.zip')
	os.system('rm master.zip')
	os.system('cp -r ember-master/* .')
	os.system('rm -r ember-master')
	os.system('pip install -r requirements.txt')
	os.system('python setup.py install')
	import ember
import pickle
import argparse
try:
	import numpy as np
except:
	os.system("pip install numpy")
	import numpy as np


from tensorflow.python.util import deprecation
deprecation._PRINT_DEPRECATION_WARNINGS = False


try:
	import tensorflow as tf
	#tf.compat.v1.disable_eager_execution()
except:
	os.system("pip install tensorflow")
	import tensorflow as tf
	#tf.compat.v1.disable_eager_execution()

with open("mms_scaler","rb") as f:
  mms = pickle.load(f)
  f.close()


def main():
    prog = "predict_sample"
    descr = "Using the model to predict a single PE's binary."
    parser = argparse.ArgumentParser(prog=prog, description=descr)
    parser.add_argument("-v", "--featureversion", type=int, default=2, help="EMBER feature version")
    parser.add_argument("binaries", metavar="BINARIES", type=str, nargs="+", help="PE files to classify")
    args = parser.parse_args()

    extractor = ember.PEFeatureExtractor(args.featureversion)
    sample_data = open(args.binaries[0],'rb').read()
    sample_data = extractor.feature_vector(sample_data)
    sample_data = np.array(sample_data, dtype=np.float32)
    sample_data = mms.transform([sample_data])
    sample_data = np.reshape(sample_data,(-1,1,2381))
    model = tf.keras.models.load_model('model.h5')
    pred = model.predict_classes(sample_data)
    if pred[0]==0:
        print("Benign.")
    else:
        print("Malicious")
    print("Completed.")

if __name__ == "__main__":
    main()
