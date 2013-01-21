# -*- coding: utf-8 -*-  pylint: disable-msg=R0801
#
# Copyright (c) 2013 Rodolphe Quiédeville <rodolphe@quiedeville.org>
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
The django views
"""
import logging
from django.shortcuts import render
from lolyx.llx.models import Job

logger = logging.getLogger(__name__)


def home(request):
    """
    The home page
    """
    last_jobs = Job.objects.filter(status__gt=0).order_by('-date_published')[:5]
    return render(request,
                  'home.html',
                  {'last_jobs': last_jobs})
