# Banco de dados relacionais 

## Create Table

Cria uma nova tabela

> **comando:** CREATE TABLE nome (coluna, tipo, opções, COMMENT comentario)

## Modelagem de Dados

##### | NOT NULL | UNIQUE | DEFAULT |

* NOT NULL: o valor não pode ser nulo
* UNIQUE: não podem ter valores repetidos nesta coluna
* DEFAULT:

*Exemplo de criação de tabela:*

> CREATE TABLE usuarios (
    id INT UNIQUE,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    endereco VARCHAR(50) NOT NULL,
    data_nascimento DATE NOT NULL);

##### INSERT

Insere valores em uma tabela

> **Comando:** INSERT INTO nome_coluna (valor1, valor2...)

*Exemplo de insert:*

> INSERT INTO usuarios (id, nome, email, endereco, data_nascimento)
VALUES (1, "Pedro", "pedroMatias@gmail.com", "Rua Pedro Matias", "1900-02-25")

##### SELECT

Lê os valores de uma tabela, podendo receber uma condição como argumento

> **Comando:** SELECT colunas FROM tabela WHERE condição

*Exemplo de leitura:*

> SELECT id, nome FROM usuarios WHERE id > 1

##### UPDATE e DELETE

Update atualiza certos valores em um tabela 

> **Comando:** UPDATE tabela
 SET coluna1 = novo_valor1, coluna2 = novo_valor2
WHERE condição

Deleta um valor da tabela

> **Comando:** DELETE FROM tabela WHERE condição

*Exemplos de Update e Delete:*

> UPDATE usuarios SET nome = "Pedro Matias WHERE nome = "Pedro"
DELETE FROM usuarios WHERE nome = "Pedro"

##### DROP e ALTER

Drop table serve para excluir uma tabela de maneira permanente 

> **Comando:** DROP TABLE tabela

Alter table permite modificar a tabela, adicionando, alterando ou excluindo clolunas, indices, restrições e outros

> **Comando:** ALTER TABLE tabela RENAME novo_nome_tabela
ALTER TABLE tabela MODIFY COLUMN endereco VARCHAR(255)

#### Chaves Primarias e Estrangeiras 

**Chave Primaria:** não pode ter valores duplicados, não poder ser null, pode haver apenas uma na tabela

> **Comando:** (ID PRIMARY KEY *AUTOINCREMENT*,)

>ALTER TABLE tabela
MODIFY COLUMN coluna INT AUTO_INCREMENT

*AUTOINCREMENT:* valor cresce sozinho sempre que uma nova linha surge

**Chave Estrangeira:** pode ser nula, e possivel ter uma ou mais na tabela

> **Comando:** CREATE TABLE tabela (
    id INT PRIMARY KEY,
    chave_estrangeira INT,
    FOREIGN KEY (chave_estrangeira) REFERENCES outra_tabela (campo)
)

Uma chave estrangeira pode ter restrições (CONSTRAINT):

* ON DELETE: especifica o que ocorre quando um registro pai é excluido
* ON UPDATE: define o comportamento do registro quando o pai é atualizado 
* CASCADE, SET NULL, SET DEFAULT e RESTRICT 

## Normalização de Dados

###### Formas Normais

Formas normais são metodos de formatar valores

* **1FN (atomicidade de dados):** faz com que todos os valores em uma tabela sejam indivisiveis, ou seja, nenhum campo deve ter multiplos valores ou listas (como um campo de endereço contendo rua, numero, cidade, estado, etc)

* **2FN:** É necessario que siga a *1FN*. Todas as colunas devem depender da chave primaria (evita dependências parciais)

* **3FN:** Nenhuma coluna não-chave deve depender de outa coluna não-chave (evita dependências indiretas)

## Consultas Avançadas 

##### JOIN

Une 2 tabelas 

* **INNER JOIN:**  retorna apenas as linhas das tabelas onde o valor especificado é igual em ambas. Utiliza ON para determinar a condição

> Select * From tabela1
INNER JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
![alt text](image-2.png)

* **LEFT JOIN:** Retorna todas as linhas da tabela à esquerda da junção e as linhas correspondentes da direita, caso não existam na direita, o valor retornado ser NULL

> SELECT * FROM tabela1
LEFT JOIN tabela2 ON tabela1.coluna = tabela2.coluna
![Left Join](image-1.png)

* **RIGHT JOIN:** Retorna todas as linhas da tabela à direita da junção e as linhas correspondentes da esquerda, caso não existam na esquerda, o valor retornado ser NULL

> SELECT * FROM tabela1
RIGHT JOIN tabela2 ON tabela1.coluna = tabela2.coluna

![Right Join](image.png)

###### Funções Agregadas

* **COUNT:** conta o numero de registros
* **SUM:** soma os valores de uma coluna numerica
* **AVG:** calcula a média dos valores de uma coluna numerica
* **MIN:** retorna o valor minimo de uma coluna
* **MAX:** retorna o valor maximo de uma coluna