import CDplayer as CD
import InputLogger

cd_player = CD.__init__(CD, "cd1", InputLogger)

CD.__init__(CD,"cd1", InputLogger)
CD.play(CD)
CD.play(CD)
CD.stop(CD)

CD.__init__(CD,"cd2", InputLogger)
CD.play(CD)
CD.stop(CD)
CD.play(CD)
CD.stop(CD)
CD.stop(CD)

CD.__init__(CD,"cd3", InputLogger)
CD.play(CD)
CD.stop(CD)

CD.__init__(CD,"cd4", InputLogger)
CD.play(CD)
CD.stop(CD)