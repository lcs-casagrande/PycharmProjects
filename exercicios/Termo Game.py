from random import randint
import unidecode
#banco de palavras

banco =['não','paz','fel','vil','sob','ser','céu','mal','ver','mãe','ter','ego','bem','mas','vão',
'vir','dar','bom','ora','dom','são','era','que','réu','elo','luz','com','nós','rol','tal',
'seu','foi','uma','hum','até','vis','pós','por','mim','lua','ato','dor','pai','dia','dou',
'sem','sol','pau','','irá','fim','tez','ler','vez','rua','tão','ode','fiz','nem',
'lei','mau','voo','mão','meu','gay','voz','dês','num','pôr','for','rio','daí','afã',
'jus','cia','fez','via','olá','ira','nau','sim','amo','sua','rei','lar','som','ido','tem',
'eco','boa','lhe','uns','mês','asa','clã','uso','aia','más','amor','fato','puta','viés','mito',
'você','caos','como','esmo','brio','vide','ação','após','sede','pois','vida','auge','saga','casa',
'ônus','ermo','medo','idem','mote','suma','tolo','além','urge','crer','apto','vovó','sina',
'veio','pude','zelo','pela','área','ruim','cota','coxo','rude','soar','ente','tudo','ater',
'fase','para','auto','alasão','mais','voga','será','rima','amar','onde','trás','logo','cedo','doce','ante',
'cujo','jugo','meio','amor','meta','sela','arte','deus','teor','cela','pelo','face','traz','nojo','numa',
'pose','base','alvo','asco','alma','teve','vale','foco','rito','agir','ócio','noia','todo','sair',
'alto','eita','ódio','alva','ágil','isso','alta','peço','tese','nexo','sido','sagaz','âmago',
'negro','êxito','mexer','termo','nobre','senso','','afeto','plena','ética','mútua','tênue',
'sutil','vigor','aquém','fazer','porém','','assim','seção','sanar','inato','fosse','',
'ideia','poder','moral','desde','muito','torpe','justo','honra','gozar','fútil','sobre','quiçá',
'anexo','razão','etnia','ícone','sonho','tange','égide','amigo','lapso','mútuo','porra','expor',
'haver','casal','hábil','tempo','seara','dengo','então','pesar','ávido','genro','posse','boçal',
'coser','ardil','causa','dizer','corja','prole','pária','detém','tenaz','dever','graça','saber',
'óbice','crivo','digno','orgia','ápice','ânimo','ânsia','brado','ceder','comum','sendo','temor',
'gleba','culto','assaz','atroz','pauta','mundo','censo','fugaz','ainda','cozer','valha','denso',
'vício','estar','exceto','cínico','idôneo','âmbito','néscio','mister','índole','vereda','apogeu',
'convém','utopia','sádico','escopo','ênfase','mérito','alusão','casual','idiota',
'anseio','hostil','pressa','boceta','hétero','cético','alheio','legado','nocivo','infame','gentil',
'clichê','exímio','afável','paixão','pneu','adorno','dádiva','adesão','sóbrio','aferir','êxtase','astuto',
'safado','otário','larica','solene','limiar','sessão','formal','também','julgar','apreço','hábito',
'glória','ensejo','lábaro','eficaz','ocioso','difuso','outrem','ímpeto','embora','júbilo','alento',
'dispor','facção','escusa','perene','exílio','cessão','abster','lúdico','','alçada','ilação',
'acento','objeto','isento','acesso','sanção','etéreo','tácito','axioma','cortês','desejo','cobiça',
'sisudo','mazela','eximir','buscar','receio','remoto','vulgar','avidez','fático','asseio','prazer',
'ciente','cômico','adágio','defina','empatia','aurélio','embuste','cônjuge','exceção','efêmero',
'prolixo','caráter','verbete','idílico','análogo','genuíno','estória','sublime','pêsames','família',
'sucinto','inferir','apático','acepção','audácia','astúcia','redimir','pródigo','recesso','estigma',
'cultura','refutar','estável','cinismo','virtude','icônico','exortar','soberba','mórbido','trivial',
'cordial','síntese','mitigar','aspecto','escória','imputar','luxúria','emergir','','sucesso',
'caralho','deboche','alegria','','candura','ademais','almejar','excerto','litígio','através',
'','contudo','orgulho','oriundo','alcunha','ambíguo','sensato','salutar',
'fomento','quimera','excesso','coragem','ambição','parcial','relação','modesto','imersão','conciso',
'saudade','erudito','exótico','escroto','demanda','isenção','amizade','notório','padecer','colosso',
'volátil','exilado','inércia','ciência','piedade','auferir','difusão','vigente','emotivo','intenso',
'Alasao','híbrido','ansioso','colapso','inerente','peculiar','respeito','denegrir','genocida',
'anuência','deferido','equidade','prudente','pandemia','iminente','essência','invasivo','',
'desgraça','alienado','eminente','extensão','abstrato','premissa','','conceito','talarico',
'ardiloso','reiterar','ascensão','devaneio','passível','prodígio','lascívia','relativo','conserto',
'analogia','modéstia','apologia','rapariga','inserção','ativista','inóspito','gratidão','monótono',
'medíocre','respaldo','remissão','sinônimo','concerne','fomentar','retórica','despeito','destarte',
'alicerce','proceder','metódico','primazia','demagogo','consiste','notívago','distinto','paralelepipedo',
'critério','portanto','desfecho','abnegado','história','complexo','inefável','sucumbir','singular',
'suscitar','amálgama','perfídia','elegível','escárnio','paradoxo','espectro','vocábulo','contexto',
'processo','jurídico','maestria','refletir','obstante','desígnio','instigar','objetivo','endêmico',
'comunhão','solícito','impávido','sanidade','resoluto','verídico','paralelo','insípido','problema',
'repudiar','imanente','','redenção','mediante','perspicaz','recíproco','impressão','concessão',
'escrúpulo','supérfluo','retificar','paradigma','presunção','','concepção','propósito',
'hipócrita','implícito','ratificar','plenitude','essencial','','corolário','incidente',
'esdrúxulo','hermético','altruísmo','altruísta','vagabundo','aleatório','persuadir','promíscuo',
'esperança','deliberar','sapiência','confiança','indelével','demasiado','mesquinho','resignado',
'regozijar','impetuoso','eminência','descrição','diligente','inusitado','compaixão','prudência',
'pretensão','analítico','discrição','explícito','','desdenhar','tsunami','ordinário',
'percepção','nostalgia','fidedigno','subjetivo','dissensão','companhia','resolução','constante',
'taciturno','supressão','expressão','autêntico','autonomia','imparcial','','restrição',
'discorrer','ignorante','arrogante','paciência','','adjacente','obstinado','outrossim',
'cognitivo','instância','interesse','consoante','sintético','limítrofe','iminência','desumilde',
'presságio','eloquente','irascível','relevante','vagabunda','ludibriar','aquisição','empecilho',
'ambicioso','convicção','plausível','excelente','recíproca','pederasta','estagnado']

