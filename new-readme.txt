first of all unzip the provided ffmeg files in a directory
and add that directory/bin to you environment variables. And
restart your pc.

then create a new environment in anaconda with python=3.7 .
then navigate to this directory and run the following command.
pip install -e .
then run another command.
pip install -r requirements.txt
then run
cd evaluation
then run the following command.
python predict3.py models/overlapped-weights368.h5 samples/id2_vcd_swwp2s.mpg
