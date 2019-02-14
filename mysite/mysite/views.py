from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse # 페이지 이동
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.http import HttpResponse
import numpy as np
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def Pandas_Graph(request):
    fig=plt.figure(figsize=(6, 4.5), dpi=80, facecolor='w', edgecolor='w')
    ax=fig.add_subplot(111)

    f=pd.DataFrame({'y':np.random.randn(10),'z':np.random.randn(10)},
                   index=pd.period_range('1-2000',periods=10))
    f.plot(ax=ax)
    canvas=FigureCanvas(fig)
    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
