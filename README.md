installation:

    quick (pip install git+):

#@anywhere
pip install git+https://github.com/iurisegtovich/proj123 #pip list #...
#pip uninstall proj123

    quick (pip install master.zip)

#@anywhere
pip install https://github.com/iurisegtovich/proj123/archive/master.zip #pip list #...
#pip uninstall proj123

    dev mode (git clone + pip install -e .):

#@/path/to/installation_dir
git clone https://github.com/iurisegtovich/proj123 proj123-master

pip install -e ./proj123-master

#pip list #>>> proj123 0.0.2 /home/segtovichisv/installation_dir/proj123-master
#pip uninstall proj123

    dev mode (pip install -e git+):

#@/path/to/some_other_project
pip install -e git+https://github.com/iurisegtovich/proj123#egg=proj123

#pip list #>>> proj123 0.0.2 /home/segtovichisv/some_other_project/src/proj123
#pip uninstall proj123
