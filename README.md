O código foi feito para um cliente num trabalho freelancer.

O objetivo era extrair todas as tabelas de um PDF e colocar num CVS.

> Os desafios:
- O python interpretar as diferentes fontes e tonalidades (itálico e negrito).
- A divisão de células, que na tabela do pdf era apenas espaços, conceito difícil do python entender.
- A divisão de linhas, o python não sabia quando uma célula acaava ou iniciava, nem mesmo as das pontas ou se elas continuavam em baixo, o que gerava erros.

Descartei os valores nulos para lidar com os espaços que eram interpretados dessa forma.

Para aceitar esse trabalho eu pedi um dia de espera, desconhecendo dos desafios que iriam aparecer e cobrando baixo, crente de que um código pronto de 4 linhas já resolveria o problema.

Consegui resolver o problema com esse códgio, ele pega padrões que eu achei e substitui por vírgulas, fazendo assim a divisão correta das células e usei palavras especificas que só ficavam no fim das linhas e usei para gerar a quebra de texto correta.
