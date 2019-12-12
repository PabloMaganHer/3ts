import os
import sys

if __name__ == '__main__':
    replace = sys.argv[1]
    function_name = sys.argv[2]
    os.system("mkdir cloud_functions_2build")
    os.system("mkdir cloud_functions_2build/{function_name}".format(function_name=function_name))
    with open('cloud_functions/{function_name}/main.py'.format(function_name=function_name), 'r') as fun:
        file = fun.read()
        if replace=="True":
            replaced_file = file.replace("_develop", "_production")
        else:
            replaced_file = file
    with open('cloud_functions_2build/{function_name}/main.py'.format(function_name=function_name), 'w') as re_fun:
        re_fun.write(replaced_file)
