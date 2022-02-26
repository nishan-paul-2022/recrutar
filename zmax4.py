import os
import math
import webbrowser
import subprocess

import tkinter as tk
from functools import partial
from tkinter import *
from tkinter.filedialog import askopenfilename, askopenfilenames


# https://www.geeksforgeeks.org/dynamically-resize-buttons-when-resizing-a-window-using-tkinter/
def dynamically_create_interface(window_title, function_packages):
	window = Tk()
	window.title(window_title)
	window.minsize(400, 200)

	function_exit = ['EXIT', window.destroy]
	function_packages.append(function_exit)

	count = len(function_packages)
	row = math.ceil(math.sqrt(count))
	column = row

	idx = 0
	for i in range(row):
		for j in range(column):
			if idx >= count:
				break
			function_name = function_packages[idx][0]
			function_set = function_packages[idx][1:]

			button = Button(window, text=function_name, padx=10, pady=10, bg="#2C3333", fg="white", command=partial(*function_set))
			button.grid(row=i, column=j, sticky="NSEW", padx=10, pady=10)
			idx += 1

	for i in range(row):
		Grid.rowconfigure(window, i, weight=1)
	for j in range(column):
		Grid.columnconfigure(window, j, weight=1)

	window.mainloop()


if __name__ == '__main__':
	directory = 'E:/CODE/PYTHON'
	prefix = 'done_backend'
	project_list = list()
	port_numbers = 8000
	for item in os.listdir(directory):
		check1 = os.path.isdir(os.path.join(directory, item))
		check2 = item.startswith(prefix)
		if check1 and check2:
			port_numbers += 1
			project_list.append((item, port_numbers))
	print(project_list)

	function_packages = list()
	for project_name, port_number in project_list:
		link = f'http://127.0.0.1:{port_number}/'
		path = f'{directory}/{project_name}'

		run_server = f'D:/C-PART-2/m2021/Scripts/activate.bat && ' \
				     f'py manage.py makemigrations main && ' \
				     f'py manage.py migrate && ' \
				     f'py manage.py runserver {port_number}'

		def function(link, cmd):
			webbrowser.open(link)
			print(path)
			os.system(f'start cmd /K && E: && cd E:/CODE/PYTHON/done_backend_job_recruitment && '
			                 f'git pull && '
			                 f'git add . && '
			                 f'git commit -m "1st commit" && '
			                 f'git push https://nishan-paul-2022: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@github.com/nishan-paul-2022/recrutar.git --all &&'
			                 f'{cmd}')

			subprocess.Popen(['start', 'cmd', '/k', cmd], shell=True)

		function_package = (project_name, function, link, run_server)
		function_packages.append(function_package)

	dynamically_create_interface('window_title', function_packages)

# https://stackoverflow.com/questions/55920419/how-to-write-to-command-line-using-python