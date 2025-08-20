from django.shortcuts import render,redirect
from .models import TrackingHistory,CurrentBalance
# Create your views here.
def index(request):
  if request.method == "POST":
    discription = request.POST.get('discription')
    amount = request.POST.get('amount')
    current_balance,_ = CurrentBalance.objects.get_or_create(id=1)
    expense_type = 'CREDIT'
    if float(amount) < 0 :
      expense_type = 'DEBIT'

    tracking_history = TrackingHistory.objects.create(amount = amount, expense_type = expense_type, current_balance = current_balance, discription = discription,)
    current_balance.current_balance +=  float(tracking_history.amount)
    current_balance.save()
    print(discription,amount)
    return redirect('/')
  return render(request,'index.html')

