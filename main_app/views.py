from django.shortcuts import render

finches = [
  {
  'type': 'Purple Finch', 
  'habitat': 'Woods, groves, suburbs. Breeds mostly in coniferous and mixed woods, both in forest interior and along edges. In Pacific states, also breeds in oak woodland and streamside trees. In migration and winter, found in a wide variety of wooded and semi-open areas, including forest, suburbs, swamps, and overgrown fields.', 
  'description': 'The purple finch has a short forked brown tail and brown wings. Adult males are raspberry red on the head, breast, back and rump; their back is streaked.',
  'population': 6500000,
  },

  {
   'type': 'Gouldian Finch', 
   'habitat': 'Live in savanna woodlands where they nest in the hollows of smooth-barked eucalypts. Gouldian finches are native to the grasslands of Australia.', 
   'description': 'The gouldian finch are small birds, with a bright green back, yellow belly and a purple breast. The facial colour is usually black, and is found in about 75 percent of the birds.', 
   'population': 2500,
  },

#   {
#    'type': '', 
#    'habitat': '', 
#    'description': '', 
#    'population': 0
#   },
]


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
  })