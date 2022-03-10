from django.views import View
from .models import Todo
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
class TodoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request, id=0):
        if(id!=0):
            todo = list(Todo.objects.filter(id=id).values())
            if(len(todo)!=0):
                return JsonResponse(
                        {
                            'message':'Success',
                            'todos': todo[0]
                        }
                )
            else:
                return JsonResponse(
                        {
                            'message':'Todo not found',
                        }
                )
        else:
            data = list(Todo.objects.values())
            if len(data) != 0:
                return JsonResponse(
                    {
                        'message':'Success',
                        'todos': data
                    }
                )
            else:
                return JsonResponse({
                        'message':'Todo not found',
                })
    
    def post(self,request):
        data = json.loads(request.body)
        Todo.objects.create(title=data['title'])
        return JsonResponse({
                'message':'Success',
        })

    def delete(self,request, id):
        todo = list(Todo.objects.filter(id=id).values())
        if len(todo) != 0 :
            Todo.objects.filter(id=id).delete()
            return JsonResponse({
                'message': "Success"
            })
        else:
            return JsonResponse({
                'message': "Todo not found..."
            })