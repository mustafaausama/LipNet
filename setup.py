from setuptools import setup

setup(name='lipnet',
    version='0.1.6',
    description='End-to-end sentence-level lipreading',
    url='http://github.com/rizkiarm/LipNet',
    author='Muhammad Rizki A.R.M',
    author_email='rizki@rizkiarm.com',
    license='MIT',
    packages=['lipnet'],
    zip_safe=False,
	install_requires=[
        # installing keras==2.4 and then install keras==2.0.2 and tensorflow==1.15.0 and numpy==1.19.0 works
        # but don't know why
        #'keras==2.0.2',
        'editdistance==0.3.1',
		#'h5py',
		'matplotlib==3.3.3',
		'python-dateutil==2.6.0',
		'scipy==1.5.4',
		'Pillow==6.2.0',
		'Theano==0.9.0',
        'nltk==3.2.2',
        'sk-video==1.1.10',
        'dlib==19.21.1',
        'opencv-python',
        'keras==2.0.2',
        'tensorflow==1.15.0',
        'numpy==1.19.0'
        # 'Keras',
        # 'editdistance',
		# 'h5py',
		# 'matplotlib',
		# 'numpy==1.19.2',
		# 'python-dateutil',
		# 'scipy',
		# 'Pillow',
        # 'opencv-python',
        # #'Theano',
		# 'tensorflow==2.3.1',
        # 'nltk',
        # 'sk-video',
        # 'dlib'
    ])
