from django.shortcuts import render, get_object_or_404
from sumStats.models import Genotype, SequenceLength
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from collections import defaultdict
import json as JSON
from scipy import stats
import numpy as np
from django.db import models
from sumStats.forms import StatForm

#class IndexView(generic.ListView):
 #   template_name = 'sumStats/index.html'
  #  context_object_name = 'latest_genotype_list'
    
   # def get_queryset(self):
    #    return Genotype.objects.filter(
     #       pub_date__lte = timezone.now()
      #      ).order_by('-pub_date')[:5]

    
class DetailView(generic.DetailView):
    model = Genotype
    template_name = 'sumStats/detail.html'

def getModelNames():
    allModels = models.get_models(models.get_app('sumStats'))
    allModelNames=[]
    for model in allModels:
        allModelNames.append(model._meta.verbose_name_raw.replace(" ",""))
    return allModelNames[1:]

def index(request):
    latest_genotype_list = Genotype.objects.order_by('-pub_date')[:5]
    form = StatForm(auto_id=False)
    context = {'latest_genotype_list': latest_genotype_list, 'form':form}
    return render(request, 'sumStats/index.html', context)

def result(request, pk):
    genotype = get_object_or_404(Genotype, pk=pk)
    allSeqs = genotype.sequencelength_set.all()
    itemSum = 0
    count = 0
    for item in allSeqs:
        itemSum += item.seqLen
        count += 1
    meanVal = float(itemSum)/count
    return render(request, 'sumStats/result.html', {'mean':meanVal})

def makeBar(request, genotype_ids, modelName):

    data = []
    for item in genotype_ids:
        genotype = get_object_or_404(Genotype, pk=item)
        exec("seqSet = genotype.%s_set.all()"%modelName)
        genotype_name = "%s" % genotype
        dataDict = defaultdict(list)
        dataDict['genotype_name'] = genotype_name
        allSeqLens = []
        for innerItem in seqSet:  
            seqName = "%s" % innerItem
            seqLen = innerItem.seqLen
            allSeqLens.append(seqLen)
            dataDict['seqObject'].append({'genotype_name':genotype_name, 'seqName':seqName, 'seqLen':seqLen})
        
        allSeqLens = np.array(allSeqLens)
        seqLenMean = np.mean(allSeqLens)
        seqLenSem = stats.sem(allSeqLens)
        dataDict['seqLenMean'] = seqLenMean
        dataDict['seqLenSem'] = seqLenSem
        data.append(dataDict)
    return JSON.dumps(data)

def makeStat(request, genotype_ids, modelName):
    
    return "sameer"

def makeKS(request, genotype_ids):
    allModelNames = getModelNames()
    
    data = {}
    criticalValue = 0.05
    
    for model in allModelNames:
        genotype = get_object_or_404(Genotype, pk=genotype_ids[0])
        exec("seqSet = genotype.%s_set.all()"%model)
        allSeqLens = []
        for innerItem in seqSet:
            allSeqLens.append(innerItem.seqLen)

        allSeqLens = np.array(allSeqLens)
        mu = np.mean(allSeqLens)
        sigma = np.std(allSeqLens)
    
        normed_allSeqLens = (allSeqLens - mu)/sigma
        result = stats.kstest(normed_allSeqLens, 'norm')
        
        if result[1] >= 0.05:
            hyp = True
        else:
            hyp = False
        
        data[model] = {"kstest":result, "hypothesis":hyp} 
    return data

def genBar(request):

    queryList = dict(request.POST.iterlists())
    genotype_ids = queryList.get('genotype_ids')

    modelName = str(queryList.get('modelName')[0])

    if modelName[-2:]=='gc':
        yAxisText = 'GC Content'
    else:
        yAxisText = 'Length'
       
    dataJson = "Select appropriate number of genotypes. n=1 for K-S, n=2 for hypothesis test, n>0 for bar graphs"
    template = 'warning.html'
    
    if genotype_ids != None:
        if 'makeBar' in request.POST:
            dataJson = makeBar(request, genotype_ids, modelName)
            template = 'genBar.html'
        elif 'genStat' in request.POST:
            if len(genotype_ids) ==2:
                dataJson = makeStat(request, genotype_ids, modelName)
                template = 'genStats.html' 
        elif 'genKS' in request.POST:
            if len(genotype_ids) == 1:
                dataJson = makeKS(request, genotype_ids)
                template = 'genKS.html'

    return render(request, 'sumStats/%s'%(template), {'result': dataJson, 'modelName':modelName, 'yAxisText': yAxisText})
 
#def detail(request, genotype_id):
 #    genotype = get_object_or_404(Genotype, pk=genotype_id)
  #   return render(request, 'sumStats/detail.html', {'genotype':genotype})
