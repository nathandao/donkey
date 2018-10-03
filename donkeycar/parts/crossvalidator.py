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
import statistics
import numpy as np
from donkeycar.parts.keras import KerasCategorical, KerasLinear
from donkeycar.parts.datastore import TubGroup


def print_mean(l, message):
    means = statistics.mean(l)
    print(message, " means: ", means)


def validate(model_path=None, tub_names=None, model_type='linear'):
    print("Using a model of type: ", model_type)
    if model_type == "categorical":
        kl = KerasCategorical()
    elif model_type == "linear":
        kl = KerasLinear()

    if model_path:
        kl.load(model_path)

    print('tub_names', tub_names)
    tubgroup = TubGroup(tub_names)

    # See Also: ShowPredictionPlots

    for tub in tubgroup.tubs:
        num_records = tub.get_num_records()
        print('cross validation set size: %d' % num_records)

        correct_angles = []
        correct_throttles = []
        estimate_angles = []
        estimate_throttles = []

        for iRec in tub.get_index(shuffled=False):
            record = tub.get_record(iRec)

            img = record["cam/image_array"]
            user_angle = float(record["user/angle"])
            user_throttle = float(record["user/throttle"])
            pilot_angle, pilot_throttle = kl.run(img)

            correct_angles.append(user_angle)
            correct_throttles.append(user_throttle)
            estimate_angles.append(pilot_angle.item())
            estimate_throttles.append(pilot_throttle.item())

            #print('CORRECT VALUES: angle: ', user_angle, " and throttle: ", user_throttle)
            #print('ESTIMATES:      angle: ', pilot_angle, " and throttle: ", pilot_throttle)

        print_mean(correct_angles, "Correct angle")
        print_mean(estimate_angles, "Estimate angle")

        print_mean(correct_throttles, "Correct throttle")
        print_mean(estimate_throttles, "Estimate throttle")


if __name__ == '__main__':
    args = docopt(__doc__)
    validate(model_path=args['--model'], tub_names=args['--tub'], model_type=args['--type'])
