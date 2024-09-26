from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def primes(number):
    prime_list = []
    if number < 2:
        return []
    for n in range(2, number + 1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            prime_list.append(n)
    return prime_list


# Input page view
def input_page(request):
    return render(request, "input_page.html")


# Output page view
def output_page(request):
    if request.method == "POST":
        number = int(request.POST["number"])
        prime_list = primes(number)
        return render(
            request, "output_page.html", {"primes": prime_list, "number": number}
        )
    return HttpResponseRedirect(reverse("input_page"))
