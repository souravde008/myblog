from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect


def admin_required(func):
	def warp(request, *args, **kwargs):
		if 'admin_id' in request.session.keys():
			return func(request, *args, **kwargs)
		else:
			return redirect("admin-index")
	return warp	