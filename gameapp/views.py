from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

from datetime import datetime
from random import choice


@csrf_protect
def home(request):
    choices = ["rock", "paper", "scissors"]
    computer_choice = choice(choices)

    if request.method == "POST":
        player_choice = request.POST.get("player_choice")
        computer_choice = request.POST.get("computer_choice")
        result = ""
        if player_choice == computer_choice:
            result = "It's a draw."
        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or (player_choice == "paper" and computer_choice == "rock")
            or (player_choice == "scissors" and computer_choice == "paper")
        ):
            result = "You are the winner!"
        else:
            result = "You lost :("

        return render(
            request,
            "result.html",
            {
                "player_choice": player_choice,
                "computer_choice": computer_choice,
                "result": result,
            },
        )
    date_joined = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    return render(
        request,
        "base.html",
        {"date_joined": date_joined, "computer_choice": computer_choice},
    )
