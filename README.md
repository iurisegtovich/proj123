installation:

    quick (with git):

pip install git+https://github.com/iurisegtovich/proj123 #pip list #...
#pip uninstall proj123

    quick (without git)

pip install https://github.com/iurisegtovich/proj123/archive/master.zip #pip list #...
#pip uninstall proj123

    dev mode (git required):

git clone https://github.com/iurisegtovich/proj123 proj123-master

pip install -e ./proj123-master

#pip list #>>> proj123 0.0.2 /home/segtovichisv/Desktop/proj123-master #pip uninstall proj123

    or

#@/path/to/projct_xyz pip install -e git+https://github.com/iurisegtovich/proj123#egg=proj123 #pip list #proj123 0.0.2 /home/segtovichisv/Desktop/some_other_project/src/proj123 #pip uninstall proj123
