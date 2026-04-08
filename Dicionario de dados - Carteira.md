
# [Usuario] Data Dictionary

| Field Name | Data Type | Description | Allowed Values/Range | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id_usuario` | `int` | Identificador único do usuário. | Positive integers. | Primary Key |
| `nome_usuario` | `varchar(60)` | Nome completo ou de exibição do usuário. | Max 60 characters. | |
| `email_usuario` | `varchar(60)` | Endereço de e-mail para login e contato. | Max 60 characters. | Unique |
| `senha_usuario` | `varchar(60)` | Senha criptografada do usuário. | Max 60 characters. | |

---

# [Carteira] Data Dictionary

| Field Name | Data Type | Description | Allowed Values/Range | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id_carteira` | `int` | Identificador único da carteira. | Positive integers. | Primary Key |
| `saldo_atual` | `double(8,2)` | Valor monetário disponível na carteira. | -999,999.99 to 999,999.99 | |
| `fk_usuario` | `int` | Referência ao dono da carteira. | Existing `id_usuario`. | Foreign Key |

---

# [Transacao] Data Dictionary

| Field Name | Data Type | Description | Allowed Values/Range | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id_transacao` | `int` | Identificador único da transação. | Positive integers. | Primary Key |
| `descricao` | `varchar(45)` | Breve texto detalhando a transação. | Max 45 characters. | |
| `valor` | `double(8,2)` | Valor financeiro da operação. | Positive/Negative double. | |
| `data_hora` | `date` | Data em que a transação ocorreu. | YYYY-MM-DD | |
| `fk_carteira` | `int` | Carteira de onde o recurso saiu/entrou. | Existing `id_carteira`. | Foreign Key |
| `fk_pagamento` | `int` | Referência ao método de pagamento. | Existing `id_metodo`. | Foreign Key |
| `fk_tipo` | `int` | Referência ao tipo de entrada/saída. | Existing `id_tipo`. | Foreign Key |

---

# [Metodo_de_Pagamento] Data Dictionary

| Field Name | Data Type | Description | Allowed Values/Range | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id_metodo` | `int` | Identificador do método de pagamento. | Positive integers. | Primary Key |
| `descricao_metodo` | `varchar(20)` | Nome do método (Ex: Crédito, PIX). | Max 20 characters. | |

---

# [Tipo_de_Entrada] Data Dictionary

| Field Name | Data Type | Description | Allowed Values/Range | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id_tipo` | `int` | Identificador da categoria da transação. | Positive integers. | Primary Key |
| `descricao_tipo` | `varchar(20)` | Entrada ou Saida de Créditos | Max 20 characters. | |
