## Tabela: usuario

| Field Name         | Data Type | Description                     | Allowed Values/Range                        | Notes       |
| :----------------- | :-------- | :------------------------------ | :------------------------------------------ | :---------- |
| `id_usuario`       | `integer` | Identificador único do usuário. | Inteiros positivos.                         | Primary Key |
| `nome_usuario`     | `string`  | Nome do usuário.                | Até 60 caracteres.                          |             |
| `email_usuario`    | `string`  | Email do usuário.               | Até 60 caracteres. |             |
| `endereco_usuario` | `string`  | Endereço do usuário.            | Até 120 caracteres.                         |             |

---

## Tabela: carrinho

| Field Name     | Data Type | Description                                | Allowed Values/Range                  | Notes       |
| :------------- | :-------- | :----------------------------------------- | :------------------------------------ | :---------- |
| `id_carrinho`  | `integer` | Identificador único do carrinho.           | Inteiros positivos.                   | Primary Key |
| `data_criacao` | `date`    | Data de criação do carrinho.               | Formato YYYY-MM-DD.                   |             |
| `fk_usuario`   | `integer` | Identificador do usuário dono do carrinho. | Deve existir em `usuario.id_usuario`. | Foreign Key |

---

## Tabela: item_carrinho

| Field Name      | Data Type | Description                | Allowed Values/Range                              | Notes       |
| :-------------- | :-------- | :------------------------- | :------------------------------------------------ | :---------- |
| `fk_carrinho`   | `integer` | Identificador do carrinho. | Deve existir em `carrinho.id_carrinho`.           | Foreign Key |
| `fk_produto`    | `integer` | Identificador do produto.  | Deve existir em `produto.id_produto`.             | Foreign Key |

---

## Tabela: produto

| Field Name          | Data Type       | Description                     | Allowed Values/Range | Notes       |
| :------------------ | :-------------- | :------------------------------ | :------------------- | :---------- |
| `id_produto`        | `integer`       | Identificador único do produto. | Inteiros positivos.  | Primary Key |
| `nome_produto`      | `string`        | Nome do produto.                | Até 60 caracteres.   |             |
| `descricao_produto` | `string`        | Descrição do produto.           | Até 400 caracteres.  |             |
| `preco_produto`     | `decimal(10,2)` | Preço do produto.               | Valores ≥ 0.         |             |
| `estoque_produto`   | `integer`       | Quantidade em estoque.          | Inteiros ≥= 0.        |             |

---
