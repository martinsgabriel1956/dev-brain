# JavaScript Ninja: operadores lógicos

Estamos de volta com um curso de JavaScript Ninja.

Agora, depois de corrigiu o exercício da anterior, vai continuar dando um giro pela linguagem, e dessa vez a gente vai falar um pouco sobre operadores lógicos.

Então, quem são os operadores lógicos em JavaScript? Operadores lógicos, basicamente o que eles fazem: eles combinam ou eles invertem valores booleanos.

Como assim, Fernando? Me explica esse negócio de multiplicar.

## Operador E

Gente vai falar primeiro sobre o operador lógico E, que são dois "e" comercial, que significa [e], ou seja, que ele vai fazer: ele vai combinar basicamente e combinar dois valores, e ele vai retornar se a combinação desses valores é true ou falso. Mover na prática como funciona isso.

Então, por exemplo, eu vou criar uma variável X que ela vai ter o valor três, certo? Eu vou querer uma variável Y que ela vai ter o valor sete, certo? É que eu quero fazer: eu vou fazer uma verificação agora se o X é igual a 3, certo? Quando eu faço essa verificação, ele vai me retornar um valor falso, certo?

Então eu verifiquei se o valor da variável X é igual a 3. Esse tipo de dela também é o número, certo? Então faça essa verificação que acabei de fazer.

Agora, se eu quiser combinar, por exemplo, que se eu quiser verificar pela variável Y, e Y é igual a 5: não, é falso, porque não é igual a 5, porque eu defini que o Y é sete, certo?

Se você perguntar se o Y é igual a 7 sei, também é falso, porque eu testei pelo tipo. Se eu estou perguntando se eu sou um social igual 7, mas eu estou fazendo uma estrovenga, ele vai dizer que é falso. Estou querendo dizer que o Y é sete número, sim, sou igual a sete números, ok? Então eu estou perguntando se ele é igual a 7, o tipo dele é o número, ele também retornando o true. Isso é verdadeiro, ou seja, ele possui 7.

Agora, se eu quiser testar pelas duas formas de uma vez só, por exemplo, eu quero testar se o X [é] igual a 3 e se o Y é sete, eu vou usar o nosso operador lógico. Então, como que eu faço isso? X é igual a 3 [e] Y é sete: ele vai retornar true, porque o X [é] 3 e o Y é 7. Ok.

Se eu perguntar se o X [é] 3 e o Y é igual a 4, e vai me retornar falso, porque o X não encontrei. Mas ele está combinando esses dois valores, ele está juntando, e eles juntos dois valores. Ele só retorna true quando os dois valores são verdadeiros. Então, se o X é verdadeiro, mas o Y é falso, em termos de retornar falso, ok?

## Operador OU

E como? Como faço para saber, por exemplo, se o único valor era o único valor verdadeiro? Aí vai entrar o nosso outro operador lógico, ou outro, ok, ok, operador. Ora são dois prestar um ao lado do outro.

O que acontece? Para testar se dois valores, qualquer um deles é verdadeiro, ou pelo menos um deles é verdadeiro, pelo menos um deles verdadeiro, eu vou testar usando o operador or, certo?

Então eu tenho lá meu variável X com o valor de é, minha variável Y com o valor sete. Então eu quero saber agora que se qualquer um desses dois valores é verdadeiro. Então eu vou testar o X é igual a 3 ou o Y é igual a 3. Quero saber se qualquer um desses dois valores é igual a 3: retornou true, porque eu não encontrei isso não, mas o X é igual a 3.

Então o operador or, que o que ele faz, ele simplesmente verifica se um ou outro valor vai ser igual. Você vai olhar pra mim verdadeiro, ok? Ficou claro até aqui? Eu acho que sim, né? Bem tranquilo, né?

## Operador not

E o próximo operador lógico, que você já viu: o not, ou o sinal de exclamação. Que o not faz? O not, que ele vai inverter um valor.

