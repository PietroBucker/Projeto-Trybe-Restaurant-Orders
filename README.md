# Projeto Restaurant Orders

## 1 - Testando classes já implementadas parte 1

> Implemente testes para a classe `Ingredient`, que se encontra no módulo `src/models/ingredient.py`.

Antes de você começar a trabalhar neste projeto, uma equipe contratada pelo Restaurante  🍝 🦐 Chapa Quente 🍛 🥘  fez a implementação de algumas das classes que serão usadas ao longo do seu desenvolvimento, contudo, a equipe não implementou os testes para estas mesmas classes e cabe a você implementá-los.

A primeira das classes implementadas é a `Ingredient` que representa os ingredientes, um objeto desta classe contém o nome e restrições alimentares do ingrediente como atributos.

A classe já possui alguns métodos mágicos já implementados que garantem funcionalidades específicas. Os métodos já implementados são: `__repr__`, `__eq__` e `__hash__`.

### Implementação

Escreva os testes para a classe `Ingredient` no arquivo `tests/ingredient/test_ingredient.py`. Seus testes devem garantir que:

- a classe pode ser instanciada corretamente de acordo com a assinatura esperada;
- o atributo conjunto `restrictions` é populado como esperado;
- o método mágico `__repr__` funcione como esperado;
- o método mágico `__eq__` funcione como esperado;
- o método mágico `__hash__` funcione como esperado.

</br>
<details>
  <summary>
    <b>🤖 Clique aqui para ver o que será verificado pelo avaliador.</b>
  </summary>

- 1.1 - Será validado que seu teste falha caso a classe retorne hashes diferentes para dois ingredientes iguais;

- 1.2 - Será validado que seu teste falha caso a classe retorne hashes iguais para dois ingredientes diferentes;

- 1.3 - Será validado que seu teste falha caso a comparação de igualdade de dois ingredientes iguais (ou de um ingrediente com ele mesmo) seja falsa;

- 1.4 - Será validado que seu teste falha caso a comparação de igualdade de dois ingredientes diferentes seja verdadeira;

- 1.5 - Será validado que seu teste falha caso a implementação do método `__repr__` retorne um valor inadequado.

- 1.6 - Será validado que seu teste falha caso o atributo `name` de um ingrediente seja diferente que o passado ao construtor.

- 1.7 - Será validado que seu teste falha caso o atributo `restrictions` de um ingrediente não contenha os valores corretos para o alimento passado.

- 1.8 - Será validado que seu teste passa com a implementação correta da classe `Ingredient`.

</details>
</br>

<details>
  <summary>
    <b>📌Como seu teste é avaliado</b>
  </summary>

  <br>

  O <strong>teste da Trybe</strong> irá avaliar se o <strong>seu teste</strong> está passando conforme o objetivo proposto, além disso, confirmará que seu teste falha em alguns casos em que deveria falhar.

  Para estes testes, em que esperemos a falha, o requisito será aprovado quando a resposta do Pytest for <code>XFAIL(Expected Fail)</code>, ao invés de <code>PASSED</code>.

</details>
</br>

## 2 - Testando classes já implementadas parte 2

> Implemente testes para a classe `Dish`, que se encontra no módulo `src/models/dish.py`.

A outra classe a ser testada é a `Dish`, que representa um prato do cardápio. Uma instância desta classe possui atributos representando o nome, o preço e a receita do prato.

Tal como a classe `Ingredient`, a classe `Dish` já possui alguns métodos já implementados: `add_ingredient_dependency`, `get_restrictions`, `get_ingredients`, `__repr__`, `__eq__` e `__hash__`.

### Implementação

Escreva os testes para a classe `Dish` no arquivo `tests/dish/test_dish.py`. Seus testes devem garantir que:

- a classe pode ser instanciada corretamente de acordo com a assinatura esperada;
- os métodos da classe, inclusive os métodos mágicos, funcionem como esperado;
- o dicionário de receita do prato devolve a quantidade correta de um ingrediente;
- são levantados erros ao criar pratos inválidos;

</br>
<details>
  <summary>
    <b>🤖 Clique aqui para ver o que será verificado pelo avaliador.</b>
  </summary>

