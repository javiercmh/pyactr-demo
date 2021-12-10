import pyactr as actr

playing_memory = actr.ACTRModel()

actr.chunktype("playgame", "game, activity")
initial_chunk = actr.makechunk(typename="playgame", game="memory")


