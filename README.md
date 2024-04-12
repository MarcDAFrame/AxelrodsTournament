# Axelrod's Tournament
Inspired by this Veritasium video

<iframe width="560" height="315" src="https://www.youtube.com/embed/mScpHTIi-kM?si=CsjvI8yKp-A3h30J" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


I wrote some code to run my own Axelrod's tournament


However after writing the code I found that there's [already a library for it](https://github.com/Axelrod-Python/Axelrod) haha. I don't think it's a complete waste however as it only took me an hour or two.


# Contributing
This project could use help with the following

1. add your own strategy
2. better vizualizations
3. the LLM strategy

## Add your own strategy
create a file in the `./players` folder with the following 
```py
@dataclass
class PlayerRound:
    you: Play
    them: Play

PlayerRoundHistory = List[PlayerRound]

def unique_player_name(
        prev: PlayerRoundHistory
    ) -> Play:
    return Play.cooperate
```

## Better Vizualizations
the world is your oyster, you can see what I've already done for vizualizations in Viz.ipynb

some sort of interactive vizualization tool would be cool though


## LLM Strategy
I really like the idea of testing LLMs against each other and against the default strategies, however this could be expensive



# TODO
- [x] write the run function
  - [x] define the inputs
  - [x] define the output
- [x] write a few players
  - [x] tit4tat
  - [x] llm based ?
- [x] run simulations
- [x] vizualize the data