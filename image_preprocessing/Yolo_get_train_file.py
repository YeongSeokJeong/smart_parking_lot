import argparse
import os
parser = argparse.ArgumentParser(description= '')
parser.add_argument('file_path')
parser.add_argument('output_file_path')
args = parser.parse_args()
path = os.getcwd()

file_list = os.listdir(args.file_path)
file_list = list(set([file_name.split('.')[0] + '.jpg' for file_name in sorted(list(file_list))]))

with open(args.output_file_path, 'w') as fw:
	for file_name in sorted(file_list):
		fw.write(path + args.file_path[1:] + '/' + file_name + '\n') 
