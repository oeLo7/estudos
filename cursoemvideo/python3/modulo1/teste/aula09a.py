frase = "Curso em Vídeo Python"
print(frase[::2])

samara = "Oi meu nome é Samara, tenho 14 anos (Teria se estivesse viva), morri aos 13 em Cascavel-PR. Eu andava de bicicleta quando não pude desviar de um arame farpado. O pior foi que o dono do lote não quis me ajudar, riu bastante mim após agonizar por 2 horas enroscada no arame eu faleci, através dessa mensagem eu peço que façam com que eu possa descançar em paz. Envie isso para 20 comunidades e minha alma estara sendo salva por você e pelos outros 20 que receberão. Caso não repasse essa mensagem vou visitar-lhe hoje a noite assim vc poderá conhecer o tal arame bem de pertinho. Dia 15 de Julho Mariana resolveu rir dessa mensagem, uma noite depois ela sumiu sem deixar vestigios. O mesmo aconteceu com Karen dia 18 de Outubro. Não quebre essa corrente por favor, a não ser que queira sentir a minha presença."

print("""Oi meu nome é Samara, tenho 14 anos (Teria se estivesse viva), 
morri aos 13 em Cascavel-PR. Eu andava de bicicleta quando não pude desviar de um arame farpado. 
O pior foi que o dono do lote não quis me ajudar, 
riu bastante mim após agonizar por 2 horas enroscada no arame eu faleci, 
através dessa mensagem eu peço que façam com que eu possa descançar em paz. 
Envie isso para 20 comunidades e minha alma estara sendo salva por você e pelos outros 20 que receberão. 
Caso não repasse essa mensagem vou visitar-lhe hoje a noite assim vc poderá conhecer o tal arame bem de pertinho. 
Dia 15 de Julho Mariana resolveu rir dessa mensagem, uma noite depois ela sumiu sem deixar vestigios. 
O mesmo aconteceu com Karen dia 18 de Outubro. Não quebre essa corrente por favor, 
a não ser que queira sentir a minha presença.""")


print(samara.lower().count("l"))
print(len(samara))

print(samara.replace(" ", "blebos"))
print(len(samara.replace(" ", "blebos")))

print(samara.split())
print(len(samara.split()))
