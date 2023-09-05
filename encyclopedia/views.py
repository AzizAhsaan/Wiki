from django.shortcuts import render
from . import util
import markdown
import random
def convertmd(title):
   file = util.get_entry(title)
   #markdown = Markdown()   if file == None:
     return None
   else:
     return markdown.Markdown().convert(file)


def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entrymethod(request,title):
   content = convertmd(title)
   if content == None:
      return render(request, "encyclopedia/errorpage.html",{"errormessge":"This entry you are looking for doesn't exist"})
   else:
      return render(request, "encyclopedia/entrypage.html",{"title":title, "content":content})

def searchbar(request):
   if request.method == "POST":
      search = request.POST['q']
      content = convertmd(search)
      if content is not None:
         return render(request, "encyclopedia/entrypage.html",{"title:":search, "content":content})
      else:
         allentries= util.list_entries()
         suggestentry=[]
         for entry in allentries:
            if search.lower() in entry.lower():
               suggestentry.append(entry)
         return render(request, "encyclopedia/search.html", {"text":suggestentry} )

def newpage(request):
   if request.method == "GET":
      return render(request, "encyclopedia/newpage.html")
   else:
      title=request.POST['title']
      content =request.POST['content']
      Title=util.get_entry(title)
      if Title is not None:
         return render(request, "encyclopedia/errorpage.html",{"errormessge":"The page that you have created does already exist!"})
      else:
         util.save_entry(title, content)
         contents=convertmd(title)
         print(title)
         return render(request, "encyclopedia/entrypage.html", {"title":title, "content":contents})

def editpage(request):
   if request.method == "POST":
      title = request.POST['entrytitle']
      content = util.get_entry(title)
      return render(request, "encyclopedia/editpage.html", {"title":title, "content":content})

def thenewedit(request):
   if request.method == "POST":
      title=request.POST['title']
      content = request.POST['content']
      util.save_entry(title, content)
      contents=convertmd(title)
      return render(request, "encyclopedia/entrypage.html", {"title":title, "content":contents})
   

def randompage(request):
   allentries=util.list_entries()
   randomentries=random.choice(allentries)
   contents=convertmd(randomentries)
   return render(request, "encyclopedia/randompage.html", {"title":randomentries, "content":contents})