Então, por exemplo, os operadores lógicos, ele sempre retornar [true] ou falso, OK? Nesse nosso caso, o operador not, ele vai inverter o valor. Então, por exemplo, se eu perguntar X é igual a 3, ele vai retornar [true]. Agora, se eu disser not X é igual a 3, ele vai retornar falso. Ok? Porque perguntou, perguntando o X é igual a 3, mas isto é, não entendo o valor dele com o not 7.

Esse formato novamente não é utilizado, então não tem utilização do formato com o not direto aqui.

## Diferente estrito e não estrito

Eu, por exemplo, eu posso usar X é diferente de três, ar que é falso, porque o X é igual a 3. Certo? Ou posso verificar também se o X é diferente, verificando também pelo tipo, de três: ele vai retornar falso, certo? Porque o X é igual a três.

Só que se eu perguntar o X é diferente... Você lembra que se eu perguntar o X é igual a 3 como string, e testando pelo tipo, ele também então era falso, porque ele tem esse meu tipo. Então aqui eu estou testando por mês. Só que o X na verdade é o três número, certo? Que acontece se eu verificar então X é diferente de 3, por exemplo? Mencionar aqui é falso, porque ele vai retornar que o X é diferente de 3. Esse timing é falso. X diferente 3 novamente.

Além disso, a diferença dos resultados vale só se você pegar o X e não testar pelo tipo e perguntar se ele é diferente de 3, ele vai dizer que é falso. Que na verdade você vai testar pelo tipo: X agora três vão testar pelo tipo, certo? Ele somente vai ser igual a três, três string, ele vai retornar true, certo? Porque eu estou, estou testando se o valor é somente igual a 3.

Então você vai testar se o X é diferente de três string, ele vai dizer que é falso, porque na verdade o X é igual a três. Agora, se eu testar com o operador de verificação estrito, ou operador é diferente, no caso estrito, e perguntar se ele é igual a si, se ele é diferente de três string, alinhamento ou neutro. Porque na verdade X é igual a três números. Se eu perguntar se é diferente de três números, ele vai dizer que é falso, porque o X na verdade é igual aos três números, ok? X é igual a 3, 7. Ficou claro até aqui?

Isso porque o que eu mostrei o esquema de baixo do diferente ali, do strict, do não estrito, do formato que você testar pelo tipo e você não testar pelo tipo. Porque você pode perceber que, dependendo do resultado, ou daquilo que você está fazendo, você pode até ter um resultado bastante diferente, se você usar o operador e não testar pelo tipo dele. Porque na verdade o X aqui ele vale três números. Então, se eu perguntar se o X é diferente de três números, ele vai dizer que é falso. Mas se eu perguntar se você é diferente de três string, ele também vai dizer que é falso. Entendeu?

Então isso é bastante problemático. Eu usei esse tipo de operador aqui porque ele pode ter alguns efeitos colaterais dessa forma que está diferente ao testar verificando pelo menos, ficando com o operador estrito, sem operadores estrito em seu estrito.

Se você viu o que eu passei o número aqui, ele disse que é falso, e aqui com operadores também, passando do tipo o número, vai dizer que é falso. Só que agora, sendo testado pelo operador estrito, é de se perguntar se o seu X é diferente de triste, ele retornou o fato. É esse, na verdade, o valor correto, porque o X não é igual a três, e sim o X é igual a três números. Então você perguntando se ele defende três números, que encaminha retornar falso, porque o X é igual a três.

## Encerramento

Ficou claro? Ficou muito complicado? Bom, sim, ficou complicado. Se foi difícil de entender essa parte, a gente vai falar mais sobre isso também, está instalada no giro pela linguagem. Como falei, só para você entender mais ou menos os valores, as coisas a gente pode usar no JavaScript.

Mas se ficou alguma dúvida com relação a isso, vai ter o desafio, no desafio de falar sobre isso. E você vai poder comentava, poder mandar um email para mim, vai poder abrir uma issue no GitHub pra poder dizer se isso aqui ficou claro ou se ficou muito difícil de você entender.

Beleza? Então agora, no próximo vídeo, vai conversar um pouco sobre operadores unários. Beleza? Mas no próximo vídeo agora você.