- 2.1 - Será validado que seu teste falha caso o atributo `name` de um prato seja diferente que o passado ao construtor.

- 2.2 - Será validado que seu teste falha caso os hashes de dois pratos iguais sejam diferentes;

- 2.3 - Será validado que seu teste falha caso os hashes de dois pratos diferentes sejam iguais;

- 2.4 - Será validado que seu teste falha caso a comparação de igualdade de dois pratos iguais (ou de um prato com ele mesmo) seja falsa;

- 2.5 - Será validado que seu teste falha caso a comparação de igualdade de dois pratos diferentes seja verdadeira;

- 2.6 - Será validado que seu teste falha caso a implementação do método `__repr__` retorne um valor inadequado;

- 2.7 - Será validado que seu teste falha caso um `TypeError` não seja levantado ao criar um prato com um valor de tipo inválido;

- 2.8 - Será validado que seu teste falha caso um `ValueError` não seja levantado ao criar um prato com um valor inválido;

- 2.9 - Será validado que seu teste falha caso o acesso a um valor do atributo `recipe`, ao ser indexado com um ingrediente válido retorne uma quantidade inválida (dica: use o método `get` do dicionário, por exemplo `dish.recipe.get(ingredient)`);

- 2.10 - Será validado que seu teste falha caso o método `get_restrictions` retorne um set de restrições diferente do esperado;

- 2.11 - Será validado que seu teste falha caso o método `get_ingredients` retorne um set de ingredientes diferente do esperado;

- 2.12 - Será validado que seu teste passa com a implementação correta da classe `Dish`.

</details>
</br>

<details>
  <summary>
    <b>📌Como seu teste é avaliado</b>
  </summary>

  <br>

  O <strong>teste da Trybe</strong> irá avaliar se o <strong>seu teste</strong> está passando conforme o objetivo proposto, além disso, confirmará que seu teste falha em alguns casos em que deveria falhar.

  Para estes testes, em que esperemos a falha, o requisito será aprovado quando a resposta do Pytest for <code>XFAIL(Expected Fail)</code>, ao invés de <code>PASSED</code>.

</details>
</br>

## 3 - Mapeamento Pratos <> Ingredientes

> Implemente a classe `MenuData` que fará todo o mapeamento de pratos e ingredientes baseado nos arquivo csv disponibilizado. Ela se encontra no módulo `src/services/menu_data.py`.

Hoje, a gestão de pratos e receitas do Restaurante  🍝 🦐 Chapa Quente 🍛 🥘 é feita por meio de um arquivo csv. Em cada linha deste arquivo há o nome do prato, seu preço no cardápio, um dos ingredientes que o compõe e a quantidade necessária daquele ingrediente na receita. Essa organização faz com que um único prato seja representado por múltiplas linhas no mesmo arquivo.

Sua tarefa é implementar uma classe que fará a leitura do arquivo csv mencionado e fará o relacionamento do prato do cardápio com sua respectiva receita, isto é, ingrediente e quantidade. Vale lembrar que já existem classes implementadas para os pratos (`Dish`) e os ingredientes (`Ingredient`). Além disso, a classe que você vai implementar precisa conter um atributo `dishes`, que deverá ser um _set_ que liste todos os pratos presentes no arquivo csv.

### Implementação

Implemente a classe `MenuData` no arquivo `src/services/menu_data.py`.  
O teste utiliza o [arquivo de mock `tests/mocks/menu_base_data.csv`](./tests/mocks/menu_base_data.csv).

Ao longo da sua implementação você deve garantir que:

- a classe, ao ser instanciada, recebe o caminho para o arquivo csv no parâmetro `source_path`;

- a classe fará a leitura do arquivo csv e baseado em seu conteúdo fará as devidas instanciações de pratos e ingredientes;

- a classe contenha o atributo `dishes` que deverá ser um _set_ com todos os pratos devidamente instanciados;

- cada um dos pratos contenha sua respectiva receita, isto é, seus ingredientes e quantidades, bem como seu preço.


<details>
  <summary>
    <b>🤖 Clique aqui para ver o que será verificado pelo avaliador.</b>
  </summary>

