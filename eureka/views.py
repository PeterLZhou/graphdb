# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from neo4j.v1 import GraphDatabase, basic_auth
from .forms import QueryForm

#DatabaseCall is the query call to a database that returns the string containing the answer?

context_dict = {'message': "This is a key value pair"}

def index(request):
    form = QueryForm()
    return render(request, 'eureka/index.html', {'form': form})

def graph(request):  
    driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo4j"))
    session = driver.session()
    if request.method == 'POST':
        receivedform = QueryForm(request.POST)
        if (receivedform.is_valid()):
            data = receivedform.cleaned_data
            stringlist = data['question'].split()
            person = stringlist[1]
            classofperson = stringlist[3]
            employer = stringlist[5]
            # results = session.run("match (n) return n as person")
            results = session.run("match (n:" + classofperson + " {name:'" + person + "'})-[r:WORKS_AT]->(m {name:'" + employer + "'}) return n as person")
            print "match (n:" + classofperson + " {name:'" + person + "'})-[r:WORKS_AT]->(m {name:'" + employer + "'}) return n as person"
    else:
        results = session.run(
            "MATCH (n:Person) "
            "RETURN n.Name AS person")
    nodes = []
    hasresults = False
    for thing in results:
        print thing["person"]
        hasresults = True
        #nodes.append(thing["person"])
        #session.close()
    if hasresults is False:
        nodes.append("no")
    else:
        nodes.append("yes")
#If nodes not empty, then return the nodes. If nodes empty, return no/not sure
    return render_to_response('eureka/results.html', {"nodes": nodes})

#We need to make a procedure for creating nodes? Object Oreinted Graph Search
