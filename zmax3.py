# INSERT INTO main_models_nationality (id, nationality)
# VALUES
# (1, 'Argentina'),
# (2, 'Armenia'),
# (3, 'Aruba'),
# (4, 'Australia'),
# (5, 'Austria'),
# (6, 'Azerbaijan'),
# (7, 'Bahamas'),
# (8, 'Bahrain'),
# (9, 'Bangladesh'),
# (10, 'Barbados'),
# (11, 'Belarus'),
# (12, 'Belgium'),
# (13, 'Belize'),
# (14, 'Benin'),
# (15, 'Bermuda'),
# (16, 'Bhutan'),
# (17, 'Bulgaria'),
# (18, 'BurkinaFaso'),
# (19, 'Burundi'),
# (20, 'Cambodia'),
# (21, 'Cameroon'),
# (22, 'Canada'),
# (23, 'CapeVerde'),
# (24, 'CaymanIslands'),
# (25, 'Colombia'),
# (26, 'Comoros'),
# (27, 'Congo'),
# (28, 'CookIslands'),
# (29, 'CostaRica'),
# (30, 'Côted'),
# (31, 'Ivoire'),
# (32, 'Croatia'),
# (33, 'Cuba'),
# (34, 'Curaçao'),
# (35, 'Cyprus'),
# (36, 'CzechRepublic'),
# (37, 'Denmark'),
# (38, 'Djibouti'),
# (39, 'Dominica'),
# (40, 'DominicanRepublic'),
# (41, 'Ecuador'),
# (42, 'Egypt'),
# (43, 'Guadeloupe'),
# (44, 'Guam'),
# (45, 'Guatemala'),
# (46, 'Guernsey'),
# (47, 'Guinea'),
# (48, 'Guinea - Bissau'),
# (49, 'Guyana'),
# (50, 'Haiti'),
# (51, 'Honduras'),
# (52, 'HongKong'),
# (53, 'Hungary'),
# (54, 'Iceland'),
# (55, 'India'),
# (56, 'Indonesia'),
# (57, 'Norway'),
# (58, 'Oman'),
# (59, 'Pakistan'),
# (60, 'Palau'),
# (61, 'Panama'),
# (62, 'PapuaNewGuinea'),
# (63, 'Paraguay'),
# (64, 'Peru'),
# (65, 'Philippines'),
# (66, 'Pitcairn'),
# (67, 'Poland'),
# (68, 'Portugal'),
# (69, 'PuertoRico'),
# (70, 'Qatar'),
# (71, 'Réunion'),
# (72, 'Romania'),
# (73, 'RussianFederation'),
# (74, 'Rwanda'),
# (75, 'Swaziland'),
# (76, 'Sweden'),
# (77, 'Switzerland'),
# (78, 'Turkey'),
# (79, 'Turkmenistan'),
# (80, 'Tuvalu'),
# (81, 'Uganda'),
# (82, 'Ukraine'),
# (83, 'UnitedKingdom'),
# (84, 'UnitedStates'),
# (85, 'Uruguay'),
# (86, 'Uzbekistan'),
# (87, 'Yemen'),
# (88, 'Zambia'),
# (89, 'Zimbabwe');

# index, Home

# freelancers-search-companies, Home, Freelancers, Search Companies
# freelancers-browse-jobs, Home, Freelancers, Jobs
# freelancers-browse-tasks, Home, Freelancers, Tasks
# freelancers-job-proposals, Home, Freelancers, Job Proposals
# freelancers-task-proposals, Home, Freelancers, Task Proposals

# employers-search-freelancers, Home, Employers, Search Freelancers
# employers-post-a-job, Home, Employers, Post a Job
# employers-post-a-task, Home, Employers, Post a Task
# employers-manage-jobs, Home, Employers, Manage Jobs
# employers-manage-tasks, Home, Employers, Manage Tasks
# employers-manage-candidates, Home, Employers, Manage Candidates
# employers-manage-bidders, Home, Employers, Manage Bidders

# dashboard-user-record, Home, Dashboard, User Record
# dashboard-bookmarks, Home, Dashboard, Bookmarks
# dashboard-messages, Home, Dashboard, Messages
# dashboard-reviews, Home, Dashboard, Reviews
# dashboard-settings, Home, Dashboard, Settings

# blog-segment., Home, Blog
# blog-post, Home, Blog, Post

# about-us, Home

# single-company-profile, Home, Search Companies
# single-freelancer-profile, Home, Search Freelancers
# single-job-page, Home, Browse Jobs
# single-task-page, Home, Browse Tasks

# pages-checkout-page, Home,
# pages-invoice-template, Home,
# pages-order-confirmation, Home,
# pages-pricing-plans, Home,

# 404

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
					 f'py manage.py runserver {port_number} && '

		cmd = f'E: && cd {path} && {run_server}'
		git = ["start", "cmd", "/k", f'E: && cd {path}', 'git', 'pull', 'add', '.', 'commit', '-m', '"1st commit"', 'push https://nishan-paul-2022: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@github.com/nishan-paul-2022/recrutar.git --all']

		def function(link_, cmd_):
			webbrowser.open(link_)
			# subprocess.Popen(git, shell=True, stdout=subprocess.PIPE)
			subprocess.Popen(["start", "cmd", "/k", cmd_], shell=True)

		function_package = (project_name, function, link, cmd)
		function_packages.append(function_package)

	dynamically_create_interface('window_title', function_packages)

# https://stackoverflow.com/questions/55920419/how-to-write-to-command-line-using-python