# Futucar

These instructions are shortcuts for more general knowledge found in [donkeycar docs](http://docs.donkeycar.com/)

Install the SW stack using those instructions. If using OSX then remember to use the same version of Tensorflow as in the car (atm ==v 1.8)

Note!! Keras models are NOT compatible between different tensorflow versions!

## Additional packages
Roughly follow these instructions for setting up the symlink to cv2.so lib
https://www.learnopencv.com/install-opencv3-on-macos/

source activate donkey
### First install opencv using brew
brew install opencv   

### Then install some python crap
pip install numpy scipy matplotlib scikit-image scikit-learn ipython pandas


### Python expects to find opencv library from <python-ver>/site-packages/cv2.so BUT of course installer installs it with different name 
find /usr/local/opt/opencv/lib/ -name cv2*.so
<should output something like /usr/local/opt/opencv/lib//python3.7/site-packages/cv2.cpython-37m-darwin.so>
<Go to your miniconda env folder>
cd ~/miniconda3/envs/donkey/lib/python3.6/site-packages

ln -s /usr/local/opt/opencv/lib/python3.7/site-packages/cv2.cpython-37m-darwin.so cv2.so

## Create car

We have our own template, create it to your home folder like this:

   ´donkey createcar --template donkey2futucar ~/futucar´

## Gather training data

TODO using the real car

Or using the simulator, just follow [donkey instructions](http://docs.donkeycar.com/guide/simulator/#typical-use)

## Train the model

    ´cd ~/futucar´
    ´python manage.py train --model=<output-path-to-model> --tub=<path-to-data> --type=<linear|categorical>´   


## Test the model

TODO Either using the car

Or the simulator, first run the server and then using the simulator app.

    ´donkey sim --type <linear|categorical> --model <path-to-model>´