- 3.1 - O tamanho do _set_ `menu_data.dishes` está correto;

- 3.2 - O _set_ `menu_data.dishes` possui os pratos corretos (com base no método de comparação dos pratos `Dish.__eq__`);

- 3.3 - A quantidade de ingredientes diferentes presentes nos pratos em `menu_data.dishes` está correta;

- 3.4 - A quantidade de cada ingrediente de cada prato presente em `menu_data.dishes` está correta.

</details>

---

## 4 - Geração dos cardápios

Atualmente o cardápio do Restaurante 🍝 🦐 Chapa Quente 🍛 🥘 tem estrutura fixa e, apesar disso não ser um problema, as pessoas fundadoras do estabelecimento desejavam que este cardápio fosse dinâmico, isso porque muitas das pessoas que frequentam o restaurante possuem restrições alimentares, e seria ideal mostrar-lhes o cardápio contendo apenas os pratos que possam comer.

Com este objetivo, a equipe que trabalhou no projeto antes de você começou a implementação de uma classe que interagisse ao mesmo tempo com o cardápio e com o estoque, e que ainda pudesse exibir os pratos do cardápio de acordo com uma determinada restrição alimentar. Sua tarefa neste requisito é fazer a implementação do método que mostrará os cardápios evitando os pratos com determinada restrição alimentar.

### Implementação

Você deve implementar o método `get_main_menu` dentro da classe `MenuBuilder` que se encontra no arquivo `src/services/menu_builder.py`. O método tem como parâmetro opcional uma restrição que deve ser levada em conta na hora de gerar o cardápio.

Seguindo a assinatura do método que foi deixada pela equipe anterior, o retorno deste método deve ser do tipo `List[Dict]`. Assim, é necessário que o método retorne uma lista de dicionários que contenham as chaves `dish_name`, `ingredients`, `price` e `restrictions` que se referem, respectivamente, ao **nome** do prato, **ingredientes** que o compõem, seu **preço** no cardápio e **restrições** daquele mesmo prato.

Ao longo de sua implementação você deve garantir que:

- a classe possa ser instanciada corretamente;

- o método `get_main_menu` retorna uma lista de dicionários com o cardápio completo quando não é passado nenhum parâmetro;

- o método `get_main_menu` retorna uma lista de dicionários com o cardápio correto respeitando a restrição alimentar passada como parâmetro;

<br>
<details>
  <summary>
    <b>🤖 Clique aqui para ver o que será verificado pelo avaliador.</b>
  </summary>

- 4.1 - O método `get_main_menu` retorna uma lista de dicionários;

- 4.2 - A lista retornada possui dicionários com as chaves `dish_name`, `ingredients`, `price` e `restrictions`;

- 4.3 - A lista retornada possui todos os pratos do arquivo do banco de dados quando o método for chamado sem especificar uma restrição;

- 4.4 - A lista retornada possui os pratos corretos quando chamado com uma restrição específica;

- 4.5 - A lista retornada não possui pratos incorretos quando chamado com uma restrição específica.

</details>
<br>


# Requisitos bônus:

## 5 - Estoque de ingredientes

A gestão de estoque do Restaurante 🍝 🦐 Chapa Quente 🍛 🥘 também é feita por meio de um arquivo csv. Para o controle de estoque é usado um arquivo em que cada uma das linhas contém um ingrediente e sua respectiva quantidade inicial no estoque. Seu objetivo neste requisito é finalizar o desenvolvimento da classe que fará o controle do estoque de ingredientes.

Assim como no requisito anterior, o time que trabalhou antes de você no projeto já iniciou a implementação da classe e cabe a você finalizar esta implementação. Você deve implementar dois métodos para a classe: `check_recipe_availability` e `consume_recipe`.

O primeiro dos métodos (`check_recipe_availability`) deve checar se a receita passada como parâmetro está ou não disponível para consumo, para isso, deve retornar `False` caso um ingrediente da receita não exista no estoque ou caso não exista quantidade suficiente destes ingredientes em estoque e `True`  caso o prato esteja disponível para consumo.

