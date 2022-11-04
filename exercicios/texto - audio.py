from gtts import gTTS

audio = 'speech.mp3'
language = 'pt'
sp = gTTS (text= 'Há um país de gozo e luz Onde só santos há; Prazeres há ali a flux;'
                 'É sempre dia lá. CORO: Marchamos para a terra além E vamos a Jerusalém; '
                 'Iremos com Jesus reinar E nunca mais nos separar. Oh, nunca separar? Não, nunca separar! '
                 'Oh, nunca separar? Não, nunca separar! Iremos com Jesus reinar E nunca mais nos separar! '
                 '2. Há sempre primavera lá, Flores não murcharão; Tão perto, sim, de nós está A eternal '
                 'mansão.', lang= language, slow=False)
sp.save(audio)

