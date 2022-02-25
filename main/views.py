from django.shortcuts import render, redirect
from django.http import HttpResponse
from main import models

argument = {
	'a0': {
		'plan': 'Basic Plan',
		'color': {'a0': r'&#9989;', 'a1': r'&#10060;', 'a2': r'&#10060;'},
		'bdt': {'a0': 100, 'a1': 500},
		'visibility': 1,
		'listing': 1
	},

	'a1': {
		'plan': 'Standard Plan',
		'color': {'a0': r'&#9989;', 'a1': r'&#9989;', 'a2': r'&#10060;'},
		'bdt': {'a0': 500, 'a1': 2000},
		'visibility': 2,
		'listing': 5
	},

	'a2': {
		'plan': 'Extended Plan',
		'color': {'a0': r'&#9989;', 'a1': r'&#9989;', 'a2': r'&#9989;'},
		'bdt': {'a0': 2500, 'a1': 8000},
		'visibility': 3,
		'listing': 25
	}
}

url_and_view_list = {
	'': 'view_index',
	'index': 'view_index',

	'freelancers_search_companies': 'view_freelancers_search_companies',
	'freelancers_browse_jobs': 'view_freelancers_browse_jobs',
	'freelancers_browse_tasks': 'view_freelancers_browse_tasks',
	'freelancers_job_proposals': 'view_freelancers_job_proposals',
	'freelancers_task_proposals': 'view_freelancers_task_proposals',

	'employers_search_freelancers': 'view_employers_search_freelancers',
	'employers_post_a_job': 'view_employers_post_a_job',
	'employers_post_a_task': 'view_employers_post_a_task',
	'employers_manage_jobs': 'view_employers_manage_jobs',
	'employers_manage_tasks': 'view_employers_manage_tasks',
	'employers_manage_bidders': 'view_employers_manage_bidders',
	'employers_manage_candidates': 'view_employers_manage_candidates',

	'single_company_profile': 'view_single_company_profile',
	'single_freelancer_profile': 'view_single_freelancer_profile',
	'single_job_page': 'view_single_job_page',
	'single_task_page': 'view_single_task_page',

	'account_settings': 'views_dashboard_settings',
	'dashboard_user_record': 'view_dashboard_user_record',
	'dashboard_bookmarks': 'view_dashboard_bookmarks',
	'dashboard_messages': 'view_dashboard_messages',
	'dashboard_reviews': 'view_dashboard_reviews',

	'blog_segment': 'view_blog_segment',
	'blog_post': 'view_blog_post',
	'pages_checkout_page': 'view_pages_checkout_page',
	'about_us': 'view_about_us',
	'pages_invoice_template': 'view_pages_invoice_template',
	'pages_order_confirmation': 'view_pages_order_confirmation',

	'404': 'view_404'
}


def view_index(request):
	context = {}
	return render(request, 'index.html', context)


def view_freelancers_search_companies(request):
	context = {}
	return render(request, 'freelancers_search_companies.html', context)


def view_freelancers_browse_jobs(request):
	context = {}
	return render(request, 'freelancers_browse_jobs.html', context)


def view_freelancers_browse_tasks(request):
	context = {}
	return render(request, 'freelancers_browse_tasks.html', context)


def view_freelancers_job_proposals(request):
	context = {}
	return render(request, 'freelancers_job_proposals.html', context)


def view_freelancers_task_proposals(request):
	context = {}
	return render(request, 'freelancers_task_proposals.html', context)


def view_employers_search_freelancers(request):
	context = {}
	return render(request, 'employers_search_freelancers.html', context)


def view_employers_post_a_job(request):
	context = {}
	return render(request, 'employers_post_a_job.html', context)


def view_employers_post_a_task(request):
	context = {}
	return render(request, 'employers_post_a_task.html', context)


def view_employers_manage_jobs(request):
	context = {}
	return render(request, 'employers_manage_jobs.html', context)


def view_employers_manage_tasks(request):
	context = {}
	return render(request, 'employers_manage_tasks.html', context)


def view_employers_manage_bidders(request):
	context = {}
	return render(request, 'employers_manage_bidders.html', context)


def view_employers_manage_candidates(request):
	context = {}
	return render(request, 'employers_manage_candidates.html', context)


def view_single_company_profile(request):
	context = {}
	return render(request, 'single_company_profile.html', context)


def view_single_freelancer_profile(request):
	context = {}
	return render(request, 'single_freelancer_profile.html', context)


def view_single_job_page(request):
	context = {}
	return render(request, 'single_job_page.html', context)


def view_single_task_page(request):
	context = {}
	return render(request, 'single_task_page.html', context)


def views_dashboard_settings(request):
	data = models.Models_nationality.objects.all()
	context = {'nationalityall': data}
	return render(request, 'account-settings.html', context)


def view_dashboard_user_record(request):
	context = {}
	return render(request, 'dashboard_user_record.html', context)


def view_dashboard_bookmarks(request):
	context = {}
	return render(request, 'dashboard_bookmarks.html', context)


def view_dashboard_messages(request):
	context = {}
	return render(request, 'dashboard_messages.html', context)


def view_dashboard_reviews(request):
	context = {}
	return render(request, 'dashboard_reviews.html', context)


def view_blog_segment(request):
	context = {}
	return render(request, 'blog_segment.html', context)


def view_blog_post(request):
	context = {}
	return render(request, 'blog_post.html', context)


def view_pages_checkout_page(request):
	context = {}
	return render(request, 'pages_checkout_page.html', context)


def view_about_us(request):
	context = {'argument': argument}
	return render(request, 'about_us.html', context)


def view_pages_invoice_template(request):
	context = {}
	return render(request, 'pages_invoice_template.html', context)


def view_pages_order_confirmation(request):
	context = {}
	return render(request, 'pages_order_confirmation.html', context)


def view_404(request):
	context = {}
	return render(request, '404.html', context)
