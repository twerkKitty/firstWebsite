from django.shortcuts import render

# Create your views here.
def index(request):
	# this is your new view
	
	number = 6
	number1 = 1
	thing = "Thing name"
	
	return render(request, 'index.html', {
		
		'number': number,
		'number1': number1,
		'thing': thing, 
		
	}
	

	)