#escolher a palavra
print('O numero de tentativas corresponde a quantidade de letra')
azul='azul'
amarela='amarela'
print(f'Letra na cor \033[34m{azul}\033[m corresponde a letra certa na posição certa')
print(f'Letra na cor \033[33m{amarela}\033[m corresponde a letra certa na posição errada')
print(f'Letra na cor branca corresponde a letra inexistente na palavra')
print()
cont=0
p=randint(0,(len(banco)))
palavra=banco[p]
#retirar os acentos
codigo = unidecode.unidecode(palavra).upper()
#print(codigo)
tamanho=(len(codigo))
print(f'Tentativas e nº de letras {tamanho}:')
#entradas de tentativas
while True:
 if cont==tamanho:
  print()
  print('PE-E-ER-D-E-D-O-RR')
  break
 print()
 teste=input(f'{cont+1}:')[0:tamanho].upper()
 if codigo==teste:
  print(f'Parabéns, você acertou!!!')
  break
 cont += 1
 # separar as letras
 for p in range(0,len(teste)):
  letra=teste[p]
  letra_cod=codigo[p]
  if letra==letra_cod:
   print(f'\033[34m{letra}\033[m', end='')
  elif letra in codigo:
   print(f'\033[33m{letra}\033[m', end = '')

  else:
   print(letra, end='')

print()
print(palavra.upper())