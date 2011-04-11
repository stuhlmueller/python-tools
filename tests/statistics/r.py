from pytools.statistics import stacked_area_plot

data = {
    1 : { "brains" : 133,
          "computers" : 598,
          "ants" : 4935,
          "bacteria" : 20,
          "evolution" : 3580 },
    2 : { "brains" : 217,
          "computers" : 968,
          "ants" : 6486,
          "bacteria" : 1148,
          "evolution" : 3593 },
    3 : { "brains" : 133,
          "computers" : 598,
          "ants" : 4935,
          "bacteria" : 20,
          "evolution" : 3580 },
    4 : { "brains" : 217,
          "computers" : 968,
          "ants" : 6486,
          "bacteria" : 1148,
          "evolution" : 3593 }        
    }

stacked_area_plot(data, "/tmp/stats.pdf", "Statistics")
