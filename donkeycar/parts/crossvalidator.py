#!/usr/bin/env python3
"""
Cross validator

Usage:
    crossvalidator.py  (--model=<model>) [--tub=<tub1,tub2,..tubn>] [--type=(linear|categorical)]

Options:
    -h --help        Show this screen.
    --tub TUBPATHS   List of paths to tubs. Comma separated. Use quotes to use wildcards. ie "~/tubs/*"
    --type TYPE          Either categorical or linear  [default: 'linear']
"""
import os
from docopt import docopt

import donkeycar as dk

#import parts
from donkeycar.parts.camera import ImageListCamera
from donkeycar.parts.keras import KerasCategorical, KerasLinear
from donkeycar.parts.datastore import TubGroup, TubWriter


def validate(model_path=None, tub_names=None, model_type='linear'):
    #path_mask = tub_path + "/*.jpg"
    #cam = ImageListCamera(path_mask=path_mask)

    print("Using a model of type: ", model_type)
    if model_type == "categorical":
        kl = KerasCategorical()
    elif model_type == "linear":
        kl = KerasLinear()

    if model_path:
        kl.load(model_path)

    #index = 0
    #while index < cam.length():
    #    index += 1
    #    frame = cam.run_threaded()
    print('tub_names', tub_names)
    #if not tub_names:
    #    tub_names = os.path.join(cfg.DATA_PATH, '*')
    tubgroup = TubGroup(tub_names)

    X_keys = ['cam/image_array']
    y_keys = ['user/angle', 'user/throttle']

    cross_val_gen, val_gen = tubgroup.get_train_val_gen(X_keys, y_keys,
                                                    batch_size=1,
                                                    train_frac=1.0)
    total_records = len(tubgroup.df)
    print('cross validation set size: %d' % total_records)

    for (X, Y) in cross_val_gen:
        #print('size %d' % len(Y))
        angle = Y[0]
        throttle = Y[1]
        print('CORRECT VALUES: angle: ', angle, " and throttle: ", throttle)
        img = X[0][0]

        steering_estimate, throttle_estimate = kl.run(img)
        print('ESTIMATES: angle: ', steering_estimate, " and throttle: ", throttle_estimate)


if __name__ == '__main__':
    args = docopt(__doc__)
    validate(model_path=args['--model'], tub_names=args['--tub'], model_type='linear')
