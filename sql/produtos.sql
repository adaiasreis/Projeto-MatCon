CREATE TABLE "produtos" (
"id" INTEGER NOT NULL UNIQUE,
"nome" TEXT NOT NULL,
"marca" TEXT NOT NULL,
"descricao" TEXT NOT NULL,
"preco_compra" REAL NOT NULL,
"preco_venda" REAL NOT NULL,
"quantidade" INTEGER NOT NULL,
PRIMARY KEY("id" AUTOINCREMENT)
);

INSERT INTO produtos (nome, marca,descricao,preco_compra,preco_venda,quantidade) VALUES ("Chave de fenda", "CFend", "Chave de fenda muito top", 20, 35.99, 10);
INSERT INTO produtos (nome, marca,descricao,preco_compra,preco_venda,quantidade) VALUES ("Chuveiro", "CFend", "Muito top", 200, 355.99, 100);
INSERT INTO produtos (nome, marca,descricao,preco_compra,preco_venda,quantidade) VALUES ("Parafuso", "Paraf", "nada pra falar", 0.20, 0.99, 1000);