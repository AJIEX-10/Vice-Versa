from django.shortcuts import render
import re
def home(request):
	return render(request, 'home.html')

def reverse(request):
	the_text=request.GET['message']
	cups=[]
	lau=re.findall('[a-zA-Z]+', the_text)
	cups.append(lau)
	dos=[len(x) for x in cups]
	dof=dos[0]

	rev_text=the_text[::-1]
	return render(request, 'reverse.html', {'message': the_text, 'pops':rev_text, 'count_of_words':dof})