O segundo método (`consume_recipe`) também recebe uma receita como parâmetro, mas deve subtrair a quantidade de ingredientes usados na receita do total disponível em estoque. Vale lembrar que a subtração só deve acontecer caso a receita esteja disponível para consumo, caso contrário, deverá ser levantada uma exceção `ValueError`.

### Implementação

A classe `InventoryMapping` se encontra no arquivo `src/services/inventory_control.py`, nela você deverá implementar os métodos `check_recipe_availability` e `consume_recipe`. Ao longo da sua implementação você deve garantir que:

- A classe possa ser devidamente instanciada;

- o método `check_recipe_availability` retorna `True` caso a receita esteja disponível para consumo e `False` caso contrário;

- o método `consume_recipe` subtrai os ingredientes da receita do total disponível em estoque caso a receita esteja disponível para consumo e levanta uma exceção `ValueError` caso contrário.

<details>
  <summary>
    <b>🤖 Clique aqui para ver o que será verificado pelo avaliador.</b>
  </summary>

- 5.1 - Valida o funcionamento do método `check_recipe_availability`;
    - 5.1.1 - O método retorna `True` se a receita pode ser feita usando os ingredientes disponíveis (mas não mais do que o disponível). O teste roda para cada um dos ingredientes do arquivo do banco de dados.
    - 5.1.2 - O método retorna `False` se a receita usa mais de algum ingrediente do que o que está disponível. O teste roda para cada um dos ingredientes do arquivo do banco de dados
- 5.2 - Valida o funcionamento do método `consume_recipe`;
    - 5.2.1 - O método retorna `None` ao consumir uma receita disponível e, não havendo nenhum erro, o inventário é atualizado conforme a receita consumida. O teste roda com várias receitas disponíveis.
    - 5.2.2 - O método levanta um `ValueError` ao tentar consumir uma receita indisponível. O teste roda com várias receitas indisponíveis, incluindo uma que só fica indisponível após uma que estava disponível ser consumida corretamente.

</details>

## 6 - Cardápios baseados no estoque 

Com a implementação que foi feita até o momento, o método gerador de cardápios, `get_main_menu`, considera apenas as restrições alimentares para fazer a geração do cardápio com os pratos que as pessoas podem comer. Isso ainda é um problema, dado que ainda não é feita a verificação se os ingredientes do prato estão disponíveis em estoque.

Sua tarefa neste requisito é complementar a implementação do método `get_main_menu` para considerar a disponibilidade em estoque dos ingredientes do prato além das restrições alimentares. Assim, o Restaurante 🍝 🦐 Chapa Quente 🍛 🥘 possuirá a ferramenta capaz de gerar cardápios dinâmicos considerando restrições alimentares e disponibilidade em estoque.

<br>

### Implementação

Você deve complementar a implementação do método `get_main_menu`, feito no requisito 4. O método agora precisa considerar também a disponibilidade em estoque dos ingredientes dos pratos. Use a classe implementada no requisito anterior, `InventoryMapping`, para ter acesso a informações do estoque.

Ao longo de sua implementação você deve garantir que:

- o método `get_main_menu` retorna uma lista de dicionários com o cardápio completo caso não exista restrição e todos os ingredientes estiverem disponíveis;

- o método `get_main_menu` retorna uma lista de dicionários com os cardápios corretos respeitando a restrição alimentar passada como parâmetro e também a disponibilidade de ingredientes no estoque;

<br>
<details>
  <summary>
    <b>🤖 Clique aqui para ver o que será verificado pelo avaliador.</b>
  </summary>

- Os testes dos requisitos 4.3 e 4.4 passando são pré-requisitos para o teste do requisito 6 rodar.

- 6 - O método `get_main_menu` retorna uma lista vazia quando o estoque não possui os ingredientes necessários para a confecção dos pratos.

</details>
<br>

<details>
  <summary>
    <b>👀 De olho na dica - Como rodar a aplicação?</b>
  </summary>

Para ver a aplicação rodando com as funcionalidades que você implementou, use o comando a seguir:

```bash
python3 -m uvicorn app:app
```

Acesse a rota `/docs` para ver a [documentação](http://127.0.0.1:8000/docs) gerada pelo FastAPI!

</details>
