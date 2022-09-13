d1 = {}
d2 = {"harry":"burger", "rohan":"fish","ramesh":"roti",
      "kalu":{"morning":"breakfast","noon":"lunch","night":"dinner"}}
d3 = d2.copy()
del(d2["harry"])
d3.update({"raj":"laptop"})
print(d3.keys())
print(d3.items())
